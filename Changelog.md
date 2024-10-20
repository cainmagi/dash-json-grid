# Dash JSON Grid

[toc]

## CHANGELOG

### 0.3.4 @ 10/20/2024

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
