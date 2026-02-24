# Streamlit App

Sales Dashboard to practise using Streamlit.

**Skills** : App creation, visualisation

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42+-red)

---

## Dashboard

This Dashboard includes :

- **Dummies Sales data**
- **KPI Cards**
- **Plotly Charts** 
- **Filters** (dates, category, regions)
- **Tables** 

---

## Requirements

To run this app locally, you should install:

### 1. Python 3.12

Vérifiez votre version :
```bash
python --version
```

### 2. uv

**uv** is a very fast Python package management. 

To Install :

**macOS / Linux :**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell) :**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Post install, check :
```bash
uv --version
```

---

## Quick Start

```bash
#1.
git clone <project>

#2.
cd streamlit-quick-app

#3. Install the project dependencies
make setup

#4. Générer les données exemple
uv run python scripts/refresh_data.py

#5. Launch the app
make run
```
The app will be launched on **http://localhost:8501**




## Fonctionnalitiess

### Pages incluses

| Page | Description |
|------|-------------|
| **Overview** | Key KPIs, trend chart, breakdown by category, top performers |
| **Details** | Interactive table with advanced filters, CSV export, detailed statistics |

---


---

## CLI

| Commande | Description |
|----------|-------------|

| `make setup` | Installs dependencies using uv |

| `make run` | Starts the Streamlit application |

| `make lint` | Checks code quality with Ruff |

| `make test` | Runs tests with pytest |

| `make refresh-data` | Regenerates sample data |

| `make clean` | Removes temporary files |

---