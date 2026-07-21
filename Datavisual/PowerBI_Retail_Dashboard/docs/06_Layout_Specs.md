# Page Layout Specifications

Canvas: **16:9** (e.g., 1280 × 720). Page background: `#F5F7FA`. Visual fill: `#FFFFFF`. Accent: `#0078D4`. Text: `#252525` / `#505050`.

Use **Align → Distribute** after placing objects. Keep ~8–12 px gaps between visuals.

---

## Page 1 — Executive Dashboard

```
Y≈0–48    HEADER
          [Dynamic Report Title measure]     [Dynamic Date Display]
          [Page Navigator]                   [Reset Filters button]

Y≈52–100  SLICERS (equal width)
          [Year]  [Category]  [Region]

Y≈108–200 KPI CARDS (4 equal columns)
          [Total Sales] [Total Profit] [Total Orders] [Customer Count]

Y≈208–300 KPI VISUALS (2 columns)
          [Sales vs Target]     [Profit vs Target]

Y≈308–500 TREND + CATEGORY (2 columns, ~60/40)
          [Line: Monthly Sales Trend]   [Column: Sales by Category]

Y≈508–700 SEGMENT
          [Donut: Sales by Segment]     [optional: AOV + Margin cards]
```

**Shadow:** subtle (bottom offset 2–4, transparency ~70%).  
**Corners:** 8 px (theme default).

---

## Page 2 — Product Analysis

```
HEADER + synced slicers (same as Page 1)

Row A (~40% height)
  [Table: Product metrics]          [Matrix: Category/Sub × Year]

Row B (~30% height)
  [Bar: Top 10 Products]            [Tree Map: Sales by Category]

Row C (~30% height)
  [Scatter: Sales vs Profit]  [Pie: Payment Mode]  [Funnel: Pipeline]
```

---

## Page 3 — Geographic Dashboard

```
HEADER + synced slicers

Row A (~45% height)
  [Map: Sales by City]              [Filled Map: Sales by State]

Row B (~25% height)
  [Area: Monthly Profit]            [Column: Sales by Region]

Row C (~25% height)
  [Line: Monthly Quantity Sold]     (full width or 2/3 + insight card)
```

---

## Color usage guide

| Element | Color |
|---------|--------|
| Primary bars / lines | `#0078D4` |
| Secondary series | `#505050` |
| Positive / good | `#107C10` |
| Negative / bad | `#D83B01` |
| Page background | `#F5F7FA` |
| Visual background | `#FFFFFF` |
| Borders | `#E1E1E1` |
| Titles | `#252525` |

Avoid extra decorative shapes, excessive icons, or more than one donut/pie per page story.
