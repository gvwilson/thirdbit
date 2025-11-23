---
title: Simulating Multiple Stages
date: 2025-11-23
---

After [yesterday's refactoring][refactoring],
we're ready to make the simulation a bit more realistic
by adding a second stage: testing.
Our updated default parameters will be:

```python
PARAMS = {
    "max_dev_time": 10.0,
    "max_test_time": 8.0,        # new
    "num_developers": 2,
    "num_testers": 3,            # new
    "random_seed": 12345,
    "simulation_time": 20,
    "task_arrival_rate": 2.0,
}
```

which will control simulation of this system:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
```

Before we start, let's make a prediction.
Development times and testing times are uniformly distributed,
so the mean for each are 5.5 and 4.5 respectively (i.e., (1+10)/2 and (1+8)/2).
With two developers,
we should be able to process one task every 2.75 timesteps;
with three testers,
we should be able to process one task every 1.5 timesteps.
We should therefore see tasks piling up in the test queue
because the testers can take them out
faster than the developers can put them in.

## The `Simulation` Class

The first step is to modify the `Simulation` class that holds all our assets
to create two queues instead of one:

```python
class Simulation:

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.Store(self.env)
        self.test_queue = simpy.Store(self.env)
```

## The `Task` Class

As described [yesterday][refactoring],
`Task` is basically a bag full of properties.
For convenience,
we have made the task generator a static method of this class
rather than a free-standing function.
In order to test our hypothesis about where tasks are going to pile up,
we will record the length of the waiting-for-development queue in each task
when it is created:

```python
class Task(Labeled):
    """A single (passive) task."""

    @staticmethod
    def generate(sim):
        """Generate tasks and add to the development queue."""

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            task["dev_queue_length"] = len(sim.dev_queue.items)
            yield sim.dev_queue.put(task)


    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self["arrived"] = sim.now
        self["dev_time"] = sim.dev_time()
        self["test_time"] = sim.test_time()
```

## The `Developer` Class

The only changes to the `Developer` are
(a) putting the task in the testing queue once development is finished
and (b) recording more information,
such as the total time this developer has spent working:

```python
class Developer(Labeled):
    """A single developer."""

    …constructor…

    def work(self):
        """Simulate work."""

        while True:
            now = self.sim.now
            task = yield self.sim.dev_queue.get()
            self["waiting"] += self.sim.now - now

            now = task["dev_start"] = self.sim.now
            yield self.sim.timeout(task["dev_time"])
            task["dev_end"] = self.sim.now
            self["working"] += self.sim.now - now

            task["test_queue_length"] = len(self.sim.dev_queue.items)
            yield self.sim.test_queue.put(task)
```

Deciding what information to record was
the hardest part of writing this version of the simulation.
Should each developer keep a list of the time spent per task
rather than just summing it up?
That felt redundant,
given that we're recording development time in each task.
But what about recording which developers do which tasks?
Or keeping track of how much time each developer spent waiting for a task to appear?
In the end we decided to record the latter but not the former.

Each of these decisions constrains what questions we can ask about our development process.
One of the reasons to use a tool like [Swarmia][swarmia] is that
they have thought through these questions
and figured out what to collect in order to get useful answers.

## The `Tester` Class

Each tester takes jobs from the testing queue,
spends some time working on them,
and records a few statistics.
The code is almost the same as that for a developer,
but after reorganizing it a couple of times
we decided that two separate classes would be easier to understand
than one class with a couple of `if` statements to control behavior:

```python
class Tester(Labeled):
    """A single (active) tester."""

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.sim = sim

    def work(self):
        """Simulate work."""

        while True:
            now = self.sim.now
            task = yield self.sim.test_queue.get()
            self["waiting"] += self.sim.now - now

            now = task["test_start"] = self.sim.now
            yield self.sim.timeout(task["test_time"])
            self["working"] += self.sim.now - now
            task["test_end"] = self.sim.now
```

## The Main Driver

We haven't shown `main` in a while,
so here is what it has become:

```python
def main(params):
    """Main driver."""

    # Handle command-line arguments and parameters.
    args = parse_args()
    update_params(params, args.params)
    random.seed(params["random_seed"])

    # Create and run the simulation and its processes.
    sim = Simulation(params)
    sim.process(Task.generate(sim))
    for _ in range(params["num_developers"]):
        dev = Developer(sim)
        sim.process(dev.work())
    for _ in range(params["num_testers"]):
        tester = Tester(sim)
        sim.process(tester.work())
    sim.run()

    # Report results.
    log = make_log(sim)
    if args.table:
        table = PrettyTable()
        table.field_names = log[0]
        table.add_rows(log[1:])
        table.align = TABLE_ALIGNMENT
        print(table)
    else:
        csv.writer(sys.stdout, lineterminator="\n").writerows(log)
```

## The Output, and Why

Running the simulation with the default parameters shown earlier
produces this output:

```
kind,id,key,value
parameter,,max_dev_time,10.0
parameter,,max_test_time,8.0
parameter,,num_developers,2
parameter,,num_testers,3
parameter,,random_seed,12345
parameter,,simulation_time,20
parameter,,task_arrival_rate,2.0
task,0,arrived,1.08
task,0,dev_queue_length,0
task,0,dev_time,1.09
task,0,dev_start,1.08
task,0,dev_end,2.17
task,0,test_queue_length,0
task,0,test_time,6.78
task,0,test_start,2.17
task,0,test_end,8.95
task,1,arrived,1.79
task,1,dev_queue_length,0
task,1,dev_time,4.32
…
…many more lines here…
…
task,13,test_time,6.77
task,13,test_start,0.0
task,13,test_end,0.0
developer,0,working,16.01
developer,0,waiting,2.37
developer,1,working,8.51
developer,1,waiting,1.89
tester,0,working,6.78
tester,0,waiting,7.53
tester,1,working,9.58
tester,1,waiting,8.53
tester,2,working,5.74
tester,2,waiting,13.8
```

which is much easier to read as a table:

| kind      |   id | key               | value |
| :---------|----: | :-----------------|-----: |
| parameter | None | max_dev_time      |  10.0 |
| parameter | None | max_test_time     |   8.0 |
| parameter | None | num_developers    |     2 |
| parameter | None | num_testers       |     3 |
| parameter | None | random_seed       | 12345 |
| parameter | None | simulation_time   |    20 |
| parameter | None | task_arrival_rate |   2.0 |
| task      |    0 | arrived           |  1.08 |
| task      |    0 | dev_queue_length  |     0 |
| task      |    0 | dev_time          |  1.09 |
| task      |    0 | dev_start         |  1.08 |
| task      |    0 | dev_end           |  2.17 |
| task      |    0 | test_queue_length |     0 |
| task      |    0 | test_time         |  6.78 |
| task      |    0 | test_start        |  2.17 |
| task      |    0 | test_end          |  8.95 |
| task      |    1 | arrived           |  1.79 |
| task      |    1 | dev_queue_length  |     0 |
| task      |    1 | dev_time          |  4.32 |
| …         |    … | …                 |     … |
| …         |    … | …                 |     … |
| task      |   13 | test_time         |  6.77 |
| task      |   13 | test_start        |   0.0 |
| task      |   13 | test_end          |   0.0 |
| developer |    0 | working           | 16.01 |
| developer |    0 | waiting           |  2.37 |
| developer |    1 | working           |  8.51 |
| developer |    1 | waiting           |  1.89 |
| tester    |    0 | working           |  6.78 |
| tester    |    0 | waiting           |  7.53 |
| tester    |    1 | working           |  9.58 |
| tester    |    1 | waiting           |  8.53 |
| tester    |    2 | working           |  5.74 |
| tester    |    2 | waiting           |  13.8 |

This is not the most readable way to format the output for human consumption:
it would be more natural to store the simulation parameters in a two-column table,
then use another table with ten columns for tasks
(one for the ID, the others for arrival time, queue lengths, development time, and so on).
However,
there isn't a standard format for storing multiple tables in a single text file.
Our options are therefore:

1.  Create multiple output files for each simulation,
    which would be a pain to manage.
2.  Use JSON or YAML,
    which would be even less readable than the four-column output shown above.
3.  Create a multi-sheet spreadsheet or use a binary format like SQLite or HDF5,
    none of which play nicely with version control.

Having all the output in a single file will make it relatively easy to build analysis tools:
we can load all the data from a single simulation into a single dataframe,
then filter to pull out data for tasks, developers, and testers,
and finally pivot it to create a wide table for each.
We'll tackle that tomorrow,
and then see if our hypothesis about developers being a bottleneck is true.

[refactoring]: @root/2025/11/22/refactoring-the-simulation/
[swarmia]: https://www.swarmia.com/
