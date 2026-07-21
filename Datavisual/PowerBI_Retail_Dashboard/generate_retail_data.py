"""
Generate a realistic Retail Sales dataset (5,000+ rows) in star-schema form
for Power BI dashboard training.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_ORDERS = 5200
OUTPUT_DIR = Path(__file__).parent / "data"

random.seed(SEED)
np.random.seed(SEED)

# ---------------------------------------------------------------------------
# Dimension: Product
# ---------------------------------------------------------------------------
PRODUCT_CATALOG = [
    # Furniture
    ("Office Chair Ergonomic", "Furniture", "Chairs", 249.99, 0.28),
    ("Executive Desk Oak", "Furniture", "Tables", 599.00, 0.32),
    ("Conference Table 8-Seat", "Furniture", "Tables", 1299.00, 0.25),
    ("Bookshelf 5-Tier", "Furniture", "Bookcases", 189.99, 0.30),
    ("Filing Cabinet Metal", "Furniture", "Storage", 159.99, 0.27),
    ("Sofa Sectional Gray", "Furniture", "Furnishings", 899.00, 0.22),
    ("Standing Desk Adjustable", "Furniture", "Tables", 449.00, 0.35),
    ("Guest Chair Mesh", "Furniture", "Chairs", 129.99, 0.26),
    # Technology
    ("Laptop Pro 15-inch", "Technology", "Computers", 1299.00, 0.18),
    ("Wireless Mouse Ergonomic", "Technology", "Accessories", 29.99, 0.42),
    ("USB-C Hub 7-in-1", "Technology", "Accessories", 49.99, 0.38),
    ("Monitor 27-inch 4K", "Technology", "Computers", 449.00, 0.20),
    ("Mechanical Keyboard RGB", "Technology", "Accessories", 89.99, 0.35),
    ("Smartphone Case Premium", "Technology", "Phones", 24.99, 0.50),
    ("Webcam HD 1080p", "Technology", "Accessories", 79.99, 0.33),
    ("Tablet 10-inch", "Technology", "Computers", 399.00, 0.22),
    ("Bluetooth Headphones", "Technology", "Accessories", 149.99, 0.28),
    ("External SSD 1TB", "Technology", "Accessories", 119.99, 0.30),
    # Office Supplies
    ("Printer Paper A4 Ream", "Office Supplies", "Paper", 8.99, 0.45),
    ("Ballpoint Pens Pack 12", "Office Supplies", "Art", 6.49, 0.48),
    ("Stapler Heavy Duty", "Office Supplies", "Fasteners", 14.99, 0.40),
    ("Binders Pack of 5", "Office Supplies", "Binders", 12.99, 0.42),
    ("Sticky Notes Assorted", "Office Supplies", "Labels", 5.99, 0.50),
    ("Whiteboard Markers Set", "Office Supplies", "Art", 9.99, 0.44),
    ("Desk Organizer Bamboo", "Office Supplies", "Storage", 34.99, 0.36),
    ("Envelopes Box 100", "Office Supplies", "Envelopes", 11.99, 0.41),
    ("Toner Cartridge Black", "Office Supplies", "Appliances", 69.99, 0.25),
    ("Scissors Titanium", "Office Supplies", "Fasteners", 12.49, 0.38),
    # Furniture extras
    ("Lounge Chair Leather", "Furniture", "Chairs", 749.00, 0.24),
    ("Coffee Table Glass", "Furniture", "Tables", 279.00, 0.29),
    # Technology extras
    ("Smart Watch Series X", "Technology", "Phones", 299.00, 0.21),
    ("Wireless Charger Pad", "Technology", "Accessories", 39.99, 0.40),
]

# ---------------------------------------------------------------------------
# Dimension: Geography (US-focused for filled maps)
# ---------------------------------------------------------------------------
GEOGRAPHY = [
    # Region, Country, State, City, Lat, Lon
    ("East", "United States", "New York", "New York City", 40.7128, -74.0060),
    ("East", "United States", "New York", "Buffalo", 42.8864, -78.8784),
    ("East", "United States", "Massachusetts", "Boston", 42.3601, -71.0589),
    ("East", "United States", "Pennsylvania", "Philadelphia", 39.9526, -75.1652),
    ("East", "United States", "Pennsylvania", "Pittsburgh", 40.4406, -79.9959),
    ("East", "United States", "New Jersey", "Newark", 40.7357, -74.1724),
    ("East", "United States", "Maryland", "Baltimore", 39.2904, -76.6122),
    ("East", "United States", "Virginia", "Richmond", 37.5407, -77.4360),
    ("East", "United States", "Florida", "Miami", 25.7617, -80.1918),
    ("East", "United States", "Florida", "Orlando", 28.5383, -81.3792),
    ("East", "United States", "Georgia", "Atlanta", 33.7490, -84.3880),
    ("East", "United States", "North Carolina", "Charlotte", 35.2271, -80.8431),
    ("Central", "United States", "Illinois", "Chicago", 41.8781, -87.6298),
    ("Central", "United States", "Illinois", "Springfield", 39.7817, -89.6501),
    ("Central", "United States", "Texas", "Houston", 29.7604, -95.3698),
    ("Central", "United States", "Texas", "Dallas", 32.7767, -96.7970),
    ("Central", "United States", "Texas", "Austin", 30.2672, -97.7431),
    ("Central", "United States", "Ohio", "Columbus", 39.9612, -82.9988),
    ("Central", "United States", "Ohio", "Cleveland", 41.4993, -81.6944),
    ("Central", "United States", "Michigan", "Detroit", 42.3314, -83.0458),
    ("Central", "United States", "Minnesota", "Minneapolis", 44.9778, -93.2650),
    ("Central", "United States", "Missouri", "Kansas City", 39.0997, -94.5786),
    ("Central", "United States", "Wisconsin", "Milwaukee", 43.0389, -87.9065),
    ("Central", "United States", "Indiana", "Indianapolis", 39.7684, -86.1581),
    ("West", "United States", "California", "Los Angeles", 34.0522, -118.2437),
    ("West", "United States", "California", "San Francisco", 37.7749, -122.4194),
    ("West", "United States", "California", "San Diego", 32.7157, -117.1611),
    ("West", "United States", "California", "Sacramento", 38.5816, -121.4944),
    ("West", "United States", "Washington", "Seattle", 47.6062, -122.3321),
    ("West", "United States", "Oregon", "Portland", 45.5152, -122.6784),
    ("West", "United States", "Colorado", "Denver", 39.7392, -104.9903),
    ("West", "United States", "Arizona", "Phoenix", 33.4484, -112.0740),
    ("West", "United States", "Nevada", "Las Vegas", 36.1699, -115.1398),
    ("West", "United States", "Utah", "Salt Lake City", 40.7608, -111.8910),
    ("South", "United States", "Tennessee", "Nashville", 36.1627, -86.7816),
    ("South", "United States", "Louisiana", "New Orleans", 29.9511, -90.0715),
    ("South", "United States", "Alabama", "Birmingham", 33.5207, -86.8025),
    ("South", "United States", "South Carolina", "Charleston", 32.7765, -79.9311),
    ("South", "United States", "Kentucky", "Louisville", 38.2527, -85.7585),
    ("South", "United States", "Oklahoma", "Oklahoma City", 35.4676, -97.5164),
]

FIRST_NAMES = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
    "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Lisa", "Daniel", "Nancy",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Timothy", "Deborah", "Ronald", "Stephanie", "Edward", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Angela", "Eric", "Shirley", "Jonathan", "Anna", "Stephen", "Brenda",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
]

SEGMENTS = ["Consumer", "Corporate", "Home Office"]
PAYMENT_MODES = ["Credit Card", "Debit Card", "Cash", "Online", "UPI"]
# Weights for payment mode realism
PAYMENT_WEIGHTS = [0.38, 0.22, 0.08, 0.25, 0.07]


def build_dim_product() -> pd.DataFrame:
    rows = []
    for i, (name, cat, sub, price, margin) in enumerate(PRODUCT_CATALOG, start=1):
        rows.append(
            {
                "ProductKey": i,
                "Product ID": f"PRD-{i:04d}",
                "Product Name": name,
                "Product Category": cat,
                "Sub Category": sub,
                "List Price": round(price, 2),
                "Base Margin": margin,
            }
        )
    return pd.DataFrame(rows)


def build_dim_geography() -> pd.DataFrame:
    rows = []
    for i, (region, country, state, city, lat, lon) in enumerate(GEOGRAPHY, start=1):
        rows.append(
            {
                "GeoKey": i,
                "Region": region,
                "Country": country,
                "State": state,
                "City": city,
                "Latitude": lat,
                "Longitude": lon,
            }
        )
    return pd.DataFrame(rows)


def build_dim_customer(n_customers: int = 850) -> pd.DataFrame:
    rows = []
    used = set()
    for i in range(1, n_customers + 1):
        while True:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            if name not in used:
                used.add(name)
                break
        segment = random.choices(SEGMENTS, weights=[0.52, 0.30, 0.18])[0]
        rows.append(
            {
                "CustomerKey": i,
                "Customer ID": f"CUS-{i:05d}",
                "Customer Name": name,
                "Segment": segment,
            }
        )
    return pd.DataFrame(rows)


def build_dim_date(start: datetime, end: datetime) -> pd.DataFrame:
    dates = pd.date_range(start, end, freq="D")
    rows = []
    for d in dates:
        rows.append(
            {
                "DateKey": int(d.strftime("%Y%m%d")),
                "Date": d.normalize(),
                "Year": d.year,
                "Quarter": f"Q{(d.month - 1) // 3 + 1}",
                "Quarter Number": (d.month - 1) // 3 + 1,
                "Month": d.month,
                "Month Name": d.strftime("%B"),
                "Month Short": d.strftime("%b"),
                "Week Number": int(d.strftime("%U")),
                "Day": d.day,
                "Day Name": d.strftime("%A"),
                "Day Short": d.strftime("%a"),
                "YearMonth": d.strftime("%Y-%m"),
                "YearMonthSort": int(d.strftime("%Y%m")),
                "Is Weekend": d.weekday() >= 5,
            }
        )
    df = pd.DataFrame(rows)
    return df


def build_dim_sales_pipeline() -> pd.DataFrame:
    """Static stages for Funnel visual (Page 2)."""
    stages = [
        ("Lead", 1, 10000),
        ("Qualified", 2, 7200),
        ("Proposal", 3, 4800),
        ("Negotiation", 4, 3100),
        ("Won", 5, 2100),
    ]
    return pd.DataFrame(
        [
            {
                "StageKey": i,
                "Stage": name,
                "Stage Order": order,
                "Pipeline Value": value,
            }
            for i, (name, order, value) in enumerate(stages, start=1)
        ]
    )


def generate_fact_sales(
    dim_product: pd.DataFrame,
    dim_customer: pd.DataFrame,
    dim_geo: pd.DataFrame,
    start: datetime,
    end: datetime,
    n_orders: int,
) -> pd.DataFrame:
    days = (end - start).days
    rows = []
    order_id = 100000

    # Slight regional / seasonal bias
    geo_weights = []
    for _, g in dim_geo.iterrows():
        w = {"East": 1.3, "West": 1.25, "Central": 1.1, "South": 0.95}[g["Region"]]
        geo_weights.append(w)
    geo_weights = np.array(geo_weights) / sum(geo_weights)

    for _ in range(n_orders):
        order_id += 1
        # More orders in Q4 and mid-year promotions
        day_offset = int(np.clip(np.random.beta(1.2, 1.0) * days, 0, days - 1))
        # Boost December / November
        order_date = start + timedelta(days=day_offset)
        if order_date.month in (11, 12) and random.random() < 0.35:
            order_date = datetime(order_date.year, random.choice([11, 12]), random.randint(1, 28))
            if order_date > end:
                order_date = end - timedelta(days=random.randint(0, 10))
        if order_date < start:
            order_date = start + timedelta(days=random.randint(0, 30))

        ship_delay = int(np.random.choice([1, 2, 3, 4, 5, 6, 7], p=[0.05, 0.15, 0.25, 0.25, 0.15, 0.10, 0.05]))
        ship_date = order_date + timedelta(days=ship_delay)

        cust = dim_customer.sample(1).iloc[0]
        geo = dim_geo.iloc[np.random.choice(len(dim_geo), p=geo_weights)]
        prod = dim_product.sample(1).iloc[0]

        # Quantity: most 1–3, occasional bulk
        qty = int(np.random.choice([1, 2, 3, 4, 5, 6, 8, 10], p=[0.35, 0.25, 0.18, 0.10, 0.05, 0.04, 0.02, 0.01]))

        # Discount: often 0, sometimes promotions
        discount = float(
            np.random.choice(
                [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
                p=[0.40, 0.18, 0.15, 0.12, 0.08, 0.05, 0.02],
            )
        )

        unit_price = float(prod["List Price"]) * (0.92 + random.random() * 0.16)  # slight price variance
        sales = round(unit_price * qty * (1 - discount), 2)

        # Profit based on base margin, reduced by discount & shipping
        base_profit = sales * float(prod["Base Margin"])
        shipping_cost = round(
            max(4.99, (8 + qty * 2.5 + unit_price * 0.02) * (0.8 + random.random() * 0.5)),
            2,
        )
        # High discount erodes profit
        profit = round(base_profit - shipping_cost * 0.35 - (sales * discount * 0.4), 2)
        # Occasional loss-leader
        if discount >= 0.25 and random.random() < 0.35:
            profit = round(-abs(profit) * random.uniform(0.3, 1.2), 2)

        payment = random.choices(PAYMENT_MODES, weights=PAYMENT_WEIGHTS)[0]

        rows.append(
            {
                "Order ID": f"ORD-{order_id}",
                "Order Date": order_date.date(),
                "Ship Date": ship_date.date(),
                "DateKey": int(order_date.strftime("%Y%m%d")),
                "CustomerKey": int(cust["CustomerKey"]),
                "ProductKey": int(prod["ProductKey"]),
                "GeoKey": int(geo["GeoKey"]),
                # Denormalized columns (also available via dims — useful for beginners)
                "Customer Name": cust["Customer Name"],
                "Customer ID": cust["Customer ID"],
                "Product Name": prod["Product Name"],
                "Product Category": prod["Product Category"],
                "Sub Category": prod["Sub Category"],
                "Region": geo["Region"],
                "Country": geo["Country"],
                "State": geo["State"],
                "City": geo["City"],
                "Sales": sales,
                "Profit": profit,
                "Quantity": qty,
                "Discount": discount,
                "Shipping Cost": shipping_cost,
                "Payment Mode": payment,
                "Segment": cust["Segment"],
            }
        )

    return pd.DataFrame(rows)


def build_targets(fact: pd.DataFrame) -> pd.DataFrame:
    """Annual sales/profit targets for KPI visuals (~90% of actual for demo stretch)."""
    yearly = fact.groupby(fact["Order Date"].apply(lambda d: d.year)).agg(
        ActualSales=("Sales", "sum"),
        ActualProfit=("Profit", "sum"),
    )
    rows = []
    for year, r in yearly.iterrows():
        rows.append(
            {
                "Year": int(year),
                "Sales Target": round(r["ActualSales"] * 1.08, 2),
                "Profit Target": round(r["ActualProfit"] * 1.10, 2),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    start = datetime(2022, 1, 1)
    end = datetime(2024, 12, 31)

    dim_product = build_dim_product()
    dim_customer = build_dim_customer(850)
    dim_geo = build_dim_geography()
    dim_date = build_dim_date(start, end)
    dim_pipeline = build_dim_sales_pipeline()

    fact = generate_fact_sales(dim_product, dim_customer, dim_geo, start, end, N_ORDERS)
    dim_targets = build_targets(fact)

    # Wide beginner-friendly flat file (all required columns)
    flat_cols = [
        "Order ID",
        "Order Date",
        "Ship Date",
        "Customer Name",
        "Customer ID",
        "Product Name",
        "Product Category",
        "Sub Category",
        "Region",
        "Country",
        "State",
        "City",
        "Sales",
        "Profit",
        "Quantity",
        "Discount",
        "Shipping Cost",
        "Payment Mode",
        "Segment",
    ]
    flat = fact[flat_cols].copy()
    flat = flat.sort_values("Order Date").reset_index(drop=True)

    # Star schema fact (keys + measures + attributes needed for slicers that stay on fact)
    fact_star = fact[
        [
            "Order ID",
            "Order Date",
            "Ship Date",
            "DateKey",
            "CustomerKey",
            "ProductKey",
            "GeoKey",
            "Sales",
            "Profit",
            "Quantity",
            "Discount",
            "Shipping Cost",
            "Payment Mode",
        ]
    ].copy()

    # Export CSVs
    flat.to_csv(OUTPUT_DIR / "Retail_Sales_Flat.csv", index=False)
    fact_star.to_csv(OUTPUT_DIR / "Fact_Sales.csv", index=False)
    dim_product.to_csv(OUTPUT_DIR / "Dim_Product.csv", index=False)
    dim_customer.to_csv(OUTPUT_DIR / "Dim_Customer.csv", index=False)
    dim_geo.to_csv(OUTPUT_DIR / "Dim_Geography.csv", index=False)
    dim_date.to_csv(OUTPUT_DIR / "Dim_Date.csv", index=False)
    dim_pipeline.to_csv(OUTPUT_DIR / "Dim_Sales_Pipeline.csv", index=False)
    dim_targets.to_csv(OUTPUT_DIR / "Dim_Targets.csv", index=False)

    # Excel workbook (all sheets)
    excel_path = OUTPUT_DIR / "Retail_Sales_StarSchema.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        flat.to_excel(writer, sheet_name="Retail_Sales_Flat", index=False)
        fact_star.to_excel(writer, sheet_name="Fact_Sales", index=False)
        dim_product.to_excel(writer, sheet_name="Dim_Product", index=False)
        dim_customer.to_excel(writer, sheet_name="Dim_Customer", index=False)
        dim_geo.to_excel(writer, sheet_name="Dim_Geography", index=False)
        dim_date.to_excel(writer, sheet_name="Dim_Date", index=False)
        dim_pipeline.to_excel(writer, sheet_name="Dim_Sales_Pipeline", index=False)
        dim_targets.to_excel(writer, sheet_name="Dim_Targets", index=False)

    print("=" * 60)
    print("Retail Sales dataset generated successfully")
    print("=" * 60)
    print(f"Fact rows:        {len(fact_star):,}")
    print(f"Products:         {len(dim_product)}")
    print(f"Customers:        {len(dim_customer)}")
    print(f"Geography:        {len(dim_geo)}")
    print(f"Date rows:        {len(dim_date)}")
    print(f"Date range:       {flat['Order Date'].min()} → {flat['Order Date'].max()}")
    print(f"Total Sales:      ${flat['Sales'].sum():,.2f}")
    print(f"Total Profit:     ${flat['Profit'].sum():,.2f}")
    print(f"Output folder:    {OUTPUT_DIR}")
    print(f"Excel workbook:   {excel_path.name}")


if __name__ == "__main__":
    main()
