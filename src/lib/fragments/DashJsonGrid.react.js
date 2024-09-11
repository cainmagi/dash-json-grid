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

import React, {Component} from 'react';

import JSONGrid from '@redheadphone/react-json-grid';

import {propTypes, defaultProps} from '../components/DashJsonGrid.react';
import {isArray} from '../utils';

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
      data,
      default_expand_depth,
      default_expand_key_tree,
      highlight_selected,
      search_text,
      theme,
      loading_state,
    } = this.props;
    console.log(this.props);

    return (
      <div
        id={id}
        className={class_name}
        data-dash-is-loading={
          (loading_state && loading_state.is_loading) || undefined
        }
      >
        <JSONGrid
          data={data}
          defaultExpandDepth={default_expand_depth}
          defaultExpandKeyTree={default_expand_key_tree}
          onSelect={this.handleOnSelect}
          highlightSelected={highlight_selected}
          searchText={search_text}
          theme={
            typeof theme === 'string' && theme.trim().length > 0
              ? theme
              : undefined
          }
          customTheme={typeof theme === 'object' ? theme : undefined}
        />
      </div>
    );
  }
}

DashJsonGrid.defaultProps = defaultProps;

DashJsonGrid.propTypes = propTypes;
