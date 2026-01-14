import psutil
import time
from datetime import datetime


def collect_cpu_usage():
    return psutil.cpu_percent(interval=1)


def collect_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "percent": memory.percent
    }


def collect_metrics():
    timestamp = datetime.now().isoformat()

    data = {
        "timestamp": timestamp,
        "cpu_percent": collect_cpu_usage(),
        "memory": collect_memory_usage()
    }

    return data


if __name__ == "__main__":
    while True:
        metrics = collect_metrics()
        print(metrics)
        time.sleep(5)