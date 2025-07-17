
# Analyze wallet credit scores: distribution, summary stats, and behavioral insights
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the wallet scores CSV
df = pd.read_csv('../wallet_scores.csv')


# Plot and save a histogram of the score distribution
bins = np.arange(0, 1100, 100)
plt.figure(figsize=(10, 6))
plt.hist(df['score'], bins=bins, edgecolor='black', alpha=0.7)
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('score_distribution.png')
print("Score distribution plot saved as 'score_distribution.png'.")
plt.show()


# Print summary stats for analysis.md
print('\nScore Range Breakdown:')
ranges = [(i, i + 100) for i in range(0, 1000, 100)]
print(f"{'Score Range':<12} | {'Wallet Count':<12}")
print('-' * 28)
for r in ranges:
    count = ((df['score'] >= r[0]) & (df['score'] < r[1])).sum()
    print(f"{r[0]:>3}-{r[1] - 1:<7} | {count:<12}")


# Show descriptive stats for lowest and highest score ranges
low = df[df['score'] < 200]
high = df[df['score'] >= 800]

print('\n---')
print('Low Score Wallets (< 200):')
if low.empty:
    print('  No wallets in this range.')
else:
    print(low.describe(include='all'))

print('\nHigh Score Wallets (≥ 800):')
if high.empty:
    print('  No wallets in this range.')
else:
    print(high.describe(include='all'))
