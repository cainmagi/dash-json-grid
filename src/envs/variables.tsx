/**
 * Environmental variables of this side.
 * Yuchen Jin, mailto:cainmagi@gmail.com
 */

import React from "react";
import Link from "@docusaurus/Link";

import InlineIcon from "../components/InlineIcon";
import mdiDot from "@iconify-icons/mdi/dot";

const variables = {
  repoURL: "https://github.com/cainmagi/dash-json-grid",
  rawURL: "https://raw.githubusercontent.com/cainmagi/dash-json-grid",
  sourceURL: "https://github.com/cainmagi/dash-json-grid/blob/v0.3.2",
};

export const rawURL = (url: string): string => {
  return variables.rawURL + "/" + url;
};

export const repoURL = (url: string): string => {
  return variables.repoURL + "/" + url;
};

export const rootURL = (url: string): string => {
  return variables.sourceURL + "/" + url;
};

export const sourceURL = (url: string): string => {
  return variables.sourceURL + "/dash_json_grid/" + url;
};

export type SourceLinkProps = {
  url: string;
  children: React.ReactNode;
};

export const SourceLink = ({url, children}: SourceLinkProps): JSX.Element => {
  return (
    <Link to={sourceURL(url)} className="noline">
      {children}
    </Link>
  );
};

export type SplitterProps = {
  padx?: string;
};

export const Splitter = ({padx = "0"}: SplitterProps): JSX.Element => {
  return (
    <span style={{padding: "0 " + padx}}>
      <InlineIcon icon={mdiDot} />
    </span>
  );
};
