# Dash JSON Grid

[toc]

## CHANGELOG

### 0.5.0 @ 11/30/2024

#### :wrench: Fix

1. Fix: Add more translations for the new docusaurus version `3.6.3`.
2. Fix: Add the broken link `dash-pmcallback` for the page `/docs/apis/DashJsonGrid`.
3. Fix: Add the missing translation for the table head in `/docs/install`.
4. Fix: Correct the punctuations in the page `/docs/apis/DashJsonGrid`.
5. Fix: Correct the icons in the page `/docs/apis/DashJsonGrid`.

### 0.5.0 @ 11/29/2024

#### :wrench: Fix

1. Fix: Correct the version numbers of the legacy document `v0.4.x`.
2. Fix: Add the missing explanations for the new optional dependency collection `example`.
3. Fix: The component `IconLink` should be replaced by `IconLinkInline` in `/docs/install`.

### 0.5.0 @ 11/27/2024

#### :mega: New

1. Add the new article `/docs/examples/editor`.

#### :wrench: Fix

1. Fix: Switch from the hook `useDocsPreferredVersion` to `useDocsVersion`. This change fix the issue caused on the change of the browser navigation.

#### :floppy_disk: Change

1. Upgrade to the new version `0.5.0`.
2. Bump the `yarn` version from `4.5.2` to `4.5.3`.
3. Bump the `docusaurus` version from `3.6.1` to `3.6.3`.
4. Bump the `typescript` version from `5.6.3` to `5.7.2`.

### 0.4.3 @ 11/22/2024

#### :floppy_disk: Change

1. Upgrade to the new version `0.4.3`.
2. Bump the `yarn` version from `4.5.1` to `4.5.2`.

### 0.4.2 @ 11/13/2024

#### :mega: New

1. Add explanations of using `default_expand_key_tree` in `docs/usages/data`.

#### :wrench: Fix

1. Fix: Fix a not translated text in the `zh-cn` doc: `docs/usages/data`.
2. Fix: Attempt to make the GitPage correctly redirect to the 404 pages for specific localizations.

#### :floppy_disk: Change

1. Bump the core dependencies to the newest version.
2. Upgrade to the new version `0.4.2`.
3. Docusaurus does not work well with multi-resolution icons. Make the favicon single-resolution.

### 0.4.1 @ 10/30/2024

#### :wrench: Fix

1. Fix: Correct small typos in `docs/apis/typehints/ThemeConfigs`.
2. Fix: `zh-cn` document cannot handle the line break correctly. Remove the unexpected line breaks.

#### :floppy_disk: Change

1. Migrate the version control of the source references to the newest version.
2. Change some links to the Chinese version for `zh-cn` docs.

### 0.4.1 @ 10/22/2024

#### :mega: New

1. Upgrade to the new version `0.4.1`.

#### :wrench: Fix

1. Fix: Synchronize the code references to the newest version.

#### :floppy_disk: Change

1. Exempt the old documents from the search list.

### 0.4.0 @ 10/22/2024

#### :mega: New

1. Upgrade to the new version `0.4.0`.
2. Add translations to the new version `0.4.0`.
3. Add translations related to the new versioning features.

#### :wrench: Fix

1. Fix: Correct a mistake of the HTML usage in the localized version `zh-cn/docs/license`.
2. Fix: Roll back the path of the current version to `/`. This change ensure that the previous pages will not be gone.
3. Fix: Correct a typo in the examples of `docs/apis/DashJsonGrid`.

#### :floppy_disk: Change

1. For the legacy doc `0.3.x`, make the guides related to the installation specified to the corresponding version.
2. Adjust the examples of `docs/apis/DashJsonGrid`.

### 0.3.4 @ 10/20/2024

#### :wrench: Fix

1. Fix: Correct some translation mistakes in the `zh-cn` doc of `docs/apis/DashJsonGrid`.

#### :floppy_disk: Change

1. Update the document to synchronize the `dash-json-grid==0.3.4`.

### 0.3.3 @ 10/20/2024

#### :mega: New

1. Add the zh-cn translation of the whole document.

#### :wrench: Fix

1. Fix: Correct the typos and ambiguous descriptions throughout the whole document.

#### :floppy_disk: Change

1. Modify the format of the license from `.md` to `.mdx`.
2. Add more keywords in `src/demo` to the translation list.
3. Adjust the style of buttons with icons. Move the icons to the left side by `1ex`.

### 0.3.3 @ 10/18/2024

#### :wrench: Fix

1. Fix: The customized `ThemedComponent` may not be suitable for rendering `<svg>` files because it only raises issues in the production build. Try to fall back to the docusaurus `ThemedImage`.

#### :floppy_disk: Change

1. Make the translation configuration totally prepared for starting the translation in the future.

### 0.3.3 @ 10/17/2024

#### :wrench: Fix

1. Fix: Correct a typo in the footer external links.
2. Fix: Correct a typo in code display: `/docs/usages/data`.
3. Fix: Rows rendered by `react-json-grid` in this document should not be styled by the colors of Docusaurus.
4. Fix: Add a one-time hook to the demo apps to ensure that they will be updated by the site theme if necessary.
5. Fix: Change the implementation of `ThemedComponent` to ensure that the dark theme can be applied correctly.

#### :floppy_disk: Change

1. Upgrade the demo version of `react-json-grid` to `0.9.2`.
2. Adjust terminlogies in some documents.
3. Make the style of the table rendered by `react-json-grid` improved to the preview of the next version.
4. Optimize the details of mermaid `<svg>` files and remove overheads.

### 0.3.3 @ 10/16/2024

#### :floppy_disk: Change

1. Update the document to synchronize the `dash-json-grid==0.3.3`.
2. Adjust the terminologies in `/docs/usages/search-and-select`.
3. Make the screenshots on the `/docs` page turn dark in the dark mode.

### 0.3.2 @ 10/16/2024

#### :mega: New

1. Create this project.
2. Upload the first version of the document, containing the tutorial and API docs.

#### :wrench: Fix

1. Correct a link in `/docs/examples`.
2. Correct another broken link in `/docs/examples`.
