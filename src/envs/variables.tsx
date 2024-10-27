/**
 * Environmental variables of this side.
 * Yuchen Jin, mailto:cainmagi@gmail.com
 */

import React from "react";
import Link from "@docusaurus/Link";
import {useDocsPreferredVersion} from "@docusaurus/theme-common";
import IconExternalLink from "@theme/Icon/ExternalLink";

import InlineIcon from "../components/InlineIcon";
import mdiDot from "@iconify-icons/mdi/dot";

const docsPluginId = undefined; // Default docs plugin instance

const variables = {
  repoURL: "https://github.com/cainmagi/dash-json-grid",
  rawURL: "https://raw.githubusercontent.com/cainmagi/dash-json-grid",
  sourceVersion: {
    "0.4.1": "v0.4.1",
    "0.3.x": "v0.3.4",
    main: "main",
  },
  dependencyVersion: {
    "0.4.1": "0.9.2",
    "0.3.x": "0.7.0",
    main: "0.9.2",
  },
};

const useCurrentSourceVersion = (): string => {
  const versionHook: any = useDocsPreferredVersion(docsPluginId);
  const versionLabel = versionHook?.preferredVersion?.label;
  return (
    variables.sourceVersion[versionLabel] || variables.sourceVersion["main"]
  );
};

export type DependencyTagProps = {
  ver: string;
};

export const DependencyTag = ({
  ver = "main",
}: DependencyTagProps): JSX.Element => {
  const versionDeps =
    variables.dependencyVersion[ver] || variables.dependencyVersion["main"];
  return (
    <Link
      href={`https://github.com/RedHeadphone/react-json-grid/tree/v${versionDeps}`}
    >
      <code>{`react-json-grid@${versionDeps}`}</code>
      <IconExternalLink />
    </Link>
  );
};

export const rawURL = (url: string): string => {
  return variables.rawURL + "/" + url;
};

export const repoURL = (url: string | undefined = undefined): string => {
  return url ? variables.repoURL + "/" + url : variables.repoURL;
};

export const releaseURL = (ver: string | undefined = undefined): string => {
  const version = variables.sourceVersion[ver] || useCurrentSourceVersion();
  if (version === "main") {
    return variables.repoURL + "/releases/latest";
  }
  return variables.repoURL + "/releases/tag/" + version;
};

export const rootURL = (url: string): string => {
  const currentSourceVersion = useCurrentSourceVersion();
  return variables.repoURL + "/blob/" + currentSourceVersion + "/" + url;
};

export const sourceURL = (url: string): string => {
  const currentSourceVersion = useCurrentSourceVersion();
  return (
    variables.repoURL +
    "/blob/" +
    currentSourceVersion +
    "/dash_json_grid/" +
    url
  );
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
