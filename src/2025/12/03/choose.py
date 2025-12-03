import simpy

N_TASK = 2
T_GEN = 1
T_DEV = 1
T_TEST = 1
T_SIM = 10

class Task:
    def __init__(self, ident):
        self.ident = ident
        self.count = 0

    def __str__(self):
        return f"task-{self.ident}/{self.count}"


class Worker:
    def __init__(self, sim):
        self.sim = sim

    @property
    def now(self):
        return self.sim.env.now

    def __str__(self):
        return f"{self.__class__.__name__}/{self.now:.2f}"


class DeveloperWrong(Worker):
    def work(self):
        while True:
            # Get either a task for development or a task for rework.
            req_dev = self.sim.q_dev.get()
            req_rework = self.sim.q_rework.get()
            print(f"{self}: wait for task(s)")
            result = yield simpy.AnyOf(self.sim.env, [req_dev, req_rework])

            # Give priority to rework.
            if req_rework in result:
                task = result[req_rework]
                print(f"{self} got {task} from rework with {len(result.events)} events")
            elif req_dev in result:
                task = result[req_dev]
                print(f"{self} got {task} from dev with {len(result.events)} events")
            else:
                assert False, "how did we get here?"

            # Do development.
            yield self.sim.env.timeout(T_DEV)

            # Put the task in the testing queue.
            yield self.sim.q_test.put(task)
            print(f"{self}: put {task} in testing queue")


class DeveloperRight(Worker):
    def work(self):
        which = "dev"
        take = None
        while True:
            # Get either a task for development or a task for rework.
            req_dev = self.sim.q_dev.get()
            req_rework = self.sim.q_rework.get()
            print(f"{self}: wait for task(s)")
            result = yield simpy.AnyOf(self.sim.env, [req_dev, req_rework])

            # Pick one.
            if len(result.events) == 2:
                print(f"{self}: ...got two events")
                if which == "dev":
                    take = "dev"
                    which = "rework"
                else:
                    take = "rework"
                    which = "dev"
            elif req_dev in result.events:
                print(f"{self}: ...got dev")
                take = "dev"
            elif req_rework in result.events:
                print(f"{self}: ...got rework")
                take = "rework"
            else:
                assert False, "how did we get here?"

            # Now take it.
            if take == "dev":
                print(f"{self}: ...taking dev")
                task = result[req_dev]
                req_rework.cancel()
            elif take == "rework":
                print(f"{self}: ...taking rework")
                task = result[req_rework]
                req_dev.cancel()
            else:
                assert False, "how did we get here?"
            print(f"{self} got {task}")

            # Do development.
            yield self.sim.env.timeout(T_DEV)

            # Put the task in the testing queue.
            yield self.sim.q_test.put(task)
            print(f"{self}: put {task} in testing queue")


class Tester(Worker):
    def work(self):
        while True:
            # Get a task from the testing queue.
            print(f"{self}: wait for task(s)")
            task = yield self.sim.q_test.get()
            print(f"{self}: got {task}")

            # Do testing.
            yield self.sim.env.timeout(T_TEST)
            task.count += 1

            # Always put the task in the rework queue.
            yield self.sim.q_rework.put(task)
            print(f"{self}: put {task} in rework queue")


class Simulation:
    def __init__(self):
        # Environment.
        self.env = simpy.Environment()

        # One developer and one tester.
        self.developer = DeveloperRight(self)
        self.tester = Tester(self)

        # Queues for new development work, rework, and testing.
        self.q_dev = simpy.Store(self.env)
        self.q_rework = simpy.Store(self.env)
        self.q_test = simpy.Store(self.env)

    def generate(self):
        i = 0
        while True:
            task = Task(i)
            i += 1
            print(f"{self.env.now:.2f} create {task}")
            yield self.q_dev.put(task)
            yield self.env.timeout(T_GEN)

    def run(self):
        self.env.process(self.generate())
        self.env.process(self.developer.work())
        self.env.process(self.tester.work())
        self.env.run(until=T_SIM)


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
