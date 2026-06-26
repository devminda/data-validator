REPORT_TEMPLATE = """
{% for issue, table in tables.items() %}
=== {{ issue.upper() }} ===
{{ table }}

{% endfor %}
"""
