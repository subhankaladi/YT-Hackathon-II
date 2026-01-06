# Feature Specification: Phase I – In-Memory Python Console Todo App

**Feature Branch**: `001-in-memory-todo`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Phase I – In-Memory Python Console Todo App. Target audience: Beginner Python developers evaluating spec-driven, agentic workflows. Focus: A basic command-line Todo app with in-memory storage and clean structure. Success criteria: Supports Add, View, Update, Delete, Mark Complete. Runs fully in memory (no files, no DB). Clean, modular Python project. Python 3.13+ using UV. Deterministic CLI behavior with input validation. Constraints: Console-only application. No persistence or external services. Single-user, offline. No manual coding (Claude Code only). Not building: Web/GUI interface, Authentication or AI features, Advanced task metadata (priority, due date)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Manage Tasks via Console (Priority: P1)

As a beginner developer, I want to manage my daily tasks through a simple console interface so that I can see how a clean, modular Python application is structured.

**Why this priority**: Core functionality of the application. It represents the MVP (Minimum Viable Product).

**Independent Test**: Can be fully tested by running the main entry point and performing CRUD operations in the terminal.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I choose to 'Add' a task with description "Buy milk", **Then** the task should be successfully stored in memory.
2. **Given** I have a task "Buy milk", **When** I 'View' my tasks, **Then** I should see "Buy milk" in the list with its completion status.
3. **Given** I have a task "Buy milk", **When** I 'Mark Complete', **Then** the status should change from pending to completed.
4. **Given** I have a task "Buy milk", **When** I 'Update' it to "Buy bread", **Then** the description should be updated.
5. **Given** I have a task "Buy bread", **When** I 'Delete' it, **Then** it should no longer appear in the task list.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a command-driven menu interface (Add, View, Update, Delete, Mark Complete, Exit).
- **FR-002**: System MUST validate all user inputs (e.g., non-empty descriptions, valid numeric selections for ID-based operations).
- **FR-003**: System MUST assign a unique identifier to each task for selection in Update/Delete/Complete operations.
- **FR-004**: System MUST store all task data exclusively in runtime memory (e.g., list or dictionary).
- **FR-005**: System MUST present a clean, formatted view of all tasks, showing ID, Status, and Description.

### Key Entities

- **TodoTask**: Represents a single task. Attributes: `id` (integer), `description` (string), `is_completed` (boolean).
- **TodoStore**: Represents the in-memory data warehouse. Responsible for CRUD operations on `TodoTask` objects.

## Success Criteria *(mandatory)*

- **SC-001**: Full CRUD operations (Add, View, Update, Delete, Mark Complete) are functional in the console.
- **SC-002**: 100% logic coverage with pytest (logic must be testable without the console shell).
- **SC-003**: Application runs using Python 3.13+ managed by `uv`.
- **SC-004**: System handles invalid inputs (e.g., letters for ID numbers, empty strings for tasks) without crashing.
- **SC-005**: All data is lost on exit (verifying strict in-memory requirement).

## Assumptions

- **A-001**: The application will use a simple numbered menu for navigation.
- **A-002**: Task IDs will increment sequentially for the duration of the session.
- **A-003**: The project structure will follow a modular layout (e.g., `src/` for logic, `tests/` for tests).
