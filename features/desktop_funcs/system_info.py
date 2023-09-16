import psutil

def get_system_info():
    # Get CPU information
    cpu_info = f"CPU utilization: {psutil.cpu_percent()}%\n"

    # Get memory information
    virtual_memory = psutil.virtual_memory()
    memory_info = f"Memory used: {virtual_memory.percent}%\n"

    # Get disk information
    partitions = psutil.disk_partitions()
    disk_info = ""
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info += f"{partition.device} drive used - {usage.percent}%\n"

    system_info = f"System Information:\n{cpu_info}{memory_info}{disk_info}"
    return system_info