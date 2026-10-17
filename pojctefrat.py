import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 23, 15, 7]
})

# Create a sample figure
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Sample Dashboard"),
    html.P("This is a simple Dash dashboard example."),
    dcc.Graph(id='sample-bar-chart', figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)