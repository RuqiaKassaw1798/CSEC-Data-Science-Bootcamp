import random

def simulate_crashes(days):
    p_crash = 0.045
    crashes = sum(1 for _ in range(days) if random.random() < p_crash)
    return crashes / days