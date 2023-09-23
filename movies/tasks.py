from celery import shared_task

import time
#simulation 10 second
@shared_task
def simulate_cpu_intensive_task():
    time.sleep(10)
    return "Task completed!"
