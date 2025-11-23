import random
import simpy
import sys

NUM = 10
DELAY = 1

def create(env, which, queue):
    for i in range(NUM):
        item = f"{which}-{i}"
        yield queue.put(item)
        yield env.timeout(DELAY)

def consume(left, right):
    for _ in range(2 * NUM):

        choice = None
        if left.items and right.items:
            choice = random.choice(["left", "right"])
        elif left.items:
            choice = "left"
        elif right.items:
            choice = "right"

        if choice == "left":
            item = yield left.get()
            print("single", item)

        elif choice == "right":
            item = yield right.get()
            print("single", item)

        else:
            left_get = left.get()
            right_get = right.get()
            result = yield left_get | right_get
            if left_get in result.events:
                item = result[left_get]
                print("double", item)
                right_get.cancel()
            else:
                item = result[right_get]
                print("double", item)
                left_get.cancel()

random.seed(int(sys.argv[1]))
env = simpy.Environment()
left = simpy.Store(env)
right = simpy.Store(env)
env.process(create(env, "left", left))
env.process(create(env, "right", right))
env.process(consume(left, right))
env.run()
