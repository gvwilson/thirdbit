import sys
import simpy

def main():
    env = simpy.Environment()
    env.process(worker(env, worker_id=1, num_jobs=3, job_time=2))
    env.process(worker(env, worker_id=2, num_jobs=3, job_time=3))
    env.run()
    print(f"Simulation completed at T={env.now}")


def worker(env, worker_id, num_jobs, job_time):
    """Actor with fixed-time jobs."""
    print(f"T={env.now} worker {worker_id} starts")

    for job_num in range(num_jobs):
        print(f"T={env.now} worker {worker_id} starts job {job_num} duration {job_time}")
        yield env.timeout(job_time)
        print(f"T={env.now} worker {worker_id} finishes job {job_num}")

    print(f"T={env.now} worker {worker_id} finishes")


if __name__ == "__main__":
    main()
