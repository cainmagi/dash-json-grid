# -*- coding: UTF-8 -*-
"""
Usage
=====
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for the `usage.py` application. These tests will run a browser emulator
powered by `selenium` and `dash.testing`. The basic functionalities of the demo
will be checked one by one.
"""

import logging

try:
    from typing import Sequence, Generator
except ImportError:
    from collections.abc import Sequence, Generator

import pytest

import dash
from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .utils import wait_for_dcc_loading


__all__ = ("TestUsage",)


@pytest.mark.with_dash
class TestUsage:
    """Test the rendering and the usage of the Dash app."""

    @pytest.fixture(scope="class")
    def dash_app(self) -> Generator[dash.Dash, None, None]:
        log = logging.getLogger("dash_json_grid.test")
        log.info("Initialize the Dash app.")
        app = import_app("usage")
        yield app
        log.info("Remove the Dash app.")
        del app

    def test_usage_select(self, dash_duo: DashComposite, dash_app: dash.Dash) -> None:
        """Test the functionalities of selecting elements from the JSON table.

        The selection will trigger the callbacks.
        """
        log = logging.getLogger("dash_json_grid.test")

        # Start a dash app contained as the variable `app` in `usage.py`
        dash_duo.start_server(dash_app)

        cells: Sequence[WebElement] = dash_duo.find_elements(
            "#viewer > div > table > tbody > tr > td > span"
        )

        cells_text = tuple(cell.text for cell in cells)
        log.info("Get the top-level of the json grid table: {0}".format(cells_text))

        assert (
            "id",
            "0001",
            "type",
            "donut",
            "name",
            "Cake",
            "ppu",
            "1111.55",
            "batters",
            "topping",
        ) == cells_text

        assert "name" in cells_text
        cells[cells_text.index("name")].click()
        dash_duo.wait_for_text_to_equal("#selected-path", "[['name']]")
        dash_duo.wait_for_text_to_equal("#selected-val", "Cake")
        log.info("Confirm the value of the keyword: {0}".format("name"))

        assert "topping" in cells_text
        cells[cells_text.index("topping")].click()
        dash_duo.wait_for_text_to_equal("#selected-path", "[['topping']]")
        dash_duo.wait_for_text_to_equal(
            "#selected-val",
            (
                "[{'id': '5001', 'type': 'None'}, {'id': '5002', 'type': 'Glazed'}, "
                "{'id': '5005', 'type': 'Sugar'}, "
                "{'id': '5007', 'type': 'Powdered Sugar'}, "
                "{'id': '5006', 'type': 'Chocolate with Sprinkles'}, "
                "{'id': '5003', 'type': 'Chocolate'}, {'id': '5004', 'type': 'Maple'}]"
            ),
        )
        log.info("Confirm the value of the keyword: {0}".format("topping"))

        assert "1111.55" in cells_text
        cells[cells_text.index("1111.55")].click()
        dash_duo.wait_for_text_to_equal("#selected-path", "['ppu']")
        dash_duo.wait_for_text_to_equal("#selected-val", "1112.55")
        log.info("Confirm the value of the keyword: {0}".format("ppu"))

    def test_usage_search(self, dash_duo: DashComposite, dash_app: dash.Dash):
        """Test the effect of using search to highlight elements."""
        log = logging.getLogger("dash_json_grid.test")

        # Start a dash app contained as the variable `app` in `usage.py`
        dash_duo.start_server(dash_app)

        search_box: WebElement = dash_duo.find_element("#search")
        for sent_text, expect_text, n_backspace in (
            ("name", "name", 0),
            ("Ca", "Cake", 4),
            ("bat", "batters", 2),
        ):
            if n_backspace > 0:
                search_box.send_keys(Keys.BACKSPACE * (2 * n_backspace))
            search_box.send_keys(sent_text)
            wait_for_dcc_loading(dash_duo, "#viewer")
            log.info(
                'Confirm the search box update "{0}" gets finalized.'.format(sent_text)
            )
            viewer: WebElement = dash_duo.find_element("#viewer")
            cell_highlight: WebElement = viewer.find_element(
                By.XPATH, ".//span[contains(@class, 'search-highlight')]"
            )
            assert cell_highlight.text == expect_text
            log.info('Confirm the results: "{0}" is searched.'.format(expect_text))

    def test_usage_theme(self, dash_duo: DashComposite, dash_app: dash.Dash):
        """Test the effect of changing the theme."""
        log = logging.getLogger("dash_json_grid.test")

        # Start a dash app contained as the variable `app` in `usage.py`
        dash_duo.start_server(dash_app)

        theme_box: WebElement = dash_duo.find_element("#theme")
        theme_input: WebElement = theme_box.find_element(By.TAG_NAME, "input")
        for theme, bg_color, fg_color in (
            ("defaultLight", "rgba(245, 245, 245, 1)", "rgba(44, 162, 44, 1)"),
            ("blueberryDark", "rgba(36, 41, 56, 1)", "rgba(39, 232, 167, 1)"),
            ("remedy", "rgba(255, 255, 255, 1)", "rgba(44, 142, 187, 1)"),
            ("softEra", "rgba(249, 245, 245, 1)", "rgba(135, 182, 190, 1)"),
            ("atomMaterial", "rgba(38, 50, 56, 1)", "rgba(195, 232, 141, 1)"),
        ):
            theme_input.send_keys(Keys.DELETE * 8)
            theme_input.send_keys(theme[:4])
            dash_duo.select_dcc_dropdown(theme_box, theme)
            wait_for_dcc_loading(dash_duo, "#viewer")
            log.info('Confirm the theme box update "{0}" gets finalized.'.format(theme))
            dash_duo.wait_for_style_to_equal(
                "#viewer > div", "background-color", bg_color
            )
            log.info(
                'Confirm the background color: "{0}" is as expectation.'.format(
                    bg_color
                )
            )
            assert (
                dash_duo.find_element("#viewer > div > table")
                .find_element(By.XPATH, ".//*[contains(text(),'0001')]")
                .value_of_css_property("color")
                == fg_color
            )
            log.info(
                'Confirm the text color: "{0}" is as expectation.'.format(fg_color)
            )
