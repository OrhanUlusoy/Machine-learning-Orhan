from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    data_path = Path(__file__).with_name("advertising.csv")
    df = pd.read_csv(data_path, index_col=0)

    X = df.drop("Sales", axis="columns")
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("Samples:", df.shape[0])
    print("Features:", X.shape[1])
    print("Coefficients (TV, Radio, Newspaper):", model.coef_)
    print("Intercept:", model.intercept_)
    print(f"MAE: {mae:.3f}  MSE: {mse:.3f}  RMSE: {rmse:.3f}  R2: {r2:.3f}")

    out_dir = repo_root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    vmin, vmax = min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())
    plt.plot([vmin, vmax], [vmin, vmax], "r--", label="Ideal")
    plt.xlabel("True Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Linear Regression: Advertising")
    plt.legend()
    out_file = out_dir / "linear_regression_predictions.png"
    plt.tight_layout()
    plt.savefig(out_file, dpi=150)
    print("Saved plot to:", out_file)


if __name__ == "__main__":
    main()
