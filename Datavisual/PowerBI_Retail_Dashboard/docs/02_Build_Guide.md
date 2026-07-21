# Step-by-Step: Build the Retail Sales Power BI Dashboard

**Estimated time:** 2–3 hours for beginners  
**Prerequisites:** Power BI Desktop (free) installed  
**Files:** `data/Retail_Sales_StarSchema.xlsx` + `theme/Retail_Corporate_Blue.json` + `dax/DAX_Measures.dax`

---

## Phase 0 — Project setup

1. Open **Power BI Desktop**.
2. **File → Options and settings → Options → Report settings** → enable modern visual tooltips if available.
3. **View → Themes → Browse for themes** → select `theme/Retail_Corporate_Blue.json`.
4. Set report page size: **Desktop** (16:9) on each page (Format page → Canvas settings).

---

## Phase 1 — Get data (star schema)

1. **Home → Get data → Excel workbook** → `Retail_Sales_StarSchema.xlsx`.
2. Select sheets:
   - `Fact_Sales`
   - `Dim_Product`
   - `Dim_Customer`
   - `Dim_Geography`
   - `Dim_Date`
   - `Dim_Targets`
   - `Dim_Sales_Pipeline`
3. Click **Transform Data** (Power Query).

### Power Query cleanup (best practice)

| Table | Steps |
|-------|--------|
| Fact_Sales | Set types: dates for Order/Ship Date; Decimal for Sales, Profit, Discount, Shipping Cost; Whole for Quantity & keys |
| Dim_Date | Type `Date` as Date; `DateKey` as Whole Number; `Is Weekend` as True/False |
| Dim_Geography | Latitude / Longitude as Decimal Number |
| All tables | **Close & Apply** |

Optional: rename `Product Category` display name if desired — keep column names consistent with DAX.

---

## Phase 2 — Build the model

1. Open **Model** view.
2. Create relationships (drag from Fact to Dim):

| Fact column | Dimension column |
|-------------|------------------|
| `Fact_Sales[DateKey]` | `Dim_Date[DateKey]` |
| `Fact_Sales[CustomerKey]` | `Dim_Customer[CustomerKey]` |
| `Fact_Sales[ProductKey]` | `Dim_Product[ProductKey]` |
| `Fact_Sales[GeoKey]` | `Dim_Geography[GeoKey]` |

3. Cardinality: **Many to One (\*:1)**. Cross-filter: **Single**.
4. Select `Dim_Date` → **Table tools → Mark as date table** → choose `Date`.
5. Create hierarchies:
   - Product: Category → Sub Category → Product Name
   - Geography: Country → Region → State → City
6. Sort columns:
   - `Dim_Date[Month Name]` sorted by `Month`
   - `Dim_Date[Day Name]` sorted by day number (add DayOfWeek if needed, or use Day Name + custom sort)
7. Hide key columns from Report view (`DateKey`, `CustomerKey`, `ProductKey`, `GeoKey`) — right-click → **Hide in report view**.
8. Create blank **Enter data** table named `_Measures` (one dummy column). Hide the column.

---

## Phase 3 — Create DAX measures

1. Select `_Measures` → **New measure**.
2. Copy each measure from `dax/DAX_Measures.dax` (create them one by one).
3. Format measures:
   - Currency: Total Sales, Total Profit, Average Sales, Average Profit, Average Order Value, Sales Target, Profit Target, YTD/MTD/Previous Month Sales
   - Percentage: Profit Margin %, Sales Achievement %, Profit Achievement %, Sales Growth %
   - Whole number: Total Orders, Total Quantity, Customer Count

**Minimum set required by the brief:**

`Total Sales`, `Total Profit`, `Total Orders`, `Total Quantity`, `Average Sales`, `Average Profit`, `Profit Margin %`, `Sales Target`, `Profit Target`, `Sales Achievement %`, `Profit Achievement %`, `Year-to-Date Sales`, `Month-to-Date Sales`, `Previous Month Sales`, `Sales Growth %`, `Customer Count`, `Average Order Value`

Also create: `Dynamic Report Title`, `Dynamic Date Display` for UX.

---

## Phase 4 — Page 1: Executive Dashboard

