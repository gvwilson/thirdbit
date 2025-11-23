from collections import defaultdict
import random
import simpy
import sys

NUM = 100000
DELAY = 1

def create(env, which, queue):
    for i in range(NUM):
        item = f"{which}"
        yield queue.put(item)
        yield env.timeout(DELAY)

def consume(env, left, right, seen):
    for _ in range(2 * NUM):
        left_get = left.get()
        right_get = right.get()
        result = yield (left_get | right_get)
        if len(result.events) == 2:
            choice = random.choice(["left", "right"])
        elif left_get in result.events:
            choice = "left"
        else:
            choice = "right"
        if choice == "left":
            item = result[left_get]
            right_get.cancel()
        else:
            item = result[right_get]
            left_get.cancel()
        seen[item] += 1

if len(sys.argv) > 1:
    random.seed(int(sys.argv[1]))
env = simpy.Environment()
left = simpy.Store(env)
right = simpy.Store(env)
seen = defaultdict(int)
env.process(create(env, "left", left))
env.process(create(env, "right", right))
env.process(consume(env, left, right, seen))
env.run()
print(seen)
