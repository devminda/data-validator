# Data Quality Validation Platform
A reusable Python application that automates dataset validation, replacing manual Excel-based inspection with a structured validation pipeline and detailed reporting.

📖 **[Full documentation →](https://devminda.github.io/data-validator/)**

---

## Setup
```bash
git clone https://github.com/devminda/data-validator.git
cd data-validator
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
docker build -t data-validator .
docker run -p 8000:8000 data-validator
```

## Tests
```bash
uv run pytest
```

## Project structure
```
.
├── app/
│   ├── config/             # column definitions, dataset mappings, constants
│   ├── models/
│   │   ├── data_loader/    # base loader and CSV/JSON/Excel implementations
│   │   └── data_validator/ # base validator, registry, and all validators
│   ├── services/
│   │   ├── pipelines/      # validation pipeline orchestration
│   │   └── report_generator/ # CLI and base report generators
│   └── main.py             # app entrypoint
├── examples/               # example usage scripts
├── notebooks/              # Jupyter notebooks — exploration & analysis
├── tests/
│   ├── unit/
│   └── integration/
├── docs/                   # MkDocs pages
├── Dockerfile
└── pyproject.toml          # all tool config lives here
```
