import pandas as pd

url = 'https://dayross23.blob.core.windows.net/data/Superstore_order.xls'


response = pd.read_excel(url)

print(response)


