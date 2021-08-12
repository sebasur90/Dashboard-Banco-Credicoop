from funciones_para_dashboard.clases import Movimientos
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table


mov = Movimientos()
df = mov.datos
df['id'] = df.fecha

layout = html.Div([
    html.Div([dbc.Nav(
        [
            dbc.NavItem(
                html.A(["Volver"], href="/pagina_inicio"), className="navbar-brand"),
        ])]),


    dash_table.DataTable(
        data=df.to_dict('records'),
        sort_action='native',
        columns=[
            {'name': 'fecha', 'id': 'fecha', 'type': 'datetime', 'editable': False},
            {'name': 'ano', 'id': 'ano', 'type': 'datetime', 'editable': False},
            {'name': 'mes', 'id': 'mes', 'type': 'datetime', 'editable': False},
            {'name': 'debito', 'id': 'debito', 'type': 'numeric'},
            {'name': 'credito', 'id': 'credito', 'type': 'numeric'},
            {'name': 'saldo', 'id': 'saldo', 'type': 'numeric'},
            {'name': 'debito_usd_ccl', 'id': 'debito_usd_ccl', 'type': 'numeric'},
            {'name': 'credito_usd_ccl', 'id': 'credito_usd_ccl', 'type': 'numeric'},
            {'name': 'concepto', 'id': 'concepto',
                'type': 'text', 'editable': True},
        ],
        editable=True,
        style_as_list_view=True,
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },


        style_data_conditional=[


            # SUELDOS
            {'if': {
                'filter_query': '{concepto} = "acreditacion de sueldos "'

            },
                'backgroundColor': '#3D9970',
                'color': 'white'
            },

            # TARJETAS
            {'if': {'filter_query': '{concepto} = "cabal"'},
             'backgroundColor': '#daa520', 'color': 'white'},
            {'if': {'filter_query': '{concepto} = "visa"'},
             'backgroundColor': '#daa520', 'color': 'white'},



        ])])
