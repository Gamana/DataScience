# Explanation of Every Visual Used

This guide explains **what each visual is for**, **how to read it**, and **why it belongs on that page** — written for beginners learning Power BI.

---

## Page 1 — Executive Dashboard

### Card — Total Sales / Total Profit / Total Orders / Total Customers

| Aspect | Detail |
|--------|--------|
| **What it is** | A single KPI number, often with a small label |
| **Business question** | “How are we doing overall right now?” |
| **Why cards** | Executives scan big numbers first; cards reduce cognitive load |
| **Interaction** | Cards update when slicers (Year, Category, Region) change |
| **Teaching tip** | Always use **measures**, not raw columns dragged as Implicit measures, so formatting and time intelligence stay consistent |

### KPI — Sales vs Target / Profit vs Target

| Aspect | Detail |
|--------|--------|
| **What it is** | Shows actual vs goal with a status bar and variance |
| **Business question** | “Are we on track against the plan?” |
| **Fields** | Indicator = actual measure; Target goals = target measure |
| **Why not just a card** | Cards show absolute value; KPIs encode **goal attainment** |
| **Teaching tip** | Targets live in `Dim_Targets`; achievement % measures explain the math behind the visual |

### Line Chart — Monthly Sales Trend

| Aspect | Detail |
|--------|--------|
| **What it is** | Continuous trend over time |
| **Business question** | “Is sales improving, flat, or declining?” |
| **Why line** | Best for time series; eye tracks slope and seasonality (e.g., Q4 peaks) |
| **Axis** | `YearMonth` (sorted by `YearMonthSort`) |
| **Interaction** | Click a month to filter other visuals to that period |

### Column Chart — Sales by Category

| Aspect | Detail |
|--------|--------|
| **What it is** | Vertical bars comparing categories |
| **Business question** | “Which product categories drive revenue?” |
| **Why column** | Ideal for few categories (Furniture, Technology, Office Supplies) |
| **Drill** | Use Product hierarchy to drill into Sub Category |

### Donut Chart — Sales by Segment

| Aspect | Detail |
|--------|--------|
| **What it is** | Part-to-whole composition with a hollow center |
| **Business question** | “How is revenue split across Consumer / Corporate / Home Office?” |
| **Why donut vs pie** | Center can hold a total card or looks cleaner in modern dashboards |
| **Caution** | Use only for **few** slices (here: 3 segments) |

### Slicers — Year / Category / Region

| Aspect | Detail |
|--------|--------|
| **What it is** | User-driven filters |
| **Business question** | “Let me focus the whole page on my slice of the business” |
| **Sync** | Sync across pages so filters persist while navigating |
| **Teaching tip** | Prefer dimension columns (`Dim_Date[Year]`) over fact columns for star-schema clarity |

---

## Page 2 — Product Analysis

### Table — Product detail

| Aspect | Detail |
|--------|--------|
| **What it is** | Row-level (or product-level) grid |
| **Shows** | Product Name, Category, Quantity, Sales, Profit |
| **Business question** | “Show me exact numbers I can scan or export” |
| **Why table** | Precision; supports sorting every column |
| **Tip** | Conditional formatting on Profit (red/green) teaches formatting without cluttering charts |

### Matrix — Category × Year

| Aspect | Detail |
|--------|--------|
| **What it is** | Pivot-table style visual |
| **Rows** | Category → Sub Category |
| **Columns** | Year |
| **Values** | Sales, Profit |
| **Business question** | “How did each sub-category perform each year?” |
| **Drill** | Expand/collapse hierarchy — core Power BI skill |

### Bar Chart — Top 10 Products by Sales

| Aspect | Detail |
|--------|--------|
| **What it is** | Horizontal bars |
| **Why bar (not column)** | Long product names remain readable |
| **Filter** | Top N = 10 by Total Sales |
| **Business question** | “What are our bestsellers?” |

### Tree Map — Sales by Category

| Aspect | Detail |
|--------|--------|
| **What it is** | Nested rectangles sized by measure |
| **Business question** | “Where is the bulk of sales concentrated?” |
| **Strength** | Instant hierarchy perception (Category space share) |
| **Limit** | Harder to compare close values than a bar chart |

### Scatter Chart — Sales vs Profit (size = Quantity)

| Aspect | Detail |
|--------|--------|
| **What it is** | Correlation / outlier plot |
| **X** | Sales · **Y** | Profit · **Size** | Quantity |
| **Business question** | “Which products sell a lot but earn little (or lose money)?” |
| **Teaching tip** | Look for high Sales + low Profit bubbles = margin problems |

### Pie Chart — Sales by Payment Mode

| Aspect | Detail |
|--------|--------|
| **What it is** | Part-to-whole for payment mix |
| **Business question** | “How do customers pay?” |
| **When to use** | ≤ 5–6 categories (Credit Card, Debit, Cash, Online, UPI) |

### Funnel Chart — Sales Pipeline

| Aspect | Detail |
|--------|--------|
| **What it is** | Stage-by-stage conversion shape |
| **Stages** | Lead → Qualified → Proposal → Negotiation → Won |
| **Data** | `Dim_Sales_Pipeline` (teaching dataset for funnel shape) |
| **Business question** | “Where do opportunities drop off?” |
| **Note** | Pipeline is illustrative here; in production it would come from CRM |

---

## Page 3 — Geographic Dashboard

### Map — Sales by City

| Aspect | Detail |
|--------|--------|
| **What it is** | Bubble/point map |
| **Location** | City (+ Lat/Long for accuracy) |
| **Size** | Total Sales |
| **Business question** | “Which cities are revenue hotspots?” |
| **Tip** | Ambiguous city names → supply Country or coordinates |

### Filled Map — Sales by State

| Aspect | Detail |
|--------|--------|
| **What it is** | Choropleth (regions shaded by value) |
| **Location** | State |
| **Color saturation** | Total Sales |
| **Business question** | “Which states lead or lag?” |
| **Contrast with Map** | Filled Map = area comparison; Map = city-level points |

### Area Chart — Monthly Profit

| Aspect | Detail |
|--------|--------|
| **What it is** | Line chart with filled area under the curve |
| **Business question** | “How does profit accumulate/trend month to month?” |
| **Why area** | Emphasizes magnitude over time; good for a single series |

### Column Chart — Sales by Region

| Aspect | Detail |
|--------|--------|
| **What it is** | Regional comparison |
| **Business question** | “East vs West vs Central vs South?” |
| **Pairs with** | Map visuals for geo storytelling |

### Line Chart — Monthly Quantity Sold

| Aspect | Detail |
|--------|--------|
| **What it is** | Units trend (not dollars) |
| **Business question** | “Are we moving more volume even if revenue is flat?” |
| **Teaching tip** | Separating **Sales** vs **Quantity** avoids false conclusions when prices change |

---

## Visual type coverage checklist

| Required visual | Where used |
|-----------------|------------|
| Table | Page 2 |
| Matrix | Page 2 |
| Card | Page 1 |
| KPI | Page 1 |
| Slicer | Page 1–3 |
| Bar Chart | Page 2 |
| Column Chart | Page 1 & 3 |
| Line Chart | Page 1 & 3 |
| Pie Chart | Page 2 |
| Donut Chart | Page 1 |
| Area Chart | Page 3 |
| Scatter Chart | Page 2 |
| Tree Map | Page 2 |
| Funnel Chart | Page 2 |
| Map | Page 3 |
| Filled Map | Page 3 |
