# Dataset Instructions

## Dataset

Use the **Brazilian E-Commerce Public Dataset by Olist**:

https://www.kaggle.com/olistbr/brazilian-ecommerce

Download the dataset and place these files in this directory:

```text
olist_orders_dataset.csv
olist_order_items_dataset.csv
olist_customers_dataset.csv
olist_sellers_dataset.csv
olist_products_dataset.csv
olist_order_reviews_dataset.csv
olist_geolocation_dataset.csv
```

The Week 1 baseline primarily requires orders, order items and customers. Sellers, products, reviews and geolocation are recommended for later extensions.

## Why the Raw Dataset Is Not Included

The raw files are intentionally excluded from GitHub to keep the repository lightweight and avoid unnecessary redistribution of third-party data.

## Data Quality Checks

Before modelling:

- inspect missing values;
- convert timestamp columns to datetime;
- check duplicate IDs;
- validate date order;
- inspect price/freight outliers;
- exclude or separately flag cancelled/unavailable orders;
- avoid target leakage when creating prediction features.
