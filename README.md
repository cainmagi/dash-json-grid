# Dash JSON Grid

<p><img alt="Banner" src="https://repository-images.githubusercontent.com/856794016/fe6159c5-0ca5-4f8e-83d5-816a36e64ce2"></p>

<p align="center">
  <a href="https://github.com/cainmagi/dash-json-grid/releases/latest"><img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/cainmagi/dash-json-grid?logo=github&sort=semver&style=flat-square"></a>
  <a href="https://github.com/cainmagi/dash-json-grid/releases"><img alt="GitHub all releases" src="https://img.shields.io/github/downloads/cainmagi/dash-json-grid/total?logo=github&style=flat-square"></a>
  <a href="https://github.com/cainmagi/dash-json-grid/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/cainmagi/dash-json-grid?style=flat-square&logo=opensourceinitiative&logoColor=white"></a>
  <a href="https://pypi.org/project/dash-json-grid"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/dash-json-grid?style=flat-square&logo=pypi&logoColor=white&label=pypi"></a>
</p>
<p align="center">
  <a href="https://github.com/cainmagi/dash-json-grid/actions/workflows/python-package.yml"><img alt="GitHub Actions (Build)" src="https://img.shields.io/github/actions/workflow/status/cainmagi/dash-json-grid/python-package.yml?style=flat-square&logo=githubactions&logoColor=white&label=build"></a>
  <a href="https://github.com/cainmagi/dash-json-grid/actions/workflows/python-publish.yml"><img alt="GitHub Actions (Release)" src="https://img.shields.io/github/actions/workflow/status/cainmagi/dash-json-grid/python-publish.yml?style=flat-square&logo=githubactions&logoColor=white&label=release"></a>
</p>

Dash JSON Grid is a Dash component library.

Dash porting version of the react project [React JSON Grid :link:][git-react-json-grid]. Provide structured and nested grid table view of complicated JSON objects/arrays.

The following two figures compare the demos of the original React version and the ported Dash version. Since this project is just a dash component wrapper on the original React component, the performance is the same.

|        React JSON Grid        |       Dash JSON Grid        |
| :---------------------------: | :-------------------------: |
| ![demo-react][pic-demo-react] | ![demo-dash][pic-demo-dash] |

## 1. Install

Intall the **latest released version** of this package by using the PyPI source:

``` sh
python -m pip install dash-json-grid
```

Or use the following commands to install **the developing version** from the GitHub Source when you have already installed [Git :hammer:][tool-git], [NodeJS :hammer:][tool-nodejs], and [Yarn :hammer:][tool-yarn]:

```bash
git clone https://github.com/cainmagi/dash-json-grid
cd dash-json-grid
python -m pip install -r requirements-dev.txt
yarn install
yarn build
python -m pip install .
```

## 2. Usages

The following codes provide a minimal example of using this component:

```python
import dash
import dash_json_grid as djg


app = dash.Dash("demo")
app.layout = djg.DashJsonGrid(
    data={
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
)

if __name__ == "__main__":
    app.run()
```

## 3. Documentation

Check the documentation to find more details about the examples and APIs.

https://cainmagi.github.io/dash-json-grid/

## 4. Contributing

See [CONTRIBUTING.md :book:][link-contributing]

## 5. Changelog

See [Changelog.md :book:][link-changelog]

## 6. Acknowledgements

- [RedHeadphone/react-json-grid :link:][git-react-json-grid]: The original React component implementation of this project.
- [jsongrid.com :link:][link-json-grid]: Grid design and styles.
- [kevincobain2000/json-to-html-table :link:][git-json-to-html]: React Component and project structure

[git-react-json-grid]:https://github.com/RedHeadphone/react-json-grid
[git-json-to-html]:https://github.com/kevincobain2000/json-to-html-table
[link-json-grid]:https://jsongrid.com/json-grid
[dash-pmcallback]:https://dash.plotly.com/pattern-matching-callbacks
[tool-git]:https://git-scm.com/downloads
[tool-nodejs]:https://nodejs.org/en/download/package-manager
[tool-yarn]:https://yarnpkg.com/getting-started/install

[pic-demo-react]:https://raw.githubusercontent.com/cainmagi/dash-json-grid/main/display/demo-react.png
[pic-demo-dash]:https://raw.githubusercontent.com/cainmagi/dash-json-grid/main/display/demo-dash.png

[link-contributing]:https://github.com/cainmagi/dash-json-grid/blob/main/CONTRIBUTING.md
[link-changelog]:https://github.com/cainmagi/dash-json-grid/blob/main/Changelog.md
