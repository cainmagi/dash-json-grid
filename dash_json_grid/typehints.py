"""
Typehints
=========
@Dash JSON Grid Viewer

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
Extra typehints used by this project.
"""

from typing_extensions import TypedDict


__all__ = ("ThemeConfigs",)


class ThemeConfigs(TypedDict, total=False):
    """Detailed configuration for defining a customized theme."""

    bgColor: str
    """Background color."""

    booleanColor: str
    """Text color of boolean variables."""

    cellBorderColor: str
    """Background color of table cells."""

    highlightBgColor: str
    """Background color when this part is highlighted."""

    indexColor: str
    """Text color of array indicies."""

    keyNameColor: str
    """Text color of JSON keys."""

    numberColor: str
    """Text color of numeric values."""

    objectColor: str
    """Text color of unrecognized objects."""

    searchHighlightBgColor: str
    """Background color of the part highlighted by the search."""

    stringColor: str
    """Text color of strings."""

    tableBorderColor: str
    """Border color of the whole table."""

    tableHeaderBgColor: str
    """Background color of the table header."""

    tableHeaderColor: str
    """Text color of the table header."""