1. Rename Page 1 to **Executive Dashboard**.
2. Page background: theme light gray (`#F5F7FA`); keep visual backgrounds white.

### Layout (approximate grid on 1280×720)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ [Logo/Title: Dynamic Report Title]              [Dynamic Date Display]   │
│ [NAV: Executive | Product | Geographic]  [Reset Filters]                 │
├──────────┬──────────┬──────────┬──────────┬─────────────┬────────────────┤
│ Year     │ Category │ Region   │          │             │                │
│ Slicer   │ Slicer   │ Slicer   │          │             │                │
├──────────┴──────────┴──────────┼──────────┼─────────────┼────────────────┤
│ Card: Total Sales              │ Card: Total Profit │ Card: Orders │ Card: Customers │
├────────────────────────────────┼────────────────────┴──────────────┴────────────────┤
│ KPI: Sales vs Target           │ KPI: Profit vs Target                               │
├────────────────────────────────┴─────────────────────────────────────────────────────┤
│ Line: Monthly Sales Trend              │ Column: Sales by Category                   │
├────────────────────────────────────────┼─────────────────────────────────────────────┤
│ Donut: Sales by Segment                │ (optional spacer / AOV card)                │
└────────────────────────────────────────┴─────────────────────────────────────────────┘
```

### Build each visual

| Visual | Fields / Measures | Format tips |
|--------|-------------------|-------------|
| **Card – Total Sales** | `[Total Sales]` | Title: Total Sales; category label off or custom |
| **Card – Total Profit** | `[Total Profit]` | Same |
| **Card – Total Orders** | `[Total Orders]` | Same |
| **Card – Total Customers** | `[Customer Count]` | Same |
| **KPI – Sales vs Target** | Indicator: `[Total Sales]` · Target goals: `[Sales Target]` | Status: green if ≥ target |
| **KPI – Profit vs Target** | Indicator: `[Total Profit]` · Target: `[Profit Target]` | Same |
| **Line – Monthly Sales Trend** | Axis: `Dim_Date[YearMonth]` (or Month Name + Year) · Values: `[Total Sales]` | Markers on; data labels optional |
| **Column – Sales by Category** | Axis: `Dim_Product[Product Category]` · Values: `[Total Sales]` | Data labels on |
| **Donut – Sales by Segment** | Legend: `Dim_Customer[Segment]` · Values: `[Total Sales]` | % of total labels |
| **Slicer – Year** | `Dim_Date[Year]` | Dropdown or tile |
| **Slicer – Category** | `Dim_Product[Product Category]` | Dropdown |
| **Slicer – Region** | `Dim_Geography[Region]` | Dropdown |

### Cards for dynamic text

- Insert **Card** with `[Dynamic Report Title]` (large font) — or use **Text box** + measure via **Value** field (Card is simpler for beginners).
- Card with `[Dynamic Date Display]`.

---

## Phase 5 — Page 2: Product Analysis

Rename page to **Product Analysis**. Duplicate slicers from Page 1 (Year, Category, Region) — you will sync them later.

| Visual | Configuration |
|--------|----------------|
| **Table** | Product Name, Category (`Product Category`), Quantity (`[Total Quantity]` or sum), Sales (`[Total Sales]`), Profit (`[Total Profit]`) |
| **Matrix** | Rows: Category, Sub Category · Columns: Year · Values: Sales, Profit |
| **Bar chart** | Y: Product Name · X: `[Total Sales]` · **Filters on this visual**: Top N = 10 by Total Sales |
| **Tree map** | Group: Product Category · Values: `[Total Sales]` |
| **Scatter** | X: `[Total Sales]` · Y: `[Total Profit]` · Size: `[Total Quantity]` · Details: Product Name (or Category) |
| **Pie** | Legend: `Payment Mode` · Values: `[Total Sales]` |
| **Funnel** | Category: `Dim_Sales_Pipeline[Stage]` · Values: `Pipeline Value` (or column Pipeline Value) · Sort by Stage Order |

**Matrix tip:** Turn on **Stepped layout** off for classic expand/collapse; enable **+/- icons** for drill.

**Scatter tip:** If one bubble dominates, format X/Y as currency and use categorical details at Product level.

---

## Phase 6 — Page 3: Geographic Dashboard

Rename page to **Geographic Dashboard**.

| Visual | Configuration |
|--------|----------------|
| **Map** | Location: `City` · Size: `[Total Sales]` · (optional Latitude/Longitude fields for accuracy) |
| **Filled Map** | Location: `State` · Color saturation: `[Total Sales]` |
| **Area chart** | Axis: YearMonth · Values: `[Total Profit]` |
| **Column chart** | Axis: Region · Values: `[Total Sales]` |
| **Line chart** | Axis: YearMonth · Values: `[Total Quantity]` |

**Map tips:**
- Set Country = United States in filter if ambiguous city names appear.
- Use Lat/Long from `Dim_Geography` on the Map visual for precise pins.

---

## Phase 7 — Interactions, drill, tooltips, sync

### Cross-filter / highlight

1. **Format → Edit interactions**.
2. For each slicer/chart, set others to **Filter** (default) or **Highlight** where you want emphasis (e.g., Category column chart → Highlight the donut).
3. Leave Map → Table as Filter for clarity.

### Sorting

- On every visual: **More options (⋯) → Sort by** the primary measure or category. Verify Top 10 bar is sorted descending by Sales.

### Drill down

- Enable on Matrix (Category → Sub Category).
- On Column/Line with date hierarchy: turn on **Drill down** / **Expand all**.

### Drill through

1. Create a hidden or visible page: **Order Details** (or reuse Product Analysis).
2. Drag `Product Name` (or Category) into **Drill through** filter well.
3. Keep back button auto-created.
4. On Executive visuals: right-click a data point → **Drill through → Product Analysis**.

### Report tooltips

1. Create page **Tooltip – Product** (Page type: **Tooltip**, size small).
2. Add cards: Sales, Profit, Margin %, Quantity for the hovered product.
3. On Scatter / Bar / Tree map → Format → Tooltip → **Report page** → select Tooltip page.

### Sync slicers

1. **View → Sync slicers**.
2. For Year, Category, Region slicers on all three pages:
   - Sync: ✓ on Executive, Product, Geographic
   - Visible: ✓ on all (or hide duplicates and keep one page’s slicers only — beginners usually keep visible copies synced)

---

## Phase 8 — Navigation, bookmarks, UX

### Navigation buttons

1. **Insert → Buttons → Blank** (or Navigator → Page navigator).
2. Easiest: **Insert → Buttons → Navigator → Page navigator** — auto links all pages.
3. Style: blue fill `#0078D4`, white text, rounded corners.

