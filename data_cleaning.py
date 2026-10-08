"""Data loading, integration and feature engineering."""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_data(data_dir=DATA_DIR):
    data_dir = Path(data_dir)
    orders = pd.read_csv(data_dir / "olist_orders_dataset.csv")
    items = pd.read_csv(data_dir / "olist_order_items_dataset.csv")
    customers = pd.read_csv(data_dir / "olist_customers_dataset.csv")
    return orders, items, customers

def convert_order_dates(orders):
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for col in date_cols:
        if col in orders.columns:
            orders[col] = pd.to_datetime(orders[col], errors="coerce")
    return orders

def build_order_level_dataset(orders, items, customers):
    orders = convert_order_dates(orders.copy())
    item_summary = (
        items.groupby("order_id")
        .agg(
            item_count=("order_id", "size"),
            merchandise_value=("price", "sum"),
            freight_value=("freight_value", "sum"),
        )
        .reset_index()
    )
    customer_cols = [
        "customer_id", "customer_zip_code_prefix",
        "customer_city", "customer_state"
    ]
    customer_subset = customers[customer_cols].drop_duplicates("customer_id")
    df = orders.merge(item_summary, on="order_id", how="left")
    df = df.merge(customer_subset, on="customer_id", how="left")

    df["delivery_days"] = (
        df["order_delivered_customer_date"] -
        df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["delay_days"] = (
        df["order_delivered_customer_date"] -
        df["order_estimated_delivery_date"]
    ).dt.total_seconds() / 86400

    df["is_late"] = (df["delay_days"] > 0).astype("int8")
    df["freight_ratio"] = (
        df["freight_value"] /
        df["merchandise_value"].replace(0, pd.NA)
    )
    return df

def get_eligible_orders(df):
    return df[
        df["order_status"].eq("delivered") &
        df["delivery_days"].notna()
    ].copy()

if __name__ == "__main__":
    orders, items, customers = load_data()
    df = build_order_level_dataset(orders, items, customers)
    print(df.head())
    print(f"Rows: {len(df):,}")
