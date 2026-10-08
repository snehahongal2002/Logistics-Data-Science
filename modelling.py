"""Baseline predictive modelling and clustering."""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans

def train_late_delivery_model(df):
    model_df = df[
        df["order_status"].eq("delivered") &
        df["delivery_days"].notna()
    ].copy()

    features = ["freight_value", "merchandise_value", "item_count", "customer_state"]
    X = model_df[features]
    y = model_df["is_late"]

    preprocess = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler())
        ]), ["freight_value", "merchandise_value", "item_count"]),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), ["customer_state"])
    ])

    model = Pipeline([
        ("preprocess", preprocess),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, predictions))
    print("ROC-AUC:", round(roc_auc_score(y_test, probabilities), 4))
    return model

def cluster_regions(df, n_clusters=4):
    model_df = df[
        df["order_status"].eq("delivered") &
        df["delivery_days"].notna()
    ].copy()

    regional = (
        model_df.groupby("customer_state")
        .agg(
            avg_delivery=("delivery_days", "mean"),
            late_rate=("is_late", "mean"),
            avg_freight=("freight_value", "mean"),
            order_volume=("order_id", "nunique")
        )
        .dropna()
    )

    X = regional[["avg_delivery", "late_rate", "avg_freight", "order_volume"]]
    scaled = StandardScaler().fit_transform(X)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    regional["cluster"] = model.fit_predict(scaled)
    return regional
