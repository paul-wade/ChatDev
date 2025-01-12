"""
Supervisor API for ChatDev that allows monitoring and injection of guidance during execution.
"""
from typing import Dict, Any, Optional, List, Set
import asyncio
from dataclasses import dataclass
from enum import Enum
import json
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class PhaseStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"

class ExecutionControl(str, Enum):
    PAUSE = "pause"
    RESUME = "resume"
    STOP = "stop"
    SKIP_PHASE = "skip_phase"
    RETRY_PHASE = "retry_phase"

class PhaseTransition(BaseModel):
    from_phase: str
    to_phase: str
    required_status: PhaseStatus
    required_artifacts: List[str] = []
    validation_rules: Dict[str, Any] = {}

class SupervisorEvent(BaseModel):
    timestamp: str
    event_type: str
    phase: str
    data: Dict[str, Any]

class SupervisorGuidance(BaseModel):
    phase: str
    guidance: str
    priority: int = 1
    timeout_seconds: int = 30

class PhaseContext(BaseModel):
    current_phase: str
    status: PhaseStatus
    agents: List[str]
    last_message: Optional[str] = None
    execution_state: ExecutionControl = ExecutionControl.RESUME
    artifacts: Dict[str, Any] = {}
    
class SupervisorAPI:
    def __init__(self):
        self.context = PhaseContext(
            current_phase="Initialization",
            status=PhaseStatus.RUNNING,
            agents=[],
            execution_state=ExecutionControl.RESUME,
            artifacts={},
            last_message=None
        )
        self.guidance_queue = []
        self.execution_state = ExecutionControl.RESUME
        self.app = FastAPI()
        self.setup_routes()

    def setup_routes(self):
        @self.app.get("/status")
        async def get_status():
            return self.context.dict()

        @self.app.get("/events")
        async def get_events():
            return {"events": []}  # TODO: Implement event history

        @self.app.post("/control/{action}")
        async def control_execution(action: str):
            if action == "pause":
                self.execution_state = ExecutionControl.PAUSE
            elif action == "resume":
                self.execution_state = ExecutionControl.RESUME
            elif action == "stop":
                self.execution_state = ExecutionControl.STOP
            return {"status": "success", "action": action}

        @self.app.post("/inject")
        async def inject_guidance(guidance: SupervisorGuidance):
            self.guidance_queue.append(guidance)
            return {"status": "success"}

    async def update_context(self, context: PhaseContext):
        """Update the current context"""
        self.context = context

    def update_context_sync(self, context: PhaseContext):
        """Synchronous version of update_context"""
        try:
            import asyncio
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
        if loop.is_running():
            self.context = context
        else:
            loop.run_until_complete(self.update_context(context))

    async def should_continue(self) -> bool:
        """Check if execution should continue"""
        return self.execution_state != ExecutionControl.STOP

    def should_continue_sync(self) -> bool:
        """Synchronous version of should_continue"""
        try:
            import asyncio
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
        if loop.is_running():
            return self.execution_state != ExecutionControl.STOP
        else:
            return loop.run_until_complete(self.should_continue())

    async def get_guidance(self, timeout: float = 0.1) -> Optional[SupervisorGuidance]:
        """Get the next guidance item if available"""
        if self.guidance_queue:
            return self.guidance_queue.pop(0)
        return None

    def get_guidance_sync(self, timeout: float = 0.1) -> Optional[SupervisorGuidance]:
        """Synchronous version of get_guidance"""
        try:
            import asyncio
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
        if loop.is_running():
            if self.guidance_queue:
                return self.guidance_queue.pop(0)
            return None
        else:
            return loop.run_until_complete(self.get_guidance(timeout))

# Create a global supervisor instance
supervisor = SupervisorAPI()
