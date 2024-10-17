/**
 * Demo used on the introduction page.
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

import JSONGrid from "@redheadphone/react-json-grid";

import {sanitizeData, sanitizeTheme} from "./utils";
import styles from "./App.module.scss";

export const AppVer = (): JSX.Element => (
  <code>{"@redheadphone/react-json-grid@0.9.2"}</code>
);

export const getDemoData = () => {
  return {
    platformName: "E-Shop",
    location: "Global",
    established: 2023,
    dailyActiveUsers: 50,
    totalUsers: 1200,
    lastUpdated: "2024-10-05",
    supportEmail: "support@eshop.com",
    active: true,
    featuredYears: [2017, 2019, 2021],
    admin: {
      name: "Sarah Williams",
      adminSince: "2023-05-06",
      role: "Chief Operating Officer",
      contact: null,
      permissions: {
        canManageUsers: true,
        canManageOrders: true,
        canEditContent: false,
        canAccessFinancials: true,
      },
    },
    users: [
      {
        isActive: true,
        age: 28,
        email: "alice.johnson@example.com",
        name: "Alice Johnson",
        gender: "female",
        orders: [
          {
            orderId: "ORD1001",
            date: "2023-09-10",
            totalAmount: 250.75,
            items: [
              {
                productName: "Laptop",
                quantity: 1,
                price: 1200.0,
              },
              {
                productName: "Mouse",
                quantity: 2,
                price: 25.0,
              },
            ],
          },
        ],
      },
      {
        isActive: false,
        email: "bob.smith@example.com",
        age: 35,
        name: "Bob Smith",
        gender: "male",
        orders: [
          {
            orderId: "ORD2001",
            date: "2023-09-20",
            totalAmount: 75.5,
            items: [
              {
                productName: "Smartphone Case",
                quantity: 1,
                price: 25.5,
              },
              {
                productName: "Wireless Charger",
                quantity: 1,
                price: 50.0,
              },
            ],
          },
        ],
      },
      {
        isActive: true,
        name: "Claire Brown",
        gender: "female",
        age: 30,
        orders: [],
      },
      {
        isActive: true,
        age: 40,
        email: "david.jones@example.com",
        name: "David Jones",
        gender: "male",
        orders: [],
      },
    ],
  };
};

type AppProps = {
  data: Object | any[] | number | string | boolean;
  theme?:
    | {
        light: string;
        dark: string;
      }
    | string;
};

const App = ({
  data,
  theme = {light: "remedy", dark: "moonLight"},
}: AppProps): JSX.Element => {
  const [highlightSelected, setHighlightSelected] = useState(true);
  const [searchText, setSearchText] = useState("");
  const [selectedValue, setSelectedValue] = useState("");

  const {colorMode, setColorMode} = useColorMode();

  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const handleOnSelect = (keyPath: (string | [string])[]) => {
    if (highlightSelected) {
      setSelectedValue(JSON.stringify(keyPath));
    }
  };

  const handleOnSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchText(event.target.value);
  };

  const handleOnHighlight = (event: React.ChangeEvent<HTMLInputElement>) => {
    setHighlightSelected(event.target.checked);
  };

  return (
    <div key={String(mounted)}>
      <p>
        <span>Search:</span>{" "}
        <input type="text" value={searchText} onChange={handleOnSearch}></input>
      </p>
      <p>
        <span>Is selection highlighted:</span>{" "}
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
          onSelect={handleOnSelect}
          highlightSelected={highlightSelected}
          searchText={
            typeof searchText === "string" && searchText.trim().length > 0
              ? searchText
              : undefined
          }
          theme={sanitizeTheme(theme, colorMode === "dark")}
          defaultExpandDepth={2}
        />
      </div>
      <p>
        Selected: <span>{selectedValue}</span>
      </p>
    </div>
  );
};

export default App;
