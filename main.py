import json
import os
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def main():
    # 1. Load the mock dataset
    data_path = os.path.join('data', 'sample_salaries.json')
    try:
        with open(data_path, 'r') as f:
            raw_data = json.load(f)
            salaries = raw_data['salaries']
    except FileNotFoundError:
        print("Error: data/sample_salaries.json not found.")
        return

    # 2. Run Statistical Analysis
    print("--- Part 1: Startup Salary Analysis ---")
    engine = StatEngine(salaries)
    print(f"Successfully loaded {len(salaries)} salaries from JSON")
    
    print(f"Mean Salary:   ${engine.get_mean():,.2f}")
    print(f"Median Salary: ${engine.get_median():,.2f}")
    print(f"Mode:          {engine.get_mode()}")
    print(f"Std Deviation: ${engine.get_std_dev(is_sample=True):,.2f}")
    
    outliers = engine.get_outliers(threshold=2)
    print(f"Outliers detected (>2 Std Dev): {outliers}")
    print("-" * 40)

    # 3. Run Monte Carlo Simulation
    print("\n--- Part 2: Server Crash Simulation (LLN) ---")
    print("Theoretical Probability: 0.045 (4.5%)")
    
    intervals = [10, 100, 1000, 10000, 100000]
    for days in intervals:
        sim_prob = simulate_crashes(days)
        error = abs(0.045 - sim_prob)
        print(f"Days: {days:7} | Simulated Prob: {sim_prob:.5f} | Error: {error:.5f}")

if __name__ == "__main__":
    main()