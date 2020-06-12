from locust import TaskSet, task, HttpLocust, between


class UserBehavior(TaskSet):
    def on_start(self):
        print('Start')

    @task(1)
    def homepage(self):
        self.client.get("/")

    @task(1)
    def search_a(self):
        self.client.get('/search/50/')


class WebsiteUser(HttpLocust):
    host = "http://47.112.201.214:80"
    task_set = UserBehavior
    wait_time = between(1500, 3500)