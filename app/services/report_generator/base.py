from abc import ABC, abstractmethod
from typing import Mapping

import pandas as pd


class ReportGeneratorBase(ABC):
    @abstractmethod
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        pass


class PDFReportGenerator(ReportGeneratorBase):
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        # Implement PDF report generation logic here
        pass


class ExcelReportGenerator(ReportGeneratorBase):
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        # Implement Excel report generation logic here
        pass


class HTMLReportGenerator(ReportGeneratorBase):
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        # Implement HTML report generation logic here
        pass


class CMDReportGenerator(ReportGeneratorBase):
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        # Implement command-line report generation logic here
        pass
