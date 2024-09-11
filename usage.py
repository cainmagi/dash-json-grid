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

import collections.abc

import dash_json_grid
import dash
from dash import Dash, dcc, callback, html, Input, Output, State

app = Dash(__name__)

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

theme = {
    "bgColor": "#f5f5f5",
    "tableBorderColor": "#d3d3d3",
    "highlightBgColor": "#e0e0e0",
    "cellBorderColor": "#c0c0c0",
    "keyNameColor": "#333333",
    "indexColor": "#666666",
    "numberColor": "#007acc",
    "booleanColor": "#007acc",
    "stringColor": "#2ca22c",
    "objectColor": "#333333",
    "tableHeaderBgColor": "#dddddd",
    "tableHeaderColor": "#333333",
    "searchHighlightBgColor": "#cccccc",
}

app.layout = html.Div(
    [
        html.P(
            [
                html.Span("Search:"),
                dcc.Input(
                    id="search",
                    type="text",
                    style={
                        "height": "32px",
                        "padding": "6px 10px",
                        "background-color": "#fff",
                        "border": "1px solid #D1D1D1",
                        "border-radius": "4px",
                        "box-shadow": "none",
                        "box-sizing": "border-box",
                    },
                ),
            ]
        ),
        html.P(
            [
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
                    ),
                    multi=False,
                    clearable=False,
                    value="default",
                ),
            ]
        ),
        dcc.Loading(
            dash_json_grid.DashJsonGrid(
                id="viewer",
                data=test_data,
                highlight_selected=True,
                theme="defaultLight",
            )
        ),
        html.Div((html.P("Selected:"), html.P(id="selected"))),
        html.Div(id="placeholder"),
    ]
)


@callback(Output("viewer", "theme"), Input("theme", "value"))
def update_theme(value):
    if not value:
        return dash.no_update
    return value


@callback(Output("viewer", "search_text"), Input("search", "value"))
def update_search(value):
    if not value:
        return None
    return value


def compare_route(route_1, route_2) -> bool:
    if (not isinstance(route_1, collections.abc.Sequence)) or (
        not isinstance(route_2, collections.abc.Sequence)
    ):
        return False
    if len(route_1) != len(route_2):
        return False
    return all((val1 == val2 for val1, val2 in zip(route_1, route_2)))


def route_data(data, route):
    cur_data = data
    for idx in route:
        if (not isinstance(idx, str)) and isinstance(idx, collections.abc.Sequence):
            if isinstance(cur_data, collections.abc.Sequence):
                return tuple(item[idx[0]] for item in cur_data)
            else:
                return cur_data[idx[0]]
        cur_data = cur_data[idx]
    return cur_data


def update_data(data, route, val):
    if not route:
        return data
    cur_data = data
    for idx in route[:-1]:
        if (not isinstance(idx, str)) and isinstance(idx, collections.abc.Sequence):
            break
    idx_last = route[-1]
    if (not isinstance(idx_last, str)) and isinstance(
        idx_last, collections.abc.Sequence
    ):
        if isinstance(cur_data, collections.abc.Sequence):
            for item, vitem in zip(cur_data, val):
                item[idx_last[0]] = vitem
        else:
            cur_data[idx_last[0]] = val
    else:
        cur_data[idx_last] = val
    return data


@callback(
    Output("selected", "children"),
    Output("viewer", "data"),
    Input("viewer", "selected_path"),
    State("viewer", "data"),
)
def display_output(route, data):
    if not route:
        return None, dash.no_update

    sel_data = route_data(data, route)
    if isinstance(sel_data, (int, float)):
        update_data(data, route, sel_data + 1)
        return str(route), data

    return str(route), dash.no_update


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
