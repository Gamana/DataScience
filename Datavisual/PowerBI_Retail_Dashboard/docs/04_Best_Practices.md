# Best Practices Followed

## 1. Data modeling

| Practice | How we applied it |
|----------|-------------------|
| **Star schema** | One fact (`Fact_Sales`) + conformed dimensions |
| **Surrogate keys** | `CustomerKey`, `ProductKey`, `GeoKey`, `DateKey` |
| **Date table** | Continuous `Dim_Date` marked as date table for time intelligence |
| **Hide technical keys** | Keys hidden in Report view |
| **Hierarchies** | Product and Geography drill paths |
| **Sort by columns** | Month names sorted chronologically |

## 2. DAX

| Practice | How we applied it |
|----------|-------------------|
| **Explicit measures** | All KPIs as named measures in `_Measures` |
| **DIVIDE()** | Safe division for margins and growth |
| **Time intelligence** | `TOTALYTD`, `TOTALMTD`, `DATEADD` on the date table |
| **Reusable logic** | Achievement % built on Total / Target measures |
| **No overly complex single measures** | Broken into readable building blocks |

## 3. Report design

| Practice | How we applied it |
|----------|-------------------|
| **Z-pattern / F-pattern** | Cards top → trends middle → breakdowns bottom |
| **One story per page** | Executive / Product / Geography |
| **Consistent theme** | Blue, dark gray, white, light gray |
| **White visual canvases** on light page background | Reduces clutter, improves print/PDF |
| **Titles on every visual** | Business language, not field names |
| **Spacing & alignment** | Grid alignment; equal gaps |
| **Limited colors** | Theme palette; avoid rainbow charts |
| **Donut/Pie only for few categories** | Segment (3), Payment Mode (5) |

## 4. Interactivity

| Practice | How we applied it |
|----------|-------------------|
| **Sync slicers** | Year / Category / Region across pages |
| **Edit interactions** | Intentional Filter vs Highlight |
| **Drill through** | From summary → product detail |
| **Report tooltips** | Rich hover without leaving the page |
| **Bookmarks** | Reset Filters for UX confidence |
| **Page navigator** | Clear multi-page navigation |

## 5. Teaching / beginner-friendly choices

| Practice | Rationale |
|----------|-----------|
| Flat CSV **and** star schema Excel | Learn visuals first, then model |
| Realistic US geography | Maps work without custom shape files |
| 5,200 rows | Feels real but stays fast on laptops |
| Documented DAX file | Copy-paste learning path |
| Funnel as separate small table | Shows visuals that need different grains |

## 6. Performance habits (even on small data)

- Prefer measures over calculated columns for aggregations.
- Avoid bi-directional filters unless necessary.
- Keep text columns in dimensions, not duplicated unnecessarily on the fact (keys + Payment Mode only).
- Use Top N at the visual level for Top 10 charts.

## 7. Accessibility & clarity

- High-contrast text (`#252525` on white).
- Data labels where they aid reading; off when they collide.
- Legends visible for multi-series charts.
- Meaningful bookmark and visual names in Selection pane.
