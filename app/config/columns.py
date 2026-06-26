HR_COLUMNS = [
    "employee_id",
    "name",
    "department",
    "salary",
    "date_of_birth",
    "age",
    "hire_date",
]
BANKING_COLUMNS = ["order_id", "customer_id", "amount", "status", "order_date"]
ORDERS_COLUMNS = ["transaction_id", "account", "amount", "currency", "transaction_type"]
INVENTORY_COLUMNS = ["product_id", "name", "price", "quantity", "supplier"]
STUDENT_COLUMNS = ["student_id", "name", "gpa", "credits", "graduation_year"]


COLUMN_SETS = {
    "hr": HR_COLUMNS,
    "banking": BANKING_COLUMNS,
    "orders": ORDERS_COLUMNS,
    "inventory": INVENTORY_COLUMNS,
    "student": STUDENT_COLUMNS,
}
