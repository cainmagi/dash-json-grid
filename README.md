# Dash JSON Grid

<p align="center">
  <a href="https://github.com/cainmagi/dash-json-grid/releases/latest"><img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/cainmagi/dash-json-grid?logo=github&sort=semver&style=flat-square"></a>
  <a href="https://github.com/cainmagi/dash-json-grid/releases"><img alt="GitHub all releases" src="https://img.shields.io/github/downloads/cainmagi/dash-json-grid/total?logo=github&style=flat-square"></a>
  <a href="https://github.com/cainmagi/dash-json-grid/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/cainmagi/dash-json-grid?style=flat-square"></a>
  <a href="https://pypi.org/project/dash-json-grid"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/dash-json-grid?style=flat-square"></a>
</p>

Dash JSON Grid is a Dash component library.

Dash porting version of the react project [React JSON Grid :link:][git-react-json-grid]. Provide structured and nested grid table view of complicated JSON objects/arrays.

The following two figures compare the demos of the original React version and the ported Dash version. Since this project is just a dash component wrapper on the original React component, the performance is the same.

|             React JSON Grid             |            Dash JSON Grid             |
| :-------------------------------------: | :-----------------------------------: |
| ![demo-react](./display/demo-react.png) | ![demo-dash](./display/demo-dash.png) |

## 1. Install

Intall the **latest released version** of this package by using the PyPI source:

``` sh
python -m pip install dash-json-grid
```

Or use the following command to install **the developing version** from the GitHub Source:

```bash
python -m pip install git+https://github.com/cainmagi/dash-json-grid
```

## 2. Usage

* The component can be initialized by the following signature:

    ``` python
    import dash_json_grid

    dash_json_grid.DashJsonGrid(
        id: str | dict{...},
        class_name: str,
        data: Any,
        default_expand_depth: int,
        default_expand_key_tree: dict,
        selected_path: list ,
        highlight_selected: bool,
        search_text: str,
        theme: str | dict,
        loading_state: dict
    )
    ```

    where we use `data` to provide the data to be viewed.

* Users can also initialize the component by a string:

    ``` python
    import dash_json_grid

    dash_json_grid.DashJsonGrid.from_str(
        json_string: str, ...
    )
    ```

    By using this signature, the first argument `json_string` will be a string that can be decoded by a JSON decoder. In this case, `data` should not be used.

* It is also allowed to use a file to initialize the component directly:
  
    ``` python
    import dash_json_grid

    dash_json_grid.DashJsonGrid.from_file(
        json_file: str | os.PathLike | IO[str], ...
    )
    ```

    By using this signature, the first argument `json_file` will be path pointing to a json file or a file-like object. In this case, `data` should not be used.

> [!WARNING]
> Note that `json_str` and `json_file` are translated to `data` during the initialization. Therefore, `json_str` or `json_file` will not be properties that can be accessed by a callback.

## 3. Properties

The `DashJsonGrid` component supports the following callback-accessible properties:

| Name                  | Type     | Description                                                           | Default       |
| --------------------- | -------- | --------------------------------------------------------------------- | ------------- |
| id                      | `str` or `dict`   | The ID of the component. A dictionary-id is used for creating a [pattern-matching callback :book:][dash-pmcallback].        | undefined     |
| class_name              | `str`   | The css-class of the component. Use ` ` to separate different names.        | undefined     |
| data                    | `Any`   | The JSON-serializable simple object to be transformed into a grid table.         | Requried :exclamation:     |
| default_expand_depth    | `int`   | The depth to which the grid is expanded by default.                   | `0`             |
| default_expand_key_tree | `dict`  | Tree-like structure with all keys that needs to be expanded. This value should be used only when `data` is a `dict`.          | undefined     |
| selected_path           | `list`  | A sequence of indicies representing the route of the currently selected element. The last value can represent a column or a table if it is a one-value list. | `[]` |
| highlight_selected      | `bool`  | Whether to highlight the selected item or not. If disabled, the selection will not trigger callbacks. | `True`          |
| search_text             | `str`   | The text that needs to be searched in the JSON data.                  | undefined     |
| theme                   | `str` or `dict`   | The theme name or the dictionary representing the details of a theme.  | 'default'     |
| loading_state           | `dict`   | The loading state set by Dash. This value should not be used by users. | undefined            |

The following arguments are **NOT** properties. They are used for providing different ways of initialization.

* Used by the class method `from_str(...)`
  
    | Name                  | Type     | Description                                                           | Default       |
    | --------------------- | -------- | --------------------------------------------------------------------- | ------------- |
    | json_string | `str`   | A string that can be decoded as json data. This value is configured for replacing `data` duirng the initialization.  | Required :exclamation:   |

* Used by the class method `from_file(...)`
  
    | Name                  | Type     | Description                                                           | Default       |
    | --------------------- | -------- | --------------------------------------------------------------------- | ------------- |
    | json_file | `str` or `PathLike` or `IO[str]` | If it is a string or a path-like object, it is used for locating the json file. It can be a file-like object, too. This value is also used for replacing `data`.  | Required :exclamation:   |

## 4. Available themes

The property `theme` can be a theme name (`str`) or a theme-configuration dictionary (`dict`). The dictionary format should be like this:

``` python
theme = {
    "bgColor": "#f5f5f5",
    "booleanColor": "#007acc",
    "cellBorderColor": "#c0c0c0",
    "highlightBgColor": "#e0e0e0",
    "indexColor": "#666666",
    "keyNameColor": "#333333",
    "numberColor": "#007acc",
    "objectColor": "#333333",
    "searchHighlightBgColor": "#cccccc",
    "stringColor": "#2ca22c",
    "tableBorderColor": "#d3d3d3",
    "tableHeaderBgColor": "#dddddd",
    "tableHeaderColor": "#333333",
}
```

The configuration `theme` can be incomplete. It is recommended that this value can be initialized by a typed dictionary:

``` python
import dash_json_grid

theme = dash_json_grid.ThemeConfigs(
    bgColor="#f5f5f5",
    booleanColor="#007acc",
    ...
)
```

When using the theme name, the available theme names are:

``` python
[
    "default", "dracula", "monokai", "oceanicPark", "panda",
    "gruvboxMaterial", "tokyoNight", "remedy", "atlanticNight",
    "defaultLight", "defaultLight2", "slime", "spacegray",
    "blueberryDark", "nord", "nightOwl", "oneMonokai", "cobaltNext",
    "shadesOfPurple", "codeBlue", "softEra", "atomMaterial",
    "evaDark", "moonLight"
]
```

## 5. Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 6. Changelog

See [Changelog.md](./Changelog.md)

## 7. Acknowledgements

- [RedHeadphone/react-json-grid :link:][git-react-json-grid]: The original React component implementation of this project.
- [jsongrid.com :link:][link-json-grid]: Grid design and styles.
- [kevincobain2000/json-to-html-table :link:][git-json-to-html]: React Component and project structure

[git-react-json-grid]:https://github.com/RedHeadphone/react-json-grid
[git-json-to-html]:https://github.com/kevincobain2000/json-to-html-table
[link-json-grid]:https://jsongrid.com/json-grid
[dash-pmcallback]:https://dash.plotly.com/pattern-matching-callbacks
