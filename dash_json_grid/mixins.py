# -*- coding: UTF-8 -*-
"""
Mixins
======
@Dash JSON Grid Viewer

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

Description
-----------
The mixins used for extending the functionalities of the automatically generated dash
component.
"""

import os
import inspect
import collections.abc
import json

from typing import Union, Any, TypeVar, IO

try:
    from typing import Sequence, Callable
except ImportError:
    from collections.abc import Sequence, Callable

from typing_extensions import ParamSpec, TypeGuard


P = ParamSpec("P")
T = TypeVar("T")
Route = Sequence[Union[str, int, Sequence[Union[str, int]]]]
__all__ = (
    "is_sequence",
    "sanitize_list_index",
    "get_item_of_object",
    "set_item_of_object",
    "pop_item_of_object",
    "Route",
    "MixinDataRoute",
    "MixinFile",
)


def is_sequence(val: Any) -> TypeGuard[Sequence[Any]]:
    """Check whether `val` is a sequence or not."""
    return (not isinstance(val, (str, bytes))) and isinstance(
        val, collections.abc.Sequence
    )


def sanitize_list_index(index: Any) -> int:
    """Try to ensure `index` to be a `int`. If failed, raise `ValueError`."""
    if isinstance(index, int):
        return index
    if isinstance(index, str):
        return int(index)
    else:
        raise ValueError("Unrecognized index value: {0}".format(index))


def get_item_of_object(data: Any, index: Any) -> Any:
    """Run `data[index]` supposing that `data` is abitrary and `index` can be a
    one-value sequence."""
    if is_sequence(index):
        if isinstance(data, collections.abc.Mapping):
            return data[index[0]]
        elif isinstance(data, collections.abc.Sequence):
            index_key = index[0]
            return tuple(d_item[index_key] for d_item in data)
    else:
        if isinstance(data, collections.abc.Mapping):
            return data[index]
        elif isinstance(data, collections.abc.Sequence):
            try:
                index = sanitize_list_index(index)
            except ValueError as exc:
                raise TypeError(
                    "Index {0} does not match the type of the data "
                    "{1}".format(repr(index), data)
                ) from exc
            return data[index]
    return data


class _set_item_of_object:
    """Private class implementation for the method `set_item_of_object`."""

    @staticmethod
    def _set_by_broadcast(data: Sequence[Any], index_key: str, value: Any):
        """Suppose that `data` is formatted like
        `[{"key": val1, ...}, {"key": val2, ...}, ...]`
        where `key` in each item is the same. This method will modify each value of
        these items by broadcasting `value` into `data`.
        """
        if not is_sequence(value):
            for item in data:
                item[index_key] = value
        elif len(value) == len(data):
            for item, vitem in zip(data, value):
                item[index_key] = vitem
        elif len(value) == 1:
            vitem = value[0]
            for item in data:
                item[index_key] = vitem
        else:
            raise IndexError(
                "The current index {0} locates a table column. However, "
                'the provided argument "val" does not match the length of '
                "the table column. len(located_column)={1}, len(val)="
                "{2}.".format(index_key, len(data), len(value))
            )

    @staticmethod
    def _call_if_idx_is_sequence(data: Any, index: Sequence[Any], value: Any) -> None:
        """Case when `index` is a sequence."""
        index_key = index[0]
        if is_sequence(data):
            _set_item_of_object._set_by_broadcast(data, index_key, value)
        elif isinstance(data, collections.abc.MutableMapping):
            data[index_key] = value
        elif isinstance(data, collections.abc.MutableSequence):
            try:
                index_key = sanitize_list_index(index_key)
            except ValueError as exc:
                raise TypeError(
                    "Index {0} does not match the type of the data "
                    "{1}".format(repr(index_key), data)
                ) from exc
            data[index_key] = value
        else:
            raise ValueError(
                "Fail to modify the data, because the given data {0} is "
                "immutable.".format(data)
            )

    @staticmethod
    def _call_if_idx_is_scalar(data: Any, index: Any, value: Any) -> None:
        """Case when `index` is not sequence."""
        if isinstance(data, collections.abc.MutableMapping):
            data[index] = value
        elif isinstance(data, collections.abc.MutableSequence):
            try:
                index = sanitize_list_index(index)
            except ValueError as exc:
                raise TypeError(
                    "Index {0} does not match the type of the data "
                    "{1}".format(repr(index), data)
                ) from exc
            data[index] = value
        else:
            raise ValueError(
                "Fail to modify the data, because the given data {0} is "
                "immutable.".format(data)
            )


