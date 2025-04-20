import pandas as pd
data = pd.read_csv(
    'nsw-property-sales-data-updated20240821.csv', sep=',')


data['Contract date'] = pd.to_datetime(
    data['Contract date'], format='%d/%m/%Y')

data['Contract date'] = data['Contract date'].dt.strftime(
    '%Y%m%d').astype('Int64')

data = data[data['Contract date'] > 20231200]


condicao1 = (data['Purchase price'] >= 900000) & (
    data['Purchase price'] <= 1000000)
condicao2 = data['Purchase price'] > 1400000

data_filtrada = data[condicao1 | condicao2]

data_filtrada.to_csv('result1.csv', index=False)

data_filtrada = data_filtrada[data_filtrada["Primary purpose"] == "Residence"]

data_filtrada = data_filtrada[data_filtrada["Property unit number"].isnull()]

data_filtrada.to_csv('result2.csv', index=False)
