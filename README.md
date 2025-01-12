# Server Log Analyzer

## Overview
The **Server Log Analyzer** is a Python tool designed to analyze server logs, extract meaningful insights, and manage log data efficiently. It supports various functionalities like log parsing, counting log levels, retrieving the most recent entries, and filtering logs by date range, all while handling errors gracefully.

---

## Features
1. **Read and Parse Logs**:
   - Parses logs into structured data and identifies malformed entries, logging them separately.
2. **Count Log Levels**:
   - Displays the number of occurrences for each log level (INFO, WARNING, ERROR, DEBUG).
3. **Find Most Recent Entry**:
   - Retrieves the most recent log entry for a specified log level.
4. **Filter Logs by Date Range**:
   - Filters log entries within a user-specified date range and saves them to a file (`filtered_logs.txt`).
5. **Error Handling**:
   - Manages malformed log entries, empty files, invalid inputs, and edge cases effectively.
6. **Unit Tests**:
   - Validates functionality using `pytest` with comprehensive test cases for all key features.

---

## Requirements
- Python 3.8 or higher.
- `pytest` for unit testing (optional).

---

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```
2. Ensure Python 3.8+ is installed on your system.
3. Install `pytest` for running unit tests (optional):
   ```bash
   pip install pytest
   ```

---

## Usage

### Input
- The program requires a log file named `logs.txt` in the following format:
  ```
  <timestamp> <log_level> <message>
  ```
  Example:
  ```
  2025-01-10 09:23:45 INFO Application started
  2025-01-10 09:25:00 WARNING Disk space low
  2025-01-10 09:26:30 ERROR Unable to connect to database
  ```

### Running the Script
1. Place `logs.txt` in the same directory as `log_analyzer.py`.
2. Execute the script:
   ```bash
   python log_analyzer.py
   ```
3. Follow the prompts:
   - Enter a log level (INFO, WARNING, ERROR, DEBUG) to retrieve the most recent entry.
   - Specify a date range in `YYYY-MM-DD` format to filter logs.

### Outputs
1. **Log Level Counts**: Displayed on the console.
2. **Most Recent Log Entry**: Displayed for the specified log level.
3. **Filtered Logs**: Saved to a file named `filtered_logs.txt`.

---

## Assumptions
1. Logs are mostly well-formed, except for occasional malformed entries.
2. Timestamps follow the `YYYY-MM-DD HH:MM:SS` format.
3. Filtering by date range includes both start and end dates.

---

## Sample Input and Output

### Sample Input
**logs.txt**:
```
2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high
```

**User Input**:
1. Log Level: ERROR  
2. Date Range: Start = 2025-01-10, End = 2025-01-10  

### Expected Output
**Console**:
```
Log Level Counts:
INFO: 1
WARNING: 2
ERROR: 2
DEBUG: 0

Most Recent Entry:
2025-01-10 09:35:20 ERROR Timeout occurred

Filtered logs saved to filtered_logs.txt
```

**filtered_logs.txt**:
```
2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high
```

---

## Testing

### Unit Testing with `pytest`
Unit tests validate the correctness of the script. They are written in a separate file, typically named `test_log_analyzer.py`. Example tests include:

1. **Test for Parsing Logs**:
   - Ensures `read_and_parse_logs` correctly parses valid entries and skips malformed ones.

2. **Test for Counting Log Levels**:
   - Verifies the counts of each log level using `count_log_levels`.

3. **Test for Most Recent Log Entry**:
   - Checks if `find_most_recent_entry` retrieves the correct entry for a given log level.

4. **Test for Filtering Logs by Date Range**:
   - Validates that `filter_logs_by_date_range` correctly filters logs within the specified date range.

5. **Test for Edge Cases**:
   - Handles scenarios like empty input, invalid date ranges, and nonexistent log levels.

### Running the Tests
Run the tests using `pytest`:
```bash
pytest test_log_analyzer.py
```

Sample `pytest` Output:
```
============================= test session starts ==============================
platform linux -- Python 3.x.y, pytest-X.Y.Z
rootdir: /path/to/your/project
collected 5 items

test_log_analyzer.py .....                                             [100%]

============================== 5 passed in 0.12s ===============================
```

---
