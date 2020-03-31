import dash
import dash_html_components as html
import dash_core_components as dcc
##

tabtitle = 'COVID-19 Income tax calculator'
###Configure app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
#app inputs
app.layout = html.Div(children=[
        html.H1(children='Shipping Estimates',
        style = {'color': colors['text']}),
        html.Div(children='''Created by: Patrick Robinson'''),
    
    ## enterbox one one 1
    html.Label('Enter your income')
    dcc.Input(id='my-id', value='initial value', type='number'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()
