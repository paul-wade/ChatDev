# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========

from typing import Dict, Type

class PromptTemplateDict:
    """Base class for prompt template dictionaries."""

    def __init__(self) -> None:
        """Initialize the prompt template dictionary."""
        self.task_dict = {}

    def get_prompt(self, task_type: str) -> str:
        """Get the prompt for a task type."""
        return self.task_dict.get(task_type, self.task_dict["default"])


class TaskPromptTemplateDict:
    """A dictionary mapping task types to prompt template dictionaries."""

    def __init__(self) -> None:
        """Initialize the task prompt template dictionary."""
        from camel.typing import TaskType
        self.task_dict = {
            TaskType.CODE: {
                "task_specify_prompt": (
                    "You are a helpful AI coding assistant. You will help me write code "
                    "to solve a programming task. Please provide clear and concise code "
                    "that solves the task effectively."
                ),
            },
            TaskType.MATH: {
                "task_specify_prompt": (
                    "You are a helpful AI math assistant. You will help me solve "
                    "mathematical problems. Please provide clear explanations and "
                    "step-by-step solutions."
                ),
            },
            TaskType.WRITING: {
                "task_specify_prompt": (
                    "You are a helpful AI writing assistant. You will help me with "
                    "writing tasks. Please provide clear and well-structured text "
                    "that effectively communicates the intended message."
                ),
            },
            TaskType.ANALYSIS: {
                "task_specify_prompt": (
                    "You are a helpful AI analysis assistant. You will help me analyze "
                    "data and information. Please provide clear insights and "
                    "recommendations based on the available information."
                ),
            },
            TaskType.CHAT: {
                "task_specify_prompt": (
                    "You are a helpful AI chat assistant. You will engage in natural "
                    "conversation and help me with various tasks. Please provide "
                    "informative and engaging responses."
                ),
            },
            TaskType.DESIGN: {
                "task_specify_prompt": (
                    "You are a helpful AI design assistant. You will help me with "
                    "design tasks. Please provide creative and effective design "
                    "solutions that meet the requirements."
                ),
            },
            TaskType.TESTING: {
                "task_specify_prompt": (
                    "You are a helpful AI testing assistant. You will help me with "
                    "software testing tasks. Please provide comprehensive test cases "
                    "and strategies to ensure code quality."
                ),
            },
        }

    def __getitem__(self, key):
        """Get the prompt template dictionary for a task type."""
        return self.task_dict[key]

    def get_prompt_template(self, task_type) -> Dict:
        """Get the prompt template dictionary for a task type.

        Args:
            task_type: The task type to get the prompt template dictionary for.

        Returns:
            The prompt template dictionary for the task type.
        """
        return self.task_dict[task_type]


class CodePromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for code tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI coding assistant. You will help me write code "
                "to solve a programming task. Please provide clear and concise code "
                "that solves the task effectively."
            ),
        }


class MathPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for math tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI math assistant. You will help me solve "
                "mathematical problems. Please provide clear explanations and "
                "step-by-step solutions."
            ),
        }


class WritingPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for writing tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI writing assistant. You will help me with "
                "writing tasks. Please provide clear and well-structured text "
                "that effectively communicates the intended message."
            ),
        }


class AnalysisPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for analysis tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI analysis assistant. You will help me analyze "
                "data and information. Please provide clear insights and "
                "recommendations based on the available information."
            ),
        }


class ChatPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for chat tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI chat assistant. You will engage in natural "
                "conversation and help me with various tasks. Please provide "
                "informative and engaging responses."
            ),
        }


class DesignPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for design tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI design assistant. You will help me with "
                "design tasks. Please provide creative and effective design "
                "solutions that meet the requirements."
            ),
        }


class TestingPromptTemplateDict(PromptTemplateDict):
    """A dictionary of prompt templates for testing tasks."""

    def __init__(self) -> None:
        super().__init__()
        self.task_dict = {
            "default": (
                "You are a helpful AI testing assistant. You will help me with "
                "software testing tasks. Please provide comprehensive test cases "
                "and strategies to ensure code quality."
            ),
        }
