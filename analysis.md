

# Aave V2 Wallet Credit Score Analysis

Welcome! This report explores the creditworthiness of wallets interacting with the Aave V2 protocol, based on their historical transaction behavior. Our goal: to assign each wallet a transparent, data-driven score from 0 (very risky) to 1000 (exceptionally reliable).

---

## Score Distribution at a Glance

How do most wallets behave? Here’s the breakdown:

| Score Range | Wallet Count |
|-------------|--------------|
| 0-99        | 0            |
| 100-199     | 0            |
| 200-299     | 3            |
| 300-399     | 15           |
| 400-499     | 1750         |
| 500-599     | 723          |
| 600-699     | 173          |
| 700-799     | 161          |
| 800-899     | 554          |
| 900-999     | 118          |

**Key takeaways:**
- The vast majority of wallets are clustered in the 400–599 range, representing average, non-risky users.
- Very few wallets are at the extremes—either very risky (0–199) or exceptionally reliable (900–999).

---

## What Do These Scores Mean?

### Low Score Wallets (0–199)

No wallets landed in this range. This suggests that either the dataset is relatively clean, or the scoring model is conservative in flagging risky behavior. In other words, there are no obvious bots or exploiters in this sample.

### Mid Score Wallets (400–599)

Most users fall here. These are your typical DeFi participants: they interact with the protocol, may borrow and repay, and generally avoid risky moves like getting liquidated. They’re neither superstars nor troublemakers—just steady users.

### High Score Wallets (800–999)

This is the “gold standard” group. Out of 3,497 wallets, 672 scored 800 or above. What sets them apart?

- **Consistent, responsible activity:** They deposit, borrow, and repay regularly.
- **Almost no liquidations:** These users rarely, if ever, get liquidated—a sign of careful risk management.
- **High, stable scores:** The average score in this group is about 852, with little variation.

---

## Statistical Deep Dive

**High Score Wallets (≥ 800):**

| Statistic                 | Value  |
|---------------------------|--------|
| Number of wallets         | 672    |
| Mean score                | 851.9  |
| Standard deviation        | 32.1   |
| Minimum score             | 800    |
| Maximum score             | 925    |
| Mean liquidations         | 1.0    |
| Mean liquidation amount   | 0.0    |

These users are the protocol’s most reliable participants: they almost never get liquidated, and their activity is both regular and responsible.

**Mid Score Wallets (400–599):**

- This is the “average” group. They may have some risk factors (e.g., occasional missed repayments or low activity), but nothing extreme.
- Liquidations are rare, and most activity is routine.

**Low Score Wallets (< 200):**

- No data available—no wallets scored this low.

---

## Visualizing the Results

To better understand the spread of wallet credit scores, we generated a histogram plot. This visualization helps quickly spot where most users fall and highlights the rarity of extremely high or low scores.

![Score Distribution](score_distribution.png)

*Figure: Distribution of wallet credit scores. Most users are in the middle ranges, with very few at the extremes.*

---

## Final Thoughts

This analysis shows that most Aave V2 users are responsible, with only a small fraction standing out as exceptionally reliable. The absence of very low scores is encouraging, suggesting a healthy user base and/or a robust scoring model. For protocol designers, this kind of scoring can help identify both top users and potential risks, supporting better DeFi ecosystem management.

If you have questions or want to extend this analysis, all code and logic are fully documented in the repository.

---

## Statistical Analysis

### Low Score Wallets (< 200)

No wallets were found in this range, so no statistical summary is available for extremely low scores. This suggests either the dataset is clean or the scoring model is not aggressive in penalizing risky behavior.

### High Score Wallets (≥ 800)

**Descriptive statistics for high score wallets:**

| Statistic | Value |
|-----------|-------|
| Count     | 672   |
| Mean Score| 851.9 |
| Std Dev   | 32.1  |
| Min Score | 800   |
| Max Score | 925   |
| Liquidations (mean) | 1.0 |
| Liquidation Amount (mean) | 0.0 |

**Behavioral summary:**
- High score wallets have almost no liquidations (mean = 1.0, but liquidation amount is 0.0, suggesting rare or minor events).
- These wallets are active, with regular deposits and repayments, and show responsible DeFi usage.
- The high mean and low standard deviation indicate a consistently good behavior among these wallets.

### Mid Score Wallets (400–599)

- The majority of wallets fall in this range, representing average users who may have some risk factors but are not highly risky or highly reliable.
- These wallets likely have moderate activity, some borrow/repay actions, and few or no liquidations.

---

## Score Distribution Plot

The following plot visualizes the distribution of wallet credit scores:

![Score Distribution](score_distribution.png)

---
