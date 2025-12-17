# 02 – Setup (uv)

Det här projektet använder uv för modern och snabb paket‑/miljöhantering.

1) Installera uv (utan PATH‑strul)

```powershell
python -m pip install -U uv
```

2) Synka miljön från pyproject.toml

```powershell
cd C:\Users\OU\Desktop\MachineLearning\Machine-learning-Orhan
python -m uv sync
```

3) Snabbkontroll

```powershell
python -m uv run python -c "import pandas, sklearn, matplotlib, numpy; print('env ok')"
```

4) Kör första exemplet

```powershell
python -m uv run python 03_linear_regression/linear_regression.py
```

Terminologi (kort)
- pyproject.toml: projektmetadata + beroenden
- .python-version: standard‑Python för projektet
- `python -m uv run <kommando>`: kör inuti projektmiljön
- `python -m uv add <paket>`: lägg till och installera ett paket
