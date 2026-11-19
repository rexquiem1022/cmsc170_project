# CMSC 170 Project: Predicting Political Dynasties in the Philippines

**Group Name:** Walang tubeg buseng  
**Lab Section:** EF-5L (4–7 PM, Th)  
**Instructor:** Zenith Arnejo  
**Live Project Page:** https://rexquiem1022.github.io/cmsc170_project/

---

## 1. Project Overview & Repository Structure

This repository contains the complete from-scratch machine learning implementation and evaluation for predicting **Fat Political Dynasties (`fat = 1`)** vs. **Non-Dynastic / Thin Officials (`fat = 0`)** in local Philippine elections using the Ateneo Policy Center dataset.

```text
cmsc170_project/
├── political_dynasty.csv            # Dataset file
├── data_preprocessing.py            # Data loading, encoding, & 50:50 undersampling
├── knn_model.py                     # Vectorized k-NN classifier
├── naive_bayes_model.py             # Gaussian Naïve Bayes classifier
├── perceptron.py                    # Single-Layer Perceptron classifier
├── kmeans_model.py                  # K-Means clustering baseline
├── generate_charts.py               # Matplotlib visualization script
├── f1_score_comparison.png          # Generated metric plot
├── precision_vs_recall_tradeoff.png # Generated metric plot
├── index.md                         # GitHub Pages Website Source
└── README.md                        # Repository documentation & task log
```

---

## 2. Prerequisites & Dataset Setup

### Prerequisites
* Python 3.8 or higher
* Required Python libraries: `numpy`, `matplotlib`

Install dependencies via terminal:
```bash
pip install numpy matplotlib
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
* **Run k-Nearest Neighbors (k-NN):**
  ```bash
  python3 knn_model.py
  ```
* **Run Gaussian Naïve Bayes:**
  ```bash
  python3 naive_bayes_model.py
  ```
* **Run Single-Layer Perceptron:**
  ```bash
  python3 perceptron.py
  ```
* **Run K-Means Clustering Baseline:**
  ```bash
  python3 kmeans_model.py
  ```
* **Generate Metric Charts:**
  ```bash
  python3 generate_charts.py
  ```

---

## 4. Member Contribution Task Log

| Member Name | Role & Core Contributions | Contribution (%) |
| :--- | :--- | :---: |
| **Lance Gabriel A. Barroso** | **Group Leader:** Implemented k-NN and Perceptron algorithms, managed repository setup, and directed experiment execution. | 25% |
| **Arman Carl P. Arañez** | **Data Engineer:** Built preprocessing pipeline, 50:50 random undersampling logic, and Min-Max feature normalization. | 25% |
| **Jmil Anchelo N. Bodiongan** | **Algorithm Developer:** Coded Gaussian Naïve Bayes classifier and implemented evaluation metric functions ($TP, FP, TN, FN$). | 25% |
| **Jericko B. Bacar** | **Data Analyst:** Implemented K-Means clustering baseline, generated performance plots, and authored project documentation. | 25% |