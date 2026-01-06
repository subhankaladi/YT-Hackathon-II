# Todo API Contracts

## Add Task
- **Operation**: Add a new todo task
- **Input**: Task description (string, non-empty)
- **Output**: Task object with ID, description, and completion status
- **Errors**: Invalid input (empty description)

## View All Tasks
- **Operation**: Retrieve all todo tasks
- **Input**: None
- **Output**: List of task objects (ID, description, completion status)
- **Errors**: None

## Update Task
- **Operation**: Update an existing task description
- **Input**: Task ID (integer), new description (string, non-empty)
- **Output**: Boolean indicating success/failure
- **Errors**: Invalid ID, invalid input (empty description)

## Delete Task
- **Operation**: Remove a task by ID
- **Input**: Task ID (integer)
- **Output**: Boolean indicating success/failure
- **Errors**: Invalid ID

## Mark Task Complete
- **Operation**: Mark a task as completed
- **Input**: Task ID (integer)
- **Output**: Boolean indicating success/failure
- **Errors**: Invalid ID

## Mark Task Incomplete
- **Operation**: Mark a completed task as incomplete
- **Input**: Task ID (integer)
- **Output**: Boolean indicating success/failure
- **Errors**: Invalid ID