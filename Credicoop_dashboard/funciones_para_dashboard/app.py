
import dash
import dash_bootstrap_components as dbc



iconos="https://use.fontawesome.com/releases/v5.15.1/css/all.css"

apli = dash.Dash('SimpleDashboard', suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.SUPERHERO,iconos] )
server = apli.server