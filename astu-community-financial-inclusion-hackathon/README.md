# Zindi Financial Inclusion in Africa — 7th Place Solution

This repository contains the complete, reproducible machine learning pipeline for the **Financial Inclusion in Africa** competition hosted on Zindi. The objective is to predict whether a survey respondent has a bank account (binary classification) using demographic and socioeconomic features.

This solution avoids overly complex model blending and instead prioritizes generalization stability, achieving **Rank 7 on the Private Leaderboard** using a robustly validated, triple-seeded CatBoost architecture.

---

## 📈 Performance Summary

- **Evaluation Metric:** Mean Absolute Error (MAE) / Misclassification Rate
- **Public Leaderboard Score:** ~0.101 – 0.102 MAE
- **Private Leaderboard Rank:** 7th Place

---

## 💡 Key Architectural Pillars

### 1. Robust Validation Framework
- **Stratified 10-Fold Cross-Validation:** Preserves the highly imbalanced target distribution (~14% positive class) across every split to ensure reliable local validation.
- **Triple-Seed Ensembling:** The 10-fold split is repeated across three distinct random seeds (`42`, `2024`, and `7`). The final predictions are the averaged probabilities of all 30 trained models, smoothing out distribution noise and preventing private leaderboard shakeup.

### 2. Feature Engineering & Leakage Prevention
- **Interaction Crosses:** Captures joint socioeconomic signals via explicit combinations: `cellphone_x_urban`, `cellphone_x_edu`, `age_x_edu`, and `formal_x_urban`.
- **Domain Ratios:** Computes `household_pressure` (`household_size` / `age`) to provide non-linear dependency metrics directly to the tree splitters.
- **Data Binning:** Groups continuous age variables into life-stage bins (`age_group`) and splits household sizes into discrete bins.
- **Leakage-Free Encoding:** Implements frequency encoding for categorical variables alongside strict **Out-of-Fold (OOF) Target Encoding** to eliminate target leakage during training.

### 3. Symmetric Tree Regularization
- **CatBoost Classifier:** Chosen as the core algorithm for its native capability to process high-cardinality categorical text and its use of symmetric (oblivious) trees, which naturally regularize against overfitting on smaller datasets (~23k rows).

### 4. Post-Processing Threshold Optimization
- Since the competition evaluates on binary hits (MAE) rather than probabilities, a grid search is performed on the accumulated OOF validation predictions (scanning `0.20` to `0.65` at `0.01` steps) to pinpoint the precise decision boundary that minimizes misclassification error under class imbalance.

---

## 📂 Repository Structure

```cat
├── Financial_Inclusion_of_Africa.ipynb  # Clean, well-commented execution notebook
├── submission_v2.csv                    # Final binarized test predictions
├── requirements.txt                     # Pinned package dependency tree
└── README.md                            # Documentation and replication guide
