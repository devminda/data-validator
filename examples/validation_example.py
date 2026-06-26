import pandas as pd

from app.services.pipelines.validate import validate_data

if __name__ == "__main__":
    hr_data = [
        {
            "employee_id": 1001,
            "name": "Alice Johnson",
            "department": "Finance",
            "salary": 72000,
            "age": 29,
            "date_of_birth": "2994-07-20",
            "hire_date": "2022-04-18",
        },
        {
            "employee_id": 1002,
            "name": "Bob Smith",
            "department": "Engineering",
            "salary": 91000,
            "age": 34,
            "date_of_birth": "1989-12-15",
            "hire_date": "2021-08-02",
        },
        {
            "employee_id": 1003,
            "name": "",
            "department": "Finance",
            "salary": -5000,
            "age": 41,
            "date_of_birth": "1983-05-10",
            "hire_date": "2023-02-10",
        },
        {
            "employee_id": 1004,
            "name": "Emily Davis",
            "department": None,
            "salary": 65000,
            "age": 25,
            "date_of_birth": "1998-03-25",
            "hire_date": "2030-01-01",
        },
        {
            "employee_id": 1002,
            "name": "Bob Smith",
            "department": "Engineering",
            "salary": 91000,
            "age": 34,
            "date_of_birth": "1989-12-15",
            "hire_date": "2021-08-02",
        },
    ]

    df = pd.DataFrame(hr_data)
    df.to_csv("hr.csv", index=False)

    validate_data("hr.csv", "csv", "hr")
