# -*- coding: UTF-8 -*-
"""
Table columns
=============
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for the data operations on table columns. These functionalities may need to
be used by the callback when updating the JSON data.
"""

import os
import logging
import collections.abc

from typing import Any

try:
    from typing import Generator
except ImportError:
    from collections.abc import Generator

import pytest

import dash_json_grid
import json

from . import utils


__all__ = ("TestTableColumns",)


class TestTableColumns:
    """Test the modification of the table columns."""

    @pytest.fixture(scope="class")
    def data_json(self) -> Generator[str, None, None]:
        """Fixture: Get the json-string formatted data."""
        log = logging.getLogger("dash_json_grid.test")
        log.info("Initialize the JSON data.")
        with open(
            os.path.join(os.path.dirname(__file__), "data_incomplete.json"), "r"
        ) as fobj:
            _data = fobj.read()
        yield _data
        log.info("Remove the JSON data.")
        del _data

    @pytest.fixture(scope="function")
    def data(self, data_json: str) -> Generator[Any, None, None]:
        """Fixture: Get the pre-loaded data in the original state."""
        yield json.loads(data_json)

    def test_table_columns_list_members(self, data: Any) -> None:
        """Test the getting, setting, and removing of the list items."""
        log = logging.getLogger("dash_json_grid.test")

        test_data = data["unstructured"]

        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, ["v1", 1]
        )
        assert isinstance(data_routed, int)
        assert data_routed == 2
        log.info("Successfully route a list element: {0}".format(data_routed))
        assert data_routed == dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, ["v1", [1]]
        )
        log.info("Successfully make an equivalent route.")

        dash_json_grid.DashJsonGrid.update_data_by_route(test_data, ["v1", [1]], "new")
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, ["v1", 1]
        )
        log.info("Successfully update a list element: {0}".format(data_routed))

        data_deleted = dash_json_grid.DashJsonGrid.delete_data_by_route(
            test_data, ["v1", [0]]
        )
        assert isinstance(data_deleted, int)
        assert data_deleted == 1
        assert test_data["v1"] == ["new", 3]
        log.info("Successfully delete a list element: {0}".format(data_deleted))

        assert utils.is_eq_mapping(
            dash_json_grid.DashJsonGrid.get_data_by_route(test_data, ["v2", ["x"]]),
            {1: 2},
        )

        for new_val in ("new", "new_2"):
            dash_json_grid.DashJsonGrid.update_data_by_route(
                test_data, ["v2", ["x"]], new_val
            )
            assert utils.is_eq_mapping(
                dash_json_grid.DashJsonGrid.get_data_by_route(test_data, ["v2", ["x"]]),
                {1: new_val},
            )
            assert 1 == dash_json_grid.DashJsonGrid.get_data_by_route(
                test_data, ["v2", [0]]
            )
            log.info(
                "Successfully update a column of an incomplete table. The value is: "
                "{0}".format(new_val)
            )

    def test_table_columns_incomplete_cols(self, data: Any) -> None:
        """Test the getting, setting, and removing of the list items."""
        log = logging.getLogger("dash_json_grid.test")

        test_data = data["table"]
        ref_data = [ditem.copy() for ditem in test_data]

        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, [["key1"]]
        )
        assert isinstance(data_routed, collections.abc.Sequence)
        log.info(
            "Successfully get a fully defined column. The value is: "
            "{0}".format(data_routed)
        )
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, [["key2"]]
        )
        assert isinstance(data_routed, collections.abc.Mapping)
        log.info(
            "Successfully get an incomplete column. The value is: "
            "{0}".format(data_routed)
        )

        data_deleted = dash_json_grid.DashJsonGrid.delete_data_by_route(
            test_data, [["key3"]]
        )
        assert utils.is_eq_mapping(data_deleted, {3: ref_data[3]["key3"]})
        assert all("key3" not in ditem for ditem in test_data)
        assert not all("key3" not in ditem for ditem in ref_data)
        log.info(
            "Successfully delete a column of an incomplete table. The value is: "
            "{0}".format(data_deleted)
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(
            test_data, [["key3"]], data_deleted
        )
        for idx in range(len(ref_data)):
            assert utils.is_eq_mapping(test_data[idx], ref_data[idx])
        log.info(
            "Successfully add the data back to the table. The value is: "
            "{0}".format(data_deleted)
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(test_data, [["key3"]], (5.0,))
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, [["key3"]]
        )
        assert utils.is_eq(data_routed, {3: 5.0})
        log.info(
            "Successfully update a column with one value. The value is: "
            "{0}".format(data_routed)
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(
            test_data, [["key2"]], "NEWDATA"
        )
        for idx in range(len(ref_data)):
            assert test_data[idx]["key2"] == "NEWDATA"
        log.info(
            "Successfully update a column by broadcasting. The value is: "
            "{0}".format(test_data[0]["key2"])
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(
            test_data, [["key5"]], ("new-A", "new-B")
        )
        data_update = tuple(ditem["key5"] for ditem in test_data if "key5" in ditem)
        assert utils.is_eq_sequence(data_update, ("new-A", "new-B"))
        log.info(
            "Successfully update a column by broadcasting. Only the existing values "
            "are updated. The new values are: {0}".format(data_update)
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(
            test_data, [["key5"]], {0: "new-C"}
        )
        data_update = tuple(ditem["key5"] for ditem in test_data if "key5" in ditem)
        assert utils.is_eq_sequence(data_update, ("new-C", "new-A", "new-B"))
        log.info(
            "Successfully update a column by broadcasting. Broadcasting is performed"
            "partially. The new values are: {0}".format(data_update)
        )

        dash_json_grid.DashJsonGrid.update_data_by_route(
            test_data, [["key5"]], ("new-A", "new-B", "new-C", "new-D", "new-E")
        )
        data_update = dash_json_grid.DashJsonGrid.get_data_by_route(
            test_data, [["key5"]]
        )
        assert utils.is_eq_sequence(
            data_update, ("new-A", "new-B", "new-C", "new-D", "new-E")
        )
        log.info(
            "Successfully update a column by broadcasting. Only the existing values "
            "are updated. The new values are: {0}".format(data_update)
        )