### Reset Filters bookmark

1. Clear all filters/slicers on Executive page.
2. **View → Bookmarks → Add** → name `Reset Filters`.
3. **Insert → Button** → Action: **Bookmark** → `Reset Filters`.
4. Update bookmark when layout is final (**Update**).
5. Optional: create one Reset bookmark **per page**, or one bookmark that applies to all pages (uncheck “Display” and check data).

### Selection pane

- Name every visual meaningfully (`Card_TotalSales`, `Slicer_Year`, …) for teaching and bookmarks.

### Responsive layout

- **View → Mobile layout** — arrange key cards and one trend chart for phone view on Executive page.

---

## Phase 9 — Polish & publish

1. Align visuals (Align → Distribute horizontally/vertically).
2. Consistent title case; turn **on** data labels where sparse charts need them; **off** when cluttered (dense line charts).
3. Add shadow lightly: Format visual → Effects → Shadow → Offset small, transparency high.
4. Rounded corners: already in theme; verify per visual.
5. **File → Save** as `Retail_Sales_Dashboard.pbix`.
6. Optional: **Publish** to Power BI Service for sharing.

---

## Quick verification checklist

- [ ] ≥ 5,000 rows loaded  
- [ ] Star schema relationships active  
- [ ] All 17+ required measures work with Year slicer  
- [ ] Three pages named correctly  
- [ ] All listed visual types present  
- [ ] Sync slicers work across pages  
- [ ] Reset bookmark clears filters  
- [ ] Page navigator works  
- [ ] Drill through + tooltip page work  
- [ ] Theme applied (blue / gray / white)  
