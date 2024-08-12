import pytest
from log_parser import parse_antivirus_log

def test_parse_antivirus_log():
    log_string = r"(actual_string_to_be_replaced)"
    expected_result = {} #Expected dict to be replaced
    assert parse_antivirus_log(log_string) == expected_result
