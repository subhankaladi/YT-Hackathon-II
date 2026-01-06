from typing import List, Optional
from src.models.todo import TodoTask
from src.repositories.todo_repository import TodoRepository


class TodoService:
    """
    Business logic layer for todo operations.
    """

    def __init__(self, repository: TodoRepository):
        """
        Initialize the service with a repository.

        Args:
            repository: The repository to use for data operations
        """
        self.repository = repository

    def add_task(self, description: str) -> TodoTask:
        """
        Add a new task.

        Args:
            description: The task description

        Returns:
            The created TodoTask
        """
        return self.repository.add_task(description)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Get all tasks.

        Returns:
            List of all TodoTask objects
        """
        return self.repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Optional[TodoTask]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The TodoTask if found, None otherwise
        """
        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Update a task's description.

        Args:
            task_id: The ID of the task to update
            description: The new description

        Returns:
            True if task was updated, False if task not found
        """
        return self.repository.update_task(task_id, description)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        return self.repository.delete_task(task_id)

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was marked complete, False if task not found
        """
        return self.repository.mark_complete(task_id)

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if task not found
        """
        return self.repository.mark_incomplete(task_id)