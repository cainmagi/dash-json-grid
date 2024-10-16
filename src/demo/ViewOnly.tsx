/**
 * Demo used for showing some view-only examples.
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 *
 * Thanks the base project:
 * https://github.com/RedHeadphone/react-json-grid
 */

import React, {useState} from "react";

import {useColorMode} from "@docusaurus/theme-common";

import JSONGrid from "@redheadphone/react-json-grid";

import {sanitizeData, sanitizeTheme, getUnsetThemeStyles} from "./utils";
import styles from "./ViewOnly.module.scss";

type customeThemeType = {
  bgColor?: string;
  borderColor?: string;
  selectHighlightBgColor?: string;
  cellBorderColor?: string;
  keyColor?: string;
  indexColor?: string;
  numberColor?: string;
  booleanColor?: string;
  stringColor?: string;
  objectColor?: string;
  tableHeaderBgColor?: string;
  tableIconColor?: string;
  searchHighlightBgColor?: string;
};

type AppProps = {
  data: Object | any[] | number | string | boolean;
  theme?:
    | {
        light: string;
        dark: string;
      }
    | string;
  customTheme?: customeThemeType;
};

const App = ({
  data,
  theme = {light: "remedy", dark: "moonLight"},
  customTheme = {},
}: AppProps): JSX.Element => {
  const {colorMode, setColorMode} = useColorMode();

  const sanitizedTheme = sanitizeTheme(theme, colorMode === "dark");
  const valTheme =
    sanitizedTheme === "inherit" ||
    sanitizedTheme === "unset" ||
    (customTheme && Object.keys(customTheme).length > 0)
      ? undefined
      : sanitizedTheme;

  const defaultCustomTheme =
    sanitizedTheme === "inherit" || sanitizedTheme === "unset"
      ? getUnsetThemeStyles(sanitizedTheme)
      : undefined;
  const valCustomTheme =
    customTheme && Object.keys(customTheme).length > 0
      ? customTheme
      : defaultCustomTheme;

  return (
    <div>
      <div className={styles.jsGridContainer}>
        <JSONGrid
          data={sanitizeData(data)}
          theme={valTheme}
          customTheme={valCustomTheme}
        />
      </div>
    </div>
  );
};

type ThemeProps = {
  value: string;
  setTheme: (value: string) => void;
};

const Theme = (props: ThemeProps): JSX.Element => {
  const Icon = (): JSX.Element => (
    <svg viewBox="0 0 10 6">
      <polyline points="1 1 5 5 9 1"></polyline>
    </svg>
  );

  return (
    <div className="select">
      <p>
        <span>Theme:</span>{" "}
        <select
          name={"theme"}
          value={props.value}
          onChange={(e) => {
            props.setTheme(e.target.value);
          }}
        >
          {[
            "default",
            "dracula",
            "monokai",
            "oceanicPark",
            "panda",
            "gruvboxMaterial",
            "tokyoNight",
            "remedy",
            "atlanticNight",
            "defaultLight",
            "defaultLight2",
            "slime",
            "spacegray",
            "blueberryDark",
            "nord",
            "nightOwl",
            "oneMonokai",
            "cobaltNext",
            "shadesOfPurple",
            "codeBlue",
            "softEra",
            "atomMaterial",
            "evaDark",
            "moonLight",
            "inherit",
            "unset",
          ].map((e, idx) => {
            return (
              <option key={idx} value={`${e}`}>
                {e}
              </option>
            );
          })}
        </select>
        <Icon />
      </p>
    </div>
  );
};

type ThemedAppProps = {
  data: Object | any[] | number | string | boolean;
};

export const ThemedApp = ({data}: ThemedAppProps): JSX.Element => {
  const {colorMode, setColorMode} = useColorMode();
  const [theme, setTheme] = useState("defaultLight");

  const sanitizedTheme = sanitizeTheme(theme, colorMode === "dark");

  const valTheme =
    sanitizedTheme === "inherit" || sanitizedTheme === "unset"
      ? undefined
      : sanitizedTheme;
  const customTheme =
    sanitizedTheme === "inherit" || sanitizedTheme === "unset"
      ? getUnsetThemeStyles(sanitizedTheme)
      : undefined;

  return (
    <div>
      <Theme value={theme} setTheme={setTheme} />
      <div className={styles.jsGridContainer}>
        <JSONGrid
          data={sanitizeData(data)}
          theme={valTheme}
          customTheme={customTheme}
        />
      </div>
    </div>
  );
};

export default App;
