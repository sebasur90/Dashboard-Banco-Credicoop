from funciones_para_dashboard.clases import Movimientos
from .app import apli

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.express as px
import pathlib
import pandas as pd
from datetime import date
import datetime as dt
import dash_bootstrap_components as dbc
import numpy as np
import math


mov = Movimientos()


datos_imp = mov.datos_importantes()
datos_imp.columns = ['concepto', 'importe']


def sueldos_prom_ult_12_meses_peso():

    sueldos_prom_ult_12_meses_peso = datos_imp[datos_imp.concepto ==
                                               "sueldos_prom_ult_12_meses_peso"].importe.iloc[0]
    sueldos_prom_12_meses_ant_peso = datos_imp[datos_imp.concepto ==
                                               "sueldos_prom_12_meses_ant_peso"].importe.iloc[0]
    if sueldos_prom_ult_12_meses_peso >= sueldos_prom_12_meses_ant_peso:
        promedio = round((sueldos_prom_ult_12_meses_peso /
                         sueldos_prom_12_meses_ant_peso - 1) * 100, 2)
        return "fas fa-arrow-up", "green", sueldos_prom_ult_12_meses_peso, sueldos_prom_12_meses_ant_peso, promedio, "fas fa-caret-up"
    else:
        promedio = round((sueldos_prom_ult_12_meses_peso /
                         sueldos_prom_12_meses_ant_peso - 1) * 100, 2)
        return "fas fa-arrow-down", "red", sueldos_prom_ult_12_meses_peso, sueldos_prom_12_meses_ant_peso, promedio, "fas fa-caret-down"


def sueldos_prom_ult_12_meses_dolar():
    sueldos_prom_ult_12_meses_dolar_ccl = \
        datos_imp[datos_imp.concepto ==
                  "sueldos_prom_ult_12_meses_dolar_ccl"].importe.iloc[0]
    sueldos_prom_12_meses_ant_dolar_ccl = \
        datos_imp[datos_imp.concepto ==
                  "sueldos_prom_12_meses_ant_dolar_ccl"].importe.iloc[0]
    if sueldos_prom_ult_12_meses_dolar_ccl >= sueldos_prom_12_meses_ant_dolar_ccl:
        promedio = round((sueldos_prom_ult_12_meses_dolar_ccl /
                         sueldos_prom_12_meses_ant_dolar_ccl - 1) * 100, 2)
        return "fas fa-arrow-up", "green", sueldos_prom_ult_12_meses_dolar_ccl, sueldos_prom_12_meses_ant_dolar_ccl, promedio, "fas fa-caret-up"
    else:
        promedio = round((sueldos_prom_ult_12_meses_dolar_ccl /
                         sueldos_prom_12_meses_ant_dolar_ccl - 1) * 100, 2)
        return "fas fa-arrow-down", "red", sueldos_prom_ult_12_meses_dolar_ccl, sueldos_prom_12_meses_ant_dolar_ccl, promedio, "fas fa-caret-down"


def sueld_prom_ano_actual_peso():
    sueld_prom_ano_actual_peso = datos_imp[datos_imp.concepto ==
                                           "sueld_prom_ano_actual_peso"].importe.iloc[0]
    sueld_prom_ano_pasado_peso = datos_imp[datos_imp.concepto ==
                                           "sueld_prom_ano_pasado_peso"].importe.iloc[0]
    if sueld_prom_ano_actual_peso >= sueld_prom_ano_pasado_peso:
        promedio = round((sueld_prom_ano_actual_peso /
                         sueld_prom_ano_pasado_peso - 1) * 100, 2)
        return "fas fa-arrow-up", "green", sueld_prom_ano_actual_peso, sueld_prom_ano_pasado_peso, promedio, "fas fa-caret-up"
    else:
        promedio = round((sueld_prom_ano_actual_peso /
                         sueld_prom_ano_pasado_peso - 1) * 100, 2)
        return "fas fa-arrow-down", "red", sueld_prom_ano_actual_peso, sueld_prom_ano_pasado_peso, promedio, "fas fa-caret-down"


