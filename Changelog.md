# Dash JSON Grid

{:toc}

## CHANGELOG

### 0.3.2 @ 09/30/2024

#### :mega: New

1. Add the `style` property to the component.
2. Allow users to specify the `theme` property as `inherit` or `unset`, which allows more flexible configurations.
3. Add the security policy and the corresponding issue template.

#### :wrench: Fix

1. Fix: When rendering the data, the component will print `data`. Remove this unexpected behavior.
2. Fix: Correct the component name and the specified style name in `usage.py`.

#### :floppy_disk: Change

1. Modify the workflow to exempt the out-of-date dependency: `borales/actions-yarn@v4`.
2. Update the issue templates by changing some examples.
3. Update the link of submitting the vulnerability issue, and the description in the security policy file.

### 0.3.1 @ 09/14/2024

#### :wrench: Fix

1. Fix: Fix some links and formats in the readme.
2. Fix: The step for installing the dev version suggested in the readme is not correct. Now it has been corrected.
3. Fix: Make `data` sanitized. Now a scalar like `int` or `str` can be passed to the property `data` and the `data` will be rendered as a one-value list.
4. Fix: When selecting a scalar element from a list, the returned index in `selected_path` is `str` but not `int`. Add `mixins.sanitize_list_index(...)` to treat this special case.

#### :floppy_disk: Change

1. Add the section "3. Additional utilities" to the readme.
2. Adjust project details and fix typos in the readme.
3. Add an explanation about `data` in the readme.
4. Adjust the metadata of the project, and remove the auto-genreated file.
5. Adjust the format of the workflow files.

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
