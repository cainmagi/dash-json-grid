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

export const isArray =
  Array.isArray ||
  ((value) => {
    return value instanceof Array;
  });

export const sanitizeData = (data) => {
  if (["object", "array"].includes(typeof data)) {
    return data;
  }

  return [data];
};
