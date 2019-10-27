import datetime
import san
import logging
import pandas as pd
import numpy as np

from env import API_KEY, START, END, INTERVAL, ITERATE_EVER_DAYS
logging.basicConfig(level = logging.INFO)


logging.info(u'Getting data...')

san.ApiConfig.api_key = API_KEY
start = datetime.datetime.strptime(START, '%Y-%m-%d').date()
end = datetime.datetime.strptime(END, '%Y-%m-%d').date()
btc_prices = pd.DataFrame(None)
eth_prices = pd.DataFrame(None)
ex_flows = pd.DataFrame(None)

for i in range(int(np.ceil((end - start).days / ITERATE_EVER_DAYS))):
    start_date = str(start + datetime.timedelta(days=ITERATE_EVER_DAYS * i))
    end_date = str(min(end, start + datetime.timedelta(days=ITERATE_EVER_DAYS * (i + 1) - 1)))

    btc_price = san.get(
        f'prices/bitcoin',
        from_date=start_date,
        to_date=end_date,
        interval=INTERVAL
    )
    eth_price = san.get(
        f'prices/ethereum',
        from_date=start_date,
        to_date=end_date,
        interval=INTERVAL
    )
    ex_flow = san.get(
        f'exchange_funds_flow/ethereum',
        from_date=start_date,
        to_date=end_date,
        interval=INTERVAL
    )
    btc_prices = btc_prices.append(btc_price)
    eth_prices = eth_prices.append(eth_price)
    ex_flows = ex_flows.append(ex_flow)

btc_prices.columns = ['btc_marketcap', 'btc_priceBtc', 'btc_priceUsd', 'btc_volume']
eth_prices.columns = ['eth_marketcap', 'eth_priceBtc', 'eth_priceUsd', 'eth_volume']

data = btc_prices.join(eth_prices).join(ex_flows)
data.to_csv('../data/onchain.csv', index=True)
logging.info(u'Successfully got data!')
