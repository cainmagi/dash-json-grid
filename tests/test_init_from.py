# -*- coding: UTF-8 -*-
"""
Initialization
==============
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for the component initialization. We provide several different kinds of
initializations via the mixins.
"""

import os
import logging

try:
    from typing import Generator
except ImportError:
    from collections.abc import Generator

import pytest

import dash_json_grid

from . import utils


__all__ = ("TestInitFrom",)


class TestInitFrom:
    """Test the component initialization by files."""

    @pytest.fixture(scope="class")
    def file_path(self) -> Generator[str, None, None]:
        """Fixture: Get the path of the testing file."""
        path = os.path.join(os.path.dirname(__file__), "data.json")
        if not os.path.isfile(path):
            raise FileNotFoundError("The testing file is missing: {0}".format(path))
        yield path

    def test_init_from_str(self, file_path: str) -> None:
        """Test the component initializaton from string."""
        log = logging.getLogger("dash_json_grid.test")

        with open(file_path, "r") as fobj:
            json_str = fobj.read()

        comp = dash_json_grid.DashJsonGrid.from_str(json_str, highlight_selected=True)
        assert isinstance(comp, dash_json_grid.DashJsonGrid)
        assert getattr(comp, "highlight_selected") is True
        comp_data = getattr(comp, "data")
        assert utils.is_mapping_with_keys(
            comp_data, ("id", "type", "name", "ppu", "batters", "topping")
        )
        log.info("Successfully initialize the component with a JSON string.")

        with pytest.raises(TypeError, match='When using "from_str", it is not allowed'):
            dash_json_grid.DashJsonGrid.from_str(json_str, data={})
        log.info(
            'Successfully validate the functionality of using "data" with from_str(...)'
        )

    def test_init_from_file(self, file_path: str) -> None:
        """Test the component initializaton from string."""
        log = logging.getLogger("dash_json_grid.test")

        comp = dash_json_grid.DashJsonGrid.from_file(file_path, default_expand_depth=2)
        assert isinstance(comp, dash_json_grid.DashJsonGrid)
        assert getattr(comp, "default_expand_depth") == 2
        comp_data = getattr(comp, "data")
        assert utils.is_mapping_with_keys(
            comp_data, ("id", "type", "name", "ppu", "batters", "topping")
        )
        log.info("Successfully initialize the component with a file path.")

        with open(file_path, "r") as fobj:
            comp = dash_json_grid.DashJsonGrid.from_file(fobj)
        assert isinstance(comp, dash_json_grid.DashJsonGrid)
        comp_data = getattr(comp, "data")
        assert utils.is_mapping_with_keys(
            comp_data, ("id", "type", "name", "ppu", "batters", "topping")
        )
        log.info("Successfully initialize the component with a file-like object.")

        with pytest.raises(
            TypeError, match='When using "from_file", it is not allowed'
        ):
            dash_json_grid.DashJsonGrid.from_file(file_path, data={})
        log.info(
            'Successfully validate the functionality of using "data" with '
            "from_file(...)"
        )
