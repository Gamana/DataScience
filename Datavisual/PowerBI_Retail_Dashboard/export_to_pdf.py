"""
Export Retail Sales Dashboard to PDF
Same story as the interactive dashboard / PowerPoint: Executive, Product, Geographic.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.gridspec import GridSpec

ROOT = Path(__file__).parent
DATA = ROOT / "data"
OUT_DIR = ROOT / "export"
PDF_PATH = OUT_DIR / "Retail_Sales_Dashboard.pdf"

BLUE = "#0078D4"
DARK = "#252525"
GRAY = "#505050"
LIGHT = "#F5F7FA"
GOOD = "#107C10"
TEAL = "#00B7C3"
ORANGE = "#D83B01"


def money(n: float) -> str:
    if abs(n) >= 1_000_000:
        return f"${n / 1_000_000:.2f}M"
    if abs(n) >= 1_000:
        return f"${n / 1_000:.1f}K"
    return f"${n:,.0f}"


def load_data():
    flat = pd.read_csv(DATA / "Retail_Sales_Flat.csv", parse_dates=["Order Date"])
    geo = pd.read_csv(DATA / "Dim_Geography.csv")
    pipeline = pd.read_csv(DATA / "Dim_Sales_Pipeline.csv")
    targets = pd.read_csv(DATA / "Dim_Targets.csv")
    flat = flat.merge(
        geo[["City", "State", "Latitude", "Longitude", "Region"]],
        on=["City", "State", "Region"],
        how="left",
    )
    flat["Year"] = flat["Order Date"].dt.year
    flat["YearMonth"] = flat["Order Date"].dt.strftime("%Y-%m")
    return flat, pipeline, targets


def page_header(fig, title: str):
    fig.patch.set_facecolor(LIGHT)
    header = fig.add_axes([0, 0.93, 1, 0.07])
    header.set_xlim(0, 1)
    header.set_ylim(0, 1)
    header.axis("off")
    header.add_patch(mpatches.Rectangle((0, 0), 1, 1, color=BLUE, transform=header.transAxes))
    header.text(0.02, 0.5, title, color="white", fontsize=14, fontweight="bold", va="center")


def kpi_box(ax, title, value, subtitle=""):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (0.02, 0.05), 0.96, 0.9,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor="white",
            edgecolor="#E1E1E1",
            linewidth=1,
            transform=ax.transAxes,
        )
    )
    ax.text(0.06, 0.72, title, fontsize=8, color=GRAY, fontweight="bold", transform=ax.transAxes)
    ax.text(0.06, 0.38, value, fontsize=16, color=BLUE, fontweight="bold", transform=ax.transAxes)
    if subtitle:
        ax.text(0.06, 0.14, subtitle, fontsize=7, color=GRAY, transform=ax.transAxes)


def build_pdf(flat, pipeline, targets):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.edgecolor": "#E1E1E1",
        "axes.labelcolor": GRAY,
        "xtick.color": GRAY,
        "ytick.color": GRAY,
        "figure.facecolor": LIGHT,
        "axes.facecolor": "white",
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.titlecolor": DARK,
    })

    total_sales = flat["Sales"].sum()
    total_profit = flat["Profit"].sum()
    total_orders = flat["Order ID"].nunique()
    total_customers = flat["Customer ID"].nunique()
    margin = total_profit / total_sales
    aov = total_sales / total_orders
    sales_target = targets["Sales Target"].sum()
    profit_target = targets["Profit Target"].sum()
    sales_ach = total_sales / sales_target
    profit_ach = total_profit / profit_target

    monthly = (
        flat.groupby("YearMonth", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Quantity=("Quantity", "sum"))
        .sort_values("YearMonth")
    )
    by_cat = flat.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)
    by_seg = flat.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    by_pay = flat.groupby("Payment Mode")["Sales"].sum().sort_values(ascending=False)
    by_reg = flat.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    top10 = (
        flat.groupby(["Product Name", "Product Category"], as_index=False)
        .agg(Quantity=("Quantity", "sum"), Sales=("Sales", "sum"), Profit=("Profit", "sum"))
        .sort_values("Sales", ascending=False)
        .head(10)
    )
    prod = flat.groupby("Product Name", as_index=False).agg(
        Sales=("Sales", "sum"), Profit=("Profit", "sum"), Quantity=("Quantity", "sum")
    )
    city = flat.groupby(["City", "Latitude", "Longitude"], as_index=False)["Sales"].sum()
    state = flat.groupby("State")["Sales"].sum().sort_values(ascending=True)
    pipe = pipeline.sort_values("Stage Order")
    mat = flat.groupby(["Product Category", "Year"])[["Sales", "Profit"]].sum().reset_index()
    years = sorted(flat["Year"].unique())

    with PdfPages(PDF_PATH) as pdf:
        # ----- Page 1: Title -----
        fig = plt.figure(figsize=(11.69, 8.27))  # A4 landscape
        fig.patch.set_facecolor(LIGHT)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis("off")
        ax.add_patch(mpatches.Rectangle((0, 0.72), 1, 0.28, color=BLUE, transform=ax.transAxes))
        ax.text(0.05, 0.86, "Retail Sales Dashboard", fontsize=28, color="white",
                fontweight="bold", transform=ax.transAxes, va="center")
        ax.text(0.05, 0.78, "Executive  ·  Product  ·  Geographic Analytics",
                fontsize=12, color="white", transform=ax.transAxes, va="center")
        ax.text(
            0.05, 0.58,
            f"5,200 orders   |   {flat['Order Date'].min().date()} → {flat['Order Date'].max().date()}",
            fontsize=13, color=DARK, transform=ax.transAxes,
        )
        ax.text(
            0.05, 0.48,
            f"Total Sales {money(total_sales)}   ·   Total Profit {money(total_profit)}   ·   "
            f"Margin {margin * 100:.1f}%",
            fontsize=13, color=GRAY, transform=ax.transAxes,
        )
        ax.text(
            0.05, 0.32,
            "PDF export of the interactive retail dashboard for presentations and teaching.\n"
            "Theme: Corporate Blue / Dark Gray / White",
            fontsize=11, color=GRAY, transform=ax.transAxes,
        )
        ax.text(0.05, 0.08, "Power BI Retail Dashboard Package", fontsize=9, color=GRAY, transform=ax.transAxes)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 2: Executive KPIs + charts -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 1 — Executive Dashboard · KPI Overview")
        gs = GridSpec(3, 4, figure=fig, left=0.04, right=0.96, top=0.90, bottom=0.06, hspace=0.45, wspace=0.25)

        kpi_box(fig.add_subplot(gs[0, 0]), "Total Sales", money(total_sales), f"AOV {money(aov)}")
        kpi_box(fig.add_subplot(gs[0, 1]), "Total Profit", money(total_profit), f"Margin {margin*100:.1f}%")
        kpi_box(fig.add_subplot(gs[0, 2]), "Total Orders", f"{total_orders:,}", "Distinct orders")
        kpi_box(fig.add_subplot(gs[0, 3]), "Total Customers", f"{total_customers:,}", "Unique customers")

        ax = fig.add_subplot(gs[1, :2])
        kpi_box(ax, "KPI — Sales vs Target", money(total_sales),
                f"Target {money(sales_target)}  ·  Achievement {sales_ach*100:.1f}%")
        ax = fig.add_subplot(gs[1, 2:])
        kpi_box(ax, "KPI — Profit vs Target", money(total_profit),
                f"Target {money(profit_target)}  ·  Achievement {profit_ach*100:.1f}%")

        ax = fig.add_subplot(gs[2, :2])
        step = max(1, len(monthly) // 12)
        mplot = monthly.iloc[::step]
        ax.plot(mplot["YearMonth"], mplot["Sales"], color=BLUE, marker="o", markersize=3, linewidth=2)
        ax.set_title("Monthly Sales Trend")
        ax.tick_params(axis="x", rotation=30, labelsize=7)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, alpha=0.25)

        ax = fig.add_subplot(gs[2, 2:])
        ax.bar(by_cat.index, by_cat.values, color=BLUE, width=0.6)
        ax.set_title("Sales by Category")
        ax.tick_params(axis="x", labelsize=8)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, axis="y", alpha=0.25)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 3: Segment donut -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 1 — Executive Dashboard · Sales by Segment")
        ax = fig.add_axes([0.08, 0.15, 0.5, 0.7])
        colors = [BLUE, GRAY, TEAL]
        wedges, texts, autotexts = ax.pie(
            by_seg.values,
            labels=by_seg.index,
            autopct="%1.1f%%",
            colors=colors,
            pctdistance=0.75,
            wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
            textprops=dict(color=DARK, fontsize=10),
        )
        for t in autotexts:
            t.set_color("white")
            t.set_fontweight("bold")
            t.set_fontsize(9)
        ax.set_title("Donut — Sales by Segment")
        ax.text(0, 0, money(total_sales), ha="center", va="center", fontsize=12, fontweight="bold", color=BLUE)

        ax2 = fig.add_axes([0.62, 0.25, 0.32, 0.5])
        ax2.axis("off")
        ax2.set_title("Segment Insights", loc="left", fontsize=12, fontweight="bold", color=DARK)
        y = 0.85
        for name, val in by_seg.items():
            ax2.text(0, y, f"{name}", fontsize=11, fontweight="bold", color=DARK, transform=ax2.transAxes)
            ax2.text(0, y - 0.08, f"{money(val)}  ({val/total_sales*100:.1f}%)",
                     fontsize=10, color=GRAY, transform=ax2.transAxes)
            y -= 0.25
        ax2.text(0, 0.1, "Slicers (live dashboard):\nYear · Category · Region",
                 fontsize=9, color=GRAY, transform=ax2.transAxes)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 4: Product top 10 -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 2 — Product Analysis · Top 10 Products")
        gs = GridSpec(1, 2, figure=fig, left=0.04, right=0.96, top=0.88, bottom=0.08, wspace=0.3)

        ax = fig.add_subplot(gs[0, 0])
        ax.axis("off")
        ax.set_title("Product Table (Top 10)", loc="left")
        cell_text = [
            [r["Product Name"][:24], r["Product Category"][:12], f"{int(r['Quantity']):,}",
             money(r["Sales"]), money(r["Profit"])]
            for _, r in top10.iterrows()
        ]
        table = ax.table(
            cellText=cell_text,
            colLabels=["Product", "Category", "Qty", "Sales", "Profit"],
            loc="center",
            cellLoc="left",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(7.5)
        table.scale(1.05, 1.55)
        for (r, c), cell in table.get_celld().items():
            if r == 0:
                cell.set_facecolor(BLUE)
                cell.set_text_props(color="white", fontweight="bold")
            elif r % 2 == 0:
                cell.set_facecolor(LIGHT)
            cell.set_edgecolor("#E1E1E1")

        ax = fig.add_subplot(gs[0, 1])
        labels = [p[:20] + ("…" if len(p) > 20 else "") for p in top10["Product Name"]]
        ax.barh(labels[::-1], top10["Sales"].values[::-1], color=BLUE)
        ax.set_title("Bar — Top 10 Products by Sales")
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.tick_params(axis="y", labelsize=8)
        ax.grid(True, axis="x", alpha=0.25)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 5: Matrix -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 2 — Product Analysis · Matrix (Category × Year)")
        ax = fig.add_axes([0.06, 0.2, 0.88, 0.65])
        ax.axis("off")
        ax.set_title("Sales & Profit by Category and Year", loc="left", fontsize=11, fontweight="bold", color=DARK, pad=12)
        cats = sorted(flat["Product Category"].unique())
        headers = ["Category"] + [f"{y} Sales" for y in years] + [f"{y} Profit" for y in years]
        rows = []
        for cat in cats:
            row = [cat]
            for y in years:
                r = mat[(mat["Product Category"] == cat) & (mat["Year"] == y)]
                row.append(money(float(r["Sales"].iloc[0])) if len(r) else "—")
            for y in years:
                r = mat[(mat["Product Category"] == cat) & (mat["Year"] == y)]
                row.append(money(float(r["Profit"].iloc[0])) if len(r) else "—")
            rows.append(row)
        table = ax.table(cellText=rows, colLabels=headers, loc="center", cellLoc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1.1, 2.2)
        for (r, c), cell in table.get_celld().items():
            if r == 0:
                cell.set_facecolor(BLUE)
                cell.set_text_props(color="white", fontweight="bold", fontsize=7)
            elif c == 0:
                cell.set_text_props(fontweight="bold")
                cell.set_facecolor(LIGHT)
            cell.set_edgecolor("#E1E1E1")
        fig.text(0.06, 0.1,
                 "In Power BI: Matrix rows = Category → Sub Category, columns = Year, values = Sales & Profit.",
                 fontsize=9, color=GRAY)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 6: Advanced product visuals -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 2 — Product Analysis · Treemap · Scatter · Pie · Funnel")
        gs = GridSpec(2, 2, figure=fig, left=0.05, right=0.97, top=0.88, bottom=0.06, hspace=0.35, wspace=0.25)

        # Treemap-like
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        ax.set_title("Tree Map — Sales by Category")
        total = by_cat.sum()
        colors_map = {"Technology": BLUE, "Furniture": GRAY, "Office Supplies": TEAL}
        x = 0
        for cat, val in by_cat.items():
            w = val / total
            ax.add_patch(mpatches.FancyBboxPatch(
                (x, 0.2), w - 0.01, 0.6,
                boxstyle="round,pad=0.01,rounding_size=0.02",
                facecolor=colors_map.get(cat, "#8764B8"), edgecolor="white", linewidth=2,
            ))
            ax.text(x + w / 2, 0.55, cat, ha="center", va="center", color="white", fontsize=9, fontweight="bold")
            ax.text(x + w / 2, 0.38, money(val), ha="center", va="center", color="white", fontsize=8)
            x += w

        # Scatter
        ax = fig.add_subplot(gs[0, 1])
        sizes = np.sqrt(prod["Quantity"]) * 6
        ax.scatter(prod["Sales"], prod["Profit"], s=sizes, c=BLUE, alpha=0.55, edgecolors="#005A9E", linewidths=0.4)
        ax.axhline(0, color=ORANGE, linewidth=0.8, linestyle="--", alpha=0.5)
        ax.set_title("Scatter — Sales vs Profit (size = Qty)")
        ax.set_xlabel("Sales ($)")
        ax.set_ylabel("Profit ($)")
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, alpha=0.25)

        # Funnel
        ax = fig.add_subplot(gs[1, 0])
        ax.set_xlim(0, 1)
        ax.set_ylim(0, len(pipe) + 0.3)
        ax.axis("off")
        ax.set_title("Funnel — Sales Pipeline")
        shades = [BLUE, "#2B88D8", TEAL, GRAY, GOOD]
        max_v = pipe["Pipeline Value"].max()
        for i, (_, r) in enumerate(pipe.iterrows()):
            width = 0.35 + 0.55 * (r["Pipeline Value"] / max_v)
            y = len(pipe) - i - 0.85
            left = (1 - width) / 2
            ax.add_patch(mpatches.FancyBboxPatch(
                (left, y), width, 0.7,
                boxstyle="round,pad=0.01,rounding_size=0.02",
                facecolor=shades[i % len(shades)], edgecolor="white",
            ))
            ax.text(0.5, y + 0.35, f"{r['Stage']}  ·  {money(r['Pipeline Value'])}",
                    ha="center", va="center", color="white", fontsize=8, fontweight="bold")

        # Pie payment
        ax = fig.add_subplot(gs[1, 1])
        palette = [BLUE, GRAY, "#2B88D8", GOOD, TEAL, ORANGE, "#8764B8"]
        ax.pie(
            by_pay.values,
            labels=by_pay.index,
            autopct="%1.1f%%",
            colors=palette[: len(by_pay)],
            textprops=dict(fontsize=8, color=DARK),
            wedgeprops=dict(edgecolor="white", linewidth=1.5),
        )
        ax.set_title("Pie — Sales by Payment Mode")
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 7: Maps -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 3 — Geographic Dashboard · Maps")
        gs = GridSpec(1, 2, figure=fig, left=0.05, right=0.97, top=0.88, bottom=0.08, wspace=0.2)

        ax = fig.add_subplot(gs[0, 0])
        sizes = (city["Sales"] / city["Sales"].max()) * 350 + 20
        ax.scatter(city["Longitude"], city["Latitude"], s=sizes, c=BLUE, alpha=0.45, edgecolors="#005A9E")
        ax.set_xlim(-130, -65)
        ax.set_ylim(24, 50)
        ax.set_title("Map — Sales by City")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.grid(True, alpha=0.2)
        for _, r in city.nlargest(5, "Sales").iterrows():
            ax.annotate(r["City"], (r["Longitude"], r["Latitude"]), fontsize=7, color=DARK,
                        xytext=(3, 3), textcoords="offset points")

        ax = fig.add_subplot(gs[0, 1])
        norm = state / state.max()
        cmap_colors = [plt.cm.Blues(0.35 + 0.65 * float(v)) for v in norm]
        ax.barh(state.index, state.values, color=cmap_colors)
        ax.set_title("Filled Map Proxy — Sales by State")
        ax.tick_params(axis="y", labelsize=6.5)
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, axis="x", alpha=0.25)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 8: Geo trends -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Page 3 — Geographic Dashboard · Trends")
        gs = GridSpec(2, 2, figure=fig, left=0.07, right=0.96, top=0.88, bottom=0.08, hspace=0.4, wspace=0.25)

        ax = fig.add_subplot(gs[0, 0])
        step = max(1, len(monthly) // 12)
        mplot = monthly.iloc[::step]
        ax.fill_between(range(len(mplot)), mplot["Profit"], color=GOOD, alpha=0.25)
        ax.plot(range(len(mplot)), mplot["Profit"], color=GOOD, linewidth=2)
        ax.set_xticks(range(len(mplot)))
        ax.set_xticklabels(mplot["YearMonth"], rotation=30, ha="right", fontsize=7)
        ax.set_title("Area — Monthly Profit")
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, alpha=0.25)

        ax = fig.add_subplot(gs[0, 1])
        ax.bar(by_reg.index, by_reg.values, color=BLUE, width=0.55)
        ax.set_title("Column — Sales by Region")
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: money(x)))
        ax.grid(True, axis="y", alpha=0.25)

        ax = fig.add_subplot(gs[1, :])
        ax.plot(mplot["YearMonth"], mplot["Quantity"], color=GRAY, marker="o", markersize=3, linewidth=2)
        ax.set_title("Line — Monthly Quantity Sold")
        ax.tick_params(axis="x", rotation=30, labelsize=7)
        ax.set_ylabel("Units")
        ax.grid(True, alpha=0.25)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 9: Checklist -----
        fig = plt.figure(figsize=(11.69, 8.27))
        page_header(fig, "Visual Coverage Checklist")
        ax = fig.add_axes([0.08, 0.1, 0.84, 0.78])
        ax.axis("off")
        visuals = [
            ("Card", "Executive — Sales, Profit, Orders, Customers"),
            ("KPI", "Sales / Profit vs Target"),
            ("Line Chart", "Monthly Sales · Monthly Quantity"),
            ("Column Chart", "Sales by Category · Sales by Region"),
            ("Donut Chart", "Sales by Segment"),
            ("Table", "Product Name, Category, Qty, Sales, Profit"),
            ("Matrix", "Category × Year Sales & Profit"),
            ("Bar Chart", "Top 10 Products by Sales"),
            ("Tree Map", "Sales by Category"),
            ("Scatter Chart", "Sales vs Profit (size = Quantity)"),
            ("Pie Chart", "Sales by Payment Mode"),
            ("Funnel Chart", "Lead → Won pipeline"),
            ("Map", "Sales by City"),
            ("Filled Map", "Sales by State"),
            ("Area Chart", "Monthly Profit"),
            ("Slicer", "Year / Category / Region (live HTML & Power BI)"),
        ]
        for i, (name, desc) in enumerate(visuals):
            col = 0 if i < 8 else 1
            row = i if i < 8 else i - 8
            x = 0.02 + col * 0.52
            y = 0.92 - row * 0.11
            ax.text(x, y, f"✓  {name}", fontsize=11, fontweight="bold", color=BLUE, transform=ax.transAxes)
            ax.text(x + 0.03, y - 0.04, desc, fontsize=9, color=GRAY, transform=ax.transAxes)
        pdf.savefig(fig)
        plt.close(fig)

        # ----- Page 10: Closing -----
        fig = plt.figure(figsize=(11.69, 8.27))
        fig.patch.set_facecolor(LIGHT)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis("off")
        ax.add_patch(mpatches.Rectangle((0, 0.35), 1, 0.3, color=BLUE, transform=ax.transAxes))
        ax.text(0.5, 0.55, "Thank You", fontsize=28, color="white", fontweight="bold",
                ha="center", va="center", transform=ax.transAxes)
        ax.text(
            0.5, 0.42,
            "Interactive: dashboard/dashboard.html   ·   PowerPoint: export/Retail_Sales_Dashboard.pptx",
            fontsize=10, color="white", ha="center", va="center", transform=ax.transAxes,
        )
        pdf.savefig(fig)
        plt.close(fig)

        # metadata
        d = pdf.infodict()
        d["Title"] = "Retail Sales Dashboard"
        d["Author"] = "Power BI Retail Dashboard Package"
        d["Subject"] = "Executive, Product, and Geographic analytics export"
        d["Keywords"] = "Retail Sales, Dashboard, Power BI, Analytics"

    return PDF_PATH


def main():
    print("Loading data…")
    flat, pipeline, targets = load_data()
    print("Building PDF…")
    out = build_pdf(flat, pipeline, targets)
    print(f"Saved: {out}")
    print(f"Size: {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
