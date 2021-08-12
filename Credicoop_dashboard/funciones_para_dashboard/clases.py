
import pandas as pd
import pathlib
from datetime import datetime, date


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


class Movimientos():
    def __init__(self):
        self.datos = pd.read_csv(
            (DATA_PATH.joinpath("./datos_procesados.csv").resolve()), sep=',')
        self.ano_actual = date.today().year
        self.ano_inicial = datetime.strptime(
            self.datos.fecha.iloc[0], '%Y-%m-%d').year
        self.anos = [ano for ano in range(
            self.ano_inicial, self.ano_actual + 1)]
        self.meses = [mes for mes in range(1, 13)]
        self.ing_proyectados = ""
        self.meses_nombres = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                              "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        self.conceptos_gastos = self.prepara_gastos()['concepto'].unique()

    def prepara_ingresos(self):
        datos_ingresos = self.datos.sort_index(ascending=True)
        sueldos = datos_ingresos.loc[(datos_ingresos['concepto'] == "acreditacion de sueldos ") | (
            datos_ingresos['concepto'] == "acreditacion de sueldos")]

        return sueldos

    def prepara_gastos(self):
        datos_gastos = self.datos.sort_index(ascending=True)
        datos_gastos.sort_index(ascending=True)
        gastos = datos_gastos[(datos_gastos['debito'] > 0) &
                              (datos_gastos['concepto'] != "suscripcion a fondo comun de inversion") &
                              (datos_gastos['concepto'] != "constitucion de plazo fijo") &
                              (datos_gastos['concepto'] != "compra/venta de moneda extranjera")]

        return gastos

    def prepara_gastos_tarjetas(self):
        datos_tarjetas = self.datos.sort_index(ascending=True)
        gastos_tarjetas = datos_tarjetas[(datos_tarjetas['debito'] > 0) &
                                         (datos_tarjetas['concepto'] == "cabal") |
                                         (datos_tarjetas['concepto'] == "visa")]

        return gastos_tarjetas

    def pivot(self, agrup1, agrup2, tipo_op, moneda):

        if moneda == "dolar":
            pivot = tipo_op.groupby([agrup1, agrup2], as_index=False)[
                'val_abs_usd_ccl'].sum()
            pivot['val_abs_usd_ccl'] = pivot['val_abs_usd_ccl'].round()
            pivot = pivot.pivot(index=agrup2, columns=agrup1,
                                values='val_abs_usd_ccl')
            return pivot

        else:
            pivot = tipo_op.groupby([agrup1, agrup2], as_index=False)[
                'val_abs'].sum()
            pivot['val_abs'] = pivot['val_abs'].round()
            pivot = pivot.pivot(index=agrup2, columns=agrup1, values='val_abs')
            return pivot

    def agrupado(self, agrup1, agrup2, tipo_op, moneda):

        if moneda == "dolar":
            agrupado = round(tipo_op.groupby([agrup1, agrup2], as_index=False)[
                             ['val_abs_usd_ccl']].sum())
            return agrupado

        else:
            agrupado = round(tipo_op.groupby(
                [agrup1, agrup2], as_index=False)[['val_abs']].sum())
            return agrupado

    def agrupado_ano_mes(self, agrup, tipo_op, moneda):

        if moneda == "dolar":
            agrupado = round(tipo_op.groupby([agrup], as_index=False)[
                             ['val_abs_usd_ccl']].sum())
            return agrupado

        else:
            agrupado = round(tipo_op.groupby(
                [agrup], as_index=False)[['val_abs']].sum())
            return agrupado

    def sueldos_sin_adicionales(self):
        sueldos = self.prepara_ingresos()
        sueldos = sueldos.sort_values('fecha')
        sueldos_sin_adic = pd.DataFrame()
        for x in self.anos:
            for y in self.meses:
                sueldos_sin_adic = sueldos_sin_adic.append(sueldos[sueldos.fecha == sueldos.fecha[(
                    sueldos['ano'] == x) & (sueldos['mes'] == y)].max()])
        sueldos_sin_adic = sueldos_sin_adic.reset_index()

        return sueldos_sin_adic

    def datos_importantes(self):
        sueldos = self.prepara_ingresos()
        datos = {}
        columnas = ['val_abs', 'val_abs_usd_ccl']
        nombres = ['peso', 'dolar_ccl']

        for col, nom in zip(columnas, nombres):
            filtro = sueldos.groupby(['ano', 'mes'], as_index=False)[col].sum()
            filtro = filtro.sort_values(by=['ano', 'mes'], ascending=False)
            dato = filtro.head(12)
            dato = int(round((dato[col].sum()) / 12))
            datos['sueldos_prom_ult_12_meses_' + str(nom)] = dato
            dato = filtro.head(24)
            dato = dato.tail(12)
            dato = int(round((dato[col].sum()) / 12))
            datos['sueldos_prom_12_meses_ant_' + str(nom)] = dato

            ano_actual = date.today().year
            ano_pasado = ano_actual - 1

            dato = filtro.loc[filtro['ano'] == ano_actual]
            dato = dato.sort_values(by=['mes'], ascending=False)
            dato = int(round((dato[col].sum()) / (dato.mes.iloc[0])))
            datos['sueld_prom_ano_actual_' + str(nom)] = dato

            dato = filtro.loc[filtro['ano'] == ano_pasado]
            dato = dato.sort_values(by=['mes'], ascending=False)
            dato = int(round((dato[col].sum()) / (dato.mes.iloc[0])))
            datos['sueld_prom_ano_pasado_' + str(nom)] = dato

        datos_importantes = pd.DataFrame(
            [[key, datos[key]] for key in datos.keys()])

        return datos_importantes

    def gastos(self):
        datos_procesados=self.datos
        datos = datos_procesados.sort_index(ascending=True)
        gastos = datos[(datos['debito'] > 0) &
                    (datos['concepto'] != "suscripcion a fondo comun de inversion") &
                    (datos['concepto'] != "constitucion de plazo fijo") &
                    (datos['concepto'] != "compra/venta de moneda extranjera")]

        return gastos


    def gastos_tarjetas(self):
        datos_procesados=self.datos
        datos = datos_procesados.sort_index(ascending=True)

        gastos_tarjetas = datos[(datos['debito'] > 0) &
                                (datos['concepto'] == "cabal") |
                                (datos['concepto'] == "visa")]
        return gastos_tarjetas