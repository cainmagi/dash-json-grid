# Dash JSON Grid

{:toc}

## CHANGELOG

### 0.3.0 @ 09/13/2024

#### :mega: New

1. Finish the first version of unit tests:
   1. Add 2 tests in "test_init_from".
   2. Add 4 tests in "test_data".
   3. Add 3 tests in "test_usage".
2. Add `conftest.py` for `pytest`.
3. Rewrite and move the guideline for the developers from `readme.md` to `contributing.md`.
4. Add the "code of conduct" file.
5. Finalize the readme file (including the usage documentation).
6. Add the typehints `dash_json_grid.ThemeConfigs` for providing the `theme` property easily.
7. Configure the python test workflow.
8. Upload the .lock file because it is required by the workflow.
9. Configure the python package uploading workflow.
10. Add the issue and pull request templates.

#### :wrench: Fix

1. Fix: The mixins needs to exclude the type `bytes` from `Sequence`.
2. Fix: Running unit tests for `Dash` needs to installl the browser. The `chrome`/`chromium` has been added to the docker file dependencies.
3. Fix: `apt` may suffer occassional failure when accessing the packages. Improve the stability by configuring the `retry` option.
4. Fix: Some docker scripts may malfunction because `~/.bashrc` provided by some base images may skip in non-interactive mode. To fix this issue, ensure the entrypoint run in the interactive mode.
5. Fix: If using the system-wide python and the newest version, the `pip` may be blocked unless a virtual environment is created. Now the python will run in the virtual environment if the system-wide python is used.
6. Fix: Adjust the workflow to fix wrong version issues.
7. Fix: `Corepack` needs to be enabled in the workflow explicitly.
8. Fix: `Yarn build` needs to be run after installing dash dependencies.

#### :floppy_disk: Change

1. Adjust the optional dependency: `test`.
2. Chage the default application from `python` to `pytest` when using the docker image.
3. Add `--python`, `--react`, and `--demo` modes for launching the docker image.
4. Adjust the dependency `dash` from `>=2.0.0` to `>=2.7.0` to prevent the issue caused by `flask`.
5. Update the meta-data of the project.
6. Expose the `mixins` and `typehints` submodules to users. 
7. Adjust `flake8` configurations to ignore some auto-generated files.
8. Adjust the project keywords.
9. Optimize the code structure to reduce the complexity reported by `flake8`.

### 0.2.0 @ 09/11/2024

#### :mega: New

1. Add `mixins` to the component `DashJsonGrid`. Now it supports more functionalities.

#### :floppy_disk: Change

1. Move some methods from `usage.py` to the package `dash_json_grid`.
2. Merge the configurations of `pyright` to `pyproject.toml`.

### 0.1.0 @ 09/11/2024

#### :mega: New

1. Create this project.
2. Finish the react implement `src` and the automatically generated package `dash_json_grid`.
3. Add the React demo `App.js`.
4. Add the Dash demo `usage.py`.
5. Add configurations `pyproject.toml`.
6. Add the devloper's environment folder `./docker` and the `Dockerfile`.
