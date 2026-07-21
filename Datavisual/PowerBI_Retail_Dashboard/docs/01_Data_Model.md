# Data Model — Star Schema

## Overview

```
                         ┌─────────────────┐
                         │    Dim_Date     │
                         │  (DateKey) PK   │
                         └────────▲────────┘
                                  │ 1
                                  │
                                  │ *
┌─────────────────┐      ┌────────┴────────┐      ┌─────────────────┐
│  Dim_Customer   │      │   Fact_Sales    │      │   Dim_Product   │
│ (CustomerKey)PK │◄─────│  CustomerKey FK │─────►│ (ProductKey) PK │
└─────────────────┘  1 * │  ProductKey  FK │ *  1 └─────────────────┘
                         │  GeoKey      FK │
                         │  DateKey     FK │
                         │  Sales, Profit… │
                         └────────┬────────┘
                                  │ *
                                  │
                                  │ 1
                         ┌────────▼────────┐
                         │  Dim_Geography  │
                         │   (GeoKey) PK   │
                         └─────────────────┘

  Standalone (no relationship to fact — used for Funnel / Targets):
  • Dim_Sales_Pipeline
  • Dim_Targets  → relate Dim_Targets[Year] to Dim_Date[Year] (Many-to-One)
```

## Tables

| Table | Role | Grain | Rows (approx.) |
|-------|------|-------|----------------|
| **Fact_Sales** | Fact | One row per order line | 5,200 |
| **Dim_Customer** | Dimension | One row per customer | 850 |
| **Dim_Product** | Dimension | One row per product | 32 |
| **Dim_Geography** | Dimension | One row per city | 40 |
| **Dim_Date** | Dimension | One row per calendar day | 1,096 (2022–2024) |
| **Dim_Targets** | Dimension / Bridge | One row per year | 3 |
| **Dim_Sales_Pipeline** | Supporting | Funnel stages | 5 |

## Relationships (Model view)

| From (Many) | To (One) | Cardinality | Cross-filter direction |
|-------------|----------|-------------|------------------------|
| `Fact_Sales[DateKey]` | `Dim_Date[DateKey]` | Many-to-One | Single (Date → Fact) |
| `Fact_Sales[CustomerKey]` | `Dim_Customer[CustomerKey]` | Many-to-One | Single |
| `Fact_Sales[ProductKey]` | `Dim_Product[ProductKey]` | Many-to-One | Single |
| `Fact_Sales[GeoKey]` | `Dim_Geography[GeoKey]` | Many-to-One | Single |
| `Dim_Targets[Year]` | `Dim_Date[Year]` | Many-to-One* | Single |

\*Year is not unique on Dim_Date (many days per year). Prefer:

**Option A (recommended for beginners):** Do **not** relate Targets to Date. Use the DAX measures that filter Targets with `VALUES(Dim_Date[Year])`.

**Option B (advanced):** Create a bridge table `Dim_Year` with unique years, relate both `Dim_Date` and `Dim_Targets` to it.

## Key columns

### Fact_Sales
- Keys: `DateKey`, `CustomerKey`, `ProductKey`, `GeoKey`
- Degenerate dimension: `Order ID`
- Measures (numeric): `Sales`, `Profit`, `Quantity`, `Discount`, `Shipping Cost`
- Attribute on fact: `Payment Mode` (low cardinality — acceptable on fact)

### Dim_Date (mark as Date Table)
- Primary: `DateKey` (YYYYMMDD integer)
- Date column for time intelligence: `Date`
- Useful attributes: `Year`, `Month Name`, `YearMonth`, `Quarter`, `Day Name`
- Sort `Month Name` by `Month`
- Sort `YearMonth` by `YearMonthSort`

### Dim_Geography
- Includes `Latitude` / `Longitude` for Map visuals
- Hierarchy: Country → Region → State → City (create hierarchy in Model view)

### Dim_Product
- Hierarchy: Product Category → Sub Category → Product Name

### Dim_Customer
- Hierarchy optional: Segment → Customer Name

## Why Star Schema?

1. **Simpler DAX** — filters flow from dimensions into the fact.
2. **Better performance** — dimensions are small; fact holds numbers.
3. **Clear teaching story** — one fact, many dimensions.
4. **Reuse** — same Product / Customer dimensions work for future facts (returns, inventory).

## Beginner path (flat file)

If you prefer one table first:

1. Load `Retail_Sales_Flat.csv` only.
2. Build all visuals from that table.
3. Later refactor into star schema using the Excel sheets.

All required columns for the assignment exist on the flat file.
