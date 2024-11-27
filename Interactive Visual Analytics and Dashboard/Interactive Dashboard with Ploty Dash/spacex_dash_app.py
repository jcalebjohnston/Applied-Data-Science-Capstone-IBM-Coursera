# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
        ],
        value='ALL',  # Default value
        placeholder="Select a Launch Site here",  # Placeholder text
        searchable=True  # Enable searching
    ),
    html.Br(),

    # TASK 2: Pie chart to show total successful launches for all sites or specific site
    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),
    html.P("Payload range (Kg):"),

    # TASK 3: Slider for Payload Range
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        marks={i: str(i) for i in range(int(min_payload), int(max_payload)+1, 1000)},
        value=[min_payload, max_payload]
    ),

    # TASK 4: Scatter chart for success vs payload
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2: Callback for Pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df  # Original dataframe
    if entered_site == 'ALL':
        # Generate pie chart for all sites
        fig = px.pie(
            data_frame=filtered_df,
            names='Launch Site',  # Group by launch site
            values='class',  # Count of success
            title='Total Success Launches by Site'
        )
        return fig
    else:
        # Filter data for the selected site
        filtered_site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        # Generate pie chart for the specific site
        fig = px.pie(
            data_frame=filtered_site_df,
            names='class',  # Success (1) vs Failed (0)
            title=f'Total Success vs Failure for site {entered_site}'
        )
        return fig


# TASK 4: Add callback for Payload slider and scatter plot
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    filtered_df = spacex_df

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    # Filter the dataframe based on payload range
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload_range[0]) &
                              (filtered_df['Payload Mass (kg)'] <= payload_range[1])]

    # Create a scatter plot
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',  # Success vs Failure
        color='Launch Site',  # Color by Launch Site
        title=f'Payload Mass vs Launch Success for {selected_site}'
    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
