from funciones_para_datasets import   procesa_cotizacion 


import pandas as pd
#import urllib
#import re
import datetime as dt
from datetime import date

import numpy as np
#import yfinance as yf
#from pandas_datareader import data as pdr
import pathlib


def proceso():

    PATH = pathlib.Path(__file__).parent

    DATA_PATH = PATH.joinpath("../datasets").resolve()

    datos_sin_procesar = pd.read_csv(
        (DATA_PATH.joinpath("./mov.csv").resolve()), sep=';')

    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
             "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

    datos = datos_sin_procesar.copy()

    # paso a minuscula las columnas y la info la descripcion
    datos.columns = datos.columns.str.lower()
    datos['descripcion'] = datos['descripcion'].str.lower()

    # le doy formato a la fecha
    datos['fecha'] = pd.to_datetime(datos['fecha'], format='%Y%m%d')

    # saca comas y puntos y convierte a numeros las columnas

    columnas = ['debito', 'credito', 'saldo']
    for columna in columnas:
        datos[columna] = datos[columna].str.replace('.', '', regex=True)
        datos[columna] = datos[columna].str.replace(',', '.', regex=True)
        datos[columna] = datos[columna].astype(float)

    anos = range(datos.fecha.iloc[-1].year, datos.fecha.iloc[0].year)

    procesa_cotizacion.proceso(datos.fecha.iloc[-1])
    dol = pd.read_excel((DATA_PATH.joinpath("./dolar.xlsx")
                         ).resolve(), sheet_name="cotizacion")
    datos_ccl = pd.read_excel(
        (DATA_PATH.joinpath("./dolar.xlsx")).resolve(), sheet_name="datos_ccl")
    datos_ccl_mensual = pd.read_excel(
        (DATA_PATH.joinpath("./dolar.xlsx")).resolve(), sheet_name="datos_ccl_mensual")

    #datasets_adicionales.descarga_datasets(datos.fecha.iloc[-1])

    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
             "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

    conceptos = []

    datos['concepto'] = np.where(datos.descripcion.str.contains("pago de servicios ente: "),
                                 datos.descripcion.map(
                                     lambda x: x[len("pago de servicios ente: "):]),
                                 np.where(datos.descripcion.str.contains("compra con tarjeta cabal debito"),
                                          datos.descripcion.map(
                                              lambda x: x[len("compra con tarjeta cabal debito tarj:xxxx comercio:"):]),
                                          np.where(
                                              datos.descripcion.str.contains(
                                                  "debito/credito automatico-tarjeta cabal"),
                                              "cabal",
                                              np.where(datos.descripcion.str.contains(
                                                  "debito/credito automatico-tarjeta visa"), "visa",
                                                  np.where(datos.descripcion.str.contains("cajero automatico"),
                                                           "retiro de cajero automatico",
                                                           np.where(datos.descripcion.str.contains(
                                                                    "debito/cred aut-segurcoop seg. empleado segur.empl. comb.fam"),
                                                                    "seguro de incendio",
                                                                    np.where(datos.descripcion.str.contains(
                                                                        "debito/cred aut-segurcoop seg. empleado"),
                                                               "seguro de incendio",
                                                               np.where(
                                                                        datos.descripcion.str.contains(
                                                                            "debito/cred aut-segurcoop seg. empleado segur.empl. autos"),
                                                                        "seguro auto",
                                                                        np.where(
                                                                            datos.descripcion.str.contains(
                                                                                "compra/venta de moneda extranjera"),
                                                                            "compra/venta de moneda extranjera", datos.descripcion
                                                                        )))))))))

    dolares = dol.copy()

    datos_final = pd.merge(datos, dolares, on='fecha', how='inner')

    datos_final['debito_usd'] = datos_final['debito'] / \
        datos_final['cotizacion']
    datos_final['credito_usd'] = datos_final['credito'] / \
        datos_final['cotizacion']

    datos_final = datos_final.fillna(0)

    datos_final['val_abs'] = datos_final['credito'] + datos_final['debito']
    datos_final['val_abs_usd'] = datos_final['credito_usd'] + \
        datos_final['debito_usd']

    conceptos = datos_final['concepto'].unique()
    conceptos.sort()

    anos = datos_final['fecha'].dt.year.unique()
    anos = anos.tolist()
    anos.sort()

    meses = datos_final['fecha'].dt.month.unique()
    meses.sort()
    meses = meses.tolist()

    dias = datos_final['fecha'].dt.day.unique()
    dias.sort()
    dias = dias.tolist()

    datos_final = pd.merge(datos_final, datos_ccl, on='fecha', how='outer')

    datos_final['ccl'] = datos_final['ccl'].fillna(method='bfill')

    datos_final = datos_final.dropna()

    datos_final['debito_usd_ccl'] = round(
        datos_final['debito'] / datos_final['ccl'], 2)
    datos_final['credito_usd_ccl'] = round(
        datos_final['credito'] / datos_final['ccl'], 2)

    datos_final = datos_final.fillna(0)

    datos_final['val_abs_usd_ccl'] = datos_final['credito_usd_ccl'] + \
        datos_final['debito_usd_ccl']

    datos_final = datos_final.set_index('fecha')
    datos_final['ano'] = datos_final.index.year
    datos_final['mes'] = datos_final.index.month

    datos_final = datos_final.sort_values(by='fecha')

    datos_final.to_csv((DATA_PATH.joinpath("./datos_procesados.csv")))

    return


def proceso_completo():
    proceso()
    

