import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def submitForm(self):
        self.client.post("/predict", json={"sq ft":"100000", "homevalue":"999999999999"})
