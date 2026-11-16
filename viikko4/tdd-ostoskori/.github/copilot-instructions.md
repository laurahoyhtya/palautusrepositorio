# Copilot instructions for tdd-ostoskori

## Project snapshot

This repository is a small TDD exercise for a shopping cart implementation in Python. The important behavior is defined by the tests in `src/tests/ostoskori_test.py`, and the cart logic is implemented in `src/ostoskori.py`.

The core domain model is intentionally split across a few small files:

- `src/tuote.py`: fixed product model (`Tuote`) with a product name and price.
- `src/ostos.py`: fixed line-item model (`Ostos`) that tracks a product and a quantity.
- `src/ostoskori.py`: cart logic that should aggregate products, calculate totals, and manage quantities.
- `src/tests/ostoskori_test.py`: the source of truth for expected behavior.

`src/index.py` is only a scratch/test area and should not be treated as the implementation reference.

## Build, test, and validation

Use the project root as the working directory when running commands.

- Full suite: `uv run pytest`
- Single test file: `uv run pytest src/tests/ostoskori_test.py`
- Single test case: `uv run pytest src/tests/ostoskori_test.py -k <test_name>`

There is no separate lint or formatting command configured in `pyproject.toml`; pytest is the active validation path.

## Architecture and implementation expectations

This project follows a very small, exercise-oriented architecture:

- `Tuote` represents a single product and exposes its price and name.
- `Ostos` is a basket line item for a product and its quantity.
- `Ostoskori` is the aggregate object that owns the basket and exposes the public cart API used by the tests.

The goal is not to build a large app or create an abstraction layer. Keep the implementation focused on the cart behavior expected by the tests.

## Codebase conventions

- Tests are the source of truth for the required behavior.
- Run tests with `uv run pytest`.
- Do not change `src/tuote.py` or `src/ostos.py`.
- Do not edit test files unless explicitly asked.
- Keep changes as narrow as possible and implement only the minimal code needed to make the tests pass.
- Avoid broad refactors, extra features, or unrelated cleanup while working on this task.
- Keep work scoped to the existing cart implementation unless the tests clearly require a different file.
