/**
 * DashJsonGrid (Implementation)
 *
 * The lazy-loaded version with the property definition.
 *
 * Author: Yuchen Jin (cainmagi)
 * GitHub: https://github.com/cainmagi/dash-json-grid
 * License: MIT
 *
 * Thanks the base project:
 * https://github.com/RedHeadphone/react-json-grid
 */

import React from "react";
import PropTypes from "prop-types";
import {DashJsonGrid as RealComponent} from "../LazyLoader";

/**
 * DashJsonGrid is a Dash porting version for the React component:
 * `react-json-grid/JSONGrid`
 *
 * This component provides a JSON Grid viewer used for viewing complicated and
 * unstructured serializable JSON data.
 */
const DashJsonGrid = (props) => {
  return (
    <React.Suspense fallback={null}>
      <RealComponent {...props} />
    </React.Suspense>
  );
};

DashJsonGrid.defaultProps = {
  default_expand_depth: 0,
  selected_path: [],
  highlight_selected: true,
  theme: "default",
};

DashJsonGrid.propTypes = {
  /**
   * The ID used to identify this component in Dash callbacks.
   */
  id: PropTypes.string,

  /**
   * Often used with CSS to style elements with common properties.
   */
  class_name: PropTypes.string,

  /**
   * Defines CSS styles which will override styles previously set.
   */
  style: PropTypes.object,

  /**
   * The JSON-serializable data to be transformed into a grid table.
   */
  data: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
    PropTypes.array,
    PropTypes.number,
    PropTypes.string,
    PropTypes.bool,
  ]).isRequired,

  /**
   * The depth to which the grid is expanded by default.
   */
  default_expand_depth: PropTypes.number,

  /**
   * Tree-like structure with all keys that needs to be expanded. This structure needs
   * to be a `Mapping` mimicing the structure of the data.
   */
  default_expand_key_tree: PropTypes.object,

  /**
   * `keyPath` captured by the `onSelect` method of the grid viewer. This value is a
   * sequence of indicies used for locating the element of the selected data.
   * Due to the limitation of the exported functionalities, this value cannot be
   * reset by the callback. In other words, using it with callbacks.Output will
   * not take effects.
   */
  selected_path: PropTypes.array,

  // /**
  //  * (Deprecated)
  //  * Values located by the current selectedPath (keyPath captured by onSelect).
  //  * This value is a part of the original data. It is only changed when select event
  //  * happens. It is read-only, which means changing the value by the callback will
  //  * not influence the data.
  //  */
  // selected_value: PropTypes.oneOfType([
  //   PropTypes.object,
  //   PropTypes.array,
  //   PropTypes.number,
  //   PropTypes.string,
  //   PropTypes.bool,
  // ]),

  /**
   * Whether to highlight the selected item or not.
   */
  highlight_selected: PropTypes.bool,

  /**
   * The text that needs to be searched in the JSON data.
   */
  search_text: PropTypes.string,

  /**
   * The theme (name) that needs to be applied. If a `Mapping` is specified, will
   * customize the color code of each part of grid viewer.
   */
  theme: PropTypes.oneOfType([
    PropTypes.oneOf([
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
    ]),
    PropTypes.exact({
      /**
       * Background color of the whole grid view.
       */
      bgColor: PropTypes.string,
      /**
       * Border color of the whole grid view.
       */
      borderColor: PropTypes.string,
      /**
       * Background color of table cells.
       */
      cellBorderColor: PropTypes.string,
      /**
       * Text color of mapping keys.
       */
      keyColor: PropTypes.string,
      /**
       * Text color of sequence indicies.
       */
      indexColor: PropTypes.string,
      /**
       * Text color of numeric values.
       */
      numberColor: PropTypes.string,
      /**
       * Text color of boolean variables.
       */
      booleanColor: PropTypes.string,
      /**
       * Text color of strings.
       */
      stringColor: PropTypes.string,
      /**
       * Text color of unrecognized objects.
       */
      objectColor: PropTypes.string,
      /**
       * Background color of the table header.
       */
      tableHeaderBgColor: PropTypes.string,
      /**
       * Text color of the icon in the table header.
       */
      tableIconColor: PropTypes.string,
      /**
       * Background color when this part is highlighted by the selection.
       */
      selectHighlightBgColor: PropTypes.string,
      /**
       * Background color of the part highlighted by the search.
       */
      searchHighlightBgColor: PropTypes.string,
    }),
  ]),

  /**
   * Dash-assigned callback that should be called to report property changes
   * to Dash, to make them available for callbacks.
   */
  setProps: PropTypes.func,

  /**
   * Object that holds the loading state object coming from dash-renderer
   */
  loading_state: PropTypes.shape({
    /**
     * Determines if the component is loading or not
     */
    is_loading: PropTypes.bool,
    /**
     * Holds which property is loading
     */
    prop_name: PropTypes.string,
    /**
     * Holds the name of the component that is loading
     */
    component_name: PropTypes.string,
  }),
};

export default DashJsonGrid;

export const defaultProps = DashJsonGrid.defaultProps;
export const propTypes = DashJsonGrid.propTypes;
