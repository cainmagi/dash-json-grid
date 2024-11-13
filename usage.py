# -*- coding: UTF-8 -*-
"""
Usage
=====
@ Dash JSON Grid Viewer

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
A demo for the project. Run the following command to view the performance:
``` shell
python usage.py
```
"""

import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_json_grid

app = Dash(__name__)

main_css = {
    "--jg-bg-color": "#fff",
    "--jg-border-color": "#a5a5a5",
    "--jg-cell-border-color": "#ddd",
    "--jg-key-color": "#32373b",
    "--jg-index-color": "#00f",
    "--jg-number-color": "#007acc",
    "--jg-boolean-color": "#00f",
    "--jg-string-color": "#a31515",
    "--jg-object-color": "#00009f",
    "--jg-table-header-bg-color": "#ddd",
    "--jg-table-icon-color": "#333",
    "--jg-select-highlight-bg-color": "#c1def133",
    "--jg-search-highlight-bg-color": "#8885",
}

test_data = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 1111.55,
    "batters": {
        "batter": [
            {"id": "1001", "type": "Regular"},
            {"id": "1002", "type": "Chocolate"},
            {"id": "1003", "type": "Blueberry"},
            {"id": "1004", "type": "Devil's Food"},
        ]
    },
    "topping": [
        {"id": "5001", "type": "None"},
        {"id": "5002", "type": "Glazed"},
        {"id": "5005", "type": "Sugar"},
        {"id": "5007", "type": "Powdered Sugar"},
        {"id": "5006", "type": "Chocolate with Sprinkles"},
        {"id": "5003", "type": "Chocolate"},
        {"id": "5004", "type": "Maple"},
    ],
}

app.layout = html.Div(
    style=main_css,
    children=[
        html.Div(
            style={"marginBottom": "1rem"},
            children=[
                html.Span("Search:"),
                dcc.Input(
                    id="search",
                    type="text",
                    style={
                        "height": "32px",
                        "padding": "6px 10px",
                        "backgroundColor": "#fff",
                        "border": "1px solid #D1D1D1",
                        "borderRadius": "4px",
                        "boxShadow": "none",
                        "boxSizing": "border-box",
                    },
                ),
            ],
        ),
        html.Div(
            style={"marginBottom": "1rem"},
            children=[
                html.Span("Theme:"),
                dcc.Dropdown(
                    id="theme",
                    options=(
                        "default",
                        "dracula",
                        "monokai",
                        "oceanicPark",
                        "panda",
                        "gruvboxMaterial",
                        "tokyoNight",
                        "remedy",
                        "atlanticNight",
                        "defaultLight",
                        "defaultLight2",
                        "slime",
                        "spacegray",
                        "blueberryDark",
                        "nord",
                        "nightOwl",
                        "oneMonokai",
                        "cobaltNext",
                        "shadesOfPurple",
                        "codeBlue",
                        "softEra",
                        "atomMaterial",
                        "evaDark",
                        "moonLight",
                        "inherit",
                        "unset",
                    ),
                    multi=False,
                    clearable=False,
                    value="default",
                ),
            ],
        ),
        dcc.Loading(
            dash_json_grid.DashJsonGrid(
                id="viewer",
                data=test_data,
                highlight_selected=True,
                theme="defaultLight",
            ),
        ),
        html.Div((html.P("Selected Path:"), html.P(id="selected-path"))),
        html.Div((html.P("Selected Value:"), html.P(id="selected-val"))),
        html.Div(id="placeholder"),
    ],
)


@app.callback(Output("viewer", "theme"), Input("theme", "value"))
def update_theme(value):
    if not value:
        return dash.no_update
    return value


@app.callback(Output("viewer", "search_text"), Input("search", "value"))
def update_search(value):
    if not value:
        return None
    return value


@app.callback(
    Output("selected-path", "children"),
    Output("selected-val", "children"),
    Output("viewer", "data"),
    Input("viewer", "selected_path"),
    State("viewer", "data"),
)
def display_output(route, data):
    if not route:
        return None, None, dash.no_update

    sel_data = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
    if isinstance(sel_data, (int, float)):
        sel_data_new = sel_data + 1
        dash_json_grid.DashJsonGrid.update_data_by_route(data, route, sel_data_new)
        return str(route), str(sel_data_new), data

    return str(route), str(sel_data), dash.no_update


if __name__ == "__main__":
    import socket

    def get_ip(method: str = "broadcast") -> str:
        """Detect the IP address of this device."""
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            if method == "broadcast":
                s_socket.connect(("10.255.255.255", 1))
                ip_value = s_socket.getsockname()[0]
            elif method == "udp":
                s_socket.connect(("8.8.8.8", 1))
                ip_value = s_socket.getsockname()[0]
            elif method == "host":
                ip_value = socket.gethostbyname(socket.gethostname())
            else:
                raise ConnectionError
        except Exception:  # pylint: disable=broad-except
            ip_value = "localhost"
        finally:
            s_socket.close()
        return ip_value

    app.run(host=get_ip(), port="8080", debug=True)
