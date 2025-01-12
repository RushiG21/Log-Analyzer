# Server Log Analyzer

## Overview
The Server Log Analyzer is a Python-based tool for analyzing server logs. It parses log files, extracts meaningful insights, and provides filtering and reporting functionality. This tool is designed to handle invalid entries gracefully and supports multiple features such as log level counting, most recent entry retrieval, and filtering by date range.

---

## Features
1. **Read and Parse Logs**: Parses logs into structured data and handles malformed entries.
2. **Count Log Levels**: Counts occurrences of log levels (INFO, WARNING, ERROR, DEBUG).
3. **Find Most Recent Entry**: Finds the most recent log entry for a specified log level.
4. **Filter Logs by Date Range**: Filters logs within a specified date range and saves them to a file.
1. **Log Level Count**: Display the number of occurrences for each log level (INFO, WARNING, ERROR, DEBUG).
2. **Most Recent Log Entry**: Retrieve the most recent log entry for a specified log level.
3. **Filter Logs by Date Range**: Extract and save logs within a specified date range to a file.
4. **Error Handling**: Manage invalid log entries, empty files, and edge cases effectively.

---

## Requirements
- Python 3.8+

---

## Installation
1. Clone the repository or download the script.
2. Ensure you have Python 3.8 or higher installed.
3. Install any required dependencies (none required for the base functionality).

---

## Usage

### Input
- The program expects a log file named `logs.txt` in the following format:

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
1. Place your `logs.txt` file in the same directory as the script.
2. Execute the script using:
   ```bash
   python log_analyzer.py
   ```
3. Follow the prompts:
   - Enter the log level (INFO, WARNING, ERROR, DEBUG) to find the most recent entry.
   - Enter a start and end date in `YYYY-MM-DD` format to filter logs.

### Output
- **Log Level Counts**: Displays on the console.
- **Most Recent Log Entry**: Displays the most recent log entry for the specified log level.
- **Filtered Logs**: Saved to `filtered_logs.txt` in the same directory.

---

## Assumptions
1. Logs are well-formed except for occasional malformed entries.
2. Log timestamps are in the `YYYY-MM-DD HH:MM:SS` format.
3. The date range for filtering is inclusive.

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
1. Include test log files to validate the script functionality.
2. Run basic tests by modifying the `logs.txt` file and observing outputs.
