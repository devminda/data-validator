from typing import Mapping

import pandas as pd
from jinja2 import Template
from tabulate import tabulate

from app.services.report_generator.base import CMDReportGenerator
from app.services.report_generator.templates import cmd_template


class CMDReportGeneratorService(CMDReportGenerator):
    def generate_report(
        self, data: Mapping[str, pd.DataFrame], dataset_name: str
    ) -> None:
        print("Generating command-line report...")
        print(f"Dataset Name: {dataset_name}")

        if not data:
            print("No issue with data.")
            return

        formatted = {
            issue: {
                "table": tabulate(
                    value.values.tolist(),
                    headers=list(value.columns),
                    tablefmt="psql",
                ),
                "count": len(value),
            }
            for issue, value in data.items()
        }

        template = Template(cmd_template.REPORT_TEMPLATE)
        report = template.render(tables=formatted)

        print(report)
