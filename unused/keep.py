    def work(self):
        """Simulate behavior."""

        # Development.
        dev = yield self.sim.developers.get()
        self.state = Task.State.DEV
        with Elapsed(dev, "busy"):
            yield self.sim.timeout(self["dev_time"])

        # Handoff.
        self.sim.developers.put(dev)
        self.state = Task.State.WAIT_TEST

        # Testing.
        tester = yield self.sim.testers.get()
        self.state = Task.State.TEST
        with Elapsed(tester, "busy"):
            yield self.sim.timeout(self["test_time"])

        # Completion.
        self.sim.testers.put(tester)
        self.state = Task.State.COMPLETE


