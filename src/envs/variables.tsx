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
import {biSlashLg} from "../components/icons/BiSlashLg";

const docsPluginId = undefined; // Default docs plugin instance

const variables = {
  repoURL: "https://github.com/cainmagi/dash-json-grid",
  rawURL: "https://raw.githubusercontent.com/cainmagi/dash-json-grid",
  sourceVersion: {
    "0.4.2": "v0.4.2",
    "0.3.x": "v0.3.4",
    main: "main",
  },
  dependencyVersion: {
    "0.4.2": "0.9.2",
    "0.3.x": "0.7.0",
    main: "0.9.2",
  },
  sourceURIs: {
    "v0.3.4": {
      ".": "__init__.py",
      DashJsonGrid: "__init__.py#L109",
      mixins: "mixins.py",
      "mixins.get_item_of_object": "mixins.py#L65",
      "mixins.is_sequence": "mixins.py#L48",
      "mixins.MixinDataRoute": "mixins.py#L227",
      "mixins.MixinFile": "mixins.py#L373",
      "mixins.pop_item_of_object": "mixins.py#L187",
      "mixins.Route": "mixins.py#L35",
      "mixins.sanitize_list_index": "mixins.py#L55",
      "mixins.set_item_of_object": "mixins.py#L172",
      typehints: "typehints.py",
      "typehints.ThemeConfigs": "typehints.py#L22",
    },
    main: {
      ".": "__init__.py",
      DashJsonGrid: "__init__.py#L109",
      mixins: "mixins.py",
      "mixins.get_item_of_object": "mixins.py#L99",
      "mixins.is_sequence": "mixins.py#L48",
      "mixins.MixinDataRoute": "mixins.py#L327",
      "mixins.MixinFile": "mixins.py#L473",
      "mixins.pop_item_of_object": "mixins.py#L294",
      "mixins.Route": "mixins.py#L35",
      "mixins.sanitize_list_index": "mixins.py#L55",
      "mixins.set_item_of_object": "mixins.py#L240",
      typehints: "typehints.py",
      "typehints.ThemeConfigs": "typehints.py#L22",
    },
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
  const _ver = ver?.toLowerCase() === "next" ? "main" : ver;
  const versionDeps = variables.dependencyVersion[_ver];
  return versionDeps ? (
    <Link
      href={`https://github.com/RedHeadphone/react-json-grid/tree/v${versionDeps}`}
    >
      <code>{`react-json-grid@${versionDeps}`}</code>
      <IconExternalLink />
    </Link>
  ) : (
    <InlineIcon icon={biSlashLg} />
  );
};

export const rawURL = (url: string): string => {
  return variables.rawURL + "/" + url;
};

export const repoURL = (url: string | undefined = undefined): string => {
  return url ? variables.repoURL + "/" + url : variables.repoURL;
};

export const releaseURL = (ver: string | undefined = undefined): string => {
  const _ver = ver?.toLowerCase() === "next" ? "main" : ver;
  const version = variables.sourceVersion[_ver] || useCurrentSourceVersion();
  if (version === "main" || _ver === "main") {
    return variables.repoURL + "/releases/latest";
  }
  return variables.repoURL + "/releases/tag/" + version;
};

export const rootURL = (url: string): string => {
  const currentSourceVersion = useCurrentSourceVersion();
  return variables.repoURL + "/blob/" + currentSourceVersion + "/" + url;
};

const getURIByVersionPath = (path: string, ver: string): string => {
  const routes = typeof path === "string" ? path.trim() : "";
  if (routes.length === 0) {
    return path;
  }
  const currentURI = variables.sourceURIs[ver] || variables.sourceURIs["main"];
  return currentURI[path] || path;
};

export const sourceURL = (url: string): string => {
  const currentSourceVersion = useCurrentSourceVersion();
  return (
    variables.repoURL +
    "/blob/" +
    currentSourceVersion +
    "/dash_json_grid/" +
    getURIByVersionPath(url, currentSourceVersion)
  );
};

export const demoURL = (url: string): string => {
  const currentSourceVersion = useCurrentSourceVersion();
  return (
    variables.repoURL + "/blob/" + currentSourceVersion + "/examples/" + url
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
