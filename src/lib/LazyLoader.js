import React from "react";

export const DashJsonGrid = React.lazy(() =>
  import(
    /* webpackChunkName: "DashJsonGrid" */ "./fragments/DashJsonGrid.react"
  )
);
