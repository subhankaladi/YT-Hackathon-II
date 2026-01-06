import sys
from typing import Optional
from ..models.todo import TodoTask
from ..repositories.todo_repository import TodoRepository
from ..services.todo_service import TodoService
from ..utils.validators import validate_task_description, validate_task_id


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """

    def __init__(self):
        """Initialize the CLI with a service instance."""
        repository = TodoRepository()
        self.service = TodoService(repository)

    def display_menu(self):
        """Display the main menu options."""
        print("\n--- Todo Application ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("------------------------")

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            The user's choice as a string
        """
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            sys.exit(0)

    def add_task(self):
        """Add a new task."""
        try:
            description = input("Enter task description: ").strip()

            if not validate_task_description(description):
                print("Error: Task description cannot be empty.")
                return

            task = self.service.add_task(description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_tasks(self):
        """View all tasks."""
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("\n--- All Tasks ---")
        for task in tasks:
            status = "✓" if task.is_completed else "○"
            print(f"{task.id}. [{status}] {task.description}")
        print("-----------------")

    def update_task(self):
        """Update an existing task."""
        try:
            task_id_str = input("Enter task ID to update: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not validate_task_id(task_id):
                print("Error: Invalid task ID.")
                return

            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            new_description = input(f"Enter new description for task '{task.description}': ").strip()

            if not validate_task_description(new_description):
                print("Error: Task description cannot be empty.")
                return

            updated = self.service.update_task(task_id, new_description)
            if updated:
                print("Task updated successfully.")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_task(self):
        """Delete a task."""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not validate_task_id(task_id):
                print("Error: Invalid task ID.")
                return

            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            confirmation = input(f"Are you sure you want to delete task '{task.description}'? (y/N): ").strip().lower()
            if confirmation in ['y', 'yes']:
                deleted = self.service.delete_task(task_id)
                if deleted:
                    print("Task deleted successfully.")
                else:
                    print("Failed to delete task.")
            else:
                print("Deletion cancelled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def mark_task_complete(self):
        """Mark a task as complete."""
        try:
            task_id_str = input("Enter task ID to mark complete: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not validate_task_id(task_id):
                print("Error: Invalid task ID.")
                return

            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            marked = self.service.mark_complete(task_id)
            if marked:
                print("Task marked as complete.")
            else:
                print("Failed to mark task as complete.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def mark_task_incomplete(self):
        """Mark a task as incomplete."""
        try:
            task_id_str = input("Enter task ID to mark incomplete: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not validate_task_id(task_id):
                print("Error: Invalid task ID.")
                return

            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            marked = self.service.mark_incomplete(task_id)
            if marked:
                print("Task marked as incomplete.")
            else:
                print("Failed to mark task as incomplete.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "7":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()