# Retail Sales Power BI Dashboard — Complete Package

Professional, beginner-friendly **Power BI** teaching project with a realistic retail dataset (5,200 orders), star-schema model, DAX measures, corporate theme, and full build documentation.

> **Note:** `.pbix` files are created inside **Power BI Desktop** (binary format). This package gives you everything needed to build the polished dashboard in under a few hours.

---

## What’s included

```
PowerBI_Retail_Dashboard/
├── README.md                          ← you are here
├── generate_retail_data.py            ← regenerate sample data anytime
├── data/
│   ├── Retail_Sales_Flat.csv          ← single denormalized table (beginner path)
│   ├── Fact_Sales.csv
│   ├── Dim_Customer.csv
│   ├── Dim_Product.csv
│   ├── Dim_Geography.csv
│   ├── Dim_Date.csv
│   ├── Dim_Targets.csv
│   ├── Dim_Sales_Pipeline.csv
│   └── Retail_Sales_StarSchema.xlsx   ← all tables in one workbook (recommended)
├── dax/
│   ├── Essential_Measures.dax         ← copy-paste ready measures
│   └── DAX_Measures.dax               ← extended reference + comments
├── theme/
│   └── Retail_Corporate_Blue.json     ← Power BI theme (blue / gray / white)
└── docs/
    ├── 01_Data_Model.md
    ├── 02_Build_Guide.md              ← step-by-step instructions
    ├── 03_Visual_Explanations.md
    ├── 04_Best_Practices.md
    ├── 05_Future_Enhancements.md
    └── 06_Layout_Specs.md
```

---

## Dataset snapshot

| Metric | Value |
|--------|--------|
| Orders (fact rows) | **5,200** |
| Customers | 850 |
| Products | 32 |
| Cities | 40 (US) |
| Date range | 2022-01-02 → 2024-12-30 |
| Total Sales | ~$3.20M |
| Total Profit | ~$656K |

### Required columns (flat file)

Order ID, Order Date, Ship Date, Customer Name, Customer ID, Product Name, Product Category, Sub Category, Region, Country, State, City, Sales, Profit, Quantity, Discount, Shipping Cost, Payment Mode, Segment

---

## Dashboard pages (build target)

### Page 1 — Executive Dashboard
Cards (Sales, Profit, Orders, Customers) · KPI (Sales/Profit vs Target) · Line (Monthly Sales) · Column (Sales by Category) · Donut (Sales by Segment) · Slicers (Year, Category, Region)

### Page 2 — Product Analysis
Table · Matrix · Bar (Top 10) · Tree Map · Scatter (Sales vs Profit, size Quantity) · Pie (Payment Mode) · Funnel (Lead→Won)

### Page 3 — Geographic Dashboard
Map (City) · Filled Map (State) · Area (Monthly Profit) · Column (Sales by Region) · Line (Monthly Quantity)

---

## Quick start (15 minutes to first chart)

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
2. **Get data** → Excel → `data/Retail_Sales_StarSchema.xlsx` → load all sheets except you may skip the flat sheet.
3. **Model view** → create relationships (see `docs/01_Data_Model.md`).
4. **Mark** `Dim_Date` as date table.
5. **View → Themes → Browse** → `theme/Retail_Corporate_Blue.json`.
6. Create measures from `dax/Essential_Measures.dax`.
7. Follow **`docs/02_Build_Guide.md`** page by page.

**Faster beginner path:** load only `Retail_Sales_Flat.csv`, build visuals first, then refactor to star schema.

---

## DAX measures included

| Measure | Purpose |
|---------|---------|
| Total Sales / Profit / Orders / Quantity | Core KPIs |
| Average Sales / Average Profit | Averages |
| Profit Margin % | Profitability |
| Sales Target / Profit Target | Goals |
| Sales Achievement % / Profit Achievement % | KPI attainment |
| Year-to-Date Sales / Month-to-Date Sales | Time intelligence |
| Previous Month Sales / Sales Growth % | Momentum |
| Customer Count / Average Order Value | Customer analytics |
| Dynamic Report Title / Dynamic Date Display | UX |

---

## Data model (star schema)

```
Dim_Date ──┐
Dim_Customer ──┼── Fact_Sales
Dim_Product ──┤
Dim_Geography ─┘

Dim_Targets          (annual goals; filtered via DAX)
Dim_Sales_Pipeline   (funnel stages)
```

Details: **`docs/01_Data_Model.md`**

---

## Interactions & UX (configured in Desktop)

| Feature | How |
|---------|-----|
| Cross filter / highlight | Format → Edit interactions |
| Sorting | Visual ⋯ → Sort by |
| Drill down | Hierarchies on Matrix / charts |
| Drill through | Drill-through page + field well |
| Report tooltips | Tooltip page type |
| Sync slicers | View → Sync slicers |
| Navigation | Insert → Buttons → Navigator → Page navigator |
| Reset Filters | Bookmark + button action |
| Dynamic title / date | Cards bound to DAX text measures |
| Responsive | View → Mobile layout |

---

## Theme

Corporate palette: **Blue `#0078D4`**, **Dark Gray `#505050`**, **White**, **Light Gray `#F5F7FA`**.  
Import: `theme/Retail_Corporate_Blue.json`.

---

## Documentation map

| Doc | Contents |
|-----|----------|
| [01_Data_Model.md](docs/01_Data_Model.md) | Relationships, keys, hierarchies |
| [02_Build_Guide.md](docs/02_Build_Guide.md) | End-to-end build steps |
| [03_Visual_Explanations.md](docs/03_Visual_Explanations.md) | Why each visual |
| [04_Best_Practices.md](docs/04_Best_Practices.md) | Industry practices used |
| [05_Future_Enhancements.md](docs/05_Future_Enhancements.md) | Next-level ideas |
| [06_Layout_Specs.md](docs/06_Layout_Specs.md) | Wireframes & spacing |

---

## Regenerate data

```bash
cd PowerBI_Retail_Dashboard
python3 generate_retail_data.py
```

Requires: `pandas`, `numpy`, `openpyxl`.

---

## Deliverables checklist

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Dashboard layout | `docs/06_Layout_Specs.md` + Build Guide |
| 2 | Sample dataset | `data/` (CSV + Excel) |
| 3 | DAX measures | `dax/` |
| 4 | Data model | `docs/01_Data_Model.md` |
| 5 | Step-by-step instructions | `docs/02_Build_Guide.md` |
| 6 | Visual explanations | `docs/03_Visual_Explanations.md` |
| 7 | Best practices | `docs/04_Best_Practices.md` |
| 8 | Future enhancements | `docs/05_Future_Enhancements.md` |

All required Power BI visual types are covered across the three pages (see visual explanations doc).
