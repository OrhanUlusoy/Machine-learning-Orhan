# 03 – Linear regression (Advertising)

Filer
- advertising.csv – datamängd (200 rader)
- linear_regression.py – skriptversion
- linear_regression.ipynb – notebook‑version

Körning (skript)
```powershell
cd C:\Users\OU\Desktop\MachineLearning\Machine-learning-Orhan
python -m uv run python 03_linear_regression/linear_regression.py
```

Vad som händer
1. Train|test‑split (30% test, `random_state=42`)
2. Skalning med MinMaxScaler
3. Träning av `LinearRegression`
4. Utskrift av MAE, MSE, RMSE, R²
5. Figur (pred vs. truth) sparas till `outputs/linear_regression_predictions.png`
