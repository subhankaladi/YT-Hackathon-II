from typing import List, Optional
from src.models.todo import TodoTask


class TodoRepository:
    """
    In-memory storage for TodoTask entities.
    """

    def __init__(self):
        """Initialize the repository with an empty list of tasks."""
        self._tasks: List[TodoTask] = []
        self._next_id = 1

    def add_task(self, description: str) -> TodoTask:
        """
        Creates and stores a new task.

        Args:
            description: The task description

        Returns:
            The created TodoTask with assigned ID
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task = TodoTask(
            id=self._next_id,
            description=description.strip(),
            is_completed=False
        )

        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Returns all tasks.

        Returns:
            List of all TodoTask objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[TodoTask]:
        """
        Returns task by ID or None.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            TodoTask if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Updates task description.

        Args:
            task_id: The ID of the task to update
            description: The new description

        Returns:
            True if task was updated, False if task not found
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        for task in self._tasks:
            if task.id == task_id:
                task.description = description.strip()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Removes task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """
        Marks task as completed.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was marked complete, False if task not found
        """
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = True
                return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Marks task as not completed.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if task not found
        """
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = False
                return True
        return False