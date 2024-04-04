import pandas as pd


def stochastic(price: pd.Series, high: pd.Series, low: pd.Series, n: int = 14, k: int = 3) -> pd.Series:
    max_high = high.rolling(n).max()
    min_low = low.rolling(n).min()
    return ((price - min_low) / (max_high - min_low)).rolling(k).mean().rolling(k).mean()


def z_score(price: pd.Series, n: int):
    window = price.rolling(n)
    return (price - window.mean()) / window.std()
