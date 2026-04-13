# 🏭 Steel Industry Energy Audit & Efficiency Analysis

### **Project Overview**
This project provides a **Digital Energy Audit** of a steel manufacturing facility. Using a high-resolution time-series dataset (35,040 observations at 15-minute intervals), I developed an analytical pipeline in Python to identify operational inefficiencies, quantify "vampire" power loads, and provide actionable engineering recommendations for cost reduction and grid stability.

### **The Real-Life Problem**
Industrial facilities like steel plants are the largest consumers of electricity. They face three primary challenges that this project addresses:
1.  **Hidden Inefficiency (The Standby Paradox):** High energy waste during "standby" hours that is invisible on standard monthly bills.
2.  **Peak Demand Penalties:** Massive utility surcharges caused by simultaneous machinery startups (Inrush Current).
3.  **Power Quality Issues:** Grid instability and heat losses caused by excessive Reactive Power.

---

### **Key Technical Features**
* **Creative Feature Engineering:** Developed a custom **Efficiency Index** to quantify the ratio of useful work (Active Power) vs. total grid draw.
* **Forensic Data Cleaning:** Implemented a **Grouped Median Imputation (MNAR Protocol)** to repair sensor dropouts without biasing operational trends.
* **Statistical Outlier Auditing:** Utilized the **Interquartile Range (IQR) method** to mathematically define and map "Peak Surge" events.
* **Multi-Dimensional Correlation:** Analyzed the relationship between efficiency, reactive waste, and carbon intensity.

---

### **Major Insights**
| Insight | Finding | Engineering Impact |
| :--- | :--- | :--- |
| **The Standby Paradox** | Efficiency collapses by **66.29%** during light-load shifts. | Justifies a "Hard Shutdown" protocol for idling machinery. |
| **Peak Surge Risk** | Surges > **123.29 kWh** are **2.05%** more likely during Max Load. | Justifies a "Staggered Startup Schedule" to avoid peak penalties. |
| **Sustainability Link** | Strong **-0.88 correlation** between efficiency and Carbon Intensity. | Proves that energy optimization is the primary driver for Green Manufacturing. |
| **Production Bound** | Positive **+0.31 correlation** between waste and efficiency. | Proves the need for **Power Factor Correction** to optimize low-load states. |

---

### **Technology Stack**
* **Language:** Python 3
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Statistical Analysis:** Scipy

---

### **How to Use**
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RuqiaKassaw1798/CSEC-Data-Science-Bootcamp.git](https://github.com/RuqiaKassaw1798/CSEC-Data-Science-Bootcamp.git)
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd "The Final project"
    ```
3.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
4.  **Run the analysis:** Open `steel_industry_analysis.ipynb` in Jupyter Lab or Google Colab.
---
