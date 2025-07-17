import argparse
import json
import pandas as pd
import numpy as np
from collections import defaultdict
from tqdm import tqdm

# --- Feature Engineering Functions ---
def extract_features(transactions):
    features = defaultdict(lambda: defaultdict(float))
    timestamps = defaultdict(list)
    assets = defaultdict(set)
    for tx in transactions:
        # Use 'userWallet' as wallet key
        wallet = tx.get('userWallet')
        if not wallet:
            continue  # skip if no wallet identifier
        action = tx.get('action', '').lower()
        # Extract amount and asset from actionData if present
        action_data = tx.get('actionData', {})
        try:
            amount = float(action_data.get('amount', 0))
        except Exception:
            amount = 0
        asset = action_data.get('assetSymbol', None)
        ts = int(tx.get('timestamp', 0))
        features[wallet]['total_tx'] += 1
        features[wallet][f'{action}_count'] += 1
        features[wallet][f'{action}_amount'] += amount
        if action == 'liquidationcall':
            features[wallet]['liquidations'] += 1
        if action == 'repay':
            features[wallet]['total_repaid'] += amount
        if action == 'borrow':
            features[wallet]['total_borrowed'] += amount
        if asset:
            assets[wallet].add(asset)
        timestamps[wallet].append(ts)
    # Post-process features
    for wallet in features:
        txs = timestamps[wallet]
        if txs:
            features[wallet]['active_days'] = (max(txs) - min(txs)) / 86400 + 1
            features[wallet]['tx_per_day'] = features[wallet]['total_tx'] / features[wallet]['active_days']
            features[wallet]['first_tx'] = min(txs)
            features[wallet]['last_tx'] = max(txs)
        else:
            features[wallet]['active_days'] = 1
            features[wallet]['tx_per_day'] = features[wallet]['total_tx']
            features[wallet]['first_tx'] = 0
            features[wallet]['last_tx'] = 0
        features[wallet]['unique_assets'] = len(assets[wallet])
        # Ratios
        features[wallet]['repay_borrow_ratio'] = (
            features[wallet]['total_repaid'] / features[wallet]['total_borrowed']
            if features[wallet]['total_borrowed'] > 0 else 0
        )
    return features

# --- Scoring Function ---
def score_wallet(feat):
    score = 500
    # Repay/Borrow ratio
    if feat['repay_borrow_ratio'] >= 0.95:
        score += 200
    elif feat['repay_borrow_ratio'] >= 0.75:
        score += 100
    elif feat['repay_borrow_ratio'] >= 0.5:
        score += 50
    else:
        score -= 100
    # Liquidations
    if feat['liquidations'] == 0:
        score += 100
    elif feat['liquidations'] <= 2:
        score += 25
    else:
        score -= 100
    # Activity
    if feat['tx_per_day'] > 2:
        score += 50
    elif feat['tx_per_day'] < 0.2:
        score -= 50
    # Unique assets
    if feat['unique_assets'] >= 3:
        score += 50
    elif feat['unique_assets'] == 1:
        score -= 25
    # Total transactions
    if feat['total_tx'] > 100:
        score += 25
    # Clamp score
    score = max(0, min(1000, int(score)))
    return score

# --- Main Script ---
def main():
    parser = argparse.ArgumentParser(description='Aave V2 Wallet Credit Scoring')
    parser.add_argument('--input', required=True, help='Path to user-transactions.json')
    parser.add_argument('--output', required=True, help='Path to output CSV file')
    args = parser.parse_args()

    print('Loading data...')
    with open(args.input, 'r') as f:
        data = json.load(f)

    print('Extracting features...')
    features = extract_features(data)

    print('Scoring wallets...')
    rows = []
    for wallet, feat in tqdm(features.items()):
        score = score_wallet(feat)
        row = {'wallet': wallet, 'score': score}
        row.update(feat)
        rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(args.output, index=False)
    print(f'Saved scores to {args.output}')

if __name__ == '__main__':
    main()
