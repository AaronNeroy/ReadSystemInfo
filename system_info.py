"""
system_info.py
==============
Pulls key hardware and OS information from the local machine and displays
it in a clean, readable report. Optionally saves the output to a .txt file.

Requirements:
    pip install psutil
"""

import platform
import socket
import datetime
import os
import psutil


def bytes_to_gb(bytes_val):
    return round(bytes_val / (1024 ** 3), 2)


def get_os_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }


def get_cpu_info():
    freq = psutil.cpu_freq()
    return {
        "CPU": platform.processor() or "N/A",
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Max Frequency (MHz)": round(freq.max, 2) if freq else "N/A",
        "Current Frequency (MHz)": round(freq.current, 2) if freq else "N/A",
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
    }


def get_ram_info():
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "Total RAM (GB)": bytes_to_gb(ram.total),
        "Available RAM (GB)": bytes_to_gb(ram.available),
        "Used RAM (GB)": bytes_to_gb(ram.used),
        "RAM Usage (%)": ram.percent,
        "Total Swap (GB)": bytes_to_gb(swap.total),
        "Used Swap (GB)": bytes_to_gb(swap.used),
    }


def get_disk_info():
    disks = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append({
                "Device": partition.device,
                "Mount Point": partition.mountpoint,
                "File System": partition.fstype,
                "Total (GB)": bytes_to_gb(usage.total),
                "Used (GB)": bytes_to_gb(usage.used),
                "Free (GB)": bytes_to_gb(usage.free),
                "Usage (%)": usage.percent,
            })
        except PermissionError:
            continue
    return disks


def print_section(title, data):
    print(f"\n{'='*45}")
    print(f"  {title}")
    print(f"{'='*45}")
    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            print(f"\n  [Disk {i}]")
            for key, val in item.items():
                print(f"    {key:<25} {val}")
    else:
        for key, val in data.items():
            print(f"  {key:<30} {val}")


def generate_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"  SYSTEM INFORMATION REPORT")
    print(f"  Generated: {timestamp}")


    sections = {
        "OPERATING SYSTEM": get_os_info(),
        "CPU": get_cpu_info(),
        "MEMORY (RAM)": get_ram_info(),
        "DISK STORAGE": get_disk_info(),
    }

    for title, data in sections.items():
        print_section(title, data)

    print(f"")
    return sections


def save_report(sections):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"system_report_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"SYSTEM INFORMATION REPORT\n")
        f.write(f"Generated: {datetime.datetime.now()}\n\n")
        for title, data in sections.items():
            f.write(f"")
            f.write(f"  {title}\n")
            f.write(f"")
            if isinstance(data, list):
                for i, item in enumerate(data, 1):
                    f.write(f"\n  [Disk {i}]\n")
                    for key, val in item.items():
                        f.write(f"    {key:<25} {val}\n")
            else:
                for key, val in data.items():
                    f.write(f"  {key:<30} {val}\n")
    print(f"  Report saved to: {filename}")
    return filename


if __name__ == "__main__":
    sections = generate_report()
    save = input("Save report to file? (y/n): ").strip().lower()
    if save == "y":
        save_report(sections)
