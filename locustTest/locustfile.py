from locust import HttpUser, between ,task

class WebsireUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        print("Starting up Login Test...")
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def about(self):
        self.client.get("/about/")