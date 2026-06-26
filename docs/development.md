# Development Guide

## Branch strategy

- `main` — protected; requires CI to pass and 1 review to merge
- `feature/<name>` — all work happens here

## Daily workflow

```bash
git checkout main && git pull
git checkout -b feature/your-task
# do work
git add .
git commit -m "feat: description"   # pre-commit hooks fire here
git push origin feature/your-task
# open PR on GitHub
```

## Code standards (hard blocks on CI)

| Tool | Purpose |
|------|---------|
| `black` | Formatting |
| `isort` | Import order |
| `mypy` | Type checking |
| `pytest` | Tests + 70% coverage |

## Adding a new endpoint

1. Create a schema in `src/app/schemas/`
2. Create a service in `src/app/services/` (business logic)
3. Create an endpoint in `src/app/api/v1/endpoints/`
4. Register it in `src/app/api/v1/router.py`
5. Add tests in `tests/`
