/**
 * Utilities
 *
 * The utilities used by other components.
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 *
 * Thanks the base project:
 * https://github.com/RedHeadphone/react-json-grid
 */

import {type} from "ramda";

export const isArray =
  Array.isArray ||
  ((value) => {
    return type(value) === "Array";
  });

export const sanitizeData = (data) => {
  const dataType = type(data);

  if (["Null", "Undefined"].includes(dataType)) {
    return {};
  }

  if (["Object", "Array"].includes(dataType)) {
    return data;
  }

  return [data];
};
