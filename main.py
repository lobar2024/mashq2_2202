class FakeLogger:
    def __init__(self):
        self.messages = []

    def log(self, msg):
        self.messages.append(msg)

fake = FakeLogger()

class Service:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("run")

svc = Service(fake)
svc.run()
print(fake.messages)  # ['run']
