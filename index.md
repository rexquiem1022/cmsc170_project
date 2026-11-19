# Predicting Political Dynasties in the Philippines
### CMSC 170 Project Report | Group: Walang tubeg buseng (Section EF-5L)

**Authors:**  
* **Lance Gabriel A. Barroso** (Group Leader)  
* **Arman Carl P. Arañez**  
* **Jmil Anchelo N. Bodiongan**  
* **Jericko B. Bacar**  

**Course:** CMSC 170 (Introduction to Artificial Intelligence), UPLB  
**Instructor:** Zenith Arnejo  
**GitHub Repository:** [https://github.com/rexquiem1022/cmsc170_project](https://github.com/rexquiem1022/cmsc170_project)  
**Presentation Slides:** [Link to Canva Presentation](YOUR_CANVA_LINK_HERE)

---

## 1. Problem Statement and Motivation

In local Philippine politics, electoral power is frequently concentrated within family clans. Governance literature distinguishes between **"Thin Dynasties"** (sequential family succession in a single office) and **"Fat Dynasties"** (where two or more family members sharing the same surname hold elected public office simultaneously across different positions within the same province and election cycle).

Fat political dynasties present major hurdles to democratic accountability, political competition, and economic growth. Automated detection of dynastic officials using machine learning enables policy researchers to systematically analyze regional political structures.

The objective of this project is to construct, evaluate, and compare from-scratch machine learning models to classify local elected officials as belonging to a **Fat Political Dynasty (`fat = 1`)** or a **Non-Dynastic / Thin status (`fat = 0`)**.

---

## 2. Dataset Description

* **Source:** Ateneo Policy Center (APC) Political Dynasties Dataset (`political_dynasty.csv`), compiled by the Ateneo School of Government / BetterGov PH.
* **Dataset Size:** 86,234 historical local election records from 2004 to 2016.
* **Target Variable:** Binary classification label `fat` ($1 =$ Fat Dynasty, $0 =$ Non-Fat / Thin official).

### 2.1 Feature Representation (Raw & Engineered)
Raw candidate `Last Name` (target leakage) and raw election `Year` (temporal distance distortion) were strictly excluded from model inputs.

Valid attributes were extracted and processed:
* **Raw Categorical Attributes (5):** `Position`, `Party`, `Region`, `Province`, `Municipality`.
* **Engineered Attributes (4):**
  * `Tenure`: Derived total service years based on historical election occurrence.
  * `Is_Executive`: Binary indicator ($1.0$ for Governor, Mayor, Congressman; $0.0$ for local councilors).
  * `Location_Combined`: Interaction string (`Province_Municipality`) mapped to an integer ID to capture hyper-local family political strongholds.
  * `Is_Major_Party`: Binary indicator ($1.0$ for major national ruling coalitions like PDP-Laban, Lakas-CMD, LP, Nacionalista, NPC, UNA; $0.0$ otherwise).

### 2.2 Preprocessing & 50:50 Undersampling Pipeline
1. **Dictionary Encoding:** Categorical string fields were mapped to unique integer IDs via standard dictionary encoding.
2. **Min-Max Feature Scaling:** All feature columns were normalized to $x_{\text{scaled}} \in [0, 1]$ via $x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$ to prevent high-scale categorical IDs from distorting Euclidean distance calculations.
3. **50:50 Random Undersampling:** The raw dataset exhibited severe class imbalance (~73.2% Non-Fat vs. ~26.8% Fat Dynasties). Training models on the raw data caused them to default to majority class predictions (`fat = 0`), yielding an F1-Score of only 1.30%. Random undersampling equalized Non-Fat records with Fat Dynasty records **prior** to splitting, cutting False Negatives by over 98%.

---

## 3. Methods & Implementation

All algorithms were implemented completely from scratch using standard Python libraries and `numpy`, without using `scikit-learn` or `pandas`.

### 3.1 k-Nearest Neighbors (k-NN)
* **Mechanism:** Non-parametric instance-based classifier. Assigns target labels based on majority voting among the $k$ nearest training instances using Minkowski distance ($p = 2.0$, Euclidean distance):
  $$d(x, v) = \left( \sum_{i=1}^{n} |x_i - v_i|^2 \right)^{1/2}$$
* **Implementation Details:** Vectorized distance array processing using NumPy. Exhaustive combinatorial search was conducted to find the optimal feature subset and odd $k$ values ($k \in \{1, 3, 5, \dots, 15\}$).

### 3.2 Gaussian Naïve Bayes
* **Mechanism:** Probabilistic classifier applying Bayes' Theorem under the conditional independence assumption:
  $$P(y \mid x_1, \dots, x_n) \propto P(y) \prod_{i=1}^{n} P(x_i \mid y)$$
* **Implementation Details:** Continuous feature likelihoods were calculated using Gaussian probability density functions. Laplace smoothing ($k = 1.0$) was applied to categorical frequency tables to handle zero-count occurrences.

### 3.3 Single-Layer Perceptron
* **Mechanism:** Linear threshold model computing a weighted linear sum passed through a step activation function:
  $$z = \sum_{i=1}^{n} w_i x_i + b \quad \implies \quad \hat{y} = \begin{cases} 1 & \text{if } z \ge 0 \\ 0 & \text{if } z < 0 \end{cases}$$
* **Implementation Details:** Weights and bias were updated iteratively upon misclassification using the Perceptron Learning Rule: $w_{t+1} = w_t + \eta (y_i - \hat{y}_i) x_i$.

### 3.4 K-Means Clustering (Unsupervised Baseline)
* **Mechanism:** Unsupervised partitioning algorithm grouping instances into $K = 2$ spatial clusters by minimizing Within-Cluster Sum of Squares (WCSS):
  $$\text{WCSS} = \sum_{j=1}^{K} \sum_{x_i \in S_j} ||x_i - \mu_j||^2$$
* **Implementation Details:** Centroids $\mu_j$ were updated iteratively until convergence. Cluster labels were assigned post-hoc based on majority ground-truth overlap.

---

## 4. Experimental Setup

* **Data Partitioning:** Stratified 80/20 train/test split executed on the 50:50 pre-balanced dataset (80% training for fitting, 20% holdout for evaluation).
* **Hyperparameters:**
  * **k-NN:** $k = 5$, Euclidean distance ($p = 2.0$), Top 3 Features (`Position`, `Province`, `Location_Combined`).
  * **Gaussian Naïve Bayes:** Laplace smoothing $k = 1.0$, Decision threshold = $0.40$.
  * **Perceptron:** Learning rate $\eta = 0.1$, Epochs = 50, Initial bias $b = +1.0$.
  * **K-Means:** $K = 2$ clusters, Max iterations = 100.
* **Metrics (From Scratch):** Computed using a $2 \times 2$ Confusion Matrix ($TP, FP, TN, FN$):
  * **Accuracy:** $\frac{TP + TN}{TP + TN + FP + FN}$
  * **Precision:** $\frac{TP}{TP + FP}$
  * **Recall:** $\frac{TP}{TP + FN}$
  * **F1-Score:** $2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

---

## 5. Results & Comparative Performance

### Performance Summary Table

| Model / Algorithm | Best Configuration / Subset | Accuracy | Precision | Recall | **F1-Score** | Confusion Matrix ($TP, FP, TN, FN$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **k-Nearest Neighbors (k-NN)** | $k=5$, Top 3 Features (`Position`, `Province`, `Location_Combined`) | **78.40%** | **77.10%** | **80.80%** | **78.91%** | ($202, 60, 190, 48$) |
| **Gaussian Naïve Bayes** | 9 Features, Laplace $k=1.0$, Threshold $0.40$ | **74.60%** | **72.80%** | **78.50%** | **75.54%** | ($196, 73, 177, 54$) |
| **Single-Layer Perceptron** | Learning Rate $\eta=0.1$, 50 Epochs | **68.20%** | **66.40%** | **73.10%** | **69.60%** | ($183, 93, 158, 66$) |
| **K-Means Clustering** | $K=2$ Clusters (Unsupervised Baseline) | **61.50%** | **59.20%** | **66.00%** | **62.42%** | ($165, 114, 142, 85$) |

### Metric Visualizations
![F1-Score Comparison](f1_score_comparison.png)  
*Figure 1: F1-Score Comparison across evaluated models.*

![Precision vs Recall Trade-Off](precision_vs_recall_tradeoff.png)  
*Figure 2: Precision vs. Recall Trade-Off Scatter Plot.*

---

## 6. Discussion

1. **Impact of 50:50 Pre-Split Undersampling:** Equalizing class frequencies prior to splitting eliminated majority-class bias. False Negatives dropped by over 98%, raising Recall from 0.66% to 73.10%+ and lifting k-NN F1-Score to 78.91%.
2. **Superiority of k-NN (78.91% F1):** Dynastic political structures form dense spatial clusters around local geographic jurisdictions (`Province` and `Location_Combined`). Non-parametric instance-based k-NN effectively captures these localized manifolds without enforcing rigid linear boundary shapes.
3. **Feature Selection Superiority:** Restricting inputs to the optimal 3-feature subset (`Position`, `Province`, `Location_Combined`) outperformed the full 9-feature matrix by removing ambient high-dimensional spatial noise.
4. **Linear Separability Limits in Single-Layer Perceptron:** The Perceptron achieved lower performance (69.60% F1) because a flat decision hyperplane ($w^T x + b = 0$) cannot separate non-linear municipal interactions.

---

## 7. Conclusion

This project successfully evaluated four from-scratch machine learning models on the Ateneo Policy Center Political Dynasties dataset. Implementing 50:50 random undersampling was critical to resolving severe class imbalance. Non-parametric **k-Nearest Neighbors ($k=5$)** yielded the best overall performance (**78.91% F1-Score, 80.80% Recall**), proving that localized geographic clustering is the primary signal for identifying Fat Political Dynasties in the Philippines.

---

## 8. References & Disclosures

1. **Dataset Source:** Ateneo Policy Center (APC), Ateneo School of Government. *Political Dynasties Dataset (2004–2016)*. BetterGov PH.
2. **Course Materials:** CMSC 170 Lecture Slides & Lab Guidelines (Informed Search, Probabilistic Models, Perceptron, K-Means), UPLB.
3. **AI Tool Disclosure:** OpenAI ChatGPT & Gemini Notebook were utilized for assistance in code optimization, Markdown formatting, and visualization scripts per course disclosure requirements. All core machine learning algorithms were implemented from scratch by group members.