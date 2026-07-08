# Sales Data Visualization — Questions

**Dataset:** `sales_data.csv` (20 records, 6 columns)  
**Columns:** `Order_ID`, `Date`, `Product`, `Region`, `Units_Sold`, `Revenue`  
**Libraries:** Matplotlib & Seaborn

---

## Part 1 — Matplotlib

### Graph 1: Line Plot — Total Revenue Over Time

**Questions to create this graph:**
- How does total revenue change from one sale date to another?
- Which month shows the highest single-day revenue?
- Is there an upward or downward trend in sales over the first half of 2024?

**Questions to answer from this graph:**
- On which dates did revenue peak above $7,000?
- Are there noticeable dips between consecutive orders?
- Does revenue generally increase toward June 2024?

---

### Graph 2: Bar Chart — Total Revenue by Region

**Questions to create this graph:**
- Which region generates the most total revenue?
- How does revenue compare across North, South, East, and West?
- Are there regions that underperform compared to others?

**Questions to answer from this graph:**
- Which region has the highest and lowest total revenue?
- Is the revenue gap between the top two regions significant?
- Which region should the sales team focus on for growth?

---

### Graph 3: Pie Chart — Revenue Share by Product

**Questions to create this graph:**
- What percentage of total revenue comes from each product?
- Which product contributes the largest share of sales?
- Are any products barely contributing to overall revenue?

**Questions to answer from this graph:**
- Which product holds the largest revenue share?
- Do Laptop and Phone together account for more than half of total revenue?
- Should the company invest more in the lowest-share product?

---

### Graph 4: Scatter Plot — Units Sold vs Revenue

**Questions to create this graph:**
- Is there a relationship between units sold and revenue per order?
- Do orders with more units always generate higher revenue?
- Are there outliers where few units still produced high revenue?

**Questions to answer from this graph:**
- Does revenue generally increase as units sold increase?
- Which orders are outliers (high revenue with relatively few units)?
- What might explain orders that deviate from the overall pattern?

---

### Graph 5: Histogram — Distribution of Revenue

**Questions to create this graph:**
- How is revenue spread across all 20 orders?
- Are most orders clustered around a specific revenue range?
- Are there unusually high or low revenue orders?

**Questions to answer from this graph:**
- What is the most common revenue range for orders?
- Is the distribution skewed toward lower or higher values?
- How many orders fall above $6,000 in revenue?

---

## Part 2 — Seaborn

### Graph 6: Bar Plot — Average Revenue by Product

**Questions to create this graph:**
- Which product has the highest average revenue per order?
- How does average order value differ between Laptop, Phone, Tablet, and Monitor?
- Which product generates the most revenue per transaction on average?

**Questions to answer from this graph:**
- Which product has the highest and lowest average revenue per order?
- Is Phone's average revenue noticeably higher than Tablet's?
- Based on this chart, which product is the most profitable per sale?

---

### Graph 7: Count Plot — Number of Orders by Region

**Questions to create this graph:**
- How many orders were placed in each region?
- Is order volume evenly distributed across regions?
- Which region has the most and fewest number of transactions?

**Questions to answer from this graph:**
- Which region received the most orders?
- Are all four regions represented equally in the dataset?
- Does higher order count always mean higher total revenue for that region?

---

### Graph 8: Box Plot — Revenue Distribution by Product

**Questions to create this graph:**
- How does revenue vary within each product category?
- Which product shows the widest spread in revenue values?
- Are there any unusual (outlier) revenue values for a given product?

**Questions to answer from this graph:**
- Which product has the highest median revenue?
- Which product shows the most variation in order revenue?
- Do any products have outlier orders far from the typical range?

---

### Graph 9: Heatmap — Total Revenue by Region and Product

**Questions to create this graph:**
- Which region–product combination generates the most revenue?
- Are there region–product pairs with very low sales?
- Can we spot patterns such as Laptops selling best in the North?

**Questions to answer from this graph:**
- Which single region–product cell has the highest revenue?
- Which combinations have zero or very low revenue?
- Should marketing focus on weak region–product pairs?

---

### Graph 10: Line Plot — Monthly Total Revenue Trend

**Questions to create this graph:**
- How does total monthly revenue change from January to June 2024?
- Which month had the highest combined sales?
- Is there a seasonal pattern in monthly revenue?

**Questions to answer from this graph:**
- Which month recorded the highest total revenue?
- Did revenue grow steadily or fluctuate month to month?
- What business decisions could be made based on this monthly trend?

---

## Quick Reference

| # | Library    | Plot Type   | Question Focus                |
|---|------------|-------------|-------------------------------|
| 1 | Matplotlib | Line Plot   | Revenue trend over dates      |
| 2 | Matplotlib | Bar Chart   | Total revenue by region       |
| 3 | Matplotlib | Pie Chart   | Revenue share by product      |
| 4 | Matplotlib | Scatter Plot| Units sold vs revenue         |
| 5 | Matplotlib | Histogram   | Revenue distribution          |
| 6 | Seaborn    | Bar Plot    | Average revenue by product    |
| 7 | Seaborn    | Count Plot  | Order count by region         |
| 8 | Seaborn    | Box Plot    | Revenue spread by product     |
| 9 | Seaborn    | Heatmap     | Region × product revenue      |
| 10| Seaborn    | Line Plot   | Monthly revenue trend         |
