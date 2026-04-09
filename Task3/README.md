# Data Manipulation & Analysis

This repository contains the complete documentation and code for **Task 3**, focusing on the application of the **Pandas** library in Python. The project is divided into two parts: building a custom dataset from scratch and performing a deep-dive analysis on the historical Titanic dataset.

## 📁 Part 1: Custom Dataset Creation
**Objective:** To demonstrate the ability to construct, label, and manipulate data structures manually.

* **Task:** Created a unique DataFrame using Python dictionaries.
* **Operations:** * Defined custom columns and indices.
    * Performed initial data inspections to verify structure and data types.
    * Demonstrated basic data entry and formatting within the Pandas environment.

## 📁 Part 2: Real-World Dataset — Titanic Analysis
**Objective:** To clean and analyze a complex dataset to uncover survival patterns from the 1912 disaster.

### **1. Data Cleaning & Preparation**
* **Imputation:** Handled missing values by filling the `Age` column with the **median** and the `Embarked` column with the **mode**.
* **Feature Selection:** Dropped the `Cabin` column due to excessive missing values (sparsity).
* **Refinement:** Removed all duplicate rows to ensure statistical accuracy.

### **2. Data Analysis (Using `groupby`)**
* **Survival by Gender:** Investigated the impact of gender on survival probability.
* **Survival by Class:** Analyzed how socioeconomic status (1st, 2nd, and 3rd class) affected rescue chances.
* **Average Age per Class:** Identified age trends across different passenger classes.
* **Survival by Age Group:** Used **Binning** (`pd.cut`) to categorize passengers into *Child, Teenager, Adult,* and *Senior*.

### **3. Advanced Filtering**
Used **Boolean Indexing** to extract high-priority insights, such as identifying all female survivors and children who successfully evacuated.

---

## 📊 Final Insights
1. **Gender:** Female passengers were significantly more likely to survive (~74% survival rate).
2. **Social Class:** A clear survival "ladder" existed, where 1st-class passengers had a much higher probability of survival (63%) compared to 3rd-class passengers (24%).
3. **Prioritization:** Children were prioritized during the rescue, showing higher survival rates than most adult groups.
4. **Conclusion:** The highest survival probability was found among **1st-class female passengers**, with a near-perfect survival rate.

---

## 🛠️ Tech Stack & Requirements
* **Language:** Python 3.x
* **Libraries:** Pandas
* **Tools:** Google Colab, GitHub

## 📂 Repository Structure
```text
Task-3/
├── Custom_Dataset.ipynb  
├── Titanic_Analysis.ipynb 
├── dataset-2.csv                
└── README.md
```
