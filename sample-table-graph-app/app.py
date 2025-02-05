# Import packages
from dash import Dash, dcc, html, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# Set app layout
app.layout = [
    html.H1(children='My Table Dash App', style={'textAlign':'left'}),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        page_size=5
    ),
    dcc.Graph(
        figure={},
        id='controls-and-graph'
    )
]

# Add controls and build interactions
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input('controls-and-radio-item', 'value')
)
def update_graph(value_chosen):
    fig = px.histogram(df, x='continent', y=value_chosen, histfunc='avg')
    return fig

# Run app
if __name__ == '__main__':
    app.run(debug = True)