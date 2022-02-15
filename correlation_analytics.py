from itertools import combinations
from os import listdir, path

import pandas as pd


klines_names = [
    "OpenTime",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "CloseTime",
    "QuoteAssetVolume",
    "NumberOfTrades",
    "TakerBuyBaseAssetVolume",
    "TakerBuyQuoteAssetVolume",
    "Ignore",
]

base_directory = path.join("binance-public-data", "python", "data", "spot", "monthly", "klines")
klines_dataframes = {}


for ticker in listdir(base_directory):
    klines_dataframes[ticker] = pd.read_csv(
        path.join(base_directory, ticker, "1d", f"{ticker}-1d-2022-01.zip"),
        header=None,
        names=klines_names,
    )


avg_correlation = 0
correlations = []
max_correlation = 0
# leveraged tokens

for first_ticker, second_ticker in combinations(klines_dataframes.keys(), 2):
    correlation = klines_dataframes[first_ticker]['Close'].corr(
        klines_dataframes[second_ticker]['Close']
    )
    print(first_ticker, second_ticker, correlation)
    correlations.append(correlation)
    max_correlation = max(correlation, max_correlation)


print(sum(correlations) / len(correlations))
# 100 - 9 = 91
