from funciones_para_dashboard import clases
import dash_html_components as html
import pathlib
import dash_bootstrap_components as dbc
from datetime import datetime

mov = clases.Movimientos()
mov = mov.datos


def total_dias():

    fecha_inicio = mov.sort_values(
        by=['fecha']).reset_index(drop=True).fecha.iloc[0]
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_actual = datetime.now()
    fecha_total_dias = (fecha_actual-fecha_inicio).days
    fecha_total_anos = round((fecha_actual-fecha_inicio).days/365)
    fecha_total_meses = round((fecha_actual-fecha_inicio).days/30)
    return fecha_total_dias, fecha_total_anos, fecha_total_meses


def total_datos():
    return len(mov)


def sumas():
    cred_usd = round(mov.credito_usd_ccl.sum())
    cred_p = round(mov.credito.sum())
    deb_usd = round(mov.debito_usd_ccl.sum())
    deb_p = round(mov.debito.sum())

    return cred_usd, cred_p, deb_usd, deb_p


def ultima_fecha_informada():
    fecha = mov.sort_values(by=['fecha']).reset_index(drop=True).fecha.iloc[-1]
    return fecha


def ultimo_valor_dolar():
    dolar = round(mov.sort_values(by=['fecha']).reset_index(
        drop=True).ccl.iloc[-1], 2)
    return dolar


layout = html.Div([
    
    html.H1("Dashboard Credicoop", className='titulo'),
    html.Div([dbc.CardDeck([
        dbc.Card(
            dbc.CardBody(
                [html.P("Total datos",
                        className="card-text"),
                 html.H2(total_datos(), className="card-dato"),
                 ])),
        dbc.Card(
            dbc.CardBody(
                [html.P("Total dias transcurridos",
                        className="card-text", ),
                 html.H2(total_dias()[0], className="card-dato"),
                 ])),
        dbc.Card(
            dbc.CardBody(
                [html.P("Total ingresos en USD",
                        className="card-text", ),
                 html.H2(sumas()[0], className="card-dato"),
                 html.P("en pesos \n" + str(sumas()[1]),
                        className="card-text", ), ])),

        dbc.Card(
            dbc.CardBody(
                [html.P("Cotizacion dolar CCL",
                        className="card-text",
                        ),
                 html.H2(ultimo_valor_dolar(), className="card-dato"),

                 ]
            )
        ),

    ], className="div_tarjetas_deck"
    )], className="div_tarjetas_1"),



    html.Div([
        dbc.CardDeck(
            [
               
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Ingresos", className="card-title"),
                                    html.P(
                                        "Sueldos historicos y graficos comparativos en pesos y en dolar contado"
                                        "con liquidacion. "
                                        "Mapas de calor y mas...",
                                        className="card-text",
                                    ),
                                    dbc.Button("Ingresar", color="primary",
                                               href="/pagina_ingresos", className="boton_ir_pagina"),
                                ]
                            ),
                        ],
                        style={"width": "30rem"}
                    ),
                

               
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Egresos", className="card-title"),
                                    html.P(
                                        "Gastos historicos y graficos comparativos de su evolucion en el tiempo ",
                                        className="card-text",
                                    ),
                                    dbc.Button("Ingresar", color="primary",
                                               href="/pagina_egresos", className="boton_ir_pagina"),
                                ]
                            ),
                        ],
                        style={"width": "30rem"}
                    ),


                
                
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Movimientos",
                                            className="card-title"),
                                    html.P(
                                        "Detalle de movimientos de cuenta historicos. ",
                                        className="card-text",
                                    ),
                                    dbc.Button("Ingresar", color="primary",
                                               href="/movimientos", id="boton_ir_pagina"),
                                ]
                            ),
                        ],
                        style={"width": "30rem"}
                    )
                
            ])], className="div_tarjetas_2")
], className="fondo_inicio")
