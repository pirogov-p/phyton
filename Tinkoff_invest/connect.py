from openapi_client import openapi
token = 't.b33Iid4Gn3-8JztmIXcRCFxQ8vsKl2wD_eYgb1PtyPtoyVSE6MYJ7EoYNNSHa9scLIXsVlmyCN0c6NmMBRicOw'
client = openapi.api_client(token)
# Получение списка облигаций
bonds = client.market.market_bonds_get()
# Получение списка ETF
etfs = client.market.market_etfs_get()
# Получение списка акций
stocks = client.market.market_stocks_get()
instr_list = bonds.payload.instruments + etfs.payload.instruments + stocks.payload.instruments

# instr_list[:3]
instr = client.market.market_search_by_ticker_get('BTI')
print(etfs)
