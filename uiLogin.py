from dash import Dash, html, dcc, callback, Input, Output
import dash

# initialize the app
app = Dash(__name__, suppress_callback_exceptions=True)

# layout for the login page
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),  # This enables page navigation
    html.Div(id='page-content')
])

# login page layout
login_layout = html.Div([
    html.H1("Spotify Analyzer",
    style={
        'textAlign': 'center',
        'color': 'white',
        'marginTop': '20px',
        'marginBottom': '30px',
        'padding': '20px'
    }
    ),
    # email textbox
    html.Div([
    html.Label("Email:", style={'color': 'white'}),
    dcc.Input(
        id='email-div',
        type='text',
        placeholder='Enter your email',
        style={
            'width': '300px',
            'padding': '10px',
            'borderRadius': '5px',
            'border': '1px solid #1DB954',
            'backgroundColor': '#282828',
            'color': 'white'
        }
    )
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'padding': '40px'
    }),
    # password textbox
    html.Div([
    html.Label("Password:", style={'color': 'white'}),
    dcc.Input(
        id='password-div',
        type='password',
        placeholder='Enter your password',
        style={
            'width': '300px',
            'padding': '10px',
            'borderRadius': '5px',
            'border': '1px solid #1DB954',
            'backgroundColor': '#282828',
            'color': 'white'
        }
    )
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'padding': '40px'
    }),
    # submit btn with Navigation
    html.Div([
    html.Button('Submit', 
        id='submit-val', 
        n_clicks=0,
        style={
            'backgroundColor': '#1DB954',
            'color': 'white',
            'border': 'none',
            'padding': '12px 24px',
            'borderRadius': '25px',
            'fontSize': '16px',
            'fontWeight': 'bold',
            'cursor': 'pointer',
            'transition': 'background-color 0.3s ease',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
        }
    )
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
    })
], style={
    'backgroundColor': '#1e1e1e',
    'height': '100vh',
    'padding': '20px'
})

# dashboard page layout
dashboard_layout = html.Div([
    html.H1("Spotify Analyzer Dashboard", 
        style={
            'textAlign': 'center',
            'color': 'white',
            'backgroundColor': '#1e1e1e',
            'padding': '20px'
        }
    )
], style={
    'backgroundColor': '#1e1e1e',
    'height': '100vh',
    'color': 'white'
})

# callback to handle page navigation
@callback(
    Output('url', 'pathname'),
    Input('submit-val', 'n_clicks'),
    prevent_initial_call=True
)
def navigate_to_dashboard(n_clicks):
    if n_clicks > 0:
        return '/dashboard'  # URL path for db page

# update page content based on URL
@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return login_layout
    elif pathname == '/dashboard':
        return dashboard_layout
    else:
        return '404 Page Not Found'

# set the initial layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)