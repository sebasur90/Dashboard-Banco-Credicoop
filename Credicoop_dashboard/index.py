


from funciones_para_datasets import procesar_datos
procesar_datos.proceso_completo()
from funciones_para_dashboard import app, pagina_inicio, pagina_ingresos, pagina_egresos, pagina_movimientos
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc




app.apli.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.apli.callback(Output('page-content', 'children'),
                   Input('url', 'pathname'))
def display_page(pathname):

    if pathname == '/pagina_inicio':
        return pagina_inicio.layout
    elif pathname == '/pagina_ingresos':
        return pagina_ingresos.layout
    elif pathname == '/pagina_egresos':
        return pagina_egresos.layout    
    elif pathname == '/movimientos':
        return pagina_movimientos.layout

    else:
        return pagina_inicio.layout


if __name__ == '__main__':
    app.apli.run_server(debug=False)
