from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd


@dataclass
class DataValidatorBase(ABC):
    data_set: str

    @abstractmethod
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        pass


@dataclass
class ValidationResult:
    is_valid: bool
    invalid_data: pd.DataFrame
    message: str = ""
