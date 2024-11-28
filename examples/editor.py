# -*- coding: UTF-8 -*-
"""
Editor
======
@ Dash JSON Grid Viewer

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
A demo for making a JSON editor with `dash-json-grid`, run the following command to
see the performance.
``` shell
python example/editor.py
```
"""

import os
import json
import logging

from typing import Optional, Any

import dash
import dash_bootstrap_components as dbc
import dash_ace as da
from dash import dcc, html, Input, Output, State


if __name__ == "__main__":
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import dash_json_grid as djg

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

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
    className="p-2",
    children=[
        dcc.Loading(
            className="mb-2",
            delay_show=500,
            children=djg.DashJsonGrid(
                id="viewer",
                data=test_data,
                highlight_selected=True,
                theme="defaultLight",
            ),
        ),
        dbc.Modal(
            id="editor",
            is_open=False,
            size="xl",
            children=(
                dbc.ModalHeader(dbc.ModalTitle("Editor")),
                dbc.ModalBody(
                    children=(
                        da.DashAceEditor(
                            id="editor-text",
                            className="mb-2",
                            width="100%",
                            height="400px",
                            value="",
                            theme="github",
                            mode="json",
                            tabSize=2,
                            placeholder=(
                                "Leave this editor blank if you want to delete the "
                                "data."
                            ),
                            enableBasicAutocompletion=False,
                            enableLiveAutocompletion=False,
                        ),
                        dbc.Alert(
                            children="",
                            id="editor-alert",
                            color="danger",
                            duration=5000,
                            is_open=False,
                        ),
                    )
                ),
                dbc.ModalFooter(
                    children=(
                        dbc.Button(
                            children="Confirm",
                            id="editor-confirm-btn",
                            color="primary",
                            className="ms-auto",
                            n_clicks=0,
                        ),
                        dbc.Button(
                            children="Cancel",
                            id="editor-cancel-btn",
                            color="danger",
                            n_clicks=0,
                        ),
                    )
                ),
            ),
        ),
    ],
)


@app.callback(
    Output("editor", "is_open"),
    # Need the following output because we want to trigger the dialog every time.
    Output("viewer", "selected_path"),
    Input("viewer", "selected_path"),
    # Use "editor-alert" to replace "editor-confirm-btn" because we do not want to
    # close the window if the error is detected.
    Input("editor-alert", "children"),
    Input("editor-cancel-btn", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_editor(
    route: djg.mixins.Route, altert_text: Optional[str], n_clicks_cancel: int
):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == "viewer":
        if route and not djg.DashJsonGrid.compare_routes(route, []):
            return True, dash.no_update
    elif trigger_id == "editor-alert":
        if not altert_text:
            return False, []
    elif trigger_id == "editor-cancel-btn":
        if n_clicks_cancel:
            return False, []

    return dash.no_update, dash.no_update


@app.callback(
    Output("viewer", "data"),
    Output("editor-alert", "is_open"),
    Output("editor-alert", "children"),
    Input("editor-confirm-btn", "n_clicks"),
    State("editor-text", "value"),
    State("viewer", "selected_path"),
    State("viewer", "data"),
    prevent_initial_call=True,
)
def confirm_data_change(
    n_clicks_confirm: int, modified_data: str, route: djg.mixins.Route, data: Any
):
    if not n_clicks_confirm:
        return dash.no_update, dash.no_update, dash.no_update

    if not route:
        return dash.no_update, dash.no_update, dash.no_update

    if not modified_data:
        try:
            djg.DashJsonGrid.delete_data_by_route(data, route)
        except (KeyError, IndexError):
            pass
        if not data:
            return dash.no_update, True, "Error: It is not allowed to delete all data."
        return data, "", False

    try:
        decoded_modified_data = json.loads(modified_data)
    except json.JSONDecodeError as exc:
        logging.error(exc, stack_info=True)
        return (
            dash.no_update,
            True,
            "{0}: {1}.".format(exc.__class__.__name__, str(exc)),
        )

    if "selected_data" not in decoded_modified_data:
        try:
            djg.DashJsonGrid.delete_data_by_route(data, route)
        except (KeyError, IndexError):
            pass
        if not data:
            return dash.no_update, True, "Error: It is not allowed to delete all data."
        return data, "", False

    try:
        djg.DashJsonGrid.update_data_by_route(
            data, route, decoded_modified_data["selected_data"]
        )
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        logging.error(exc, stack_info=True)
        return (
            dash.no_update,
            True,
            "{0}: {1}.".format(exc.__class__.__name__, str(exc)),
        )

    if not data:
        return dash.no_update, True, "Error: It is not allowed to delete all data."

    return data, "", False


@app.callback(
    Output("editor-text", "value"),
    Input("viewer", "selected_path"),
    State("viewer", "data"),
    prevent_initial_call=True,
)
def configure_current_editor_data(route: djg.mixins.Route, data: Any):
    if not route:
        return dash.no_update

    try:
        sel_data = djg.DashJsonGrid.get_data_by_route(data, route)
    except (KeyError, IndexError):  # Select an undefined cell.
        return ""

    selected_data = {"selected_data": sel_data}

    return json.dumps(selected_data, ensure_ascii=False, indent=2)


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
