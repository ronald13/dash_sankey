import os
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from charts import create_sankey
import dash_trich_components as dtc
from prep import prepare_sahkey_data

all_numerics, names, count_dict, source_list, target_list = prepare_sahkey_data('data/Simulated_Customer_Data_Sankey.csv')

app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

theme_toggle = dtc.ThemeToggle(
        bg_color_dark='#232323',
        # icon_color_dark='#EDC575',
        # bg_color_light='#07484E',
        icon_color_light='#C8DBDC',
        tooltip_text='Toggle light/dark theme'
    )
theme_switch = html.Div(theme_toggle, className='theme__switcher')
header = html.Div([
        html.H1('Sankey Diagram'),
        html.P('How to make Sankey diagrams in Plotly'),
], className='dash__header')

footer = html.Div([
    html.P('Source:', style={}),

], className='dash__footer')



app.layout = html.Div([
                    header,
                    theme_switch,
                    html.Div([
                          html.P('Customer Segmentation', style={'font-size':'16px', 'font-weight':'600'}),
                          html.P('Month on Month'),
                          dcc.Graph(figure=create_sankey(all_numerics, names, count_dict, source_list, target_list ), style={'width':'100%'})
                    ], className='dash__graph_block'),
                    footer

                ], className='dash__wrapper', style={})


# don't run when imported, only when standalone
if __name__ == '__main__':
    port = os.getenv("DASH_PORT", 8053)
    app.run_server(debug=True,  port=port)


