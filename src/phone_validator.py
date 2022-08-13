"""This module conatins functions to validate a phone number."""
import re

def phone_validator(phone_number: str) -> bool:
    """
    Validates a spanish phone number.

    valid formats:
        972-35-56-57
        (972)355-567
        972-355-567
        972 355 567
        972355567
        34 972 355 567

    :param phone_number: The phone number to validate.
    :return: True if the phone number is valid, False otherwise.
    """

    # Optional starting whit 34
    regex_starting_34 = r"^(34)?"

    # first 3 digits with or without parenthesis. It can start with space or -
    regex_first_group_with_parenthesis = r"[-\s]?(\([0-9]{3}\))"
    regex_first_group_without_parenthesis = r"[-\s]?([0-9]{3})"

    # Remaining digits grouped by 3 or 2 separated by space, - or without separator
    other_digits_grouped_by_3 = r"(([-\s]?)[0-9]{3}){2}$"
    other_digits_grouped_by_2 = r"(([-\s]?)[0-9]{2}){3}$"

    regex = (
        f"{regex_starting_34}"
        f"({regex_first_group_with_parenthesis}|{regex_first_group_without_parenthesis})"
        f"({other_digits_grouped_by_3}|{other_digits_grouped_by_2})"
    )
    pattern = re.compile(regex)

    return bool(pattern.match(phone_number))
