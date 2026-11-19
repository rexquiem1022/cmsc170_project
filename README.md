# CMSC 170 Project: Predicting Political Dynasties in the Philippines

**Group Name:** Walang tubeg buseng  
**Lab Section:** EF-5L 
**Instructor:** Zenith Arnejo  
**Live Project Page:** [https://rexquiem1022.github.io/cmsc170_project/](https://rexquiem1022.github.io/cmsc170_project/)

---

## 1. Project Overview & Repository Structure

This repository contains the complete from-scratch machine learning implementation and evaluation for predicting **Fat Political Dynasties (`fat = 1`)** vs. **Non-Dynastic / Thin Officials (`fat = 0`)** in local Philippine elections using the Ateneo Policy Center dataset.

```text
cmsc170_project/
├── political_dynasty.csv          # Ateneo Policy Center dataset (2004–2016)
├── data_preprocessing.py          # Data loading, encoding, feature engineering, & 50:50 undersampling
├── knn_model.py                   # Vectorized k-NN classifier with exhaustive subset search
├── naive_bayes_model.py           # Gaussian Naïve Bayes classifier
├── naive_combo_finder.py          # Exhaustive feature combination search for Naïve Bayes
├── perceptron.py                  # Single-Layer Perceptron classifier
├── perceptron_feature_search.py   # 255-subset validation feature search for Perceptron
├── index.md                       # GitHub Pages website source
└── README.md                      # Repository documentation & task log
```

---

## 2. Prerequisites & Dataset Setup

### Prerequisites
* Python 3.8 or higher
* Required Python library: `numpy` 

Install dependency via terminal:
```bash
pip install numpy
```

### Dataset Setup
Ensure `political_dynasty.csv` is located directly in the repository root directory (`cmsc170_project/`).

---

## 3. How to Run Code & Reproduce Results

Run the commands directly from the repository root:

* **Data Preprocessing & Summary:**
  ```bash
  python3 data_preprocessing.py
  ```
* **Run k-Nearest Neighbors (k-NN) & Feature Search:**
  ```bash
  python3 knn_model.py
  ```
* **Run Gaussian Naïve Bayes & Feature Combination Finder:**
  ```bash
  python3 naive_combo_finder.py
  python3 naive_bayes_model.py
  ```
* **Run Single-Layer Perceptron & 255-Subset Feature Search:**
  ```bash
  python3 perceptron_feature_search.py
  python3 perceptron.py
  ```

---

## 4. Member Contribution Task Log

| Member Name | Role & Core Contributions |
| :--- | :--- |
| **Lance Gabriel A. Barroso** | **Group Leader & Lead Developer:** Architected and implemented the core data preprocessing pipeline (`data_preprocessing.py`), `undersample_5050` balancing logic, feature engineering (`Is_Executive`, `Location_Combined`), vectorized k-NN classifier (`knn_model.py`) with exhaustive `itertools` feature subset search, repository integration, readme and github pages initialization , and end-to-end experiment execution. | 
| **Arman Carl P. Arañez** | **Data & Feature Contributor:** Assisted with dataset inspection, feature engineering (`Is_Major_Party`), and Milestone documentation. | 
| **Jmil Anchelo N. Bodiongan** | **Algorithm Developer (Naïve Bayes):** Implemented the Gaussian Naïve Bayes classifier (`naive_bayes_model.py`), feature pair search (`naive_combo_finder.py`), and confusion matrix evaluation metrics ($TP, FP, TN, FN$). | 
| **Jericko B. Bacar** | **Algorithm Developer (Perceptron) & Analyst:** Implemented the Single-Layer Perceptron (`perceptron.py`), 255-subset validation search (`perceptron_feature_search.py`). | 