# -*- coding: UTF-8 -*-
"""
Empty
=====
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for the `empty.py` application. These tests will run a browser emulator
powered by `selenium` and `dash.testing`. The basic functionalities of the demo
will be checked one by one.
"""

import logging

try:
    from typing import Generator
except ImportError:
    from collections.abc import Generator

import pytest

import dash
import dash_json_grid as djg

from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite
from selenium.webdriver.remote.webelement import WebElement

from .utils import wait_for_dcc_loading


__all__ = ("TestEmpty",)


@pytest.mark.with_dash
class TestEmpty:
    """Test the incorrect usage when making the `data` empty."""

    @pytest.fixture(scope="class")
    def dash_app(self) -> Generator[dash.Dash, None, None]:
        log = logging.getLogger("dash_json_grid.test")
        log.info("Initialize the Dash app.")
        app = import_app("tests.apps.empty")
        yield app
        log.info("Remove the Dash app.")
        del app

    def test_empty_switch_tab(
        self, dash_duo: DashComposite, dash_app: dash.Dash
    ) -> None:
        """Test the functionalities of switching tabs when an empty value is specified.

        The selection will trigger the callbacks.
        """
        log = logging.getLogger("dash_json_grid.test")

        # Start a dash app contained as the variable `app` in `usage.py`
        dash_duo.start_server(dash_app)

        dash_duo.wait_for_element_by_id("text-1")
        dash_duo.wait_for_text_to_equal("#text-1", "Text of Page 1")

        btn: WebElement = dash_duo.find_element("#btn-tabs")
        btn.click()

        wait_for_dcc_loading(dash_duo, "#tabs")
        dash_duo.wait_for_element_by_id("text-2")
        dash_duo.wait_for_text_to_equal("#text-2", "Text of Page 2")
        log.info("Confirm that the empty app works when switching tabs.")

    def test_empty_bad_init(self):
        """Test the error thrown by the bad initialization."""
        log = logging.getLogger("dash_json_grid.test")

        assert isinstance(djg.DashJsonGrid(data=None), djg.DashJsonGrid)

        with pytest.raises(TypeError, match=r"^Required argument"):
            djg.DashJsonGrid()

        log.info("Confirm that the bad initialization can be detected.")
