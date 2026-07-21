# Suggestions for Future Enhancements

Use these ideas after the core three-page dashboard works end-to-end.

## Data & model

1. **Returns / cancellations fact** — second fact table related to the same dimensions; teach multi-fact models.
2. **Budget by Category × Month** — richer targets than annual totals; variance waterfalls.
3. **Customer 360** — RFM segmentation (Recency, Frequency, Monetary) with calculated columns or a Python/R script in Power Query.
4. **Slowly Changing Dimensions (SCD Type 2)** — track customers moving between segments over time.
5. **Role-playing dates** — separate Ship Date dimension related to `Ship Date` / ship `DateKey`.

## DAX & analytics

6. **What-if parameters** — discount simulator affecting projected profit.
7. **Dynamic Top N** — parameter to switch Top 5 / 10 / 20 products.
8. **ABC classification** — Pareto of products contributing 80% of sales.
9. **Moving averages** — 3-month sales smoother on the trend line.
10. **Field parameters** — let users switch measure (Sales / Profit / Quantity) on one chart.

## Visuals & UX

11. **Decomposition tree** — AI visual for category → subcategory → product contribution.
12. **Smart narrative** — auto-generated insights for executives.
13. **Buttons + bookmarks** — toggle “Sales view” vs “Profit view” on the same page.
14. **Custom tooltip pages** per visual type (geo tooltip with state rank).
15. **Mobile-priority layouts** for field sales managers.
16. **Accessibility theme** — larger fonts, pattern fills for color-blind safe charts.

## Governance & deployment

17. **Power BI Service app** — workspace + app for business users.
18. **Row-level security (RLS)** — filter by Region based on user role.
19. **Incremental refresh** — when fact grows past millions of rows.
20. **Certification & endorsement** — mark the dataset as certified in the Service.
21. **Deployment pipelines** — Dev → Test → Prod.
22. **Automated data refresh** from OneDrive/SharePoint or a database.

## Advanced storytelling

23. **Scorecard / Metrics (Power BI Goals)** connected to Sales Achievement %.
24. **Paginated report** — printable invoice-style order list for finance.
25. **Integration with Excel Analyze in Excel** for analysts who prefer pivot tables.

---

### Recommended learning path after this project

1. Recreate the dashboard from the **flat file** only (1 hour).  
2. Rebuild using **star schema** (this package).  
3. Add **RLS** by Region.  
4. Publish and build a **phone layout**.  
5. Replace sample CSV with a live SQL source and map the same model.
