REPORT_TEMPLATE = """
{% for issue, details in tables.items() %}
=== {{ issue.upper() }} ===
Records affected: {{ details.count }}

{{ details.table }}

{% endfor %}
"""
