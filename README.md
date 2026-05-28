Displays hardware and OS information for the machine that runs the script. Useful for IT support and quick system diagnostics.


- OS name, version, architecture, hostname, and IP address
- CPU model, core count, frequency, and current usage
- RAM total, used, available, and swap details
- Disk partitions with size, usage, and file system type
- Option to save the report as a timestamped `.txt` file

## Requirements

- Python 3.7+

- psutil library
pip install psutil


## How to Run
Write in terminal:
python system_info.py

Optional input to save displayed information to a file

## Example Output


  SYSTEM INFORMATION REPORT
  Generated: 2026-05-28 10:45:22


---------------------------------------------
  OPERATING SYSTEM
---------------------------------------------
  OS                             Windows
  OS Version                     10.0.22621
  Hostname                       DESKTOP-ABC123
  IP Address                     192.168.1.10

---------------------------------------------
  CPU
---------------------------------------------
  Physical Cores                 8
  Logical Cores                  16
  CPU Usage (%)                  12.4

  

## Skills Demonstrated

- Python scripting
- Use of psutil and platform libraries
- Structured data collection and output formatting
- File I/O for saving reports
