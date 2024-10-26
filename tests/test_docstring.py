# -*- coding: UTF-8 -*-
"""
Docstring
=========
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The tests for validating the consistency between the docstrings of the main component
and the auto-generated comonent.
"""

import logging

from dash_json_grid import DashJsonGrid
from dash_json_grid.DashJsonGrid import DashJsonGrid as _DashJsonGrid

from . import utils


__all__ = ("TestDocstring",)


class TestDocstring:
    """Test the consistency between the mixin-merged component and the auto-genrated
    component."""

    def test_docstring_components(self) -> None:
        """Test the comparison between the docstrings of the components."""
        log = logging.getLogger("dash_json_grid.test")

        assert utils.docstring_space_remove(
            DashJsonGrid
        ) == utils.docstring_space_remove(_DashJsonGrid)
        log.info("Confirm that {0}.__doc__ is valid.".format(DashJsonGrid.__name__))
