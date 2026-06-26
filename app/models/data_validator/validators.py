import pandas as pd

from app.config.columns import COLUMN_SETS
from app.config.values import MINIMUM_WAGE
from app.models.data_validator.base import DataValidatorBase, ValidationResult
from app.models.data_validator.registry import register


@register(name="Invalid Columns")
class ColumnsValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        expected_columns = COLUMN_SETS.get(self.data_set, [])
        if list(data.columns) != expected_columns:
            return ValidationResult(
                is_valid=False,
                invalid_data=data.head(5),
                message=(
                    f"Invalid columns. Expected: {expected_columns}, "
                    f"Found: {list(data.columns)}"
                ),
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="Columns are valid.",
        )


@register(name="Missing Values")
class MissingValueValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        if data.isnull().values.any():
            data = data.loc[data.isnull().any(axis=1)]
            return ValidationResult(
                is_valid=False,
                invalid_data=data,
                message="Rows with missing values found.",
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="No missing values found.",
        )


@register(name="Duplicate Rows")
class DuplicateRowsValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        if data.duplicated().any():
            data = data[data.duplicated()]
            return ValidationResult(
                is_valid=False,
                invalid_data=data,
                message="Duplicate rows found.",
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="No duplicate rows found.",
        )


@register(name="Negative Salaries")
class NegativeSalariesValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        if "salary" in data.columns and (data["salary"] < 0).any():
            data = data[data["salary"] < 0]
            return ValidationResult(
                is_valid=False,
                invalid_data=data,
                message="Rows with negative salaries found.",
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="No negative salaries found.",
        )


@register(name="Invalid Date")
class InvalidDateValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        dob = pd.to_datetime(data["date_of_birth"], errors="coerce")
        hire = pd.to_datetime(data["hire_date"], errors="coerce")
        invalid_dates = dob.isna() | hire.isna()

        if invalid_dates.any():
            data = data[invalid_dates]
            return ValidationResult(
                is_valid=False,
                invalid_data=data,
                message="Rows with invalid dates found.",
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="No invalid dates found.",
        )


@register(name="Salary Range Below Minimum Wage")
class SalaryRangeValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        if "salary" in data.columns:
            below_min = data["salary"] < MINIMUM_WAGE
            if below_min.any():
                data = data[below_min]
                return ValidationResult(
                    is_valid=False,
                    invalid_data=data,
                    message="Rows with salaries below minimum wage found.",
                )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="All salaries are within the valid range.",
        )


@register(name="Future Date of Birth")
class FutureDOBValidator(DataValidatorBase):
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        dob = pd.to_datetime(data["date_of_birth"], errors="coerce", utc=True)
        now = pd.Timestamp.now(tz="UTC")
        mask = dob.notna() & (dob > now)

        if mask.any():
            invalid_rows = data.loc[mask]
            return ValidationResult(
                is_valid=False,
                invalid_data=invalid_rows,
                message="Rows with future dates of birth found.",
            )

        return ValidationResult(
            is_valid=True,
            invalid_data=pd.DataFrame(),
            message="No future dates of birth found.",
        )
