from funciones_para_dashboard.clases import Movimientos
from .app import apli
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

mov = Movimientos()

layout = html.Div([
    html.Div([dbc.Nav(
        [
            dbc.NavItem(
                html.A(["Volver"], href="/pagina_inicio"), className="navbar-brand"),


        ], className="navbar navbar-expand-lg navbar-dark bg-dark"
    )]),



    html.Div([
        html.H2("Egresos"),
    ], className='titulo2'),

    html.Div([
        dcc.Dropdown(
            id='ano-selector',
            options=[{'label': c, 'value': c} for c in mov.anos],
            value=mov.anos,
            multi=True),

        dcc.Dropdown(id='mes-selector',
                     options=[{'label': c, 'value': c} for c in mov.meses],
                     value=mov.meses,
                     multi=True)

    ]),

    html.Div([dcc.Dropdown(id='concepto-selector',

                           options=[{'label': c, 'value': c}
                                    for c in mov.conceptos_gastos],

                           value="cabal")], className='selector_concepto'),

    html.Div([
        dcc.Graph(
            id='gastos',
            animate=True)
    ]), html.H4("Grafico de burbujas para saber cuando y cuanto se gasto ( burbuja mas grande significa mayor gasto) ", className='leyenda_graficos_100'),

    html.Div([
        html.Div([
        html.Div([
            dcc.Graph(
                id='gastos_torta_ind',
                animate=True)
        ]), html.H4("Grafico de torta sobre los gastos anuales ", className='leyenda_graficos_50')]),
        html.Div([
        html.Div([
            dcc.Graph(
                id='gastos_torta',
                animate=True)
        ]), html.H4("Grafico de torta sobre los gastos segun concepto ", className='leyenda_graficos_50'), ], className="gastos_torta_columnas")]),

    html.Div([
        dcc.Graph(
            id='gastos_cuadro',
            animate=True)
    ]), html.H4("Mapa de calor de los gastos mensuales en dolar CCL. A mayor gasto corresponde color mas claro ", className='leyenda_graficos_100'),

    html.Div([
        dcc.Graph(
            id='cuadro_relacion',
            animate=True)
    ]), html.H4("Grafico de la relacion entre los ingresos y los gastos ", className='leyenda_graficos_100'),
    html.Div([

        html.Div([
            dcc.Graph(
                id='gastos_tarjetas',
                animate=True)
        ], className='grafico_con_info'),


        html.Div([
            dcc.Graph(
                id='muestra_tarjetas',
                animate=True)
        ], className='info_grafico'),

    ], className='tarjetas'), html.H4("Grafico de la evolucion de gastos en tarjetas VISA y CABAL ", className='leyenda_graficos_70'),



])


@apli.callback(Output(component_id='gastos', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def graf_scatter_gastos(ano_elegido):

    filtro = mov.prepara_gastos()
    filtro.reset_index(inplace=True)
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    fig = px.scatter(filtro, x="fecha", y="val_abs",
                     size="val_abs", color="concepto",
                     size_max=55, hover_name="concepto", log_y=True,
                     title="Distribucion gastos"
                     )

    fig.update_xaxes(title_text="Fecha", tickangle=-90)
    fig.update_yaxes(title_text="Total")
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Distribucion de gastos',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='gastos_torta_ind', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
               Input(component_id='concepto-selector',
                     component_property='value')
                ])