def set_item_of_object(data: Any, index: Any, value: Any) -> None:
    """Run `data[index] = value` supposing that `data` is abitrary and `index` can be a
    one-value sequence.

    Raise an `ValueError` if the item of `data` cannot be set.

    Raise an `IndexError` if the item of `data` is a sequence, while `value` cannot
    be broadcast to this item.
    """
    if is_sequence(index):
        return _set_item_of_object._call_if_idx_is_sequence(data, index, value)
    else:
        return _set_item_of_object._call_if_idx_is_scalar(data, index, value)


def pop_item_of_object(data: Any, index: Any) -> Any:
    """Run `val = data[index]; del data[index]; return val` supposing that `data` is
    abitrary and `index` can be a one-value sequence."""
    if is_sequence(index):
        index_key = index[0]
        if is_sequence(data):
            return tuple(
                (
                    item.pop(index_key, None)
                    if isinstance(item, collections.abc.MutableMapping)
                    else item.pop(index_key)
                )
                for item in data
            )
        elif isinstance(data, collections.abc.MutableMapping):
            return data.pop(index_key, None)
        else:
            raise ValueError(
                "Fail to modify the data, because the given data {0} is "
                "immutable.".format(data)
            )
    else:
        if isinstance(data, collections.abc.MutableMapping):
            return data.pop(index, None)
        elif isinstance(data, collections.abc.MutableSequence):
            try:
                index = sanitize_list_index(index)
            except ValueError as exc:
                raise TypeError(
                    "Index {0} does not match the type of the data "
                    "{1}".format(repr(index), data)
                ) from exc
            return data.pop(index)
        else:
            raise ValueError(
                "Fail to modify the data, because the given data {0} is "
                "immutable.".format(data)
            )


class MixinDataRoute:
    @staticmethod
    def compare_routes(route_1: Route, route_2: Route) -> bool:
        """Compare two different routes.

        The comparison results will not change if the arguments are swapped. This
        method is used for checking whether `route_1` and `route_2` point to the
        same location.

        Arguments
        ---------
        route_1: `[str | int | (str,)]`
        route_2: `[str | int | (str,)]`
            The routes are provided by the `selected_path` callback. Each element
            represents a index of the routing level sequentially. The last element
            may be a one-element sequence. In this case, it represents the selected
            value is a table or a table column.

        Returns
        -------
        #1: `bool`
            A flag. If `True`, it represents that `route_1` and `route_2` are the same.
        """
        if (not isinstance(route_1, collections.abc.Sequence)) or (
            not isinstance(route_2, collections.abc.Sequence)
        ):
            return False
        if len(route_1) != len(route_2):
            return False
        return all((val1 == val2 for val1, val2 in zip(route_1, route_2)))

    @staticmethod
    def get_data_by_route(data: Any, route: Route) -> Any:
        """Get the small part of the data by a specific route.

        Arguments
        ---------
        data: `Any`
            The whole data object to be routed.

        route: `[str | int | (str,)]`
            A sequence of indicies used for locating the specific value in `data`. If
            the last element of this `route` locates a table column, will locate each
            value of the column as a sequence.

        Returns
        -------
        #1: `Any`
            The value located by `route`.
        """
        cur_data: Any = data
        if not isinstance(
            cur_data, (collections.abc.Sequence, collections.abc.Mapping)
        ):
            return cur_data
        for idx in route:
            cur_data = get_item_of_object(cur_data, idx)
        return cur_data

    @staticmethod
    def update_data_by_route(data: Any, route: Route, val: Any) -> Any:
        """Update a specific part of `data` by a route.

        If the update fails (for example, maybe the data is immutable), raise a
        `ValueError`.

        Arguments
        ---------
        data: `Any`
            The whole data object to be updated.

        route: `[str | int | (str,)]`
            A sequence of indicies used for locating the specific value in `data`. If
            the last element of this `route` locates a table column, will apply the
            update to each value of the column.

        val: `Any`
            The value used for updating the located part of the given dictionary. If
            a table column is located, this `val` will be broadcasted to each value of
            the column. If the broadcasting fails, raise an `IndexError`.

        Returns
        -------
        #1: `Any`
            The modified `data`. Since `data` is mutable, even if this returned value
            is not used, the modification will still take effect.
        """
        if not route:
            return data
        if not isinstance(data, (collections.abc.Sequence, collections.abc.Mapping)):
            return data
        cur_data = data
        idx_last = route[-1]
        for idx in route[:-1]:
            if is_sequence(idx):
                idx_last = idx
                break
            cur_data = get_item_of_object(cur_data, idx)
        set_item_of_object(cur_data, idx_last, val)
        return data

    @staticmethod
    def delete_data_by_route(data: Any, route: Route) -> Any:
        """Delete the data part specified by a route.

        If the deletion fails (for example, maybe the data is immutable), raise a
        `ValueError`.

        Arguments
        ---------
        data: `Any`
            The whole data object to be modified, where the located part will be
            deleted.

        route: `[str | int | (str,)]`
            A sequence of indicies used for locating the specific value in `data`. If
            the last element of this `route` locates a table column, will pop out the
            each value of the column.

        Returns
        -------
        #1: `Any`
            The data that is deleted and poped out.
        """
        cur_data = data
        if not isinstance(
            cur_data, (collections.abc.Sequence, collections.abc.Mapping)
        ):
            raise KeyError(
                "Fail to locate the data, because the given data is immutable."
            )
        idx_last = route[-1]
        for idx in route[:-1]:
            if is_sequence(idx):
                idx_last = idx
                break
            cur_data = get_item_of_object(cur_data, idx)
        return pop_item_of_object(cur_data, idx_last)


