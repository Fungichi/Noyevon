# Noyevon (Readme AI-Generated :) )

## Description
This Python script checks the status of the `VeyonService` Windows service every 5 seconds. If the service is running, the script attempts to stop it. The script requires administrator privileges to function properly.

## Prerequisites
- Windows operating system
- Python installed (version 3.x recommended)

## Requirements
- The script must be run with administrator privileges to stop the service.
- Python's `subprocess`, `ctypes`, `sys`, and `time` modules (these are built-in and require no additional installation).

## Installation
1. Download the script and save it to your preferred location.
2. Ensure you have Python installed on your system.

## Usage
1. Open a command prompt as administrator.
2. Navigate to the directory where the script is located.
3. Run the script using:
   ```sh
   python script_name.py
   ```

## How It Works
- The script continuously checks the status of `VeyonService` using the `sc query` command.
- If the service is running, it attempts to stop it using the `sc stop` command.
- If the script is not run with administrative privileges, it automatically attempts to restart itself with elevated permissions.

## Notes
- If the service fails to stop, an error message will be displayed.
- The script runs in an infinite loop with a 5-second delay between checks.

## License
This script is provided as-is, without any guarantees. Use at your own risk.

## Author
Your Name (Replace with your actual name)

