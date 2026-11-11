# Copilot instructions for the login project

This is a uv-based Python project. Run commands with `uv run ...`.

## Commands

From `viikko3/login`:

- Install dependencies: `uv sync`
- Start the app: `uv run python src/index.py`
  - The Flask app runs on `http://localhost:5001`
- Run all Robot Framework tests: `uv run robot src/tests`
  - The app must already be running before the tests start.
- Run a single suite: `uv run robot src/tests/login.robot`
- Run a single test case: `uv run robot -t "Login With Correct Credentials" src/tests/login.robot`

## Where validation happens

Username/password validation is in `src/services/user_service.py`.

- `UserService.validate()` checks required values, minimum length, password confirmation, and duplicate usernames.
- `UserService.check_credentials()` checks that the user exists and that the submitted password matches.
- `src/app.py` calls these methods during login/register requests and flashes any exceptions back to the form.

## Important project behavior

- The app uses an in-memory repository in `src/repositories/user_repository.py`; no database is used.
- Robot tests use `src/AppLibrary.py` and the Browser library, and they rely on the app being live on `localhost:5001`.
- `src/app.py` exposes `/tests/reset` to clear in-memory state between test runs.
