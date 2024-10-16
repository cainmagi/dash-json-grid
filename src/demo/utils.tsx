/**
 * Utilities
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 */

export const sanitizeData = (data: any): Record<string, any> | Array<any> => {
  if (["object", "array"].includes(typeof data)) {
    return data;
  }

  return [data];
};

export const sanitizeTheme = (
  theme: {light: string; dark: string} | string,
  isDarkTheme: boolean = false
): string => {
  if (typeof theme === "string") {
    return theme;
  } else {
    return isDarkTheme ? theme?.dark || "moonLight" : theme?.light || "remedy";
  }
};

export const getUnsetThemeStyles = (style?: "inherit" | "unset") => {
  return {
    bgColor: style,
    borderColor: style,
    selectHighlightBgColor: style,
    cellBorderColor: style,
    keyColor: style,
    indexColor: style,
    numberColor: style,
    booleanColor: style,
    stringColor: style,
    objectColor: style,
    tableHeaderBgColor: style,
    tableIconColor: style,
    searchHighlightBgColor: style,
  };
};
