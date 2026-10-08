# Logistics Data Science – Week 1

## Strategic Planning and Data Exploration in Logistics

This project develops a data-driven analytical framework for an e-commerce logistics operation. It focuses on delivery performance, freight costs, late-delivery risk, regional patterns, clustering, and future route optimization.

**Dataset:** Brazilian E-Commerce Public Dataset by Olist  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, OR-Tools

## Objectives

- Define a realistic logistics business problem.
- Establish measurable logistics KPIs.
- Integrate and clean multi-table logistics data.
- Perform exploratory data analysis.
- Identify drivers of delivery delays and freight costs.
- Build a baseline late-delivery prediction model.
- Segment regions using clustering.
- Design a route-optimization approach.
- Translate findings into business recommendations.

## Key KPIs

| KPI | Purpose |
|---|---|
| On-Time Delivery Rate | Delivery reliability |
| Average Delivery Lead Time | Customer waiting time |
| Freight Cost per Order | Transport efficiency |
| Freight-to-Order Value Ratio | High-cost shipment detection |
| Late Delivery Rate | Service-failure measurement |
| Average Review Score | Customer-experience outcome |

## Repository Structure

```text
logistics-data-science-week1/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── notebooks/
│   └── logistics_week1_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── kpi_analysis.py
│   └── modelling.py
├── outputs/
│   └── README.md
└── Week_1_Logistics_Strategic_Planning_Report.docx
```

## Analytical Roadmap

`Data Collection → Cleaning → Integration → Feature Engineering → KPI Baseline → EDA → Prediction → Clustering → Route Optimization → Recommendations`

## Setup

```bash
git clone https://github.com/YOUR-USERNAME/logistics-data-science-week1.git
cd logistics-data-science-week1
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Then place the Olist CSV files in `data/` as explained in `data/README.md` and launch:

```bash
jupyter notebook
```

Open `notebooks/logistics_week1_analysis.ipynb`.

## Business Questions

1. Which regions have the highest late-delivery rates?
2. How does freight cost vary by region and order value?
3. Which factors are associated with longer delivery times?
4. Can late deliveries be predicted before completion?
5. Can regions be grouped by logistics performance?
6. How could route optimization reduce travel distance or delivery time?

## Expected Outcomes

The analysis is intended to help logistics teams identify delay-prone regions, monitor KPIs, prioritize high-risk orders, understand cost/service trade-offs, segment operational regions, and build a foundation for route optimization.

## Limitations

The Olist dataset is historical and does not represent current logistics conditions. It does not contain live GPS tracking, real-time traffic, complete vehicle capacity data, or every event required for production-grade routing.

## References

- Olist dataset: https://www.kaggle.com/olistbr/brazilian-ecommerce
- Scikit-learn: https://scikit-learn.org/stable/user_guide.html
- Scikit-learn clustering: https://scikit-learn.org/stable/modules/clustering.html
- Google OR-Tools routing: https://developers.google.com/optimization/routing
