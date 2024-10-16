/* eslint no-magic-numbers: 0 */
import React, {useState} from "react";

import "./style.css";
import {DashJsonGrid} from "../lib";

const Search = (props) => {
  return (
    <div>
      <p>
        <span>Search:</span>
        <input
          value={props.value}
          onChange={(e) => {
            let val = e.target.value;
            props.setSearch(val.trim().length > 0 ? val : undefined);
          }}
        />
      </p>
    </div>
  );
};

const Theme = (props) => {
  return (
    <div>
      <p>
        <span>Theme:</span>
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
      </p>
    </div>
  );
};

const Output = (props) => {
  return (
    <div>
      <p>
        <span>{props.label}:</span>
        <span>{JSON.stringify(props.children)}</span>
      </p>
    </div>
  );
};

const App = () => {
  const _data = {
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

  const [data, setData] = useState(_data);
  const [searchText, setSearchText] = useState(undefined);
  const [defaultExpandPath, setDefaultExpandPath] = useState(0);
  const [selectedPath, setSelectedPath] = useState([]);
  const [hightlightSelected, setHightlightSelected] = useState(true);
  const [theme, setTheme] = useState("defaultLight");

  const states = {
    data: setData,
    search_text: setSearchText,
    default_expand_depth: setDefaultExpandPath,
    selected_path: setSelectedPath,
    highlight_selected: setHightlightSelected,
    theme: setTheme,
  };

  const setProps = (newProps) => {
    Object.entries(newProps).forEach(([key, value]) => {
      states[key](value);
    });
  };

  return (
    <div>
      <Search value={searchText} setSearch={setSearchText} />
      <Theme value={theme} setTheme={setTheme} />
      <DashJsonGrid
        setProps={setProps}
        data={data}
        search_text={searchText}
        default_expand_depth={defaultExpandPath}
        selected_path={selectedPath}
        highlight_selected={hightlightSelected}
        theme={theme}
      />
      <Output label={"Selected"}>{selectedPath}</Output>
    </div>
  );
};

export default App;
