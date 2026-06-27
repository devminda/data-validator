"""Application entrypoint."""

from fastapi import FastAPI

from app.services.pipelines.validate import validate_data

app = FastAPI(
    title="TODO: Project Name",
    version="0.1.0",
    description="TODO: project description",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    # Example usage of the validate_data function
    data = "path/to/your/data.csv"  # Replace with your actual data path
    data_format = (
        "csv"  # Replace with the actual format of your data (csv, json, excel)
    )
    dataset_name = "default"
    validate_data(data, data_format, dataset_name)
