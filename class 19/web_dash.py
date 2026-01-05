import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")

app = dash.Dash(__name__)

fig = px.line(df, x="date", y="sales")

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)


















# # 1) Update system
# sudo apt update && sudo apt upgrade -y

# # 2) Install Python, pip and venv
# sudo apt install -y python3 python3-venv python3-pip

# # 3) Verify
# python3 --version
# python3 -m pip --version

# # 4) Change to project directory
# cd "/home/steampup-qbh/Desktop/Hussain Alam (XI)/Hussain-Alam/20th class"

# # 5) Create and activate virtual environment
# python3 -m venv .venv
# source .venv/bin/activate

# # 6) Upgrade pip and install dependencies
# pip install --upgrade pip setuptools wheel
# pip install dash plotly pandas numpy seaborn matplotlib

# # 7) (Optional) Open the file to remove the duplicated code block if present
# nano dashboard.py
# # — remove the repeated copy of the script at the bottom and save (Ctrl+O, Enter, Ctrl+X)

# # 8) Run the Dash app (local)
# python dashboard.py

# # 9) To make the app reachable from other devices on your LAN, edit the run_server line in dashboard.py:
# # change app.run_server(debug=True) -> app.run_server(debug=True, host='0.0.0.0', port=8050)
# # then run:
# python dashboard.py