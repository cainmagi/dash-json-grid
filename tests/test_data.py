# -*- coding: UTF-8 -*-
"""
Data
=====
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for the data operations. These functionalities may need to be used by the
callback when updating the JSON data.
"""

import os
import logging
from typing import Any

try:
    from typing import Generator
except ImportError:
    from collections.abc import Generator

import pytest

import dash_json_grid
import json

from . import utils


__all__ = ("TestData",)


class TestData:
    """Test the routing and modification of the json data."""

    @pytest.fixture(scope="class")
    def data_json(self) -> Generator[str, None, None]:
        """Fixture: Get the json-string formatted data."""
        log = logging.getLogger("dash_json_grid.test")
        log.info("Initialize the JSON data.")
        with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as fobj:
            _data = fobj.read()
        yield _data
        log.info("Remove the JSON data.")
        del _data

    @pytest.fixture(scope="function")
    def data(self, data_json: str) -> Generator[Any, None, None]:
        """Fixture: Get the pre-loaded data in the original state."""
        yield json.loads(data_json)

    @staticmethod
    def compare_route(
        log: logging.Logger,
        route_1: dash_json_grid.mixins.Route,
        route_2: dash_json_grid.mixins.Route,
    ) -> None:
        assert dash_json_grid.DashJsonGrid.compare_routes(route_1, route_1) is True
        assert dash_json_grid.DashJsonGrid.compare_routes(route_2, route_2) is True
        assert dash_json_grid.DashJsonGrid.compare_routes(route_1, route_2) is False
        log.info("Successfully compare routes: {0} vs {1}".format(route_1, route_2))

    def test_data_compare_route(self) -> None:
        """Test the comparison between different routes."""
        log = logging.getLogger("dash_json_grid.test")

        self.compare_route(log, ["a", "b", 1], ["a", "b", "1"])
        self.compare_route(log, ["a", "b", "c"], ["a", "B", "c"])
        self.compare_route(log, ["a", "b", "c"], ["a", "b", "c", "d"])
        self.compare_route(log, ["a", "b", 1], ["a", "b", [1]])
        self.compare_route(log, ["a", "b", "c"], ["a", "B", ["c"]])

    def test_data_get_by_route(self, data: Any) -> None:
        """Test the functionality of using a rotue to locate a part of the data."""
        log = logging.getLogger("dash_json_grid.test")

        route = ["batters", "batter", 0, "id"]
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert data_routed == "1001"
        log.info("Successfully route an element.")

        route = ["batters", "batter", 2]
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert utils.is_eq_mapping(data_routed, {"id": "1003", "type": "Blueberry"})
        log.info("Successfully route a row.")

        route = ["topping", ["type"]]
        data_routed = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        log.info(data_routed)
        assert utils.is_eq_sequence(
            data_routed,
            (
                "None",
                "Glazed",
                "Sugar",
                "Powdered Sugar",
                "Chocolate with Sprinkles",
                "Chocolate",
                "Maple",
            ),
        )

    def test_data_update_by_route(self, data: Any) -> None:
        """Test the functionality of using a rotue to update a part of the data."""
        log = logging.getLogger("dash_json_grid.test")

        route = ["batters", "batter", 0, "id"]
        data_prev = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert data_prev == "1001"
        dash_json_grid.DashJsonGrid.update_data_by_route(data, route, "9999")
        data_now = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert data_now == "9999"
        log.info(
            "Successfully update an element: {0} -> {1}.".format(data_prev, data_now)
        )

        route = ["batters", "batter", 1]
        data_prev = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert utils.is_eq_mapping(data_prev, {"id": "1002", "type": "Chocolate"})
        dash_json_grid.DashJsonGrid.update_data_by_route(
            data, route, {"id": "9998", "type": "Modified"}
        )
        data_now = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert utils.is_eq_mapping(data_now, {"id": "9998", "type": "Modified"})
        log.info("Successfully update a row: {0} -> {1}.".format(data_prev, data_now))

        route = ["topping", ["id"]]
        data_prev = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert utils.is_eq_sequence(
            data_prev, ("5001", "5002", "5005", "5007", "5006", "5003", "5004")
        )
        dash_json_grid.DashJsonGrid.update_data_by_route(
            data, route, ("3001", "3002", "3005", "3007", "3006", "3003", "3004")
        )
        data_now = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert utils.is_eq_sequence(
            data_now, ("3001", "3002", "3005", "3007", "3006", "3003", "3004")
        )
        log.info("Successfully update a row: {0} -> {1}.".format(data_prev, data_now))

    def test_data_delete_by_route(self, data: Any) -> None:
        log = logging.getLogger("dash_json_grid.test")

        route = ["batters", "batter", 0, "id"]
        data_prev = dash_json_grid.DashJsonGrid.delete_data_by_route(data, route)
        assert data_prev == "1001"
        with pytest.raises(KeyError, match="id"):
            dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        log.info("Successfully remove an element: {0}.".format(data_prev))

        route = ["topping", 3]
        data_prev = dash_json_grid.DashJsonGrid.delete_data_by_route(data, route)
        assert utils.is_eq_mapping(data_prev, {"id": "5007", "type": "Powdered Sugar"})
        data_now = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert not utils.is_eq_mapping(
            data_now, {"id": "5007", "type": "Powdered Sugar"}
        )
        log.info("Successfully remove a row: {0}.".format(data_prev))

        route = ["batters", "batter", ["type"]]
        data_prev = dash_json_grid.DashJsonGrid.delete_data_by_route(data, route)
        assert utils.is_eq_sequence(
            data_prev, ("Regular", "Chocolate", "Blueberry", "Devil's Food")
        )
        with pytest.raises(KeyError, match="type"):
            dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        route = ["batters", "batter"]
        data_now = dash_json_grid.DashJsonGrid.get_data_by_route(data, route)
        assert (
            not set()
            .union(*(tuple(ditem.keys()) for ditem in data_now))
            .difference(("id",))
        )
        log.info("Successfully remove a column: {0}.".format(data_prev))
