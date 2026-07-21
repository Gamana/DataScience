# Interactive Retail Sales Dashboard (Web)

Open this HTML dashboard to explore **all graph visuals** from the Power BI brief, powered by the same 5,200-row retail dataset.

## Open the dashboard

From this folder:

```bash
cd PowerBI_Retail_Dashboard/dashboard
python3 -m http.server 8765
```

Then open: **http://localhost:8765/dashboard.html**

> Loading `dashboard.html` via double-click (`file://`) will fail because the browser blocks fetching `dashboard_data.json`. Always use a local server.

## Pages & visuals

| Page | Visuals |
|------|---------|
| **Executive** | Cards, KPI bars, Line, Column, Donut, Year/Category/Region slicers |
| **Product** | Sortable Table, Matrix, Top 10 Bar, Tree Map, Scatter, Pie, Funnel |
| **Geographic** | City Map (Leaflet), State filled choropleth, Area, Column, Line |

## Features

- Synced slicers across pages (Year, Category, Region)
- Reset Filters button
- Dynamic title and date
- Cross-page navigation
- Corporate blue / gray / white theme

## Files

- `dashboard.html` — UI + charts
- `dashboard_data.json` — aggregated + fact data (regenerate via `../generate_retail_data.py` then re-run the JSON export if you change source data)
