# Dash JSON Grid

{:toc}

## CHANGELOG

### 0.5.0 @ 11/27/2024

#### :mega: New

1. Add an example folder showing the usage with other vendor packages.
2. Add functionalities of using examples with the developers' docker image (the contributing guide is also updated).

#### :wrench: Fix

1. Fix: Correct the ToC numbers in the readme file.

#### :floppy_disk: Change

1. Bump `Yarn` version from `4.5.2` to `4.5.3`.

### 0.4.3 @ 11/22/2024

#### :wrench: Fix

1. Fix: Fix a severe bug of importing the components in a wrong list. Now the scope is limited to the auto-generated codes.
2. Fix: Correct the path of submitting a vulnerability issue in the security policy.
3. Fix: Correct wrong (old) version numbers in contributing guide.

#### :floppy_disk: Change

1. Bump `Yarn` version from `4.5.1` to `4.5.2`.

### 0.4.2 @ 11/13/2024

#### :mega: New

1. Add tests for passing an empty value to the `data` property.
2. Add SCSS styles when the property `highighlight_selected == False`. This change make the cursor become normal if the grid elements are not selectable.

#### :wrench: Fix

1. Fix: Improve the sanitization of the input data. Previously, the sanitization does not work correctly if the `data` is specified by `None`.
2. Fix: The comparison of the docstring may fail because different versions of `dash` may produce docstrings in different order. Make the docstring comparison more robust.
3. Fix: Improve the robustness of the type check by replacing `typeof` with `ramda.type`.

#### :floppy_disk: Change

1. The `callback` is replaced by `app.callback` in `usage.py`.
2. The issue and PR templates are adjusted, and the vulnerability issue tempate is removed because we decide to use a different way to accept vulnerability reports.
3. Make the package information updated to `v0.4.2`.

### 0.4.1 @ 10/26/2024

#### :mega: New

1. Add a test for validating that the docstring of the main component is consistent with that of the auto-generated component.

#### :wrench: Fix

1. Fix: Update the docstring of the component and the typehint `ThemeConfigs` to the newest version.

#### :floppy_disk: Change

1. Change the behavior of `DashJsonGrid.update_data_by_route(...)`. When a column is specified, a length-one sequence is provided, and the number available items of the column is also one, will broadcast the one available value rather than broadcasting all the sequence item to all columns.

### 0.4.0 @ 10/21/2024

#### :mega: New

1. Upgrade the core dependency `react-json-grid` from `v0.7.0` to `v0.9.2`, where several bugs are fixed.
2. Update the tests to match the new `react-json-grid@0.9.2`.
3. Make the data routing support the new indexing rule like: `[..., ..., [2]]`, where the last value is an `int` in a one-element list.
4. Allow the `DashJsonGrid.update_data_by_route(...)` to accept a mapping value when updating a column. If all keys in this mapping are `int`, will treat the mapping as the index set.
5. Add tests for this new version.

#### :wrench: Fix

1. Fix: Correct some ambiguous descriptions in the docstrings.

#### :floppy_disk: Change

1. Configure `.gitattributes` for specifying the line-breaks of files.
2. Make the returned column data of `DashJsonGrid.get_data_by_route(...)` or `pop_item_of_object(...)` become `OrderedDict()` if the column data is incomplete.
3. Improve the compatibility of `dash_json_grid.DashJsonGrid.update_data_by_route(...)`. Now it can update table data even if it contains invalid rows.
4. Update the security policy file.

### 0.3.4 @ 10/20/2024

#### :wrench: Fix

1. Fix: The modification in `0.3.3` incorrectly allows `DashJsonGrid.pop_item_of_object(...)` to export a table row/cell even if the data fails to be routed. Now this situation is disallowed.
2. Fix: A bug of `react-json-grid<=0.9.0` causes the selection may return an incorrect route containing `null`. Now the codes will handle this case. When routing the data, the routing will stop by the parent of the place where the `null` index is applied to. When modifying the data, using a route containing `null` will do nothing.
3. Fix: Correct typos in the docstrings of `mixins` and `pytest`.
4. Fix: Add extra rules to `DashJsonGrid.get_data_by_route(...)` to raise an `KeyError` if a column cannot export any value.

#### :floppy_disk: Change

1. Previously, `DashJsonGrid.get_data_by_route(...)` cannot get a column if the column name does not exist in a specific row. Now, the `undefined` value will be treated as `None` when acquired to make this method compatible with a partially complete column.
2. Update the project metadata.

### 0.3.3 @ 10/16/2024

#### :wrench: Fix

1. Fix: Correct a typo of the html codes in the readme file.

#### :floppy_disk: Change

1. Add the folder `/docs` to the ignore list of `git`, `docker`, `flake8`, `black`, and `pyright`.
2. Add the banner to the readme file.
3. Add more files to the `MANIFEST.in` list.
4. Previously, `DashJsonGrid.pop_item_of_object(...)` cannot pop a column if the column name does not exist in a specific row. Now, the `undefined` value will be treated as `None` when popped out to make this method compatible with a partially complete column.
5. Modify `pyproject.toml` to add the link of the documentation.
6. Remove the documentation in `readme` because the new documentation has been finalized in the [GitPage](https://cainmagi.github.io/dash-json-grid/).
7. Make `DashJsonGrid` (with mixins version) synchronized with the auto-generated docstring.
8. Adjust `.gitattributes` for providing more auto-linebreak rules.
9. Adjust the automatic formatter and editor configurations for the compatibility with the package manager.
10. Change the dependency configurations (but the dependency versions are not changed).
11. Python 3.13 is released, add this version to the test profile.
12. Change the version information which previously caused the release failed.

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
