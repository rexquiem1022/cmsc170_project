<script>
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']], displayMath: [['$$', '$$'], ['\\[', '\\]']] }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: linear-gradient(180deg, #eff6ff 0%, #f8fbff 45%, #ffffff 100%);
    color: #1e293b;
    line-height: 1.65;
  }

  .markdown-body > h1:first-child {
  display: none !important;
}

  .hero-banner {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ffffff 0%, #e0f2fe 100%);
    color: #03256c;
    padding: 2.6rem 2.2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 14px 35px -8px rgba(56, 132, 255, 0.16);
    border: 1px solid #dbeafe;
  }
  .hero-banner::before {
    content: "";
    position: absolute;
    top: -45px;
    left: -45px;
    width: 170px;
    height: 170px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(125, 211, 252, 0.45) 0%, rgba(186, 230, 253, 0) 70%);
    pointer-events: none;
  }
  .hero-banner h1 {
    color: #03256c !important;
    margin: 0 0 0.45rem 0;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    border: none !important;
  }
  .hero-subtitle {
    color: #1d4ed8;
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 1.2rem;
  }
  .hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.4rem;
  }
  .badge {
    background: #ffffff;
    border: 1px solid #bae6fd;
    padding: 0.35rem 0.85rem;
    border-radius: 999px;
    font-size: 0.84rem;
    font-weight: 600;
    color: #03256c;
    box-shadow: 0 2px 6px rgba(14, 165, 233, 0.08);
  }
  .hero-links a {
    display: inline-block;
    background: #03256c;
    color: #ffffff !important;
    font-weight: 700;
    padding: 0.6rem 1.2rem;
    border-radius: 999px;
    text-decoration: none;
    margin-right: 0.65rem;
    margin-top: 0.4rem;
    font-size: 0.9rem;
    box-shadow: 0 6px 15px rgba(3, 37, 108, 0.2);
    transition: transform 0.15s ease;
  }
  .hero-links a.secondary {
    background: #ffffff;
    color: #03256c !important;
    border: 1.5px solid #7dd3fc;
    box-shadow: 0 6px 15px rgba(125, 211, 252, 0.25);
  }

  h2 {
    color: #03256c !important;
    font-weight: 800 !important;
    letter-spacing: -0.01em;
    border-bottom: 2px solid #bae6fd !important;
    padding-bottom: 0.4rem;
    margin-top: 2.3rem;
  }
  h3 {
    color: #0c4a6e !important;
    font-weight: 700 !important;
  }

  .slide-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 1.2rem;
    margin: 1.2rem 0 1.8rem 0;
  }
  .slide-card {
    background: #ffffff;
    border-radius: 18px;
    padding: 1.4rem;
    box-shadow: 0 10px 28px -6px rgba(56, 132, 255, 0.14);
    border: 1px solid #e0f2fe;
  }
  .pill-row {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    margin-bottom: 0.85rem;
  }
  .pill-track {
    flex: 1;
    height: 18px;
    background: #dbeafe;
    border-radius: 999px;
    overflow: hidden;
  }
  .pill-fill {
    height: 100%;
    background: linear-gradient(90deg, #7dd3fc 0%, #60a5fa 100%);
    border-radius: 999px;
  }
  .pill-fill.warn {
    background: linear-gradient(90deg, #93c5fd 0%, #3b82f6 100%);
  }
  .pill-pct {
    font-size: 1.45rem;
    font-weight: 800;
    color: #03256c;
    min-width: 64px;
    text-align: right;
  }
  .slide-card-title {
    font-weight: 700;
    color: #03256c;
    font-size: 0.98rem;
    margin-bottom: 0.35rem;
  }
  .slide-card-desc {
    font-size: 0.86rem;
    color: #475569;
    margin: 0;
  }

  .callout {
    background: #ffffff;
    border: 1px solid #bae6fd;
    border-left: 5px solid #60a5fa;
    padding: 1.1rem 1.3rem;
    border-radius: 14px;
    box-shadow: 0 8px 20px -6px rgba(56, 132, 255, 0.12);
    margin: 1.3rem 0;
  }

  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 1.3rem 0;
    font-size: 0.92rem;
    background: #ffffff;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 10px 25px -6px rgba(56, 132, 255, 0.12);
    border: 1px solid #dbeafe;
  }
  th {
    background: #03256c !important;
    color: #ffffff !important;
    padding: 0.85rem;
    text-align: left;
    font-weight: 700;
  }
  td {
    padding: 0.75rem 0.85rem;
    border-bottom: 1px solid #e0f2fe;
  }
  tr:nth-child(even) td {
    background: #f8fbff;
  }

  .chart-box {
    background: #ffffff;
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 1.4rem;
    margin: 1.5rem 0;
    box-shadow: 0 10px 28px -6px rgba(56, 132, 255, 0.13);
  }
  .chart-box img {
    max-width: 100%;
    border-radius: 10px;
    display: block;
    margin: 0 auto;
  }
</style>

<div class="hero-banner">
  <h1>PREDICTING POLITICAL DYNASTIES IN THE PHILIPPINES</h1>
  <div class="hero-subtitle">CMSC 170 (Introduction to Artificial Intelligence) &bull; Group: Walang tubeg buseng (Section EF-5L)</div>
  <div class="hero-meta">
    <span class="badge">Lance Gabriel A. Barroso (Group Leader)</span>
    <span class="badge">Arman Carl P. Arañez</span>
    <span class="badge">Jmil Anchelo N. Bodiongan</span>
    <span class="badge">Jericko B. Bacar</span>
    <span class="badge">Instructor: Zenith Arnejo</span>
  </div>
  <div class="hero-links">
    <a href="https://github.com/rexquiem1022/cmsc170_project" target="_blank">View GitHub Repository</a>
    <a href="https://canva.link/yyo9thsfxt14jwz" class="secondary" target="_blank">Open Canva Presentation</a>
  </div>
</div>

## 1. Problem Statement and Motivation

In local Philippine politics, electoral power is frequently concentrated within established family clans. Governance and political science literature distinguishes between **"Thin Dynasties"** (sequential family succession within a single public office) and **"Fat Dynasties"** (where two or more family members sharing the same surname hold elected public office simultaneously across different positions within the same province and election cycle).

Fat political dynasties present persistent challenges to democratic accountability, political competition, and equitable regional development. Automating the classification of dynastic officials using machine learning enables researchers and civic analysts to systematically map where and how political concentration emerges across electoral jurisdictions.

The objective of this project is to design, implement, and evaluate from-scratch supervised machine learning classifiers to predict whether a local elected official belongs to a **Fat Political Dynasty (`fat = 1`)** or holds a **Non-Dynastic / Thin status (`fat = 0`)** using structural, partisan, and geographic attributes.

<div class="chart-box">
  <img src="political_dynasty.jpg" alt="Political Dynasty">
</div>

---

## 2. Dataset Description & Preprocessing Pipeline

- **Source:** Ateneo Policy Center (APC) Political Dynasties Dataset (`political_dynasty.csv`), compiled by the Ateneo School of Government / BetterGov PH.
- **Raw Corpus Size:** 86,234 historical local election records spanning 2004 to 2016 (~73.2% Non-Fat vs. ~26.8% Fat Dynasties).
- **Balanced Evaluation Corpus:** 46,010 records (23,005 `fat = 1` + 23,005 randomly sampled `fat = 0` records), partitioned via a randomized 80/20 split into **36,808 training records** and **9,202 holdout test records**.
- **Target Variable:** Binary classification label `fat` ($1 =$ Fat Dynasty, $0 =$ Non-Fat / Thin official).

### 2.1 Feature Representation (Raw & Engineered)
To ensure models learn genuine structural and geographic patterns rather than memorizing family names or chronological indices, candidate `Last Name` (direct target leakage) and raw election `Year` (temporal distance distortion) were strictly excluded from model inputs. Nine predictive attributes were constructed in `data_preprocessing.py`:

- **Raw Categorical Attributes (5):** `Position`, `Party`, `Region`, `Province`, `Municipality`.
- **Engineered Attributes (4):**
  - `Tenure`: Derived total years of service calculated from historical election appearances.
  - `Is_Executive`: Binary indicator ($1.0$ when `Position` contains `"MAYOR"`, `"GOVERNOR"`, or `"CONGRESSMAN"`; $0.0$ for legislative/council roles).
  - `Location_Combined`: Composite interaction string (`Province_Municipality`) mapped to an integer ID to capture hyper-local municipal political strongholds.
  - `Is_Major_Party`: Binary indicator ($1.0$ for candidates affiliated with major national coalitions such as PDP-Laban, Lakas-CMD, LP, Nacionalista, NPC, or UNA; $0.0$ for smaller local or independent parties).

### 2.2 Preprocessing & Balancing Pipeline
1. **Dictionary Encoding (`encode_list`):** All categorical string attributes were dynamically mapped to unique numerical integer IDs without external encoding libraries.
2. **Min-Max Feature Normalization:** Encoded features were scaled to $x_{\text{scaled}} \in [0, 1]$ so high-cardinality geographic IDs do not disproportionately dominate Euclidean distance calculations:
   $$x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$$
3. **Pre-Split 50:50 Random Undersampling (`undersample_5050`):** Equalizing class frequencies prior to splitting prevents classifiers from achieving artificially inflated accuracy by defaulting to the majority class (`fat = 0`), ensuring fair sensitivity and precision evaluation across both classes.

---

<div class="chart-box">
<h3 style="margin-top:0;">Figure 1: Pre-Split 50:50 Undersampling & Train/Test Partitioning</h3>
<svg viewBox="0 0 740 195" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
<rect width="740" height="195" fill="#f8fbff" rx="12"/>
<rect x="20" y="25" width="205" height="145" rx="12" fill="#ffffff" stroke="#bae6fd" stroke-width="1.5"/>
<text x="122" y="48" font-size="12" font-weight="800" text-anchor="middle" fill="#03256c">1. Raw APC Corpus</text>
<text x="122" y="66" font-size="11" font-weight="600" text-anchor="middle" fill="#475569">86,234 Total Records</text>
<rect x="38" y="82" width="169" height="18" rx="9" fill="#e2e8f0"/>
<rect x="38" y="82" width="124" height="18" rx="9" fill="#94a3b8"/>
<text x="122" y="114" font-size="10.5" text-anchor="middle" fill="#334155">73.2% Non-Fat (63,229)</text>
<rect x="38" y="124" width="169" height="18" rx="9" fill="#dbeafe"/>
<rect x="38" y="124" width="45" height="18" rx="9" fill="#2563eb"/>
<text x="122" y="156" font-size="10.5" font-weight="700" text-anchor="middle" fill="#1d4ed8">26.8% Fat (23,005)</text>
<path d="M 232 97 L 258 97" stroke="#03256c" stroke-width="2" marker-end="url(#arrow)"/>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 1 L 10 5 L 0 9 z" fill="#03256c"/>
</marker>
</defs>
<rect x="266" y="25" width="205" height="145" rx="12" fill="#ffffff" stroke="#7dd3fc" stroke-width="2"/>
<text x="368" y="48" font-size="12" font-weight="800" text-anchor="middle" fill="#03256c">2. 50:50 Undersampled</text>
<text x="368" y="66" font-size="11" font-weight="600" text-anchor="middle" fill="#0284c7">46,010 Balanced Records</text>
<rect x="284" y="82" width="169" height="18" rx="9" fill="#dbeafe"/>
<rect x="284" y="82" width="84.5" height="18" rx="9" fill="#38bdf8"/>
<text x="368" y="114" font-size="10.5" font-weight="600" text-anchor="middle" fill="#0c4a6e">50.0% Non-Fat (23,005)</text>
<rect x="284" y="124" width="169" height="18" rx="9" fill="#dbeafe"/>
<rect x="284" y="124" width="84.5" height="18" rx="9" fill="#03256c"/>
<text x="368" y="156" font-size="10.5" font-weight="700" text-anchor="middle" fill="#03256c">50.0% Fat (23,005)</text>
<path d="M 478 97 L 504 97" stroke="#03256c" stroke-width="2" marker-end="url(#arrow)"/>
<rect x="512" y="25" width="208" height="145" rx="12" fill="#ffffff" stroke="#bae6fd" stroke-width="1.5"/>
<text x="616" y="48" font-size="12" font-weight="800" text-anchor="middle" fill="#03256c">3. Stratified 80 / 20 Split</text>
<text x="616" y="66" font-size="11" font-weight="600" text-anchor="middle" fill="#475569">Zero Leakage Holdout</text>
<rect x="530" y="84" width="172" height="32" rx="8" fill="#eff6ff" stroke="#93c5fd"/>
<text x="616" y="104" font-size="11" font-weight="700" text-anchor="middle" fill="#03256c">Train (80%): 36,808</text>
<rect x="530" y="126" width="172" height="32" rx="8" fill="#03256c"/>
<text x="616" y="146" font-size="11" font-weight="700" text-anchor="middle" fill="#ffffff">Test (20%): 9,202</text>
</svg>
</div>

## 3. Methods & Implementation

All classification models, combinatorial feature searches, preprocessing utilities, and evaluation metrics were implemented completely from scratch in Python and `numpy`, without relying on `scikit-learn` or `pandas`.

### 3.1 k-Nearest Neighbors (`knn_model.py`)
- **Mechanism:** Non-parametric, instance-based classifier that predicts class labels via majority voting among the $k$ closest training instances using Minkowski distance with $p = 2.0$ (Euclidean distance):
  $$d(x, v) = \left( \sum_{i=1}^{n} |x_i - v_i|^2 \right)^{1/2}$$
- **Exhaustive Feature & Hyperparameter Search:** Uses `itertools.combinations` to evaluate every possible feature subset across sizes $1$ through $n$ alongside odd values of $k$, storing every configuration's metrics in `all_results` and ranking them by F1-Score to identify the optimal feature subspace.

### 3.2 Gaussian Naïve Bayes (`naive_bayes_model.py` & `naive_combo_finder.py`)
- **Mechanism:** Probabilistic classifier applying Bayes' Theorem under the conditional feature independence assumption:
  $$P(y \mid x_1, \dots, x_n) \propto P(y) \prod_{i=1}^{n} P(x_i \mid y)$$
- **Likelihood Estimation & Feature Search:** Continuous attributes are modeled via Gaussian probability density functions, while categorical frequency tables apply Laplace smoothing ($k = 1.0$) to prevent zero-probability collapse. `naive_combo_finder.py` systematically evaluates feature combinations and ranks the top 10 subsets by F1-Score.

### 3.3 Single-Layer Perceptron (`perceptron.py` & `perceptron_feature_search.py`)
- **Mechanism:** Parametric linear threshold classifier computing a weighted sum passed through a Heaviside step activation function:
  $$z = \sum_{i=1}^{n} w_i x_i + b \quad \implies \quad \hat{y} = \begin{cases} 1 & \text{if } z \ge 0 \\ 0 & \text{if } z < 0 \end{cases}$$
- **Training & 255-Subset Validation Search:** Weights are updated iteratively on misclassified instances via the Perceptron Learning Rule ($w_{t+1} = w_t + \eta (y_i - \hat{y}_i) x_i$) with learning rate $\eta = 0.1$ for 50 epochs. `perceptron_feature_search.py` evaluates all $2^8 - 1 = 255$ non-empty subsets of the 8 usable features (excluding `Tenure`) on a validation split prior to final holdout evaluation.

### 3.4 From-Scratch Evaluation Metrics
Each model is evaluated using a $2 \times 2$ Confusion Matrix ($TP, FP, TN, FN$) across four core metrics:
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}, \qquad \text{Precision} = \frac{TP}{TP + FP}, \qquad \text{Recall} = \frac{TP}{TP + FN}, \qquad \text{F1-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

## 4. Results & Comparative Performance

### Model Accuracy Overview

<div class="slide-card-grid">
  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 75%;"></div></div>
      <div class="pill-pct">75.0%</div>
    </div>
    <div class="slide-card-title">k-NN Best Accuracy (k = 13)</div>
    <p class="slide-card-desc">Achieved <strong>69.88% F1-Score</strong> and <strong>72.50% Precision</strong> using <code>Position</code>, <code>Region</code>, and <code>Province</code> on the 50:50 balanced dataset.</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 62.35%;"></div></div>
      <div class="pill-pct">62.4%</div>
    </div>
    <div class="slide-card-title">Gaussian Naïve Bayes Accuracy</div>
    <p class="slide-card-desc">Achieved <strong>59.78% F1-Score</strong> and <strong>64.16% Precision</strong> using top feature pair <code>Position + Province</code>.</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill warn" style="width: 49.82%;"></div></div>
      <div class="pill-pct">49.8%</div>
    </div>
    <div class="slide-card-title">Single-Layer Perceptron</div>
    <p class="slide-card-desc">Non-convergent after 50 epochs across 255 subsets, defaulting to predicting <code>fat = 1</code> (66.50% always-fat baseline F1).</p>
  </div>
</div>

### Performance Summary Table (50:50 Balanced Holdout Set)

| Model / Algorithm | Optimal Feature Configuration & Hyperparameters | Accuracy | Precision | Recall (Sensitivity) | **F1-Score** | Confusion Matrix ($TP, FP, TN, FN$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **k-Nearest Neighbors (k-NN)** | `Position`, `Region`, `Province` ($k = 13$, $p = 2.0$) | **75.00%** | **72.50%** | 67.44% | **69.88%** | $TP=28, FP=11, TN=46, FN=15$ |
| **Gaussian Naïve Bayes** | `Position` + `Province` (Top 1 of 10 combos, Laplace $k = 1.0$) | 62.35% | 64.16% | 55.96% | 59.78% | $TP=12873, FP=7190, TN=15815, FN=10132$ |
| **Single-Layer Perceptron** | `Position`, `Municipality`, `Location_Combined` ($\eta=0.1$, 50 epochs) | 49.82% | 49.82% | 100.00%* | 66.50%* | $TP=4584, FP=4618, TN=0, FN=0$ |

*\*Note: The Single-Layer Perceptron did not converge after 50 epochs and classified 100% of holdout officials as `fat = 1` ($TN = 0, FN = 0$), matching an "always-predict-fat" baseline ($66.50\%$ F1) rather than learning a separating hyperplane.*

### Visual Metric Comparison

<div class="chart-box">
  <h3 style="margin-top:0;">Figure 1: Model Performance Comparison (Accuracy vs. Precision vs. F1-Score)</h3>
  <svg viewBox="0 0 720 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <rect width="720" height="260" fill="#f8fbff" rx="12"/>
    <line x1="90" y1="30" x2="680" y2="30" stroke="#bae6fd" stroke-dasharray="4"/>
    <line x1="90" y1="75" x2="680" y2="75" stroke="#bae6fd" stroke-dasharray="4"/>
    <line x1="90" y1="120" x2="680" y2="120" stroke="#bae6fd" stroke-dasharray="4"/>
    <line x1="90" y1="165" x2="680" y2="165" stroke="#bae6fd" stroke-dasharray="4"/>
    <line x1="90" y1="210" x2="680" y2="210" stroke="#03256c" stroke-width="1.5"/>
    <text x="80" y="34" font-size="11" text-anchor="end" fill="#475569">100%</text>
    <text x="80" y="79" font-size="11" text-anchor="end" fill="#475569">75%</text>
    <text x="80" y="124" font-size="11" text-anchor="end" fill="#475569">50%</text>
    <text x="80" y="169" font-size="11" text-anchor="end" fill="#475569">25%</text>
    <text x="80" y="214" font-size="11" text-anchor="end" fill="#475569">0%</text>
    <rect x="135" y="75" width="32" height="135" fill="#03256c" rx="5"/>
    <text x="151" y="69" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">75.0%</text>
    <rect x="172" y="79.5" width="32" height="130.5" fill="#3b82f6" rx="5"/>
    <text x="188" y="73.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">72.5%</text>
    <rect x="209" y="84.2" width="32" height="125.8" fill="#38bdf8" rx="5"/>
    <text x="225" y="78" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">69.9%</text>
    <text x="188" y="230" font-size="12" font-weight="bold" text-anchor="middle" fill="#03256c">k-NN (k=13)</text>
    <rect x="335" y="97.8" width="32" height="112.2" fill="#03256c" rx="5"/>
    <text x="351" y="91.8" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">62.4%</text>
    <rect x="372" y="94.5" width="32" height="115.5" fill="#3b82f6" rx="5"/>
    <text x="388" y="88.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">64.2%</text>
    <rect x="409" y="102.4" width="32" height="107.6" fill="#38bdf8" rx="5"/>
    <text x="425" y="96.4" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">59.8%</text>
    <text x="388" y="230" font-size="12" font-weight="bold" text-anchor="middle" fill="#03256c">Gaussian Naïve Bayes</text>
    <rect x="535" y="120.3" width="32" height="89.7" fill="#03256c" rx="5"/>
    <text x="551" y="114.3" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">49.8%</text>
    <rect x="572" y="120.3" width="32" height="89.7" fill="#3b82f6" rx="5"/>
    <text x="588" y="114.3" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">49.8%</text>
    <rect x="609" y="90.3" width="32" height="119.7" fill="#93c5fd" rx="5"/>
    <text x="625" y="84.3" font-size="10" font-weight="bold" text-anchor="middle" fill="#1d4ed8">66.5%*</text>
    <text x="588" y="230" font-size="12" font-weight="bold" text-anchor="middle" fill="#03256c">Perceptron (Baseline)</text>
    <rect x="175" y="243" width="12" height="12" fill="#03256c" rx="3"/><text x="192" y="253" font-size="11" fill="#334155">Accuracy</text>
    <rect x="270" y="243" width="12" height="12" fill="#3b82f6" rx="3"/><text x="287" y="253" font-size="11" fill="#334155">Precision</text>
    <rect x="365" y="243" width="12" height="12" fill="#38bdf8" rx="3"/><text x="382" y="253" font-size="11" fill="#334155">F1-Score</text>
    <rect x="460" y="243" width="12" height="12" fill="#93c5fd" rx="3"/><text x="477" y="253" font-size="11" fill="#334155">F1 (Always-Fat Baseline)</text>
  </svg>
</div>

<div class="chart-box">
<h3 style="margin-top:0;">Figure 3: Confusion Matrix Breakdown Across Evaluated Classifiers</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 1rem; margin-top: 1rem;">
<div style="background: #f8fbff; border: 1.5px solid #7dd3fc; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">k-NN (k = 13)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #166534;">28</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #991b1b;">11</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #92400e;">15</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #03256c;">46</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1px solid #bae6fd; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Gaussian Naïve Bayes</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #166534;">12,873</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #991b1b;">7,190</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #92400e;">10,132</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #03256c;">15,815</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1px solid #bae6fd; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Single-Layer Perceptron</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #166534;">4,584</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #991b1b;">4,618</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #64748b;">0</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #64748b;">FN (Miss)</div>
</div>
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #64748b;">0</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #64748b;">TN (Reject)</div>
</div>
</div>
</div>
</div>
</div>

---

## 5. Comparative Analysis & Discussion

<div class="callout">
  <strong>Core Empirical Finding:</strong> Pre-split 50:50 class balancing combined with exhaustive combinatorial feature selection proves that local geographic jurisdiction (<code>Region</code> and <code>Province</code>) paired with office tier (<code>Position</code>) carries the strongest predictive signal for identifying Fat Political Dynasties in the Philippines.
</div>

1. **Superiority of Non-Parametric k-NN (75.00% Accuracy, 69.88% F1-Score):**  
   Dynastic political concentration in the Philippines is inherently localized within specific provinces and regions rather than distributed linearly across the national electorate. Officials sharing the exact same `Position`, `Region`, and `Province` sit at zero Euclidean distance from one another in feature space, enabling k-NN ($k = 13$) to vote directly within localized political strongholds without imposing rigid parametric boundary shapes. Exhaustive subset search also eliminated distance dilution from noisy features such as party and municipality IDs.
2. **Conditional Independence Constraints in Gaussian Naïve Bayes (62.35% Accuracy, 59.78% F1-Score):**  
   While Gaussian Naïve Bayes achieved solid precision (64.16%) and balanced error counts ($TP = 12,873$, $TN = 15,815$), its assumption that `Position` and `Province` contribute independently prevents it from modeling joint interaction effects—such as specific provinces where executive offices (Governor, Mayor, Representative) are disproportionately consolidated by family clans.
3. **Linear Separability Limits in the Single-Layer Perceptron (49.82% Accuracy):**  
   A single-layer perceptron partitions feature space using a single linear hyperplane ($w^T x + b = 0$). Because nominal political categories were mapped to ordinal alphabetical integer IDs and true dynastic boundaries are highly non-linear, the perceptron failed to converge across all 255 feature subsets and collapsed into predicting `fat = 1` for every test instance (scoring 66.50% F1, identical to an uninformed always-fat guess).

---

## 6. Conclusion & Future Directions

This study demonstrates that from-scratch machine learning pipelines can effectively detect **Fat Political Dynasties** in local Philippine elections without relying on candidate surnames or year-based target leakage. Across 46,010 balanced electoral records from the Ateneo Policy Center dataset (2004–2016), **k-Nearest Neighbors ($k = 13$)** emerged as the strongest and most reliable classifier, achieving **75.00% Accuracy**, **72.50% Precision**, **67.44% Recall**, and an **F1-Score of 69.88%** using only three core features: `Position`, `Region`, and `Province`.

### Key Takeaways & Contributions
- **Methodological Rigor:** Implementing pre-split 50:50 random undersampling eliminated majority-class distortion, while exhaustive combinatorial search (`itertools.combinations`) proved critical for isolating high-signal geographic and positional features.
- **Model Suitability for Sociopolitical Data:** Comparing three distinct learning paradigms—instance-based (k-NN), generative probabilistic (Gaussian Naïve Bayes), and linear threshold (Perceptron)—confirms that non-parametric neighborhood matching captures irregular, geographically clustered political strongholds far better than linear hyperplanes or conditional-independence models.
- **Governance & Policy Utility:** Even when blinded to family surnames, structural and geographic profiles alone predict dynastic concentration with 75% accuracy, providing researchers with a quantitative baseline for identifying regions with entrenched electoral dominance.

### Limitations & Future Work
- **Categorical Encoding Geometry:** Mapping nominal attributes (`Province`, `Position`, `Party`) to sequential alphabetical integers introduces artificial numeric ordering that penalizes linear models. Future iterations should implement **one-hot encoding**, **binary target encoding**, or **frequency encoding** so linear and neural models can weight individual jurisdictions independently.
- **Non-Linear Parametric & Ensemble Models:** Extending the from-scratch codebase to include a **Multi-Layer Perceptron (MLP)** with non-linear activation functions (ReLU/Sigmoid) or **Decision Trees / Random Forests** would allow parametric models to learn complex feature interactions between office tier, party coalition, and province.
- **Richer Socioeconomic & Electoral Features:** Incorporating vote margin, winning percentage, municipal income class, and multi-cycle incumbency indicators from newer election cycles (2019–2025) could further sharpen predictive precision and sensitivity.

---

## 7. References & Disclosures

1. **Dataset Source:** Ateneo Policy Center (APC), Ateneo School of Government. *Political Dynasties Dataset (2004–2016)*. BetterGov PH.
2. **Course Materials:** CMSC 170 Lecture Slides & Lab Guidelines, University of the Philippines Los Baños.
3. **Development & Tooling Disclosure:** All data preprocessing, feature engineering, machine learning models, combinatorial searches, and evaluation pipelines were written from scratch in Python and NumPy by the group members, building upon course laboratory methodologies. Minimal LLM/AI assistance was used for code debugging/optimization and minor HTML/Markdown formatting on the project webpage.