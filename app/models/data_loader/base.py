from __future__ import annotations

from abc import ABC, abstractmethod
from os import PathLike

import pandas as pd


class DataLoaderBase(ABC):
    @abstractmethod
    def read_data(self, data: str | PathLike[str]) -> pd.DataFrame:
        pass
