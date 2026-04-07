# Statistical Analysis & Simulation Project
## Project Overview
The goal of this assignment was to build a functional Python-based statistical engine from scratch and use it to analyze raw data (Startup Salaries). Additionally, I implemented a Monte Carlo simulation to demonstrate the Law of Large Numbers (LLN) using server crash probabilities.
## 1. Mathematical Implementation
I developed the StatEngine class to process numerical data using the following formulas:
 * Mean & Median: Standard calculations for central tendency. For the median, the code specifically checks if the dataset length is even or odd to ensure accuracy.
 * Mode: Designed to handle "multimodal" cases (where more than one number repeats equally). It returns a clear message if all values in the dataset are unique.
 * Variance & Std Deviation: Implemented both Population Variance and Sample Variance (which uses n-1 for Bessel's Correction). This allows the engine to be used for different types of data analysis.
 * Outliers: Used the "2 Standard Deviations" rule to flag extreme values in the salary dataset.
## 2. Simulation & The Law of Large Numbers
In Part 2, I created a simulation for a startup's server failure rate (set at a theoretical 4.5%).
Key Findings:
 * When running the simulation for a small number of days (e.g., 10 or 100), the "Simulated Probability" varies significantly from the 4.5% target.
 * As the number of days increases to 100,000, the error drops almost to zero.
 * Conclusion: This demonstrates that small datasets are unreliable for predicting yearly budgets. A startup needs a large amount of historical data to accurately forecast maintenance costs.
## 3. How to Run the Project
I have organized the project into the required folder structure (src, data, tests).
 1. Run the Main Analysis:
   Execute the following command in the terminal to see the salary stats and simulation results:
  
   python main.py
   
   
 2. Run the Unit Tests:
   To verify the math logic in stat_engine.py:
  
   python -m unittest discover tests
   
   
## 4. Requirements Checklist
 * [x] Standard Python libraries only (math, random, unittest).
 * [x] Robust error handling for empty lists and mixed data types.
 * [x] Correct folder structure as per the assessment instructions.