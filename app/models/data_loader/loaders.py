from __future__ import annotations

from os import PathLike

import pandas as pd

from app.models.data_loader.base import DataLoaderBase


class CSVLoader(DataLoaderBase):
    def read_data(self, data: str | PathLike[str]) -> pd.DataFrame:
        # Implement CSV reading logic here
        df = pd.read_csv(data)
        return df


class JSONLoader(DataLoaderBase):
    def read_data(self, data: str | PathLike[str]) -> pd.DataFrame:
        # Implement JSON reading logic here
        df = pd.read_json(data)
        return df


class ExcelLoader(DataLoaderBase):
    def read_data(self, data: str | PathLike[str]) -> pd.DataFrame:
        # Implement Excel reading logic here
        df = pd.read_excel(data)
        return df
