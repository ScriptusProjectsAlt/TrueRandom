import time
import hashlib

def get_entropy():
    data = []

    for _ in range(300):
        start = time.perf_counter_ns()
        sum(i*i for i in range(100))
        end = time.perf_counter_ns()
        data.append(end - start)

    return hashlib.sha256(str(data).encode()).digest()