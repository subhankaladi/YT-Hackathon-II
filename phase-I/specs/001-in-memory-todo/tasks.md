---
description: "Task list for Phase I In-Memory Python Console Todo App implementation"
---

# Tasks: Phase I – In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-in-memory-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks included per feature specification requirements (100% logic coverage with pytest).
**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure (Strict Phase I Constraints)

- [X] T001 Initialize Phase I Python environment (no external DB dependencies)
- [X] T002 Setup pytest for 100% logic coverage
- [X] T003 Configure linting/formatting (ruff/black)
- [X] T004 Create project directory structure per plan.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create TodoTask data model in src/models/todo.py
- [X] T006 Create TodoRepository in-memory storage in src/repositories/todo_repository.py
- [X] T007 Create TodoService business logic in src/services/todo_service.py
- [X] T008 Create validation utilities in src/utils/validators.py
- [X] T009 Create main CLI entry point in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Manage Tasks via Console (Priority: P1) 🎯 MVP

**Goal**: Implement full CRUD operations (Add, View, Update, Delete, Mark Complete) for todo tasks in console interface

**Independent Test**: Can be fully tested by running the main entry point and performing CRUD operations in the terminal.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Unit test for TodoTask model in tests/unit/models/test_todo.py
- [X] T011 [P] [US1] Unit test for TodoRepository in tests/unit/repositories/test_todo_repository.py
- [X] T012 [P] [US1] Unit test for TodoService in tests/unit/services/test_todo_service.py
- [X] T013 [P] [US1] Contract test for todo operations in tests/contract/test_todo_contracts.py
- [X] T014 [P] [US1] Integration test for CLI flow in tests/integration/cli/test_cli_flow.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Implement TodoTask model with id, description, is_completed in src/models/todo.py
- [X] T016 [P] [US1] Implement TodoRepository with add_task, get_all_tasks, get_task_by_id in src/repositories/todo_repository.py
- [X] T017 [P] [US1] Implement TodoRepository with update_task, delete_task, mark_complete, mark_incomplete in src/repositories/todo_repository.py
- [X] T018 [US1] Implement TodoService with all CRUD operations in src/services/todo_service.py
- [X] T019 [US1] Implement validation functions for task description in src/utils/validators.py
- [X] T020 [US1] Implement CLI menu with Add, View, Update, Delete, Mark Complete, Exit options in src/cli/main.py
- [X] T021 [US1] Implement CLI input handling and error validation in src/cli/main.py
- [X] T022 [US1] Add formatted output for viewing tasks in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for TodoTask model in tests/unit/models/test_todo.py"
Task: "Unit test for TodoRepository in tests/unit/repositories/test_todo_repository.py"
Task: "Unit test for TodoService in tests/unit/services/test_todo_service.py"

# Launch all models for User Story 1 together:
Task: "Implement TodoTask model with id, description, is_completed in src/models/todo.py"
Task: "Implement TodoRepository with add_task, get_all_tasks, get_task_by_id in src/repositories/todo_repository.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence