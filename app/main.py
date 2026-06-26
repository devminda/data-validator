"""Application entrypoint."""

from fastapi import FastAPI

app = FastAPI(
    title="TODO: Project Name",
    version="0.1.0",
    description="TODO: project description",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