class MixinFile:
    @classmethod
    def from_str(
        cls: Callable[P, T], json_string: str, *args: P.args, **kwargs: P.kwargs
    ) -> T:
        """Use a JSON string to initialize the component.

        If using this method, users should leave the argument `"data"` blank because
        this method will load `json_string` and pass it to the `data` argument.

        Extra Arguments
        ---------------
        json_string: `str`
            A string where JSON data is encoded.

        Other Arugments
        ---------------
        The same as the initialization.

        Returns
        -------
        The component initialized by `json_string`, where the other details of the
        component is the same as the initialization.
        """
        all_args = inspect.signature(cls).bind(*args, **kwargs).arguments.keys()
        if "data" in all_args:
            raise TypeError(
                'When using "from_str", it is not allowed to specify the argument '
                '"data" because "data" is delegated to the argument "json_string".'
            )
        data = json.loads(json_string)
        kwargs["data"] = data
        return cls(*args, **kwargs)

    @classmethod
    def from_file(
        cls: Callable[P, T],
        json_file: Union[str, os.PathLike, IO[str]],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> T:
        """Use a JSON file to initialize the component.

        If using this method, users should leave the argument `"data"` blank because
        this method will load `json_file` and pass it to the `data` argument.

        Extra Arguments
        ---------------
        json_file: `str | os.PathLike | IO[str]`
            If a `str`| os.PathLike` is provided, will open the file specified by this
            path and load the file content as the data.

            If an `IO[str]` is provided, wil load data from this file-like object
            directly.

        Other Arugments
        ---------------
        The same as the initialization.

        Returns
        -------
        The component initialized by `json_file`, where the other details of the
        component is the same as the initialization.
        """
        all_args = inspect.signature(cls).bind(*args, **kwargs).arguments.keys()
        if "data" in all_args:
            raise TypeError(
                'When using "from_str", it is not allowed to specify the argument '
                '"data" because "data" is delegated to the argument "json_string".'
            )
        if isinstance(json_file, (str, os.PathLike)):
            with open(json_file, "r") as fobj:
                data = json.load(fobj)
        else:
            data = json.load(json_file)
        kwargs["data"] = data
        return cls(*args, **kwargs)
