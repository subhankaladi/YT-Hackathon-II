# Data Model: Phase I – In-Memory Python Console Todo App

## TodoTask Entity

**Name**: TodoTask
**Description**: Represents a single todo task in the system

### Fields
- `id`: integer - Unique identifier for the task (auto-incremented)
- `description`: string - The task description/text (required, non-empty)
- `is_completed`: boolean - Completion status of the task (default: False)

### Validation Rules
- `id`: Must be a positive integer
- `description`: Must be non-empty string (1+ characters)
- `is_completed`: Must be boolean value

### State Transitions
- Initial state: `is_completed = False`
- When marked complete: `is_completed` changes from `False` to `True`
- When marked incomplete: `is_completed` changes from `True` to `False`

## TodoRepository

**Name**: TodoRepository
**Description**: In-memory storage for TodoTask entities

### Operations
- `add_task(description: str) -> TodoTask`: Creates and stores a new task
- `get_all_tasks() -> List[TodoTask]`: Returns all tasks
- `get_task_by_id(id: int) -> Optional[TodoTask]`: Returns task by ID or None
- `update_task(id: int, description: str) -> bool`: Updates task description
- `delete_task(id: int) -> bool`: Removes task by ID
- `mark_complete(id: int) -> bool`: Marks task as completed
- `mark_incomplete(id: int) -> bool`: Marks task as not completed

### Constraints
- All operations are in-memory only
- Task IDs are unique within the session
- Task IDs are auto-incremented from 1