from celery import shared_task

import time

@shared_task
def simulate_cpu_intensive_task():
    time.sleep(5)
    return "Task completed!"
