import simpy

N_TASK = 1
T_DEV = 3
T_TEST = 2
T_SIM = 10

class Log:
    def __init__(self, who, msg):
        self.who = who
        self.msg = msg

    def __enter__(self):
        print(f"{self.who.sim.env.now:.2f} / {self.who}: START {self.msg}")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{self.who.sim.env.now:.2f} / {self.who}: END {self.msg}")

class Worker:
    def __init__(self, sim, ident):
        self.sim = sim
        self.ident = ident

    def __str__(self):
        return f"{self.__class__.__name__}-{self.ident}"

class Developer(Worker):
    def work(self):
        while True:
            with Log(self, "wait for either queue"):
                req_dev = self.sim.q_dev.get()
                req_rework = self.sim.q_rework.get()
                result = yield (req_dev | req_rework)
                task = result[list(result.keys())[0]]
            with Log(self, f"develop {task}"):
                yield self.sim.env.timeout(T_DEV)
            with Log(self, f"put {task} in testing queue"):
                yield self.sim.q_test.put(task)

class Tester(Worker):
    def work(self):
        while True:
            with Log(self, "wait for testing queue"):
                task = yield self.sim.q_test.get()
            with Log(self, f"test {task}"):
                yield self.sim.env.timeout(T_TEST)
            with Log(self, f"put {task} in rework queue"):
                yield self.sim.q_rework.put(task)

class Simulation:
    def __init__(self):
        self.env = simpy.Environment()
        self.developer = Developer(self, 0)
        self.tester = Tester(self, 0)
        self.q_dev = simpy.Store(self.env)
        self.q_rework = simpy.Store(self.env)
        self.q_test = simpy.Store(self.env)

    def generate(self):
        for i in range(N_TASK):
            yield self.q_dev.put(f"task-{i}")

    def run(self):
        self.env.process(self.generate())
        self.env.process(self.developer.work())
        self.env.process(self.tester.work())
        self.env.run(until=T_SIM)

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
