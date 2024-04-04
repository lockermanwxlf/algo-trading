import pandas as pd
from datetime import datetime
from os.path import exists


def get_ticker(symbol: str, from_date_string: str):
    to_date_string = '-'.join(datetime.today().isoformat('-').split('-')[0:-1])
    cache_name = f'{symbol}_{from_date_string}_{to_date_string}.csv'
    timestamp1 = round(datetime.fromisoformat(from_date_string).timestamp())
    timestamp2 = round(datetime.today().timestamp())

    if exists(f'csv_cache/{cache_name}'):
        print(f'{symbol} data found in cache.')
        df = pd.read_csv(f'csv_cache/{cache_name}', parse_dates=True, index_col=0, date_format='%Y-%m-%d')
    else:
        print(f'Obtaining {symbol} from remote.')
        df = pd.read_csv(
            f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={timestamp1}&period2={timestamp2}&interval=1d&events=history&includeAdjustedClose=true',
            parse_dates=True, index_col=0)
        df.to_csv(f'csv_cache/{cache_name}')
    df.index.name = 'Date'
    return df
