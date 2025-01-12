import pytest
from datetime import datetime
from log_analyzer import read_and_parse_logs, count_log_levels, find_most_recent_entry, filter_logs_by_date_range

# Test data
logs = [
    {"timestamp": datetime(2025, 1, 10, 9, 23, 45), "log_level": "INFO", "message": "Application started"},
    {"timestamp": datetime(2025, 1, 10, 9, 25, 0), "log_level": "WARNING", "message": "Disk space low"},
    {"timestamp": datetime(2025, 1, 10, 9, 26, 30), "log_level": "ERROR", "message": "Unable to connect to database"},
    {"timestamp": datetime(2025, 1, 10, 9, 30, 15), "log_level": "INFO", "message": "User logged in"},
    {"timestamp": datetime(2025, 1, 10, 9, 35, 20), "log_level": "ERROR", "message": "Timeout occurred"},
]

# Test for read_and_parse_logs
def test_read_and_parse_logs(tmp_path):
    test_file = tmp_path / "logs.txt"
    test_file.write_text(
        "2025-01-10 09:23:45 INFO Application started\n"
        "2025-01-10 09:25:00 WARNING Disk space low\n"
        "Malformed entry\n"
        "2025-01-10 09:26:30 ERROR Unable to connect to database\n"
    )
    
    parsed_logs = read_and_parse_logs(str(test_file))
    assert len(parsed_logs) == 3
    assert parsed_logs[0]["log_level"] == "INFO"
    assert parsed_logs[1]["log_level"] == "WARNING"

# Test for count_log_levels
def test_count_log_levels():
    counts = count_log_levels(logs)
    assert counts == {"INFO": 2, "WARNING": 1, "ERROR": 2, "DEBUG": 0}

# Test for find_most_recent_entry
def test_find_most_recent_entry():
    most_recent_error = find_most_recent_entry(logs, "ERROR")
    assert most_recent_error["message"] == "Timeout occurred"
    assert most_recent_error["timestamp"] == datetime(2025, 1, 10, 9, 35, 20)

    most_recent_info = find_most_recent_entry(logs, "INFO")
    assert most_recent_info["message"] == "User logged in"

# Test for filter_logs_by_date_range
def test_filter_logs_by_date_range():
    start_date = datetime(2025, 1, 10).date()
    end_date = datetime(2025, 1, 10).date()
    filtered_logs = filter_logs_by_date_range(logs, start_date, end_date)
    assert len(filtered_logs) == 5

    start_date = datetime(2025, 1, 10).date()
    end_date = datetime(2025, 1, 10).date()
    filtered_logs = filter_logs_by_date_range(logs, start_date, end_date)
    assert len(filtered_logs) == 5

# Test for empty log input
def test_empty_logs():
    empty_logs = []
    assert count_log_levels(empty_logs) == {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    assert find_most_recent_entry(empty_logs, "ERROR") is None
    assert filter_logs_by_date_range(empty_logs, datetime(2025, 1, 1).date(), datetime(2025, 1, 10).date()) == []
