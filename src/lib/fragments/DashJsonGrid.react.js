/**
 * DashJsonGrid (Implementation)
 *
 * The implementation of the real component.
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 *
 * Thanks the base project:
 * https://github.com/RedHeadphone/react-json-grid
 */

import React, {Component} from "react";
import {type} from "ramda";
import clsx from "clsx/lite";

import JSONGrid from "@redheadphone/react-json-grid";

import {propTypes, defaultProps} from "../components/DashJsonGrid.react";
import {isArray, sanitizeData} from "../utils";

import styles from "./DashJsonGrid.module.scss";

/**
 * DashJsonGrid is a Dash porting version for the React component:
 * `react-json-grid/JSONGrid`
 *
 * This component provides a JSON Grid viewer used for viewing complicated and
 * unstructured serializable JSON data.
 */
export default class DashJsonGrid extends Component {
  constructor(props) {
    super(props);
    this.handleOnSelect = this.handleOnSelect.bind(this);
  }

  /**
   * (Deprecated) get the child data from a specified route.
   * @param {object} data - The whole data maintained by this component.
   * @param {array} route - The route used for locating a small part of the data.
   * @returns {object} The data chosen by route.
   */
  routeData(data, route) {
    if (!isArray(route) || route.length == 0) {
      return data;
    }
    let cur_data = data;
    for (let cur_idx of route.values()) {
      if (isArray(cur_idx)) {
        if (isArray(cur_data)) {
          cur_idx = cur_idx[0];
          return cur_data.map((element) => {
            return element[cur_idx];
          });
        } else {
          return cur_data[cur_idx[0]];
        }
      } else {
        cur_data = cur_data[cur_idx];
      }
    }
    return cur_data;
  }

  /**
   * Get the theme configurations
   * @param {string | Object.<string, string>} theme - The theme name or the theme
   * definition object.
   * @returns {{
   *   themeName: string, customTheme: Object.<string, string>
   * }} The dispatched theme name and the theme object. If either of them is
   *    configured, the other one should be undefined.
   */
  getTheme(theme) {
    const themeType = type(theme);
    if (themeType === "Object") {
      return {
        themeName: undefined,
        customTheme: theme,
      };
    }
    if (themeType === "String") {
      if (theme === "inherit" || theme == "unset") {
        return {
          themeName: undefined,
          customTheme: {
            bgColor: theme,
            borderColor: theme,
            selectHighlightBgColor: theme,
            cellBorderColor: theme,
            keyColor: theme,
            indexColor: theme,
            numberColor: theme,
            booleanColor: theme,
            stringColor: theme,
            objectColor: theme,
            tableHeaderBgColor: theme,
            tableIconColor: theme,
            searchHighlightBgColor: theme,
          },
        };
      } else {
        return {
          themeName: theme,
          customTheme: undefined,
        };
      }
    }
    return {
      themeName: "default",
      customTheme: undefined,
    };
  }

  /**
   * Handle the onSelect() event of `<JSONGrid/>`
   * @param {array} keyPath - A flattened sequence of indicies used for locating
   * (routing) the selected part of the data.
   */
  handleOnSelect(keyPath) {
    const selectable = this.props.highlight_selected;
    if (selectable) {
      this.props.setProps({
        selected_path: keyPath,
        // selected_value: this.routeData(this.props.data, keyPath),
      });
    }
  }

  render() {
    const {
      id,
      class_name,
      style,
      data,
      default_expand_depth,
      default_expand_key_tree,
      highlight_selected,
      search_text,
      theme,
      loading_state,
    } = this.props;

    const {themeName, customTheme} = this.getTheme(theme);

    return (
      <div
        id={id}
        className={clsx(
          styles["js-grid-container"],
          !highlight_selected && styles["no-select"],
          class_name
        )}
        style={style}
        data-dash-is-loading={
          (loading_state && loading_state.is_loading) || undefined
        }
      >
        <JSONGrid
          data={sanitizeData(data)}
          defaultExpandDepth={default_expand_depth}
          defaultExpandKeyTree={default_expand_key_tree}
          onSelect={this.handleOnSelect}
          highlightSelected={highlight_selected}
          searchText={search_text}
          theme={themeName}
          customTheme={customTheme}
        />
      </div>
    );
  }
}

DashJsonGrid.defaultProps = defaultProps;

DashJsonGrid.propTypes = propTypes;
