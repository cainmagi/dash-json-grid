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
    """Background color of the whole grid view."""

    booleanColor: str
    """Text color of boolean variables."""

    borderColor: str
    """Border color of the whole grid view."""

    cellBorderColor: str
    """Background color of table cells."""

    indexColor: str
    """Text color of sequence indicies."""

    keyColor: str
    """Text color of mapping keys."""

    numberColor: str
    """Text color of numeric values."""

    objectColor: str
    """Text color of unrecognized objects."""

    searchHighlightBgColor: str
    """Background color of the part highlighted by the search."""

    selectHighlightBgColor: str
    """Background color when this part is highlighted by the selection."""

    stringColor: str
    """Text color of strings."""

    tableHeaderBgColor: str
    """Background color of the table header."""

    tableIconColor: str
    """Text color of the icon in the table header."""
