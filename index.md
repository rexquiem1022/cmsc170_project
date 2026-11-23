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

  .formula-box {
    background: #f8fbff;
    border: 1px solid #dbeafe;
    border-radius: 12px;
    padding: 0.85rem 1.2rem;
    margin: 0.7rem 0 1.1rem 0;
    font-family: "Cambria Math", "Times New Roman", serif;
    font-size: 1.05rem;
    color: #03256c;
    text-align: center;
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

The objective of this project is to design, implement, and evaluate from-scratch supervised machine learning classifiers—comparing **Exhaustive 2<sup>9</sup> Combinatorial Feature Search (Method 1)** against **Naïve Bayes-Guided Feature Transfer (Method 2)**—to classify whether a local elected official belongs to a **Fat Political Dynasty (`fat = 1`)** or holds a **Non-Dynastic / Thin status (`fat = 0`)**.

<div class="chart-box">
  <img src="political_dynasty.jpg" alt="Political Dynasty">
</div>

---

## 2. Dataset Description & Preprocessing Pipeline

- **Source:** Ateneo Policy Center (APC) Political Dynasties Dataset (`political_dynasty.csv`), compiled by the Ateneo School of Government / BetterGov PH.
- **Raw Corpus Size:** 86,234 historical local election records spanning 2004 to 2016 (~73.2% Non-Fat vs. ~26.8% Fat Dynasties).
- **Balanced Evaluation Corpus:** 46,010 records (23,005 `fat = 1` + 23,005 randomly sampled `fat = 0` records), partitioned via a randomized 80/20 split into **36,808 training records** and **9,202 holdout test records** (49.82% `fat = 1` test rate).
- **Target Variable:** Binary classification label `fat` (1 = Fat Dynasty, 0 = Non-Fat / Thin official).

### 2.1 Feature Representation (Raw & Engineered)
To ensure models learn genuine structural and geographic patterns rather than memorizing family names or chronological indices, candidate `Last Name` (direct target leakage) and raw election `Year` (temporal distance distortion) were strictly excluded from model inputs. Nine predictive attributes were constructed in `data_preprocessing.py`:

- **Raw Categorical Attributes (5):** `Position`, `Party`, `Region`, `Province`, `Municipality`.
- **Engineered Attributes (4):**
  - `Tenure`: Derived total years of service calculated from historical election appearances.
  - `Is_Executive`: Binary indicator (`1.0` when `Position` contains `"MAYOR"`, `"GOVERNOR"`, or `"CONGRESSMAN"`; `0.0` for legislative/council roles).
  - `Location_Combined`: Composite interaction string (`Province_Municipality`) mapped to an integer ID to capture hyper-local municipal political strongholds.
  - `Is_Major_Party`: Binary indicator (`1.0` for candidates affiliated with major national coalitions such as PDP-Laban, Lakas-CMD, LP, Nacionalista, NPC, or UNA; `0.0` for smaller local or independent parties).

### 2.2 Preprocessing & Balancing Pipeline
1. **Dictionary Encoding (`encode_list`):** All categorical string attributes were dynamically mapped to unique numerical integer IDs without external encoding libraries.
2. **Min-Max Feature Normalization:** Encoded features were scaled to <i>x</i><sub>scaled</sub> &isin; [0, 1] so high-cardinality geographic IDs do not disproportionately dominate Euclidean distance calculations or step-function weights:
   <div class="formula-box">
     <i>x</i><sub>scaled</sub> = (<i>x</i> &minus; <i>x</i><sub>min</sub>) / (<i>x</i><sub>max</sub> &minus; <i>x</i><sub>min</sub>)
   </div>
3. **Pre-Split 50:50 Random Undersampling (`undersample_5050`):** Equalizing class frequencies prior to splitting prevents classifiers from achieving artificially inflated accuracy by defaulting to the majority class (`fat = 0`), ensuring fair sensitivity and precision evaluation across the full **9,202 holdout test population**.

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
<text x="616" y="66" font-size="11" font-weight="600" text-anchor="middle" fill="#475569">Full Holdout Evaluation</text>
<rect x="530" y="84" width="172" height="32" rx="8" fill="#eff6ff" stroke="#93c5fd"/>
<text x="616" y="104" font-size="11" font-weight="700" text-anchor="middle" fill="#03256c">Train (80%): 36,808</text>
<rect x="530" y="126" width="172" height="32" rx="8" fill="#03256c"/>
<text x="616" y="146" font-size="11" font-weight="700" text-anchor="middle" fill="#ffffff">Test (20%): 9,202</text>
</svg>
</div>

---

## 3. Methods & Two-Stage Feature Selection Architecture

All classification algorithms, combinatorial searches, preprocessing utilities, and evaluation metrics were implemented completely from scratch in Python and `numpy`, without relying on `scikit-learn` or `pandas`. Because feature subsets strongly govern distance geometry, probability distributions, and linear separability across 9 attributes, our experimental design evaluates two distinct feature selection strategies across the full **9,202-record holdout test set**:

### 3.1 Method 1: Exhaustive 2<sup>9</sup> Combinatorial Search (Brute-Force Optimization)
In **Method 1**, each classifier independently searches the entire power set of the 9 engineered and raw features (2<sup>9</sup> = 512 combinations in `naive_combo_finder.py` using 5-fold grouped cross-validation with Laplace smoothing <i>k</i> = 1.0; 2<sup>9</sup> &minus; 1 = 511 non-empty subsets across odd <i>k</i> &isin; {1, 3, 5, 7, 9, 11, 13, 15} in `knn_model.py`; and 2<sup>9</sup> &minus; 1 = 511 subsets in `perceptron_feature_search.py` over 50 epochs). Every candidate model is evaluated independently and ranked strictly by highest F1-Score.

- **How it works:** Treats feature selection as an unconstrained global search over all 511 non-empty feature combinations (`itertools.combinations`), allowing each algorithm to pick whatever subset maximizes its F1-Score.
- **Advantages:**
  - **Model-Specific Freedom:** Does not force a distance-based model (k-NN) or linear threshold model (Perceptron) to use features preferred by a probabilistic model.
  - **Complete Search Coverage:** Guarantees that no single-feature or high-order interaction subset is overlooked within the 9-feature space.
- **Disadvantages:**
  - **High Computational Cost:** Evaluating 511 subsets across 8 values of <i>k</i> (4,088 k-NN runs over 36,808 training and 9,202 test vectors) or across 50 Perceptron epochs is computationally expensive.
  - **Susceptibility to Metric Gaming / Single-Class Collapse:** Because predicting `fat = 1` for every official on a 50:50 balanced test set yields 100% Recall and 49.82% Precision, an uninformed all-positive guess achieves a **66.50% F1-Score** (<i>TN</i> = 0, <i>FN</i> = 0). In k-NN, low-dimensional binary subsets like `['Is_Executive']` (Rank 1 at <i>k</i> = 3, Rank 2 at <i>k</i> = 5) and `['Is_Executive', 'Is_Major_Party']` (Rank 3 at <i>k</i> = 3) collapse thousands of candidates onto identical binary coordinates (`0.0` or `1.0`), causing majority-vote ties to swing sharply between **66.50% F1 (all-positive collapse at <i>k</i> = 3, 5)** and **42.84% F1 (all-negative collapse at <i>k</i> &ge; 7)** and tricking an F1-only ranker into choosing a degenerate classifier.

### 3.2 Method 2: Naïve Bayes-Guided Feature Transfer (`knn_bayes_3.py` & `perceptron.py`)
In **Method 2**, Gaussian Naïve Bayes serves as the upstream baseline and probabilistic feature filter before tuning k-NN and the Single-Layer Perceptron. Because Naïve Bayes estimates continuous and categorical class likelihoods independently rather than relying on raw distance ties, it naturally resists single-class collapse during exhaustive search. Its **Top 3 feature groups** are transferred directly to k-NN (<i>k</i> &isin; {1, 3, 5, 7, 9, 11, 13, 15}) and the Single-Layer Perceptron (`50 epochs`):
1. **NB Rank 1 Group (Baseline Best):** `Position + Region + Province + Tenure + Is_Major_Party` (61.53% Acc, 60.78% F1)
2. **NB Rank 2 Group:** `Position + Region + Province + Tenure` (60.76% F1)
3. **NB Rank 3 Group:** `Position + Province + Tenure` (60.52% F1)

- **How it works:** Separates feature selection from classifier tuning—Gaussian Naïve Bayes establishes the benchmark accuracy/F1 and isolates multi-feature subsets with genuine two-class separation, while downstream models (`knn_bayes_3.py` and `perceptron.py`) optimize across those top 3 subsets so their best-performing configurations can be directly compared against the Naïve Bayes baseline.
- **Advantages:**
  - **Prevents Degenerate Single-Feature Collapse:** Anchoring k-NN to multi-attribute combinations (`Position`, `Province`, `Region`, `Tenure`) eliminates binary tie instability and ensures meaningful True Negative (<i>TN</i>) and True Positive (<i>TP</i>) predictions across every neighborhood size <i>k</i>.
  - **Dramatic Speedup:** Reduces k-NN hyperparameter search from 511 &times; 8 = 4,088 evaluations down to 3 &times; 8 = 24 targeted evaluations (~170&times; faster).
- **Disadvantages:**
  - **Filter Bias (Conditional Independence Assumption):** Because the top 3 subsets are chosen under Naïve Bayes' independence assumption, feature combinations that rely on strong linear or geometric interactions—which a Perceptron or k-NN might prefer—can be filtered out before downstream evaluation.

### 3.3 Method 1 vs. Method 2 Comparison Summary

| Dimension | Method 1: Exhaustive 2<sup>9</sup> Search | Method 2: Naïve Bayes-Guided Transfer |
| :--- | :--- | :--- |
| **Search Scope** | All 2<sup>9</sup> &minus; 1 = 511 non-empty subsets per model | Top 3 subsets ranked by Gaussian Naïve Bayes baseline |
| **Evaluations Required** | 512 (NB), 4,088 (k-NN), 511 (Perceptron) | 24 (k-NN), 3 (Perceptron) |
| **Primary Strength** | Unbiased, model-specific global search | Eliminates binary tie collapse; fast & stable |
| **Primary Weakness** | Vulnerable to 66.50% F1 all-positive trap (`['Is_Executive']`) | Constrained by Naïve Bayes' feature ranking |
| **Top Model Outcome** | Naïve Bayes: **61.53% Acc / 60.78% F1** | NB Baseline: **61.53% Acc** &bull; Top k-NN: **60.69% Acc / 59.22% F1** |

### 3.4 Core Model Formulations & Evaluation Metrics
- **Gaussian Naïve Bayes:** Computes posterior class likelihoods under conditional independence with Laplace smoothing (<i>k</i> = 1.0):
  <div class="formula-box">
    <i>P</i>(<i>y</i> | <i>x</i><sub>1</sub>, &hellip;, <i>x</i><sub><i>n</i></sub>) &prop; <i>P</i>(<i>y</i>) &prod;<sub><i>i</i>=1..<i>n</i></sub> <i>P</i>(<i>x</i><sub><i>i</i></sub> | <i>y</i>)
  </div>
- **k-Nearest Neighbors (k-NN):** Classifies test instances via majority vote among the <i>k</i> nearest training neighbors under Euclidean distance (<i>p</i> = 2.0):
  <div class="formula-box">
    <i>d</i>(<i>x</i>, <i>v</i>) = ( &Sigma;<sub><i>i</i>=1..<i>n</i></sub> |<i>x</i><sub><i>i</i></sub> &minus; <i>v</i><sub><i>i</i></sub>|<sup>2</sup> )<sup>1/2</sup>
  </div>
- **Single-Layer Perceptron:** Evaluates a linear hyperplane <i>z</i> = &Sigma;<sub><i>i</i>=1..<i>n</i></sub> <i>w</i><sub><i>i</i></sub><i>x</i><sub><i>i</i></sub> + <i>b</i> passed through a Heaviside step activation (<i>&#375;</i> = 1 if <i>z</i> &ge; 0, else 0), updated via <i>w</i><sub><i>t</i>+1</sub> = <i>w</i><sub><i>t</i></sub> + &eta;(<i>y</i><sub><i>i</i></sub> &minus; <i>&#375;</i><sub><i>i</i></sub>)<i>x</i><sub><i>i</i></sub> over 50 epochs.
- **Evaluation Metrics:** Computed from scratch across all **9,202 holdout test instances** (<i>TP</i>, <i>FP</i>, <i>TN</i>, <i>FN</i>):
  <div class="formula-box">
    Accuracy = (<i>TP</i> + <i>TN</i>) / (<i>TP</i> + <i>TN</i> + <i>FP</i> + <i>FN</i>) &nbsp;&nbsp;|&nbsp;&nbsp;
    Precision = <i>TP</i> / (<i>TP</i> + <i>FP</i>) &nbsp;&nbsp;|&nbsp;&nbsp;
    Recall = <i>TP</i> / (<i>TP</i> + <i>FN</i>) &nbsp;&nbsp;|&nbsp;&nbsp;
    F1 = 2 &middot; (Precision &middot; Recall) / (Precision + Recall)
  </div>

---

## 4. Method 1 Results: Exhaustive 2<sup>9</sup> Combinatorial Search

### 4.1 Method 1 Performance Overview

<div class="slide-card-grid">
  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 61.53%;"></div></div>
      <div class="pill-pct">61.5%</div>
    </div>
    <div class="slide-card-title">Gaussian Naïve Bayes (Method 1 Best)</div>
    <p class="slide-card-desc">Achieved <strong>61.53% Accuracy</strong> and <strong>60.78% CV F1-Score</strong> across 512 combinations using <code>Position + Region + Province + Tenure + Is_Major_Party</code>.</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 55.30%;"></div></div>
      <div class="pill-pct">55.3%</div>
    </div>
    <div class="slide-card-title">Single-Layer Perceptron (Method 1 Best)</div>
    <p class="slide-card-desc">Selected <code>Region + Province + Tenure + Is_Executive</code> (50 epochs, non-convergent), achieving <strong>55.30% Accuracy</strong>, <strong>65.72% Precision</strong>, and <strong>36.97% F1-Score</strong>.</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 49.82%;"></div></div>
      <div class="pill-pct">49.8%</div>
    </div>
    <div class="slide-card-title">k-NN (Method 1 Degenerate Collapse)</div>
    <p class="slide-card-desc">Top 3 ranks collapsed on binary attributes: Rank 1 &amp; 2 <code>['Is_Executive']</code> (<i>k</i> = 3, 5) and Rank 3 <code>['Is_Executive', 'Is_Major_Party']</code> (<i>k</i> = 3), predicting 100% <code>fat = 1</code> (<strong>49.82% Accuracy</strong>, <strong>66.50%* F1</strong>, <i>TN</i> = 0).</p>
  </div>
</div>

### 4.2 Method 1 Results Table (All Models Under Exhaustive Search)

| Classifier (Method 1) | Best Feature Subset & Parameters | Accuracy | Precision | Recall | **F1-Score** | Confusion Matrix (<i>TP</i>, <i>FP</i>, <i>TN</i>, <i>FN</i>) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Gaussian Naïve Bayes (Rank 1)** | `Position + Region + Province + Tenure + Is_Major_Party` (<i>k</i> = 1.0) | **61.53%** | 62.00% | **59.60%** | **60.78%** | <i>TP</i> = 13,712, <i>FP</i> = 8,405, <i>TN</i> = 14,600, <i>FN</i> = 9,293 |
| **Single-Layer Perceptron (Best)** | `Region + Province + Tenure + Is_Executive` (50 epochs, unconverged) | 55.30% | **65.72%** | 25.71% | 36.97% | <i>TP</i> = 1,206, <i>FP</i> = 629, <i>TN</i> = 3,883, <i>FN</i> = 3,484 |
| **k-NN (Rank 1 &amp; Rank 2)** | `['Is_Executive']` (<i>k</i> = 3, 5) — *Degenerate All-Positive Collapse* | 49.82% | 49.82% | 100.00%* | 66.50%* | <i>TP</i> = 4,584, <i>FP</i> = 4,618, <i>TN</i> = 0, <i>FN</i> = 0 |
| **k-NN (Rank 3)** | `['Is_Executive', 'Is_Major_Party']` (<i>k</i> = 3) — *Degenerate Collapse* | 49.82% | 49.82% | 100.00%* | 66.50%* | <i>TP</i> = 4,584, <i>FP</i> = 4,618, <i>TN</i> = 0, <i>FN</i> = 0 |

*\*Note on Method 1 k-NN Collapse: Because `['Is_Executive']` only takes binary values (`0.0` or `1.0`), majority voting across tied neighbors predicts `fat = 1` for every test record at k = 3 and k = 5—yielding 100.00% Recall and 49.82% Precision (66.50% F1) with zero True Negatives (TN = 0).*

### 4.3 Method 1 Visual Charts & Confusion Matrices

<div class="chart-box">
<h3 style="margin-top:0;">Figure 2: Method 1 (Exhaustive 2⁹ Search) Metric Comparison</h3>
<svg viewBox="0 0 740 270" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
<rect width="740" height="270" fill="#f8fbff" rx="12"/>
<line x1="80" y1="30" x2="700" y2="30" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="75" x2="700" y2="75" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="120" x2="700" y2="120" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="165" x2="700" y2="165" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="210" x2="700" y2="210" stroke="#03256c" stroke-width="1.5"/>
<text x="70" y="34" font-size="11" text-anchor="end" fill="#475569">100%</text>
<text x="70" y="79" font-size="11" text-anchor="end" fill="#475569">75%</text>
<text x="70" y="124" font-size="11" text-anchor="end" fill="#475569">50%</text>
<text x="70" y="169" font-size="11" text-anchor="end" fill="#475569">25%</text>
<text x="70" y="214" font-size="11" text-anchor="end" fill="#475569">0%</text>
<rect x="130" y="99.2" width="32" height="110.8" fill="#03256c" rx="4"/>
<text x="146" y="93" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">61.5%</text>
<rect x="166" y="98.4" width="32" height="111.6" fill="#3b82f6" rx="4"/>
<text x="182" y="92" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">62.0%</text>
<rect x="202" y="100.6" width="32" height="109.4" fill="#38bdf8" rx="4"/>
<text x="218" y="94.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">60.8%</text>
<text x="182" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">Gaussian Naïve Bayes</text>
<rect x="330" y="110.5" width="32" height="99.5" fill="#03256c" rx="4"/>
<text x="346" y="104.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">55.3%</text>
<rect x="366" y="91.7" width="32" height="118.3" fill="#3b82f6" rx="4"/>
<text x="382" y="85.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">65.7%</text>
<rect x="402" y="143.5" width="32" height="66.5" fill="#38bdf8" rx="4"/>
<text x="418" y="137.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">37.0%</text>
<text x="382" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">Perceptron (M1 Search)</text>
<rect x="530" y="120.3" width="32" height="89.7" fill="#03256c" rx="4"/>
<text x="546" y="114" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">49.8%</text>
<rect x="566" y="120.3" width="32" height="89.7" fill="#3b82f6" rx="4"/>
<text x="582" y="114" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">49.8%</text>
<rect x="602" y="90.3" width="32" height="119.7" fill="#93c5fd" rx="4"/>
<text x="618" y="84" font-size="10" font-weight="bold" text-anchor="middle" fill="#1d4ed8">66.5%*</text>
<text x="582" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">k-NN ['Is_Executive']</text>
<rect x="165" y="248" width="12" height="12" fill="#03256c" rx="3"/><text x="182" y="258" font-size="11" fill="#334155">Accuracy</text>
<rect x="260" y="248" width="12" height="12" fill="#3b82f6" rx="3"/><text x="277" y="258" font-size="11" fill="#334155">Precision</text>
<rect x="355" y="248" width="12" height="12" fill="#38bdf8" rx="3"/><text x="372" y="258" font-size="11" fill="#334155">Valid F1-Score</text>
<rect x="470" y="248" width="12" height="12" fill="#93c5fd" rx="3"/><text x="487" y="258" font-size="11" fill="#334155">Degenerate All-Fat F1*</text>
</svg>
</div>

<div class="chart-box">
<h3 style="margin-top:0;">Figure 3: Method 1 Confusion Matrix Breakdown</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
<div style="background: #f8fbff; border: 1.5px solid #7dd3fc; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Gaussian Naïve Bayes (M1)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">13,712</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">8,405</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">9,293</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #03256c;">14,600</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1.5px solid #7dd3fc; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Perceptron (M1 Best Subset)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">1,206</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">629</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">3,484</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #03256c;">3,883</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1px solid #bae6fd; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">k-NN ['Is_Executive'] (M1 Collapse)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">4,584</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">4,618</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">0</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #64748b;">0</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #64748b;">TN (Collapsed)</div>
</div>
</div>
</div>
</div>
</div>

---

## 5. Method 2 Results: Naïve Bayes-Guided Feature Transfer

### 5.1 Method 2 Top-Rank Comparison (Baseline vs. Best Downstream k-NN & Perceptron)

In Method 2, Gaussian Naïve Bayes serves as the reference baseline whose top-ranked feature subsets guide downstream tuning. Comparing the **Gaussian Naïve Bayes baseline** directly against the **top-performing k-NN configuration** and **top-performing Perceptron configuration** isolates how distance-based and linear classifiers behave on the exact feature spaces validated by probabilistic search:

<div class="slide-card-grid">
  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 61.53%;"></div></div>
      <div class="pill-pct">61.5%</div>
    </div>
    <div class="slide-card-title">Gaussian Naïve Bayes (Feature Baseline)</div>
    <p class="slide-card-desc">Reference benchmark that selected the top feature groups: <strong>61.53% Accuracy</strong>, <strong>62.00% Precision</strong>, <strong>59.60% Recall</strong>, and <strong>60.78% F1-Score</strong>.</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 60.69%;"></div></div>
      <div class="pill-pct">60.7%</div>
    </div>
    <div class="slide-card-title">Top k-NN (NB Rank 3 Group, <i>k</i> = 11)</div>
    <p class="slide-card-desc">Best Method 2 F1-Score: <strong>60.69% Accuracy</strong>, <strong>61.28% Precision</strong>, <strong>57.29% Recall</strong>, and <strong>59.22% F1</strong> on <code>Position + Province + Tenure</code> (reaching <strong>61.46% Acc</strong> with <code>Region</code> at <i>k</i> = 15).</p>
  </div>

  <div class="slide-card">
    <div class="pill-row">
      <div class="pill-track"><div class="pill-fill" style="width: 49.52%;"></div></div>
      <div class="pill-pct">49.5%</div>
    </div>
    <div class="slide-card-title">Top Perceptron (NB Rank 1 Group)</div>
    <p class="slide-card-desc">Best Method 2 Perceptron F1-Score: <strong>49.52% Accuracy</strong>, <strong>50.37% Precision</strong>, <strong>65.48% Recall</strong>, and <strong>56.94% F1</strong> on <code>Position + Region + Province + Tenure + Is_Major_Party</code>.</p>
  </div>
</div>

### 5.2 Method 2 Top-Rank Comparison Table

| Classifier & Role (Method 2) | Top Feature Subset & Parameters | Accuracy | Precision | Recall | **F1-Score** | Confusion Matrix (<i>TP</i>, <i>FP</i>, <i>TN</i>, <i>FN</i>) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Gaussian Naïve Bayes (Baseline)** | `Position + Region + Province + Tenure + Is_Major_Party` (NB Rank 1) | **61.53%** | **62.00%** | 59.60% | **60.78%** | <i>TP</i> = 13,712, <i>FP</i> = 8,405, <i>TN</i> = 14,600, <i>FN</i> = 9,293 |
| **k-NN (Top Method 2 F1)** | `Position + Province + Tenure` (NB Rank 3, <i>k</i> = 11, <i>p</i> = 2.0) | 60.69% | 61.28% | 57.29% | 59.22% | <i>TP</i> = 2,626, <i>FP</i> = 1,659, <i>TN</i> = 2,959, <i>FN</i> = 1,958 |
| **Single-Layer Perceptron (Top M2 F1)** | `Position + Region + Province + Tenure + Is_Major_Party` (NB Rank 1, 50 epochs) | 49.52% | 50.37% | **65.48%** | 56.94% | <i>TP</i> = 3,071, <i>FP</i> = 3,026, <i>TN</i> = 1,486, <i>FN</i> = 1,619 |

*Note: Across the remaining Naïve Bayes candidate subsets, k-NN achieved **61.46% Accuracy** (58.82% F1) at k = 15 on NB Rank 2 (`Position + Region + Province + Tenure`), while the unconverged Perceptron dropped to **16.33%–24.58% F1** on NB Rank 2 and Rank 3 due to severe negative-class bias.*

### 5.3 Method 2 Visual Charts & Confusion Matrices

<div class="chart-box">
<h3 style="margin-top:0;">Figure 4: Method 2 Top-Rank Comparison (Naïve Bayes Baseline vs. Top k-NN & Perceptron)</h3>
<svg viewBox="0 0 740 270" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
<rect width="740" height="270" fill="#f8fbff" rx="12"/>
<line x1="80" y1="30" x2="700" y2="30" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="75" x2="700" y2="75" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="120" x2="700" y2="120" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="165" x2="700" y2="165" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="210" x2="700" y2="210" stroke="#03256c" stroke-width="1.5"/>
<text x="70" y="34" font-size="11" text-anchor="end" fill="#475569">100%</text>
<text x="70" y="79" font-size="11" text-anchor="end" fill="#475569">75%</text>
<text x="70" y="124" font-size="11" text-anchor="end" fill="#475569">50%</text>
<text x="70" y="169" font-size="11" text-anchor="end" fill="#475569">25%</text>
<text x="70" y="214" font-size="11" text-anchor="end" fill="#475569">0%</text>
<rect x="130" y="99.2" width="32" height="110.8" fill="#03256c" rx="4"/>
<text x="146" y="93" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">61.5%</text>
<rect x="166" y="98.4" width="32" height="111.6" fill="#3b82f6" rx="4"/>
<text x="182" y="92" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">62.0%</text>
<rect x="202" y="100.6" width="32" height="109.4" fill="#38bdf8" rx="4"/>
<text x="218" y="94.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">60.8%</text>
<text x="182" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">Naïve Bayes (Baseline)</text>
<rect x="330" y="100.8" width="32" height="109.2" fill="#03256c" rx="4"/>
<text x="346" y="94.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">60.7%</text>
<rect x="366" y="99.7" width="32" height="110.3" fill="#3b82f6" rx="4"/>
<text x="382" y="93.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">61.3%</text>
<rect x="402" y="103.4" width="32" height="106.6" fill="#38bdf8" rx="4"/>
<text x="418" y="97" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">59.2%</text>
<text x="382" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">Top k-NN (k=11, NB3)</text>
<rect x="530" y="120.9" width="32" height="89.1" fill="#03256c" rx="4"/>
<text x="546" y="114.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#03256c">49.5%</text>
<rect x="566" y="119.3" width="32" height="90.7" fill="#3b82f6" rx="4"/>
<text x="582" y="113" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">50.4%</text>
<rect x="602" y="107.5" width="32" height="102.5" fill="#38bdf8" rx="4"/>
<text x="618" y="101.5" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7">56.9%</text>
<text x="582" y="229" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#03256c">Top Perceptron (NB1)</text>
<rect x="220" y="248" width="12" height="12" fill="#03256c" rx="3"/><text x="237" y="258" font-size="11" fill="#334155">Accuracy</text>
<rect x="330" y="248" width="12" height="12" fill="#3b82f6" rx="3"/><text x="347" y="258" font-size="11" fill="#334155">Precision</text>
<rect x="440" y="248" width="12" height="12" fill="#38bdf8" rx="3"/><text x="457" y="258" font-size="11" fill="#334155">F1-Score</text>
</svg>
</div>

<div class="chart-box">
<h3 style="margin-top:0;">Figure 5: Method 1 vs. Method 2 k-NN Neighborhood Size (k) Tuning Comparison</h3>
<p style="font-size: 0.88rem; color: #475569; margin-top: -0.4rem; margin-bottom: 1rem;">
  Comparing how k-NN F1-Score evolves across odd neighborhood sizes (<i>k</i> = 1 to 15): <strong>Method 1</strong> (<code>['Is_Executive']</code>) exhibits extreme binary tie instability—spiking to the <strong>66.50%</strong> all-positive trap at <i>k</i> = 3, 5 before collapsing to <strong>42.84%</strong> at <i>k</i> &ge; 7—whereas <strong>Method 2</strong> (<code>Position + Province + Tenure</code>) produces a smooth, genuine discrimination curve peaking at <strong>59.22% F1 (<i>k</i> = 11)</strong>.
</p>
<svg viewBox="0 0 740 275" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
<rect width="740" height="275" fill="#f8fbff" rx="12"/>
<line x1="80" y1="30" x2="700" y2="30" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="60" x2="700" y2="60" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="90" x2="700" y2="90" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="120" x2="700" y2="120" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="150" x2="700" y2="150" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="180" x2="700" y2="180" stroke="#bae6fd" stroke-dasharray="4"/>
<line x1="80" y1="210" x2="700" y2="210" stroke="#03256c" stroke-width="1.5"/>
<text x="70" y="34" font-size="10.5" text-anchor="end" fill="#475569">70%</text>
<text x="70" y="64" font-size="10.5" text-anchor="end" fill="#475569">65%</text>
<text x="70" y="94" font-size="10.5" text-anchor="end" fill="#475569">60%</text>
<text x="70" y="124" font-size="10.5" text-anchor="end" fill="#475569">55%</text>
<text x="70" y="154" font-size="10.5" text-anchor="end" fill="#475569">50%</text>
<text x="70" y="184" font-size="10.5" text-anchor="end" fill="#475569">45%</text>
<text x="70" y="214" font-size="10.5" text-anchor="end" fill="#475569">40%</text>
<text x="115" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=1</text>
<text x="195" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=3</text>
<text x="275" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=5</text>
<text x="355" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=7</text>
<text x="435" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=9</text>
<text x="515" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#03256c">k=11</text>
<text x="595" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=13</text>
<text x="675" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="#334155">k=15</text>
<line x1="115" y1="125.4" x2="195" y2="51" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="195" y1="51" x2="275" y2="51" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="275" y1="51" x2="355" y2="193" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="355" y1="193" x2="435" y2="193" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="435" y1="193" x2="515" y2="193" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="515" y1="193" x2="595" y2="193" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<line x1="595" y1="193" x2="675" y2="193" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<circle cx="115" cy="125.4" r="4.5" fill="#64748b"/>
<text x="115" y="140" font-size="9" font-weight="bold" text-anchor="middle" fill="#64748b">54.1%</text>
<circle cx="195" cy="51" r="6" fill="#f59e0b" stroke="#92400e" stroke-width="1.5"/>
<text x="235" y="40" font-size="9.5" font-weight="800" text-anchor="middle" fill="#b45309">M1 Trap Peak: 66.50% (k=3, 5)</text>
<circle cx="275" cy="51" r="5" fill="#f59e0b" stroke="#92400e" stroke-width="1.2"/>
<circle cx="355" cy="193" r="4.5" fill="#64748b"/>
<text x="355" y="182" font-size="9" font-weight="bold" text-anchor="middle" fill="#64748b">42.8%</text>
<circle cx="435" cy="193" r="4.5" fill="#64748b"/>
<circle cx="515" cy="193" r="4.5" fill="#64748b"/>
<circle cx="595" cy="193" r="4.5" fill="#64748b"/>
<circle cx="675" cy="193" r="4.5" fill="#64748b"/>
<text x="675" y="182" font-size="9" font-weight="bold" text-anchor="middle" fill="#64748b">42.8%</text>
<line x1="115" y1="109.2" x2="195" y2="130.8" stroke="#03256c" stroke-width="3"/>
<line x1="195" y1="130.8" x2="275" y2="111.6" stroke="#03256c" stroke-width="3"/>
<line x1="275" y1="111.6" x2="355" y2="98.4" stroke="#03256c" stroke-width="3"/>
<line x1="355" y1="98.4" x2="435" y2="103.8" stroke="#03256c" stroke-width="3"/>
<line x1="435" y1="103.8" x2="515" y2="94.7" stroke="#03256c" stroke-width="3"/>
<line x1="515" y1="94.7" x2="595" y2="104.4" stroke="#03256c" stroke-width="3"/>
<line x1="595" y1="104.4" x2="675" y2="101.4" stroke="#03256c" stroke-width="3"/>
<circle cx="115" cy="109.2" r="4.5" fill="#03256c"/>
<text x="115" y="99" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">56.8%</text>
<circle cx="195" cy="130.8" r="4.5" fill="#03256c"/>
<text x="195" y="146" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">53.2%</text>
<circle cx="275" cy="111.6" r="4.5" fill="#03256c"/>
<text x="275" y="101" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">56.4%</text>
<circle cx="355" cy="98.4" r="4.5" fill="#03256c"/>
<text x="355" y="88" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">58.6%</text>
<circle cx="435" cy="103.8" r="4.5" fill="#03256c"/>
<text x="435" y="119" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">57.7%</text>
<circle cx="515" cy="94.7" r="6.5" fill="#10b981" stroke="#03256c" stroke-width="2"/>
<text x="515" y="81" font-size="10.5" font-weight="800" text-anchor="middle" fill="#047857">M2 Valid Peak: 59.22% (k=11)</text>
<circle cx="595" cy="104.4" r="4.5" fill="#03256c"/>
<text x="595" y="119" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">57.6%</text>
<circle cx="675" cy="101.4" r="4.5" fill="#03256c"/>
<text x="675" y="91" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#03256c">58.1%</text>
<line x1="120" y1="256" x2="148" y2="256" stroke="#03256c" stroke-width="3"/>
<circle cx="134" cy="256" r="4" fill="#10b981" stroke="#03256c" stroke-width="1.5"/>
<text x="155" y="260" font-size="11" font-weight="600" fill="#03256c">Method 2: Position + Province + Tenure (Stable)</text>
<line x1="435" y1="256" x2="463" y2="256" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6,4"/>
<circle cx="449" cy="256" r="4" fill="#f59e0b"/>
<text x="470" y="260" font-size="11" font-weight="600" fill="#475569">Method 1: ['Is_Executive'] (Tie-Collapse Step)</text>
</svg>
</div>

<div class="chart-box">
<h3 style="margin-top:0;">Figure 6: Method 2 Top-Rank Confusion Matrix Breakdown</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
<div style="background: #f8fbff; border: 1.5px solid #7dd3fc; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Gaussian Naïve Bayes (Baseline)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">13,712</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">8,405</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">9,293</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #03256c;">14,600</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1.5px solid #7dd3fc; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Top k-NN (k=11, NB Rank 3)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">2,626</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">1,659</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">1,958</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #03256c;">2,959</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
<div style="background: #f8fbff; border: 1px solid #bae6fd; border-radius: 14px; padding: 1rem; text-align: center;">
<div style="font-weight: 800; color: #03256c; margin-bottom: 0.6rem;">Top Perceptron (NB Rank 1)</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
<div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #166534;">3,071</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #15803d;">TP (Hit)</div>
</div>
<div style="background: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">3,026</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b91c1c;">FP (False Alarm)</div>
</div>
<div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #92400e;">1,619</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #b45309;">FN (Miss)</div>
</div>
<div style="background: #dbeafe; border: 1px solid #93c5fd; border-radius: 8px; padding: 0.6rem;">
<div style="font-size: 1.1rem; font-weight: 800; color: #03256c;">1,486</div>
<div style="font-size: 0.72rem; font-weight: 700; color: #1d4ed8;">TN (Reject)</div>
</div>
</div>
</div>
</div>
</div>

---

## 6. Comparative Analysis & Discussion

<div class="callout">
  <strong>Core Empirical Findings:</strong> Across both experimental pipelines, non-linear probabilistic and local-neighborhood models (Gaussian Naïve Bayes at <strong>61.53% Accuracy</strong> and Method 2 k-NN at <strong>60.69%–61.46% Accuracy / 59.22% F1-Score</strong>) substantially outperform the linear Single-Layer Perceptron (<strong>49.52%–55.30% Accuracy</strong>). Training diagnostics confirm that the dataset is fundamentally <strong>non-linearly separable</strong>—over 12,055–12,580 training records share identical feature vectors with opposite dynastic labels, preventing the Perceptron from ever converging (<code>Converged: False</code>).
</div>

1. **Why the Single-Layer Perceptron Failed to Converge Across Both Methods (`Converged: False`):**  
   In every experiment across Method 1 (`perceptron_feature_search.py`) and Method 2 (`perceptron.py`), the Perceptron ran all 50 epochs without converging. Our diagnostic check (`unavoidable with these features`) revealed that even on the training set of 36,808 records, **12,055 to 12,580 records** have identical encoded feature tuples (`Position`, `Region`, `Province`, `Tenure`) belonging to *both* `fat = 1` and `fat = 0` classes. Because a single linear hyperplane cannot separate overlapping feature points, the final-epoch step weights oscillated wildly depending on the last batch of updates—predicting `fat = 1` only **8.1%–12.3%** of the time on NB Rank 2 and Rank 3 (9.47%–15.25% Recall) while swinging to **66.3%** positive predictions on NB Rank 1 (65.48% Recall, 49.52% Accuracy). Under Method 1's exhaustive search, selecting `Region + Province + Tenure + Is_Executive` stabilized Accuracy at **55.30%** and Precision at **65.72%**, but Recall remained limited to **25.71%** (36.97% F1).
2. **Why Method 1 Collapsed on Binary k-NN Features (`['Is_Executive']`, 66.50% F1, 49.82% Accuracy):**  
   When k-NN searched all 511 feature subsets on the full 36,808-record training corpus, the top 3 configurations collapsed onto pure binary indicators (`['Is_Executive']` at <i>k</i> = 3, 5 and `['Is_Executive', 'Is_Major_Party']` at <i>k</i> = 3). Because every candidate is mapped onto only two discrete binary values (`0.0` or `1.0`), thousands of neighbors tie at zero distance. As shown in **Figure 5**, changing <i>k</i> causes the majority vote to flip abruptly like a step function—from **54.1% F1** at <i>k</i> = 1, up to **66.50% F1 (predicting 100% `fat = 1`, <i>TN</i> = 0)** at <i>k</i> = 3 and <i>k</i> = 5, and down to **42.84% F1** for all <i>k</i> &ge; 7—tricking an F1-only ranker into selecting a degenerate classifier.
3. **How Method 2 Restored True Two-Class Discrimination for k-NN (60.69%–61.46% Accuracy):**  
   Transferring Naïve Bayes' top multi-feature combinations (`Position`, `Province`, `Region`, `Tenure`, and `Is_Major_Party`) gave k-NN enough geographic and institutional resolution to separate local dynastic strongholds from non-dynastic officials. On `Position + Province + Tenure` (<i>k</i> = 11), k-NN achieved **60.69% Accuracy, 61.28% Precision, 57.29% Recall, and 59.22% F1-Score** (2,626 <i>TP</i> and 2,959 <i>TN</i>), while adding `Region` (<i>k</i> = 15) raised Accuracy to **61.46%** and Precision to **62.88%**.
4. **Why Gaussian Naïve Bayes Achieved the Strongest Overall Performance (61.53% Accuracy, 60.78% F1):**  
   Unlike a hard linear threshold (Perceptron) or discrete neighbor tie-voting (Method 1 k-NN), Gaussian Naïve Bayes models smooth class-conditional likelihood distributions across all 512 combinations. This allowed it to handle overlapping feature profiles gracefully and achieve the highest overall Accuracy (**61.53%**) and F1-Score (**60.78%**) with balanced true predictions (13,712 <i>TP</i> and 14,600 <i>TN</i>).

---

## 7. Conclusion & Future Directions

Based on our empirical experiments across **46,010 balanced election records** (evaluated on the full **9,202 holdout test population**), the data supports four concrete conclusions regarding both algorithmic behavior and Philippine political dynasty prediction:

1. **Gaussian Naïve Bayes Is the Best-Performing Classifier (61.53% Accuracy, 60.78% F1-Score):**  
   Across all models and feature selection strategies, Gaussian Naïve Bayes achieved the highest valid overall performance (**61.53% Accuracy, 62.00% Precision, 59.60% Recall, and 60.78% F1-Score**), correctly classifying **13,712 Fat Dynasty officials** and **14,600 Non-Fat officials** using `Position + Region + Province + Tenure + Is_Major_Party`. Its probabilistic likelihood estimation proved far more resilient to overlapping feature profiles than linear decision boundaries.
2. **Guided Feature Transfer (Method 2) Rescues k-NN from Method 1's Metric Trap:**  
   While Method 1's unconstrained 511-subset search was fooled by the **66.50% F1 all-positive baseline trap** (selecting binary `['Is_Executive']` at <i>k</i> = 3, 5 with 49.82% accuracy and 0 True Negatives), transferring Naïve Bayes' top feature subsets in Method 2 restored genuine two-class separation. Method 2 k-NN reached **60.69% Accuracy and 59.22% F1-Score** at <i>k</i> = 11 (`Position + Province + Tenure`, with 2,626 <i>TP</i> and 2,959 <i>TN</i>) and **61.46% Accuracy and 62.88% Precision** at <i>k</i> = 15 (`Position + Region + Province + Tenure`, with 2,533 <i>TP</i> and 3,123 <i>TN</i>), while cutting k-NN search runtime by ~99.4% (from 4,088 runs down to 24).
3. **Non-Linear Class Overlap Explains the Single-Layer Perceptron's Ceiling (49.52%–55.30% Accuracy):**  
   Diagnostic mistake counts prove that **12,055 to 12,580 training records** share identical structural feature vectors across opposite dynastic labels. Because the classes are not linearly separable in the encoded feature space, the Single-Layer Perceptron failed to converge (`Converged: False`) across every run—oscillating between conservative negative predictions (9.47%–15.25% Recall on NB Rank 2–3) and noisy positive bias (49.52% Accuracy on NB Rank 1), reaching at best **55.30% Accuracy and 36.97% F1-Score** under Method 1's exhaustive search (`Region + Province + Tenure + Is_Executive`).
4. **Structural & Geographic Features Alone Yield a ~61.5% Accuracy Ceiling Without Surnames:**  
   Across both Naïve Bayes (**61.53% Accuracy**) and Method 2 k-NN (**61.46% Accuracy**), the exact same four attributes consistently drive predictive signal: **electoral office (`Position`)**, **provincial/regional jurisdiction (`Province`, `Region`)**, **service duration (`Tenure`)**, and **coalition affiliation (`Is_Major_Party`)**. Deliberately excluding candidate `Last Name` prevents target leakage, but the resulting ~38.5% irreducible error demonstrates that non-dynastic incumbents frequently share identical office, party, and provincial profiles with Fat Dynasty officials.

### Limitations & Future Work
- **Averaged / Pocket Perceptron Stabilization:** Because standard single-layer Perceptron weights oscillate on non-linearly separable data (17,224–18,284 final-epoch training mistakes vs. 12,055–12,580 unavoidable mistakes), implementing the **Pocket Algorithm** (retaining the weight vector with the lowest training error across epochs) or an **Averaged Perceptron** would prevent final-epoch weight drift.
- **Categorical Encoding Geometry:** Mapping high-cardinality nominal attributes (`Province`, `Position`, `Party`) to sequential alphabetical integers introduces artificial numeric ordering that distorts Euclidean distances and linear hyperplanes. Future work should implement **one-hot encoding** or **out-of-fold target encoding**.
- **Richer Electoral & Socioeconomic Features:** Breaking past the ~61.5% structural ceiling will require incorporating non-surname electoral indicators—such as **vote margin**, **number of challengers**, **municipal income class**, and **multi-cycle incumbency streaks**—alongside non-linear ensemble classifiers such as **Random Forests** or **Multi-Layer Perceptrons (MLPs)**.

---

## 8. References & Disclosures

1. **Dataset Source:** Ateneo Policy Center (APC), Ateneo School of Government. *Political Dynasties Dataset (2004–2016)*. BetterGov PH.
2. **Course Materials:** CMSC 170 Lecture Slides & Lab Guidelines, University of the Philippines Los Baños.
3. **Development & Tooling Disclosure:** All data preprocessing, feature engineering, machine learning models, combinatorial searches, and evaluation pipelines were written from scratch in Python and NumPy by the group members, building upon course laboratory methodologies. Minimal LLM/AI assistance was used for code debugging/optimization and minor HTML/Markdown formatting on the project webpage.