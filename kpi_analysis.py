"""Logistics KPI calculations."""

def calculate_kpis(df):
    eligible = df[
        df["order_status"].eq("delivered") &
        df["delivery_days"].notna()
    ].copy()

    return {
        "on_time_delivery_rate_pct": round((1 - eligible["is_late"].mean()) * 100, 2),
        "late_delivery_rate_pct": round(eligible["is_late"].mean() * 100, 2),
        "average_delivery_days": round(eligible["delivery_days"].mean(), 2),
        "average_freight_per_order": round(eligible["freight_value"].mean(), 2),
        "average_freight_ratio_pct": round(eligible["freight_ratio"].mean() * 100, 2),
        "eligible_orders": len(eligible),
    }

def monthly_kpis(df):
    eligible = df[
        df["order_status"].eq("delivered") &
        df["delivery_days"].notna()
    ].copy()

    eligible["month"] = (
        eligible["order_purchase_timestamp"]
        .dt.to_period("M").astype(str)
    )

    monthly = (
        eligible.groupby("month")
        .agg(
            orders=("order_id", "nunique"),
            late_rate=("is_late", "mean"),
            avg_delivery_days=("delivery_days", "mean"),
            avg_freight=("freight_value", "mean"),
        )
        .reset_index()
    )

    monthly["on_time_rate"] = (1 - monthly["late_rate"]) * 100
    monthly["late_rate"] *= 100
    return monthly