def sueld_prom_ano_actual_dolar_ccl():
    sueld_prom_ano_actual_dolar_ccl = datos_imp[datos_imp.concepto ==
                                                "sueld_prom_ano_actual_dolar_ccl"].importe.iloc[0]
    sueld_prom_ano_pasado_dolar_ccl = datos_imp[datos_imp.concepto ==
                                                "sueld_prom_ano_pasado_dolar_ccl"].importe.iloc[0]
    if sueld_prom_ano_actual_dolar_ccl >= sueld_prom_ano_pasado_dolar_ccl:
        promedio = round((sueld_prom_ano_actual_dolar_ccl /
                         sueld_prom_ano_pasado_dolar_ccl - 1) * 100, 2)

        return "fas fa-arrow-up", "green", sueld_prom_ano_actual_dolar_ccl, sueld_prom_ano_pasado_dolar_ccl, promedio, "fas fa-caret-up"
    else:

        promedio = round((sueld_prom_ano_actual_dolar_ccl /
                         sueld_prom_ano_pasado_dolar_ccl - 1) * 100, 2)
        return "fas fa-arrow-down", "red", sueld_prom_ano_actual_dolar_ccl, sueld_prom_ano_pasado_dolar_ccl, promedio, "fas fa-caret-down"


layout = html.Div([
    html.Link(rel="stylesheet", href='estilo.css'),
    html.Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css", rel="stylesheet",
              integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"),

    html.Div([dbc.Nav(
        [
            dbc.NavItem(
                html.A(["Volver"], href="/pagina_inicio"), className="navbar-brand"),

        ], className="navbar navbar-expand-lg navbar-dark bg-dark"
    ),

        html.Div([
            html.H2("Ingresos"),
            html.Link(
                href="https://fonts.googleapis.com/css2?family=Sen&display=swap", rel="stylesheet")
        ], className='titulo2'),

        html.Link(rel="stylesheet",

                  href="all.min.css"),

        html.Div([dbc.CardDeck([

            dbc.Card(
                dbc.CardBody(
                    [html.P("Sueldo promedio ultimos 12 meses pesos ", className="card-text"),
                     html.H2(sueldos_prom_ult_12_meses_peso()
                             [2], className="card-dato"),
                     html.Div([
                         html.I(className=sueldos_prom_ult_12_meses_peso()[0])],
                         className=sueldos_prom_ult_12_meses_peso()[1]),
                     html.P("Anteriores ", className="card-text"),
                     html.P(sueldos_prom_ult_12_meses_peso()[3]),
                     html.Div([
                         html.P(str(sueldos_prom_ult_12_meses_peso()[
                                4]) + "%", className="div_promedio"),
                         html.Div([
                             html.I(className=sueldos_prom_ult_12_meses_peso()[5])],
                             className=sueldos_prom_ult_12_meses_peso()[1]),

                     ], className="div_promedio")])),

            dbc.Card(
                dbc.CardBody(
                    [html.P("Sueldo promedio ultimos 12 meses USD ", className="card-text"),
                     html.H2(sueldos_prom_ult_12_meses_dolar()
                             [2], className="card-dato"),
                     html.Div([
                         html.I(className=sueldos_prom_ult_12_meses_dolar()[0])],
                         className=sueldos_prom_ult_12_meses_dolar()[1]),
                     html.P("Anteriores ", className="card-text"),
                     html.P(sueldos_prom_ult_12_meses_dolar()[3]),
                     html.Div([
                         html.P(str(sueldos_prom_ult_12_meses_dolar()
                                [4]) + "%", className="div_promedio"),
                         html.Div([
                             html.I(className=sueldos_prom_ult_12_meses_dolar()[5])],
                             className=sueldos_prom_ult_12_meses_dolar()[1]),

                     ], className="div_promedio")])),

            dbc.Card(
                dbc.CardBody(
                    [html.P("Sueldo promedio año actual pesos", className="card-text"),
                     html.H2(sueld_prom_ano_actual_peso()
                             [2], className="card-dato"),
                     html.Div([
                         html.I(className=sueld_prom_ano_actual_peso()[0])], className=sueld_prom_ano_actual_peso()[1]),
                     html.P("Anteriores ", className="card-text"),
                     html.P(sueld_prom_ano_actual_peso()[3]),
                     html.Div([
                         html.P(str(sueld_prom_ano_actual_peso()[
                                4]) + "%", className="div_promedio"),
                         html.Div([
                             html.I(className=sueld_prom_ano_actual_peso()[5])],
                             className=sueld_prom_ano_actual_peso()[1]),

                     ], className="div_promedio")])),

            dbc.Card(
                dbc.CardBody(
                    [html.P("Sueldo promedio año actual dolar", className="card-text"),
                     html.H2(sueld_prom_ano_actual_dolar_ccl()
                             [2], className="card-dato"),
                     html.Div([
                         html.I(className=sueld_prom_ano_actual_dolar_ccl()[0])],
                         className=sueld_prom_ano_actual_dolar_ccl()[1]),
                     html.P("Anteriores ", className="card-text"),
                     html.P(sueld_prom_ano_actual_dolar_ccl()[3]),
                     html.Div([
                         html.P(str(sueld_prom_ano_actual_dolar_ccl()
                                [4]) + "%", className="div_promedio"),
                         html.Div([
                             html.I(className=sueld_prom_ano_actual_dolar_ccl()[5])],
                             className=sueld_prom_ano_actual_dolar_ccl()[1]),

                     ], className="div_promedio")]
                ))], className="div_tarjetas_1"),

            html.Div([
                dcc.Dropdown(
                    id='ano-selector',
                    options=[{'label': c, 'value': c} for c in mov.anos],
                    value=mov.anos,
                    multi=True,

                    style=dict(
                        width='40%',
                        verticalAlign="middle",
                        display="inline"

                    )),

                dcc.Dropdown(id='mes-selector',
                             options=[{'label': c, 'value': c}
                                      for c in mov.meses],
                             value=mov.meses,
                             multi=True,
                             style=dict(
                                 width='40%',

                                 display="inline"
                             ))

            ]),



            html.Div([
                dcc.Graph(
                    id='ingresos_media',
                    animate=True)
            ], className='grafico_con_info'),

            html.Div([dcc.Graph(
                id='sueldos',
                animate=True)

            ], className='info_grafico'),

            html.H4("Grafico de sueldos mensuales en dolar CCL",
                    className='leyenda_graficos_70')
        ], className='div_sueldos'),

        html.Div([
            dcc.Graph(
                id='grafico_peso_dolar',
                animate=True)
        ]), html.H4("Grafico de sueldos mensuales en pesos y dolar CCL ",
                    className='leyenda_graficos_100'),

        html.Div([

            html.Div([
                dcc.Graph(
                    id='grafico_sueldo_heat',
                    animate=True)
            ]), html.H4(
                "Mapa de calor de los ingresos mensuales en dolar CCL. A mayor ingresos corresponde color mas claro ",
                className='leyenda_graficos_33'),

            html.Div([
                dcc.Graph(
                    id='grafico_mejor_ano',
                    animate=True)
            ]),
            html.H4("Mapa de calor del mejor año medido en  dolar CCL. A mayor ingresos corresponde color mas claro ",
                    className='leyenda_graficos_33'),
            html.Div([
                dcc.Graph(
                    id='grafico_mejor_mes',
                    animate=True)
            ]),
            html.H4("Mapa de calor del mejor mes medido en  dolar CCL. A mayor ingresos corresponde color mas claro ",
                    className='leyenda_graficos_33'), ], className="columnas_sueldos_heat"),

        html.Div([
            dcc.Graph(
                id='ingresos_cuadro',
                animate=True)
        ]), html.H4(
            "Mapa de calor de los ingresos en dolar CCL y su distribucion segun el valor de cada mes. A mayor ingresos corresponde color mas claro ",
            className='leyenda_graficos_100'),

        html.Div([
            dcc.Graph(
                id='grafico_sueldo_comparativo',
                animate=True)
        ]), html.H4(
            "Ingresos proporcionales por año. Permite divisar cual fue el mejor mes de cada año en particular, medido en dolar CCL ",
            className='leyenda_graficos_100'),

        html.Div([

            html.Div([
                dcc.Graph(
                    id='ingresos_repe_ccl',
                    animate=True)
            ]),
            html.H4(
                "Histograma para saber que rango de sueldos son los mas comunes, medido en dolar CCL "
            ),

            html.Div([
                dcc.Graph(
                    id='ingresos_repe_pesos',
                    animate=True)
            ]),
            html.H4(
                "Histograma para saber que rango de sueldos son los mas comunes, medido en pesos ")

        ], className="graficos_repetidos"),

        html.Div([
            dcc.Graph(
                id='sueldos_color',
                animate=True)
        ]),
        html.H4(
            "Me permite saber como esta posicionado mi ultimo sueldo respecto de los ingresos historicos "),


    ], className='body_graficos'),

])


