from django.test import TestCase
from movies.tasks import simulate_cpu_intensive_task

class CeleryTaskTest(TestCase):
    def test_simulate_cpu_intensive_task(self):
        result = simulate_cpu_intensive_task.delay().get()
        self.assertEqual(result, 'Task completed!')
