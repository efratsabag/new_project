# Sample Dash Dashboard

A small [Plotly Dash](https://dash.plotly.com/) app that shows a sample bar chart.

## What it does

`pojctefrat.py` loads a tiny pandas DataFrame (categories A–D with sample values), builds a Plotly Express bar chart, and serves it in a local Dash dashboard titled **Sample Dashboard**.

## Requirements

- Python 3.8+
- Packages:
  - `dash`
  - `plotly`
  - `pandas`

Install them with:

```bash
pip install dash plotly pandas
```

## Run the app

From the project folder:

```bash
python pojctefrat.py
```

Then open the URL printed in the terminal (typically `http://127.0.0.1:8050`).

Debug mode is on, so the server reloads when you change the code.

## Project layout

```
new_project/
├── pojctefrat.py   # Dash app and sample chart
└── README.md
```
