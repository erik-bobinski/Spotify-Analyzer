from dash import Dash, html, dcc, callback, Input, Output, State
import pandas as pd
from Recommender import Recommender
from DataProcessor import DataProcessor

def uiLogin(reccomender):

    # Initialize the app
    app = Dash(__name__, suppress_callback_exceptions=True)

    # Login page layout
    login_layout = html.Div([
        html.H1("Spotify Analyzer",
                style={
                    'textAlign': 'center',
                    'color': 'white',
                    'marginTop': '20px',
                    'marginBottom': '30px',
                    'padding': '20px'
                }),
        # Email and Password Inputs
        html.Div([
            html.Label("Email:", style={'color': 'white'}),
            dcc.Input(
                id='email-div',
                type='text',
                placeholder='Enter your email',
                style={'width': '300px', 'padding': '10px', 'borderRadius': '5px', 'backgroundColor': '#282828', 'color': 'white'}
            )
        ], style={'textAlign': 'center', 'padding': '10px'}),
        html.Div([
            html.Label("Password:", style={'color': 'white'}),
            dcc.Input(
                id='password-div',
                type='password',
                placeholder='Enter your password',
                style={'width': '300px', 'padding': '10px', 'borderRadius': '5px', 'backgroundColor': '#282828', 'color': 'white'}
            )
        ], style={'textAlign': 'center', 'padding': '10px'}),
        # Submit Button
        html.Div([
            html.Button('Submit', id='submit-val', n_clicks=0,
                        style={'backgroundColor': '#1DB954', 'color': 'white', 'border': 'none', 'padding': '10px 20px', 'borderRadius': '5px'})
        ], style={'textAlign': 'center', 'padding': '10px'})
    ], style={'backgroundColor': '#1e1e1e', 'height': '100vh', 'padding': '20px'})

    # Dashboard layout
    dashboard_layout = html.Div([
        html.H1("Spotify Analyzer Dashboard",
                style={'textAlign': 'center', 'color': 'white', 'backgroundColor': '#1e1e1e', 'padding': '20px'}),
        html.Div([
            html.Label("Search for a Song:", style={'color': 'white'}),
            dcc.Input(
                id='song-search-input',
                type='text',
                placeholder='Type to search for a song...',
                debounce=True,
                style={'width': '50%', 'padding': '10px', 'borderRadius': '5px', 'backgroundColor': '#282828', 'color': 'white'}
            ),
            html.Div(id='song-search-output', style={'color': 'white', 'paddingTop': '10px'})
        ], style={'padding': '20px'}),
        html.Div([
            html.Label("Recommendation Parameters:", style={'color': 'white'}),
            dcc.Checklist(
                id='recommendation-parameters',
                options=[
                    {'label': 'Valence', 'value': 'valence'},
                    {'label': 'Danceability', 'value': 'danceability'},
                    {'label': 'Energy', 'value': 'energy'},
                    {'label': 'Tempo', 'value': 'tempo'},
                    {'label': 'Acousticness', 'value': 'acousticness'}
                ],
                value=['valence', 'danceability', 'energy'],
                inline=True,
                style={'color': 'white'}
            )
        ], style={'padding': '20px'}),
        html.Div([
            html.Button("Get Recommendations",
                        id='recommend-button',
                        n_clicks=0,
                        style={'backgroundColor': '#1DB954', 'color': 'white', 'padding': '10px 20px', 'borderRadius': '5px'})
        ], style={'padding': '20px'}),
        html.Div(id='recommendations-output', style={'color': 'white', 'paddingTop': '20px'})
    ], style={'backgroundColor': '#1e1e1e', 'height': '100vh'})

    # Callbacks for Navigation
    @callback(
        Output('url', 'pathname'),
        Input('submit-val', 'n_clicks'),
        prevent_initial_call=True
    )
    def navigate_to_dashboard(n_clicks):
        return '/dashboard' if n_clicks > 0 else '/'

    @callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/':
            return login_layout
        elif pathname == '/dashboard':
            return dashboard_layout
        return '404 Page Not Found'

    # Dynamic Dropdown Search for Songs
    @callback(
        Output('song-search-output', 'children'),
        Input('song-search-input', 'value')
    )
    def update_song_options(search_value):
        if not search_value:
            return "Start typing to search for a song..."
        filtered_df = df[df['name'].str.contains(search_value, case=False, na=False)]
        if filtered_df.empty:
            return "No matching songs found."
        return html.Div([
            dcc.Dropdown(
                id='song-dropdown',
                options=[
                    {'label': name, 'value': song_id} for name, song_id in zip(filtered_df['name'], filtered_df['id'])
                ],
                placeholder='Select a song...',
                style={'width': '100%', 'color': 'black'}
            )
        ])

    @callback(
        Output('recommendations-output', 'children'),
        Input('recommend-button', 'n_clicks'),
        State('song-dropdown', 'value'),
        State('recommendation-parameters', 'value'),
        prevent_initial_call=True
    )
    def get_recommendations(n_clicks, song_id, parameters):
        if not song_id or not parameters:
            return "Please select a song and parameters for recommendations."
        
        # Ensure the parameters exist in the data
        available_columns = df.columns.tolist()
        missing_columns = [param for param in parameters if param not in available_columns]
        
        if missing_columns:
            return f"The following parameters are missing from the data: {', '.join(missing_columns)}"
        
        recommender.data = df[parameters + ['id', 'name', 'artists']]  # Pass the selected parameters
        recommendations = recommender.recommend(song_id)
        return html.Ul([html.Li(f"{rec['name']} by {rec['artists']}") for rec in recommendations.to_dict('records')])


    # App Layout
    app.layout = html.Div([
        dcc.Location(id='url', refresh=True),
        html.Div(id='page-content')
    ])

    return app