def graf_torta_gasto_individual(ano_elegido, concepto_elegido):
    filtro = mov.agrupado("concepto", "ano", mov.prepara_gastos(), "dolar")
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    filtro = filtro[filtro.concepto == concepto_elegido]
    fig = px.pie(filtro, values='val_abs_usd_ccl',
                 names='ano', title=concepto_elegido, hole=.5, labels={'val_abs_usd_ccl': 'Gastos anuales'})
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_layout(title_text='Gastos por año',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='gastos_torta', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def graf_torta_gasto(ano_elegido):
    filtro = mov.agrupado("concepto", "ano", mov.prepara_gastos(), "dolar")
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    filtro = filtro.sort_values(by='val_abs_usd_ccl', ascending=False)
    filtro = filtro.head(15)

    fig = px.pie(filtro, values='val_abs_usd_ccl', names='concepto',
                 title="Gastos totales por año", hole=.5, labels={'val_abs_usd_ccl': 'Importe'})    
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_layout(title_text='Gastos por concepto',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='gastos_cuadro', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def graf_cuadro_gasto(ano_elegido):

    filtro = mov.agrupado("ano", "mes", mov.prepara_gastos(), "dolar")
    filtro = filtro[filtro.ano.isin(ano_elegido)]
    fig = px.treemap(filtro, path=[px.Constant('gastos'), 'ano', 'mes'], values='val_abs_usd_ccl',
                     color='val_abs_usd_ccl')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Mapa de calor: Gastos',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )
    return fig


@apli.callback(Output(component_id='cuadro_relacion', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def graf_cuadro_relacion(ano_elegido):
    gastos_filtro = mov.agrupado_ano_mes("ano", mov.prepara_gastos(), "dolar")
    gastos_filtro = gastos_filtro.val_abs_usd_ccl.to_numpy()
    ingresos_filtro = mov.agrupado_ano_mes(
        "ano", mov.prepara_ingresos(), "dolar")
    ingresos_filtro = ingresos_filtro.val_abs_usd_ccl.to_numpy()
    x = mov.anos
    fig = go.Figure(go.Bar(x=x, y=ingresos_filtro, name='Ingresos'))
    fig.add_trace(go.Bar(x=x, y=gastos_filtro, name='Gastos'))
    fig.update_layout(barmode='stack', xaxis={
                      'categoryorder': 'category ascending'})
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white', zeroline=False)
    fig.update_layout(title_text='Relacion ingresos-gastos',
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      title_font_color='white', title_yanchor='top', font_color='white'
                      )

    return fig


@apli.callback(Output(component_id='gastos_tarjetas', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
                ])
def gast_tarjetas(ano_elegido):
    filtro = mov.prepara_gastos_tarjetas()
    filtro = filtro.sort_values(by='ano', ascending=True)
    filtro_cabal = filtro[filtro.concepto == 'cabal']
    filtro_visa = filtro[filtro.concepto == 'visa']

    fig = go.Figure(data=[
        go.Bar(name='cabal', x=[
               filtro_cabal.ano, filtro_cabal.mes], y=filtro_cabal.val_abs_usd_ccl),
        go.Bar(name='visa', x=[filtro_visa.ano,
               filtro_visa.mes], y=filtro_visa.val_abs_usd_ccl)
    ])    
    fig.update_layout(barmode='group')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')

    return fig


@apli.callback(Output(component_id='muestra_tarjetas', component_property='figure'),
               [Input(component_id='ano-selector', component_property='value'),
               Input(component_id='mes-selector', component_property='value')])
def muestra_tarjetas(ano_elegido, mes_elegido):
    filtro = mov.agrupado("ano", "mes", mov.prepara_gastos_tarjetas(), "dolar")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-3],
        title={
            "text": f'Gastos tarjetas al {filtro.mes.iloc[-3]}/ {filtro.ano.iloc[-3]}'},
        domain={'x': [0, 0.5], 'y': [0, 0.3]},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-4], 'relative': True, 'position': "top"}))

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-2],
        title={
            "text": f'Gastos tarjetas al {filtro.mes.iloc[-2]} /{filtro.ano.iloc[-2]}'},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-3], 'relative': True},
        domain={'x': [0, 0.5], 'y': [0.5, 0.9]}))

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=filtro.val_abs_usd_ccl.iloc[-1],
        title={
            "text": f'Gastos tarjetas  al {filtro.mes.iloc[-1]}/ {filtro.ano.iloc[-1]}'},
        delta={'reference': filtro.val_abs_usd_ccl.iloc[-2], 'relative': True},
        domain={'x': [0.6, 1], 'y': [0, 1]}))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    fig.update_xaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')
    fig.update_yaxes(showgrid=False, showdividers=False,
                     showline=False, tickfont_color='white')

    return fig
