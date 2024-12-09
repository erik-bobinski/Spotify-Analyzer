from dash import Dash, html, dcc

# initialize the app
app = Dash(__name__)

# parent div
app.layout = html.Div([
    # title text
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
            'border': '1px solid #1DB954',  # spotify green
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
    # submit Button
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
        },
    )
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
    })
], style={ # parent div styling
    'backgroundColor': '#1e1e1e',
    'height': '100vh',
    'padding': '20px',
})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)