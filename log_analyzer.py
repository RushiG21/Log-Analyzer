import re
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(filename='log_analyzer.log', level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Function to read and parse logs from the file
def read_and_parse_logs(file_path):
    """
    Reads and parses a log file into structured log entries.
    Skips malformed entries with warnings.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: A list of parsed log entries as dictionaries.
        Each dictionary contains 'timestamp', 'log_level', and 'message'.
    """
    logs = []
    malformed_entries = 0
    malformed_lines = []

    if not file_path.endswith(".txt"):
        logging.error("Invalid file format. Only .txt files are supported.")
        print("Error: Invalid file format. Only .txt files are supported.")
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                
                # Try to match a valid log entry (timestamp, log level, and message)
                match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR|DEBUG) (.+)$', line)
                if match:
                    # If valid, add the entry to logs
                    logs.append({
                        "timestamp": datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S"),
                        "log_level": match.group(2),
                        "message": match.group(3)
                    })
                
                else:
                    # Otherwise, identify malformed issues
                    issues = []
                    if not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
                        issues.append("Invalid timestamp format")
                    if not re.search(r' (INFO|WARNING|ERROR|DEBUG)(\s+|$)', line):
                        issues.append("Invalid or missing log level")
                    if not re.search(r'^\s*(.+)$', line):
                        issues.append("Missing message")
                    
                    # Only add to malformed lines if there are issues
                    if issues:
                        malformed_entries += 1
                        malformed_lines.append(f"{line}  # {' & '.join(issues)}\n")

        # If there were any malformed entries, log them
        if malformed_entries:
            logging.warning(f"Skipped {malformed_entries} malformed log entries.")
            print(f"Warning: Skipped {malformed_entries} malformed log entries.")
            with open("malformed_logs.txt", "w", encoding='utf-8') as malformed_file:
                malformed_file.write(f"Skipped {malformed_entries} malformed entries.\n")
                malformed_file.write("Details of skipped entries:\n")
                malformed_file.writelines(malformed_lines)
            logging.info("Details of skipped entries have been saved to 'malformed_logs.txt'.")
            print("Details of skipped entries have been saved to 'malformed_logs.txt'.")

        return logs

    except FileNotFoundError:
        logging.error(f"The file '{file_path}' was not found.")
        print(f"Error: The file '{file_path}' was not found.")
        return []
    
    except PermissionError:
        logging.error(f"Insufficient permissions to read the file '{file_path}'.")
        print(f"Error: Insufficient permissions to read the file '{file_path}'.")
        return []

# Function to count occurrences of each log level
def count_log_levels(logs):
    """
    Counts the occurrences of each log level in the parsed logs.

    Args:
        logs (list): List of parsed log entries.

    Returns:
        dict: A dictionary with counts for each log level.
    """
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    for log in logs:
        counts[log["log_level"]] += 1
    return counts

# Function to find the most recent log entry for a specific log level
def find_most_recent_entry(logs, log_level):
    """
    Finds the most recent log entry for a specified log level.

    Args:
        logs (list): List of parsed log entries.
        log_level (str): Log level to filter by.

    Returns:
        dict or None: The most recent log entry or None if not found.
    """
    filtered_logs = [log for log in logs if log["log_level"] == log_level]
    if not filtered_logs:
        return None
    return max(filtered_logs, key=lambda log: log["timestamp"])

# Function to filter logs within a specified date range
def filter_logs_by_date_range(logs, start_date, end_date):
    """
    Filters logs within the specified date range.

    Args:
        logs (list): List of parsed log entries.
        start_date (date): Start date for the filter.
        end_date (date): End date for the filter.

    Returns:
        list: A list of filtered log entries.
    """
    return [log for log in logs if start_date <= log["timestamp"].date() <= end_date]

# Function to save filtered logs to a file
def save_filtered_logs(filtered_logs, output_path):
    """
    Saves the filtered log entries to a file.

    Args:
        filtered_logs (list): List of filtered log entries.
        output_path (str): Path to save the filtered logs.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for log in filtered_logs:
                file.write(f"{log['timestamp']} {log['log_level']} {log['message']}\n")
        print(f"Filtered logs saved to '{output_path}'.")
    except IOError as e:
        print(f"Error: Unable to save filtered logs. {e}")

# Main function
def main():
    """
    Main function to run the log analyzer.
    Handles user inputs and coordinates the processing of logs.
    """
    
    print("Welcome to the Server Log Analyzer!")
    # Prompt the user to enter the log file name
    log_file = input("Enter the name of the log file (e.g., logs.txt): ").strip()
    if log_file.lower() == "exit":
        print("Exiting the program. Goodbye!")
        return

    # Step 1: Read and parse the log file
    logs = read_and_parse_logs(log_file)
    if not logs:
        print("Error: No valid log entries found. Exiting.")
        return

    # Step 2: Count log levels
    counts = count_log_levels(logs)
    print("\nLog Level Counts:")
    for level, count in counts.items():
        print(f"{level}: {count}")

    # Step 3: Find the most recent log entry for a given log level
    valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG"}
    log_level = input("\nEnter log level to find the most recent entry (INFO, WARNING, ERROR, DEBUG): ").strip().upper()
    while log_level not in valid_levels:
        log_level = input("Invalid log level. Enter one of (INFO, WARNING, ERROR, DEBUG): ").strip().upper()

    recent_entry = find_most_recent_entry(logs, log_level)
    if recent_entry:
        print("\nMost Recent Log Entry:")
        print(f"{recent_entry['timestamp']} {recent_entry['log_level']} {recent_entry['message']}")
    else:
        print("No entries found for the specified log level.")

    # Step 4: Filter logs by date range
    while True:
        try:
            start_date = datetime.strptime(input("\nEnter start date (YYYY-MM-DD): ").strip(), "%Y-%m-%d").date()
            end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): ").strip(), "%Y-%m-%d").date()
            if start_date > end_date:
                print("Error: Start date cannot be after end date.")
            else:
                break
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    filtered_logs = filter_logs_by_date_range(logs, start_date, end_date)
    if filtered_logs:
        save_filtered_logs(filtered_logs, "filtered_logs.txt")
    else:
        print("No logs found in the specified date range.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")