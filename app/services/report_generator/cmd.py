from typing import Mapping

import pandas as pd
from jinja2 import Template
from tabulate import tabulate

from app.services.report_generator.base import CMDReportGenerator
from app.services.report_generator.templates import cmd_template


class CMDReportGeneratorService(CMDReportGenerator):
    def generate_report(self, data: Mapping[str, pd.DataFrame]) -> None:
        print("Generating command-line report...")

        if not data:
            print("No issue with data.")
            return

        formatted = {
            issue: tabulate(
                value.values.tolist(),
                headers=list(value.columns),
                tablefmt="psql",
            )
            for issue, value in data.items()
        }

        template = Template(cmd_template.REPORT_TEMPLATE)
        report = template.render(tables=formatted)

        print(report)
