from locust import HttpUser, task, between

class ChatUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def send_message(self):
        payload = {"user_id": 42, "message": "Load test message!"}
        headers = {"Content-Type": "application/json"}
        with self.client.post("/chat", json=payload, headers=headers, catch_response=True) as resp:
            if resp.status_code == 201 or resp.status_code == 200:
                resp.success()
            else:
                resp.failure(f"Unexpected status {resp.status_code}")

        self.client.post("http://localhost:5000/chat", json=payload)
