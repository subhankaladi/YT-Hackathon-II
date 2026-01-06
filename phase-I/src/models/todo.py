from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoTask:
    """
    Represents a single todo task in the system.

    Attributes:
        id: Unique identifier for the task (positive integer)
        description: The task description/text (non-empty string)
        is_completed: Completion status of the task (default: False)
    """
    id: int
    description: str
    is_completed: bool = False

    def __post_init__(self):
        """Validate the TodoTask after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError(f"Description must be a non-empty string, got {self.description}")

        if not isinstance(self.is_completed, bool):
            raise ValueError(f"is_completed must be a boolean, got {self.is_completed}")