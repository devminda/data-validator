from os import PathLike
from typing import Dict

import pandas as pd

from app.config.mappings import DATASET_VALIDATORS
from app.models.data_loader.loaders import CSVLoader, ExcelLoader, JSONLoader
from app.models.data_validator.registry import CLASS_REGISTRY
from app.services.report_generator.cmd import CMDReportGeneratorService


def validate_data(
    data: str | PathLike[str], data_format: str, dataset_name: str
) -> None:
    # Determine the appropriate data loader based on the data format
    loaders: dict[str, CSVLoader | JSONLoader | ExcelLoader] = {
        "csv": CSVLoader(),
        "json": JSONLoader(),
        "excel": ExcelLoader(),
    }

    loader = loaders.get(data_format.lower())
    if loader is None:
        raise ValueError(f"Unsupported data format: {data_format}")

    # Read the data using the selected loader
    df = loader.read_data(data)
    print(f"Data loaded successfully. Shape: {df.shape}")
    validation_results: Dict[str, pd.DataFrame] = {}

    # Iterate through all registered validators and apply them to the data
    validator_names = DATASET_VALIDATORS.get(dataset_name, [])
    for name in validator_names:
        validator_cls = CLASS_REGISTRY.get(name)
        if validator_cls is None:
            print(f"Validator not found: {name}")
            continue
        print(f"Running validator: {name}")
        validator = validator_cls(data_set=dataset_name)
        try:
            validation_result = validator.validate(df)
        except Exception as e:
            print(f"Error occurred while running validator {name}: {e}")
            continue

        if not validation_result.is_valid:
            validation_results[name] = validation_result.invalid_data
    print("Done running all validators.")
    # Generate a report based on the validation results
    report_generator = CMDReportGeneratorService()
    report_generator.generate_report(validation_results, dataset_name)
