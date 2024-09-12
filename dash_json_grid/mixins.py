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

from typing_extensions import ParamSpec


P = ParamSpec("P")
T = TypeVar("T")
Route = Sequence[Union[str, int, Sequence[Union[str, int]]]]
__all__ = ("Route", "MixinDataRoute", "MixinFile")


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
            if (not isinstance(idx, (str, bytes))) and isinstance(
                idx, collections.abc.Sequence
            ):
                if isinstance(cur_data, collections.abc.Sequence):
                    return tuple(item[idx[0]] for item in cur_data)
                else:
                    return cur_data[idx[0]]
            if isinstance(cur_data, collections.abc.Mapping):
                cur_data = cur_data[idx]
            elif isinstance(cur_data, collections.abc.Sequence):
                if not isinstance(idx, int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx, cur_data)
                    )
                cur_data = cur_data[idx]
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
            if (not isinstance(idx, (str, bytes))) and isinstance(
                idx, collections.abc.Sequence
            ):
                idx_last = idx
                break
            if isinstance(cur_data, collections.abc.Mapping):
                cur_data = cur_data[idx]
            elif isinstance(cur_data, collections.abc.Sequence):
                if not isinstance(idx, int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx, cur_data)
                    )
                cur_data = cur_data[idx]
        if (not isinstance(idx_last, (str, bytes))) and isinstance(
            idx_last, collections.abc.Sequence
        ):
            if (not isinstance(cur_data, (str, bytes))) and isinstance(
                cur_data, collections.abc.Sequence
            ):
                if isinstance(val, (str, bytes)) or (
                    not isinstance(val, collections.abc.Sequence)
                ):
                    for item in cur_data:
                        item[idx_last[0]] = val
                elif len(val) == len(cur_data):
                    for item, vitem in zip(cur_data, val):
                        item[idx_last[0]] = vitem
                elif len(val) == 1:
                    for item in cur_data:
                        item[idx_last[0]] = val[0]
                else:
                    raise IndexError(
                        'The argument "route" {0} locates a table column. However, '
                        'the provided argument "val" does not match the length of '
                        "the table column. len(located_column)={1}, len(val)="
                        "{2}.".format(route, len(cur_data), len(val))
                    )
            elif isinstance(cur_data, collections.abc.MutableMapping):
                cur_data[idx_last[0]] = val
            elif isinstance(cur_data, collections.abc.MutableSequence):
                if not isinstance(idx_last[0], int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx_last[0], cur_data)
                    )
                cur_data[idx_last[0]] = val
            else:
                raise ValueError(
                    "Fail to modify the data, because the given data {0} is "
                    "immutable.".format(cur_data)
                )
        else:
            if isinstance(cur_data, collections.abc.MutableMapping):
                cur_data[idx_last] = val
            elif isinstance(cur_data, collections.abc.MutableSequence):
                if not isinstance(idx_last, int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx_last, cur_data)
                    )
                cur_data[idx_last] = val
            else:
                raise ValueError(
                    "Fail to modify the data, because the given data {0} is "
                    "immutable.".format(cur_data)
                )
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
            if (not isinstance(idx, (str, bytes))) and isinstance(
                idx, collections.abc.Sequence
            ):
                idx_last = idx
                break
            if isinstance(cur_data, collections.abc.Mapping):
                cur_data = cur_data[idx]
            elif (not isinstance(cur_data, (str, bytes))) and isinstance(
                cur_data, collections.abc.Sequence
            ):
                if not isinstance(idx, int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx, cur_data)
                    )
                cur_data = cur_data[idx]
        if (not isinstance(idx_last, (str, bytes))) and isinstance(
            idx_last, collections.abc.Sequence
        ):
            if (not isinstance(cur_data, (str, bytes))) and isinstance(
                cur_data, collections.abc.Sequence
            ):
                return tuple(item.pop(idx_last[0]) for item in cur_data)
            elif isinstance(cur_data, collections.abc.MutableMapping):
                return cur_data.pop(idx_last[0])
            else:
                raise ValueError(
                    "Fail to modify the data, because the given data {0} is "
                    "immutable.".format(cur_data)
                )
        else:
            if isinstance(cur_data, collections.abc.MutableMapping):
                return cur_data.pop(idx_last)
            elif isinstance(cur_data, collections.abc.MutableSequence):
                if not isinstance(idx_last, int):
                    raise TypeError(
                        "Index {0} does not match the type of the data "
                        "{1}".format(idx_last, cur_data)
                    )
                return cur_data.pop(idx_last)
            else:
                raise ValueError(
                    "Fail to modify the data, because the given data {0} is "
                    "immutable.".format(cur_data)
                )


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
