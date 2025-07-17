import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to user-transactions.json')
args = parser.parse_args()

with open(args.input, 'r') as f:
    data = json.load(f)

print('First 3 records:')
for i, tx in enumerate(data[:3]):
    print(f'--- Record {i+1} ---')
    for k, v in tx.items():
        print(f'{k}: {v}')
    print()