@apli.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value'))
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


@apli.callback(Output(component_id='grafico_peso_dolar', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def graf_peso_dolar(ano_elegido, mes_elegido):
    filtro_sueldo = mov.prepara_ingresos()
    filtro_sueldo.reset_index(inplace=True)
    filtro_sueldo = filtro_sueldo[filtro_sueldo.ano.isin(ano_elegido)]
    filtro_sueldo = filtro_sueldo[filtro_sueldo.mes.isin(mes_elegido)]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    nombres = ['Peso', 'Dolar CCL']
    columnas = ['val_abs',  'val_abs_usd_ccl']
    secundario = [False, True, True]
    fff = []
    for x in range(len(filtro_sueldo)):
        fff.append(filtro_sueldo.fecha.iloc[x])

    for nom, secu, col in zip(nombres, secundario, columnas):
        dato = filtro_sueldo[col].to_numpy()
        fig.add_trace(
            go.Scatter(x=fff, y=dato, name=nom), secondary_y=secu)

    fig.update_xaxes(title_text="fechas", tickangle=-90, automargin=True, showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Ingresos en Pesos vs  Dolar CCL',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='grafico_sueldo_comparativo', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def graf_sueldos_comparativo_anos(ano_elegido, mes_elegido):
    filtro_sueldo = mov.prepara_ingresos()
    filtro_sueldo.reset_index(inplace=True)
    rows = []
    cols = []

    for i in range(1, 5 + 1):
        x = 1
        y = 2
        cols.append(x)
        cols.append(y)
        rows.append(i)
        rows.append(i)

    rows = rows[:len(mov.anos)]
    cols = cols[:len(mov.anos)]

    # rows=[1,1,2,2]
    # cols=[1,2,1,2]
    filas_grafico = math.ceil(len(cols) / 2)
    fig = make_subplots(rows=filas_grafico, cols=2,
                        start_cell="top-left", subplot_titles=mov.anos)

    for ano, ro, co in zip(mov.anos, rows, cols):
        filtro_sueldo_ano = filtro_sueldo[filtro_sueldo.ano == ano]
        filtro_sueldo_mes = round(filtro_sueldo_ano.groupby(
            ['mes'], as_index=False)['val_abs_usd_ccl'].sum())
        val_abs_usd_ccl = filtro_sueldo_mes.val_abs_usd_ccl.to_numpy()

        fig.add_trace(go.Bar(x=mov.meses, y=val_abs_usd_ccl, name=ano),
                      row=ro, col=co)
    fig.update_xaxes(showgrid=False, showdividers=False, showline=False, tickfont_color='white', zeroline=False,
                     tickvals=mov.meses_nombres)
    fig.update_yaxes(title_text="Meses", showgrid=False, showdividers=False, showline=False, tickfont_color='white',
                     zeroline=False)
    fig.update_layout(title_text='Ingresos proporcionales segun mes (año por año)',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='grafico_sueldo_heat', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def graf_mapacalor(ano_elegido, mes_elegido):
    filtro = mov.pivot("ano", "mes", mov.prepara_ingresos(), "dolar")
    datos = filtro.to_numpy()
    trace = go.Heatmap(
        x=mov.anos,
        y=mov.meses,
        z=datos,
        type='heatmap',
        colorscale='Viridis'
    )

    data = [trace]
    fig = go.Figure(data=data)
    fig.update_xaxes(title_text="Años", showgrid=False, showdividers=False, showline=False, tickfont_color='white',
                     zeroline=False)
    fig.update_yaxes(title_text="Meses", showgrid=False, showdividers=False, showline=False, tickfont_color='white',
                     zeroline=False)
    fig.update_layout(title_text='Mapa de calor : INGRESOS',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='grafico_mejor_ano', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def graf_mejor_ano(ano_elegido, mes_elegido):
    filtro = mov.agrupado_ano_mes("ano", mov.prepara_ingresos(), "dolar")
    fig = px.bar(filtro, x='ano', y='val_abs_usd_ccl', color='val_abs_usd_ccl',

                 labels={'val_abs_usd_ccl': 'Ingresos anuales', 'ano': 'Año'})

    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_traces(textposition='outside')
    fig.update_layout(title_text='Mapa de calor : mejor año',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='grafico_mejor_mes', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def graf_mejor_mes(ano_elegido, mes_elegido):
    filtro = mov.agrupado_ano_mes("mes", mov.prepara_ingresos(), "dolar")
    fig = px.bar(filtro, x='mes', y='val_abs_usd_ccl', color='val_abs_usd_ccl',

                 labels={'val_abs_usd_ccl': 'Ingresos mensuales', 'mes': 'Mes'})
    fig.update_xaxes(showgrid=False, showdividers=False, showline=False, tickfont_color='white', tickvals=mov.meses,
                     zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Mapa de calor : Mejor mes',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='ingresos_cuadro', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def graf_cuadro_ingreso(ano_elegido):
    filtro = mov.agrupado("mes", "ano", mov.prepara_ingresos(), "dolar")
    fig = px.treemap(filtro, path=[px.Constant('Ingresos'), 'ano', 'mes'], values='val_abs_usd_ccl',
                     color='val_abs_usd_ccl', labels={'val_abs_usd_ccl': 'Ingresos'})
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Mapa de calor : Ingresos',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='sueldos', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def muestra_sueldos(ano_elegido, mes_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_ingresos(), "dolar")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-3],
        title={
            "text": f'sueldo de {filtro.mes.iloc[-3]} / {filtro.ano.iloc[-3]}'},
        domain={'x': [0, 0.5], 'y': [0, 0.3]},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-4], 'relative': True, 'position': "top"}))

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-2],
        title={
            "text": f'sueldo de {filtro.mes.iloc[-2]} / {filtro.ano.iloc[-2]}'},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-3], 'relative': True},
        domain={'x': [0, 0.5], 'y': [0.5, 0.9]}))

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-1],
        title={
            "text": f'Ultimo sueldo  {filtro.mes.iloc[-1]} / {filtro.ano.iloc[-1]}'},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-2], 'relative': True},
        domain={'x': [0.6, 1], 'y': [0, 1]}))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')

    return fig


