# Machine-learning-Orhan

Quick course scaffold using uv (modern Python package and environment manager), plus a runnable linear regression example on the Advertising dataset.

Getting started (Windows PowerShell)

1) Install uv if you don't have it yet

```powershell
pip install uv
```

2) Sync the environment for this project

```powershell
cd Machine-learning-Orhan
python -m uv sync
```

3) Run a quick sanity check

```powershell
python -m uv run python -c "import pandas, sklearn, matplotlib, numpy; print('env ok')"
```

4) Run the linear regression example and see metrics + plot

```powershell
python -m uv run python 03_linear_regression/linear_regression.py
```

Outputs are written to outputs/linear_regression_predictions.png

Tip (Windows): make `uv` a command without `python -m` using pipx

```powershell
pipx install uv
```

Notebook

- We include a Jupyter version at 03_linear_regression/linear_regression.ipynb.
- In VS Code, open the notebook and select the `.venv` kernel if asked.
- Or run from terminal:

```powershell
python -m uv run jupyter nbconvert --to notebook --execute 03_linear_regression/linear_regression.ipynb --output executed.ipynb
```

Terminology (uv)

- pyproject.toml: project metadata and dependencies
- .python-version: default Python version for the project
- uv sync: create/update the virtual env from pyproject
- uv run <cmd>: run a command inside the project environment
- uv add <pkg>: add and install a dependency

Project layout

- pyproject.toml
- .python-version
- .gitignore
- main.py
- 00_intro/
- 01_course_structure/
- 02_setup/
- 03_linear_regression/
	- advertising.csv
	- linear_regression.py
	- linear_regression.ipynb
- outputs/ (created at runtime)