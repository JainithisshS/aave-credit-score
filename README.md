# Aave V2 Wallet Credit Scoring

This repository provides a robust, transparent machine learning pipeline to assign a credit score (0-1000) to wallets based on their historical transaction behavior on the Aave V2 protocol.

## Project Structure

- `src/score_wallets.py` — Main script to process the raw transaction JSON and output wallet scores.
- `analysis.md` — Post-scoring analysis, including score distribution and behavioral insights.
- `README.md` — This file. Explains methodology, features, and scoring logic.


## How to Use & Deploy

### 1. Prerequisites

- Python 3.8 or newer
- Recommended: Create a virtual environment
- Required Python packages:
  - pandas
  - numpy
  - tqdm
  - matplotlib (for analysis/visualization)

Install dependencies:
```sh
pip install pandas numpy tqdm matplotlib
```

### 2. Download the Data

Download the user-transactions JSON file from the provided link and place it in your project directory.

### 3. Score Wallets

Run the scoring script to generate wallet scores:
```sh
python src/score_wallets.py --input path/to/user-transactions.json --output wallet_scores.csv
```
This will create a `wallet_scores.csv` file with all wallet scores and features.

### 4. Analyze Results & Visualize

To generate a score distribution plot and summary statistics, run:
```sh
python src/analyze_scores.py
```
This will create `score_distribution.png` and print summary stats for your report.

### 5. Review the Analysis

Open `analysis.md` to see:
- Score distribution table
- Behavioral insights for low, mid, and high score wallets
- Statistical summaries
- The score distribution plot

---

## Methodology Overview

- **Feature Engineering**: Extracts behavioral features from transaction history (e.g., action counts, ratios, time-based stats, liquidation events).
- **Scoring Model**: Uses a transparent, explainable model (e.g., rule-based or tree-based ML) to assign scores.
- **Transparency**: All logic and features are documented for extensibility.


See below for more details on features and scoring logic.

---

## Features Used

- Total number of transactions
- Counts of each action type (deposit, borrow, repay, redeem, liquidation)
- Ratios (e.g., repay/borrow, deposit/borrow)
- Number and frequency of liquidations
- Average and variance of transaction amounts
- Time between transactions (activity regularity)
- First and last activity timestamps
- Unique assets interacted with

## Scoring Logic

- High scores: Consistent repayments, low/no liquidations, regular activity, diversified assets, high repay/borrow ratio.
- Low scores: Frequent liquidations, high borrow with low repay, erratic or bot-like activity, single-asset focus, short-lived wallets.

---

## Project Highlights

- **One-step scoring**: Easily process any compatible Aave V2 transaction dataset.
- **Transparent logic**: All features and scoring rules are documented and easy to extend.
- **Actionable analysis**: Quickly identify reliable, average, and risky wallets for further investigation or reward.
- **Ready for production**: Modular code and clear documentation make it easy to adapt or deploy in other environments.

For any questions or to extend this project, see the code and comments in the `src/` directory.