@apli.callback(Output(component_id='ingresos_media', component_property='figure'),
               Input(component_id='ano-selector', component_property='value'))
def ing_media(ano_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_ingresos(), "dolar")
    filtro = filtro[filtro.ano.isin(ano_elegido)]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=[filtro.ano, filtro.mes],
                  y=filtro.val_abs_usd_ccl, name="Sueldos en Dolares"))

    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_layout(hovermode="x")
    return fig


@apli.callback(Output(component_id='ingresos_repe_ccl', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def ing_repetidos_ccl(ano_elegido, mes_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_ingresos(), "dolar")
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    fig = px.histogram(filtro, x="val_abs_usd_ccl", labels={
                       'val_abs_usd_ccl': 'Ingresos'})
    fig.update_layout(title_text='Histograma de sueldos en dolar ccl', paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')

    return fig


@apli.callback(Output(component_id='ingresos_repe_pesos', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def ing_repetidos_pesos(ano_elegido, mes_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_ingresos(), "pesos")
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    fig = px.histogram(filtro, x="val_abs", labels={'val_abs': 'Ingresos'})
    fig.update_layout(title_text='Histograma de sueldos en pesos', paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')

    return fig


@apli.callback(Output(component_id='sueldos_color', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                Input(component_id='mes-selector', component_property='value')])
def sueldos_color(ano_elegido, mes_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_ingresos(), "dolar")

    filtro['val_abs_usd_ccl'] = filtro['val_abs_usd_ccl'].round()

    orden_tiempo = filtro.sort_values(
        ['ano', 'mes'], ascending=False).reset_index(drop=True)
    orden_valor = filtro.sort_values(
        ['val_abs_usd_ccl'], ascending=False).reset_index(drop=True)

    orden_tiempo = orden_tiempo.reset_index()
    orden_tiempo.columns = ['indice_tiempo', 'ano', 'mes', 'val_abs_usd_ccl']
    orden_valor = orden_valor.reset_index()
    orden_valor.columns = ['indice_valor', 'ano', 'mes', 'val_abs_usd_ccl']

    datos_final = pd.merge(orden_valor, orden_tiempo, how='inner')
    dat = datos_final[datos_final.indice_tiempo == 0]
    indice_ultimo_sueldos = dat.index.to_list()
    ultimo_sueldo_ind = indice_ultimo_sueldos[0]

    colores = ['lightslategray', ] * len(filtro)

    colores[ultimo_sueldo_ind] = 'crimson'

    texto = []
    for x in range(len(orden_valor)):
        ano = str(orden_valor.ano.iloc[x])
        mes = str(orden_valor.mes.iloc[x])
        unidos = ano + "-" + mes
        texto.append(unidos)

    fig = px.bar(orden_valor, y='val_abs_usd_ccl', color=colores,
                 text=texto, labels={'val_abs_usd_ccl': 'Ingresos', 'index': 'Sueldos ordenados por importacia'})
    fig.update_layout(title_text='Posicionamiento historico del ultimo sueldo', paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_layout(hovermode=False)
    return fig
