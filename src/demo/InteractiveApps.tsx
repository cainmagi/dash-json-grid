/**
 * Demo used for showing some interactive features.
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 *
 * Thanks the base project:
 * https://github.com/RedHeadphone/react-json-grid
 */

import React, {useState, useEffect} from "react";
import clsx from "clsx/lite";

import {useColorMode} from "@docusaurus/theme-common";
import Translate from "@docusaurus/Translate";

import JSONGrid from "@redheadphone/react-json-grid";

import {sanitizeData, sanitizeTheme} from "./utils";
import styles from "./InteractiveApps.module.scss";

export const getDemoData = () => {
  return {
    id: "0001",
    type: "donut",
    name: "Cake",
    ppu: 1111.55,
    batters: {
      batter: [
        {id: "1001", type: "Regular"},
        {id: "1002", type: "Chocolate"},
        {id: "1003", type: "Blueberry"},
        {id: "1004", type: "Devil's Food"},
      ],
    },
    topping: [
      {id: "5001", type: "None"},
      {id: "5002", type: "Glazed"},
      {id: "5005", type: "Sugar"},
      {id: "5007", type: "Powdered Sugar"},
      {id: "5006", type: "Chocolate with Sprinkles"},
      {id: "5003", type: "Chocolate"},
      {id: "5004", type: "Maple"},
    ],
  };
};

type DemoAppProps = {
  data: Object | any[] | number | string | boolean;
};

export const SearchOnlyApp = ({data}: DemoAppProps): JSX.Element => {
  const {colorMode, setColorMode} = useColorMode();
  const [searchText, setSearchText] = useState("");

  const handleOnSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchText(event.target.value);
  };

  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div>
      <p>
        <span>
          <Translate
            id="demo.interactive.searchonly.search"
            description="Text of the search input, demo: SearchOnlyApp."
          >
            Search:
          </Translate>
        </span>{" "}
        <input type="text" value={searchText} onChange={handleOnSearch}></input>
      </p>
      <div className={styles.jsGridContainer}>
        <JSONGrid
          data={sanitizeData(data)}
          theme={sanitizeTheme(
            {light: "remedy", dark: "moonLight"},
            colorMode === "dark"
          )}
          searchText={
            typeof searchText === "string" && searchText.trim().length > 0
              ? searchText
              : undefined
          }
          defaultExpandDepth={2}
        />
      </div>
    </div>
  );
};

export const SelectableOnlyApp = ({data}: DemoAppProps): JSX.Element => {
  const {colorMode, setColorMode} = useColorMode();
  const [highlightSelected, setHighlightSelected] = useState(true);

  const handleOnHighlight = (event: React.ChangeEvent<HTMLInputElement>) => {
    setHighlightSelected(event.target.checked);
  };

  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div>
      <p>
        <span>
          <Translate
            id="demo.interactive.selectableonly.selhighlight"
            description="Text of the selectable toggle box, demo: SelectableOnlyApp."
          >
            Is selection highlighted:
          </Translate>
        </span>{" "}
        <input
          type="checkbox"
          checked={highlightSelected}
          onChange={handleOnHighlight}
        ></input>
      </p>
      <div
        className={clsx(
          styles.jsGridContainer,
          !highlightSelected ? styles.noSelect : undefined
        )}
      >
        <JSONGrid
          data={sanitizeData(data)}
          theme={sanitizeTheme(
            {light: "remedy", dark: "moonLight"},
            colorMode === "dark"
          )}
          highlightSelected={highlightSelected}
          defaultExpandDepth={2}
        />
      </div>
    </div>
  );
};

export const OnSelectApp = ({data}: DemoAppProps): JSX.Element => {
  const {colorMode, setColorMode} = useColorMode();
  const [selectedValue, setSelectedValue] = useState("");

  const handleOnSelect = (keyPath: (string | [string])[]) => {
    setSelectedValue(JSON.stringify(keyPath));
  };

  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div key={String(mounted)}>
      <div className={styles.jsGridContainer}>
        <JSONGrid
          data={sanitizeData(data)}
          theme={sanitizeTheme(
            {light: "remedy", dark: "moonLight"},
            colorMode === "dark"
          )}
          onSelect={handleOnSelect}
          defaultExpandDepth={2}
        />
      </div>
      <p>
        <Translate
          id="demo.interactive.onselectapp.selected"
          description="Text of the selected value, demo: OnSelectApp."
        >
          Selected:
        </Translate>{" "}
        <span>{selectedValue}</span>
      </p>
    </div>
  );
};
