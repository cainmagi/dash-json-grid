# -*- coding: UTF-8 -*-
"""
App: Empty
==========
@ Dash JSON Grid Viewer

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The testing application `empty` used for testing.
"""

import os

from typing import Optional

import dash
from dash import Dash, dcc, html, Input, Output, State


if __name__ == "__main__":
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


import dash_json_grid


app = Dash(__name__)

app.layout = html.Div(
    (
        html.Div(html.Button(id="btn-tabs", children="Change Tab")),
        dcc.Loading(
            dcc.Tabs(
                id="tabs",
                value="page-1",
                children=[
                    dcc.Tab(
                        label="Page 1",
                        value="page-1",
                        children=html.P(id="text-1", children="Text of Page 1"),
                    ),
                    dcc.Tab(
                        label="Page 2",
                        value="page-2",
                        children=(
                            html.P(id="text-2", children="Text of Page 2"),
                            dash_json_grid.DashJsonGrid(
                                id="viewer",
                                data=None,
                                highlight_selected=True,
                                theme="defaultLight",
                            ),
                        ),
                    ),
                ],
            ),
            show_initially=False,
            delay_hide=500,
        ),
    )
)


@app.callback(
    Output("tabs", "value"),
    Input("btn-tabs", "n_clicks"),
    State("tabs", "value"),
    prevent_initial_call=True,
)
def update_tab(n_clicks: Optional[int], prev_tab: Optional[str]):
    if not n_clicks:
        return dash.no_update
    if not prev_tab:
        return "page-1"
    return "page-2" if prev_tab == "page-1" else "page-1"


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

    app.run(host=get_ip(), port="8080", debug=False)
