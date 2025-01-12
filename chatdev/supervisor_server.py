"""
FastAPI server for the ChatDev supervisor API
"""
import os
import sys

# Add ChatDev to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from chatdev.supervisor import supervisor

app = FastAPI()
active_websockets = set()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the supervisor API
app.mount("/supervisor", supervisor.app)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_websockets.add(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except:
        active_websockets.remove(websocket)

# Update supervisor to broadcast updates
async def broadcast_update(context):
    """Broadcast context updates to all connected clients"""
    if active_websockets:
        for websocket in active_websockets:
            try:
                await websocket.send_json(context.dict())
            except:
                active_websockets.remove(websocket)

# Patch supervisor's update_context method to broadcast updates
original_update_context = supervisor.update_context
async def patched_update_context(context):
    await original_update_context(context)
    await broadcast_update(context)
supervisor.update_context = patched_update_context

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
