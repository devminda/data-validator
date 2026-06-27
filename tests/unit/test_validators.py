import pandas as pd
import pytest

from app.models.data_validator.validators import (
    DuplicateRowsValidator,
    FutureDOBValidator,
    MissingValueValidator,
    NegativeSalariesValidator,
    SalaryRangeValidator,
)


@pytest.fixture
def hr_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "employee_id": [1, 2],
            "name": ["Alice", "Bob"],
            "department": ["Finance", "Engineering"],
            "salary": [50000, 60000],
            "date_of_birth": ["1990-01-01", "1985-06-15"],
            "age": [34, 39],
            "hire_date": ["2020-01-01", "2019-03-01"],
        }
    )


# ── Missing Values ────────────────────────────────────────────────────────────


def test_missing_value_validator_passes_clean_data(hr_df: pd.DataFrame) -> None:
    result = MissingValueValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is True
    assert result.invalid_data.empty


def test_missing_value_validator_detects_nulls(hr_df: pd.DataFrame) -> None:
    hr_df.loc[0, "name"] = None
    result = MissingValueValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is False
    assert len(result.invalid_data) == 1


# ── Duplicate Rows ────────────────────────────────────────────────────────────


def test_duplicate_rows_validator_passes_unique_data(hr_df: pd.DataFrame) -> None:
    result = DuplicateRowsValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is True


def test_duplicate_rows_validator_detects_duplicates(hr_df: pd.DataFrame) -> None:
    df = pd.concat([hr_df, hr_df.iloc[[0]]], ignore_index=True)
    result = DuplicateRowsValidator(data_set="hr").validate(df)
    assert result.is_valid is False
    assert len(result.invalid_data) == 1


# ── Negative Salaries ─────────────────────────────────────────────────────────


def test_negative_salary_validator_passes_positive(hr_df: pd.DataFrame) -> None:
    result = NegativeSalariesValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is True


def test_negative_salary_validator_detects_negative(hr_df: pd.DataFrame) -> None:
    hr_df.loc[0, "salary"] = -5000
    result = NegativeSalariesValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is False
    assert len(result.invalid_data) == 1


# ── Salary Range ──────────────────────────────────────────────────────────────


def test_salary_range_validator_passes_above_minimum(hr_df: pd.DataFrame) -> None:
    result = SalaryRangeValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is True


def test_salary_range_validator_detects_below_minimum(hr_df: pd.DataFrame) -> None:
    hr_df.loc[0, "salary"] = 100
    result = SalaryRangeValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is False


# ── Future DOB ────────────────────────────────────────────────────────────────


def test_future_dob_validator_passes_past_dates(hr_df: pd.DataFrame) -> None:
    result = FutureDOBValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is True


def test_future_dob_validator_detects_future_dates(hr_df: pd.DataFrame) -> None:
    hr_df.loc[0, "date_of_birth"] = "2999-01-01"
    result = FutureDOBValidator(data_set="hr").validate(hr_df)
    assert result.is_valid is False
    assert len(result.invalid_data) == 1
