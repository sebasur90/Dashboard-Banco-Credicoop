import pandas as pd
import urllib
import urllib.request
import pathlib
import datetime as dt
from pandas_datareader import data as pdr


PATH = pathlib.Path(__file__).parent

DATA_PATH = PATH.joinpath("../datasets").resolve()


def proceso(fecha_inicio_dataset_credicoop):

    url = "https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/com3500.xls"
    urllib.request.urlretrieve(
        url, (DATA_PATH.joinpath("./dolar.xlsx"))) 
    cotizacion = pd.read_excel((DATA_PATH.joinpath("./dolar.xlsx")))
    

    cotizacion = cotizacion.drop(
        ["Unnamed: 0", "Unnamed: 1", "Unnamed: 4", "Unnamed: 5"], axis=1)

    cotizacion = cotizacion.drop(range(0, 3), axis=0)

    cotizacion.columns = ['fecha', 'cotizacion']

    cotizacion['fecha'] = pd.to_datetime(cotizacion['fecha'], format='%Y%m%d')

    #yf.pdr_override()

    start = fecha_inicio_dataset_credicoop

    now = dt.datetime.now()

    df_peso = pdr.get_data_yahoo("ggal.ba", start, now)

    df_dolar = pdr.get_data_yahoo("ggal", start, now)

    df_peso = df_peso.reset_index()

    df_dolar = df_dolar.reset_index()

    datos_ccl = pd.merge(df_peso, df_dolar, on='Date', how='outer')

    datos_ccl.columns = datos_ccl.columns.str.lower()

    datos_ccl = datos_ccl.sort_values(by='date', ascending=False)

    datos_ccl = datos_ccl.fillna(method='bfill')

    datos_ccl['ccl'] = datos_ccl['adj close_x']*10 / datos_ccl['adj close_y']

    datos_ccl.rename(columns={'date': 'fecha'}, inplace=True)

    datos_ccl = datos_ccl.drop(datos_ccl.columns[1: 13], axis=1)

    datos_ccl_mensual = datos_ccl.copy()

    datos_ccl_mensual = datos_ccl_mensual.set_index('fecha')

    datos_ccl_mensual['ano'] = datos_ccl_mensual.index.year
    datos_ccl_mensual['mes'] = datos_ccl_mensual.index.month

    datos_ccl_mensual = datos_ccl_mensual.groupby(
        ['ano', 'mes'], as_index=False)['ccl'].mean()

    with pd.ExcelWriter((DATA_PATH.joinpath("./dolar.xlsx"))) as writer:
        cotizacion.to_excel(writer, sheet_name='cotizacion'),
        datos_ccl.to_excel(writer, sheet_name='datos_ccl'),
        datos_ccl_mensual.to_excel(writer, sheet_name='datos_ccl_mensual')

    return cotizacion, datos_ccl, datos_ccl_mensual



