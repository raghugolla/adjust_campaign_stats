from voluptuous import Schema, Optional, Invalid
from shuttlis import validators
from shuttlis.validators import datetime_validator

possible_group_by_fields = ["channel", "country", "os", "campaign_date"]

bulk_create_schema = Schema(
    {
        Optional("url"): str,
    }
)


def validate_group_by(value):
    try:
        group_by_fields = [string for string in value.split(",")]

        if not all(x in possible_group_by_fields for x in group_by_fields):
            raise Invalid("Please provide valid group by fields")
    except Exception as e:
        raise Invalid(str(e))


search_schema = Schema(
    {
        Optional("channels"): validators.csv_strings,
        Optional("countries"): validators.csv_strings,
        Optional("os"): validators.csv_strings,
        Optional("from_time"): datetime_validator,
        Optional("to_time"): datetime_validator,
        Optional("group_by"): validate_group_by,
        Optional("sum_of"): validators.csv_strings,
        Optional("order_by"): str,
        Optional("order"): str,
        Optional("cpi"): str,
    }
)
