# -*- coding: UTF-8 -*-
"""
Dash JSON Grid Viewer
=====================

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
Dash porting version of the react project React JSON Grid. Provide structured and
nested grid table view of complicated JSON objects/arrays.

Thanks to
---------
RedHeadphone/react-json-grid

https://github.com/RedHeadphone/react-json-grid
"""

import os as _os
import sys as _sys
import json

import dash as _dash

from . import typehints
from . import mixins

# noinspection PyUnresolvedReferences
from ._imports_ import DashJsonGrid as _DashJsonGrid
from ._imports_ import __all__ as __import_all__
from .mixins import MixinDataRoute as _MixinDataRoute, MixinFile as _MixinFile
from .typehints import ThemeConfigs

__all__ = ("typehints", "mixins", "DashJsonGrid", "ThemeConfigs")

if not hasattr(_dash, "__plotly_dash") and not hasattr(_dash, "development"):
    print(
        "Dash was not successfully imported. "
        "Make sure you don't have a file "
        'named \n"dash.py" in your current directory.',
        file=_sys.stderr,
    )
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, "package-info.json"))
with open(_filepath) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")
__version__ = package["version"]

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]

async_resources = [
    "DashJsonGrid",
]

_js_dist = []

_js_dist.extend(
    [
        {
            "relative_package_path": "async-{}.js".format(async_resource),
            "external_url": ("https://unpkg.com/{0}@{2}" "/{1}/async-{3}.js").format(
                package_name, __name__, __version__, async_resource
            ),
            "namespace": package_name,
            "async": True,
        }
        for async_resource in async_resources
    ]
)

# TODO: Figure out if unpkg link works
_js_dist.extend(
    [
        {
            "relative_package_path": "async-{}.js.map".format(async_resource),
            "external_url": (
                "https://unpkg.com/{0}@{2}" "/{1}/async-{3}.js.map"
            ).format(package_name, __name__, __version__, async_resource),
            "namespace": package_name,
            "dynamic": True,
        }
        for async_resource in async_resources
    ]
)

_js_dist.extend(
    [
        {"relative_package_path": "dash_json_grid.min.js", "namespace": package_name},
        {
            "relative_package_path": "dash_json_grid.min.js.map",
            "namespace": package_name,
            "dynamic": True,
        },
    ]
)

_css_dist = []


class DashJsonGrid(_DashJsonGrid, _MixinDataRoute, _MixinFile):
    """A DashJsonGrid component.
    DashJsonGrid is a Dash porting version for the React component:
    `react-json-grid/JSONGrid`

    This component provides a JSON Grid viewer used for viewing complicated and
    unstructured serializable JSON data.

    Keyword arguments:

    - id (string; optional):
        The ID used to identify this component in Dash callbacks.

    - class_name (string; optional):
        Often used with CSS to style elements with common properties.

    - data (a value equal to: null | dict | list | number | string | boolean; required):
        The JSON-serializable data to be transformed into a grid table.

    - default_expand_depth (number; default 0):
        The depth to which the grid is expanded by default.

    - default_expand_key_tree (dict; optional):
        Tree-like structure with all keys that needs to be expanded. This
        structure needs to be a `Mapping` mimicing the structure of the
        data.

    - highlight_selected (boolean; default True):
        Whether to highlight the selected item or not.

    - loading_state (dict; optional):
        Object that holds the loading state object coming from
        dash-renderer.

        `loading_state` is a dict with keys:

        - is_loading (boolean; optional):
            Determines if the component is loading or not.

        - prop_name (string; optional):
            Holds which property is loading.

        - component_name (string; optional):
            Holds the name of the component that is loading.

    - search_text (string; optional):
        The text that needs to be searched in the JSON data.

    - selected_path (list; optional):
        `keyPath` captured by the `onSelect` method of the grid viewer.
        This value is a sequence of indicies used for locating the element
        of the selected data. Due to the limitation of the exported
        functionalities, this value cannot be reset by the callback. In
        other words, using it with callbacks.Output will not take effects.

    - style (dict; optional):
        Defines CSS styles which will override styles previously set.

    - theme (dict; default "default"):
        The theme (name) that needs to be applied. If a `Mapping` is
        specified, will customize the color code of each part of grid
        viewer.

        `theme` is a a value equal to: "default", "dracula", "monokai",
        "oceanicPark", "panda", "gruvboxMaterial", "tokyoNight", "remedy",
        "atlanticNight", "defaultLight", "defaultLight2", "slime",
        "spacegray", "blueberryDark", "nord", "nightOwl", "oneMonokai",
        "cobaltNext", "shadesOfPurple", "codeBlue", "softEra",
        "atomMaterial", "evaDark", "moonLight", "inherit", "unset" | dict
        with keys:

        - bgColor (string; optional):
            Background color of the whole grid view.

        - borderColor (string; optional):
            Border color of the whole grid view.

        - cellBorderColor (string; optional):
            Background color of table cells.

        - keyColor (string; optional):
            Text color of mapping keys.

        - indexColor (string; optional):
            Text color of sequence indicies.

        - numberColor (string; optional):
            Text color of numeric values.

        - booleanColor (string; optional):
            Text color of boolean variables.

        - stringColor (string; optional):
            Text color of strings.

        - objectColor (string; optional):
            Text color of unrecognized objects.

        - tableHeaderBgColor (string; optional):
            Background color of the table header.

        - tableIconColor (string; optional):
            Text color of the icon in the table header.

        - selectHighlightBgColor (string; optional):
            Background color when this part is highlighted by the
            selection.

        - searchHighlightBgColor (string; optional):
            Background color of the part highlighted by the search."""


for _component in __import_all__:
    setattr(locals()[_component], "_js_dist", _js_dist)
    setattr(locals()[_component], "_css_dist", _css_dist)
