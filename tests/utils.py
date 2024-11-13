# -*- coding: UTF-8 -*-
"""
Utilities
=========
@ Dash JSON Grid Viewer - Tests

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
Extra functionalities used for enhancing the tests.
"""

import collections.abc

from typing import Optional, Any

try:
    from typing import Sequence, Mapping
    from typing import FrozenSet
except ImportError:
    from collections.abc import Sequence, Mapping
    from builtins import frozenset as FrozenSet


from dash.testing.composite import DashComposite
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException


__all__ = (
    "is_eq",
    "is_eq_mapping",
    "is_eq_sequence",
    "is_mapping_with_keys",
    "docstring_space_remove",
    "attribute_value_neq",
    "wait_for_the_attribute_value_neq",
    "wait_for_dcc_loading",
)


def is_eq(val: Any, ref: Any) -> bool:
    """Safely check whether `val == ref`"""
    if isinstance(ref, (str, bytes)):
        return isinstance(val, ref.__class__) and val == ref
    if isinstance(ref, collections.abc.Sequence):
        return is_eq_sequence(val, ref)
    elif isinstance(ref, collections.abc.Mapping):
        return is_eq_mapping(val, ref)
    else:
        return isinstance(val, ref.__class__) and val == ref


def is_eq_mapping(val: Any, ref: Mapping[Any, Any]) -> bool:
    """Safely check whether `val == ref`, where `ref` is a mapping."""
    if not isinstance(val, collections.abc.Mapping):
        return False
    return dict(val) == dict(ref)


def is_eq_sequence(val: Any, ref: Sequence[Any]) -> bool:
    """Safely check whether `val == ref`, where `ref` is a sequence."""
    if isinstance(val, (str, bytes)) or (not isinstance(val, collections.abc.Sequence)):
        return False
    return tuple(val) == tuple(ref)


def is_mapping_with_keys(val: Any, keys: Sequence[Any]) -> bool:
    """Check whether `val` is mapping and this mapping has keys specified by `keys`.

    If `keys` is not a sequence, will treat it as one key.
    """
    if isinstance(keys, (str, bytes)) or (
        not isinstance(keys, collections.abc.Sequence)
    ):
        keys = (keys,)
    if not isinstance(val, collections.abc.Mapping):
        return False
    return set(val.keys()) == set(keys)


def docstring_space_remove(obj: Any) -> FrozenSet[str]:
    """Get the docstring of an object, with the leading/trailing spaces removed.

    Arguments
    ---------
    obj: `Any`
        The object containing a docstring.

    Returns
    -------
    #1: `str`
        The normalized docstring of `obj` where the leading/trailing spaces are
        removed.
    """
    doc = getattr(obj, "__doc__", None)
    if not doc:
        return frozenset(("",))
    if not isinstance(doc, str):
        return frozenset(("",))
    return frozenset(line.strip() for line in doc.splitlines())


class attribute_value_neq:
    """Wait-for method: attribute value does not equal to something.

    The instance of this class serves as a method used by `DashComposite._waitfor`.
    It will listen to the state of the chosen element until its specific attribute
    value is not the specified value any more.
    """

    def __init__(self, element: WebElement, attribute: str, value: Any) -> None:
        """Initialization.

        Arguments
        ---------
        element: `WebElement`
            The selected selenium `WebElement` where the attribtue will be listened to.

        attribtue: `str`
            The attribute name to be checked. Normally, this name should starts with
            `"data-"`.

        value: `Any`
            The value that the attribute needs to quit from. Normally, this value
            should be a string.
        """
        self.element = element
        self.attribute = attribute
        self.value = value
        self.value_type = type(value)

    def __call__(self, driver: WebDriver):
        """Wait-for method."""
        try:
            element_attribute = self.element.get_attribute(self.attribute)
            return (not isinstance(element_attribute, self.value_type)) or (
                element_attribute != self.value
            )
        except StaleElementReferenceException:
            return False


def wait_for_the_attribute_value_neq(
    dash_duo: DashComposite,
    selector: str,
    by: str = "CSS_SELECTOR",
    attribute: str = "data-any",
    value: Any = "",
    timeout: Optional[int] = None,
) -> None:
    """Select an element, and wait until its attribute does not equal to the specific
    value.

    Arguments
    ---------
    dash_duo: `DashComposite`
        The dash emulator providing the `_wait_for` method.

    selector: `str`
        The selector used for locating the target element.

    by: `str`
        The method of using the selector.
        Valid values: "CSS_SELECTOR", "ID", "NAME", "TAG_NAME",
        "CLASS_NAME", "LINK_TEXT", "PARTIAL_LINK_TEXT", "XPATH".

    attribtue: `str`
        The attribute name to be checked. Normally, this name should starts with
        `"data-"`.

    value: `Any`
        The value that the attribute needs to quit from. Normally, this value should
        be a string.

    timeout: `int | None`
        The customized time out (seconds) length that this method needs to wait.
    """
    dash_duo._wait_for(
        attribute_value_neq(dash_duo.find_element(selector, by), attribute, value),
        timeout=None,
        msg=(
            "timeout {0}s => waiting for the element {1} until the attribute {2} is "
            "not {3}.".format(
                timeout or dash_duo._wait_timeout, selector, attribute, value
            )
        ),
    )


def wait_for_dcc_loading(
    dash_duo: DashComposite,
    selector: str,
    by: str = "CSS_SELECTOR",
    timeout: Optional[int] = None,
) -> None:
    """Select an element, and wait until it quits from the is-loading state.

    Arguments
    ---------
    dash_duo: `DashComposite`
        The dash emulator providing the `_wait_for` method.

    selector: `str`
        The selector used for locating the target element.

    by: `str`
        The method of using the selector.
        Valid values: "CSS_SELECTOR", "ID", "NAME", "TAG_NAME",
        "CLASS_NAME", "LINK_TEXT", "PARTIAL_LINK_TEXT", "XPATH".

    timeout: `int | None`
        The customized time out (seconds) length that this method needs to wait.
    """
    dash_duo._wait_for(
        attribute_value_neq(
            dash_duo.find_element(selector, by), "data-dash-is-loading", "true"
        ),
        timeout=None,
        msg=(
            "timeout {0}s => waiting for the element {1} to be loaded.".format(
                timeout or dash_duo._wait_timeout, selector
            )
        ),
    )
