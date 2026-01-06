# Quickstart Guide: Phase I – In-Memory Python Console Todo App

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone the repository
2. Install dependencies: `uv sync` (or `uv pip install` if using directly)
3. Run the application: `python src/cli/main.py`

## Usage
1. The application starts with a menu showing available options
2. Select options by entering the corresponding number
3. Follow the prompts for each operation
4. The application runs in memory only - all data is lost on exit

## Development
1. All business logic is in the `services/` directory
2. Data models are in the `models/` directory
3. In-memory storage is handled in the `repositories/` directory
4. CLI interface is in the `cli/` directory
5. Run tests with: `pytest`

## Architecture
- Clean architecture with separation of concerns
- Business logic independent of CLI interface
- Easy to extend with additional interfaces (API, GUI) in future phases