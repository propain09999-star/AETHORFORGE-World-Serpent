import subprocess, time
from pathlib import Path

def get_telemetry() -> dict:
    """Real device stats from /proc — works on Termux"""
    # RAM
    try:
        lines = open("/proc/meminfo").readlines()
        total = int(lines[0].split()[1]) // 1024
        avail = int(lines[2].split()[1]) // 1024
        used  = total - avail
    except:
        total = used = avail = 0

    # CPU load
    try:
        load = open("/proc/loadavg").read().split()[0]
    except:
        load = "?"

    # Storage
    try:
        r = subprocess.run(["df", "-h", str(Path.home())],
            capture_output=True, text=True)
        storage = r.stdout.split("\n")[1].split()[3] + " free"
    except:
        storage = "?"

    # Uptime
    try:
        secs = float(open("/proc/uptime").read().split()[0])
        h, m = int(secs // 3600), int((secs % 3600) // 60)
        uptime = f"{h}h {m}m"
    except:
        uptime = "?"

    return {
        "ram_used_mb":  used,
        "ram_total_mb": total,
        "ram_free_mb":  avail,
        "cpu_load":     load,
        "storage":      storage,
        "uptime":       uptime,
        "timestamp":    time.strftime("%H:%M:%S"),
    }

if __name__ == "__main__":
    import json
    print(json.dumps(get_telemetry(), indent=2))

