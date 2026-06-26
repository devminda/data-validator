# TODO: Project Name


TODO: project description.

📖 **[Full documentation →](https://TODO-org.github.io/TODO-repo/)**

---

## Setup

```bash
git clone https://github.com/TODO-org/TODO-repo.git
cd TODO-repo
cp .env.example .env       # fill in your values
pip install uv
uv sync --extra dev --extra docs
uv run pre-commit install
```

## Run locally

```bash
uv run uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Run with Docker

```bash
docker build -t app .
docker run -p 8000:8000 app
```

## Tests

```bash
uv run pytest
```

## Project structure

```
.
├── app/
│   ├── data/               # data loading and processing utilities
│   ├── db/                 # database connection & schemas
│   ├── models/             # ORM models (if needed)
│   ├── routes/             # route handlers
│   ├── services/           # business logic
│   └── main.py             # app entrypoint
├── notebooks/              # Jupyter notebooks — exploration & analysis
├── tests/
│   ├── unit/
│   └── integration/
├── docs/                   # MkDocs pages
├── Dockerfile
├── .env.example
└── pyproject.toml          # all tool config lives here
```

## TODO checklist after cloning this template

- [ ] Replace all `TODO` placeholders in `pyproject.toml`, `mkdocs.yml`, `README.md`
- [ ] Fill in `.env` from `.env.example`
- [ ] Enable GitHub Pages: Settings → Pages → GitHub Actions
- [ ] Set up branch protection: Settings → Rules → New ruleset
- [ ] Delete the example `items` endpoint and write your own
