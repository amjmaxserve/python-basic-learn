# 📦 Inventory Analytics Project

A Python project that generates a realistic product inventory dataset, analyses it by supplier, and produces an enriched Excel report — all using only the `openpyxl` standard library wrapper.

---

## 📁 Project Structure

```
python-learn/
├── generate_inventory.py          # Step 1 — Generate the source Excel file
├── inventory.xlsx                 # Generated source data (1 000 products)
├── main.py                        # Step 2 — Analyse & enrich the Excel file
├── inventory_with_total_value.xlsx  # Output report with Total Inventory Price
└── requirements.txt               # Python dependencies
```

---

## 🗂️ File Descriptions

### `generate_inventory.py`
Generates the source dataset **`inventory.xlsx`** with **1 000 product rows** across four columns:

| Column | Type | Description |
|--------|------|-------------|
| **Product Number** | Integer (1–1000) | Sequential unique product ID |
| **Inventory** | Integer (0–2000) | Current stock quantity |
| **Price ($)** | Float | Price based on product category |
| **Supplier** | String | One of 10 named suppliers |

**Key features:**
- Products are assigned to one of **8 categories** (`ELEC`, `FURN`, `CLTH`, `FOOD`, `TOOL`, `BOOK`, `SPRT`, `HOME`), each with a realistic price range
- **10 suppliers** are randomly distributed across all products
- Low-stock rows (inventory < 20) are highlighted in **red bold** for quick visual identification
- Header row uses deep **navy blue** styling with white bold text
- **Alternating row colours** (light blue / white) for readability
- **Auto-filter** and **frozen header row** enabled out of the box
- Uses `random.seed(42)` so the dataset is fully **reproducible**

---

### `main.py`
Reads `inventory.xlsx`, performs three aggregations grouped by supplier, then writes the result back as a new enriched file.

#### Aggregations computed

| Dictionary | What it stores |
|-----------|----------------|
| `products_per_supplier` | Number of product lines per supplier |
| `total_inventory_per_supplier` | Total stock units held per supplier |
| `total_value_per_supplier` | Total inventory value (`inventory × price`) per supplier |

#### How it works — step by step

```
1. Load inventory.xlsx → "Inventory" sheet
2. Loop 1 — Count product lines per supplier
3. Loop 2 — Sum inventory units per supplier
4. Loop 3 — Sum inventory value (inventory × price) per supplier
5. Write "Total Inventory Price ($)" as a new Column E (styled to match existing headers)
6. Save result as inventory_with_total_value.xlsx (original file untouched)
7. Print a formatted summary table to the console
```

#### Console output (sample)

```
✅  inventory_with_total_value.xlsx created with 'Total Inventory Price' column.

── Products per supplier ──
  Apex Trade Group               104 products
  BlueStar Logistics             100 products
  ...

── Total inventory units per supplier ──
  Apex Trade Group               97686 units
  BlueStar Logistics             103383 units
  ...

── Total inventory value per supplier ──
  Apex Trade Group               $25,865,047.10
  BlueStar Logistics             $28,436,853.80
  ...
```

---

### `inventory.xlsx`
Auto-generated source file created by `generate_inventory.py`.  
**Do not edit manually** — re-run the generator script to recreate it.

---

### `inventory_with_total_value.xlsx`
The enriched output file produced by `main.py`.  
It is identical to `inventory.xlsx` but includes an additional **Column E — "Total Inventory Price ($)"** showing the total inventory value for each product's supplier across all their products.

---

## ⚙️ Requirements

- **Python 3.x**
- **openpyxl** (third-party library for reading/writing Excel `.xlsx` files)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Step 1 — Generate the source inventory data

```bash
python3 generate_inventory.py
```

This creates `inventory.xlsx` with 1 000 styled product rows.

### Step 2 — Analyse and produce the enriched report

```bash
python3 main.py
```

This reads `inventory.xlsx`, computes supplier-level aggregations, and outputs:
- **`inventory_with_total_value.xlsx`** — Excel report with the new "Total Inventory Price" column
- **Console summary** — tabulated breakdown of products, units, and total value per supplier

> **Note:** Run Step 1 first before Step 2. `main.py` reads from `inventory.xlsx` which must exist.

---

## 🧠 Concepts Used

| Concept | Where used |
|---------|-----------|
| `openpyxl` — load & save workbooks | `main.py`, `generate_inventory.py` |
| `openpyxl` — cell styling (Font, Fill, Border, Alignment) | Both files |
| Python **dictionaries** | Aggregation logic in `main.py` |
| **`for` loops** | Iterating over all 1 000 rows |
| **`if / else`** conditionals | Dictionary accumulation pattern |
| `random` module with seed | Reproducible data generation |
| f-strings | Formatted console output |
| Auto-filter & frozen panes | Excel UX in `generate_inventory.py` |

---

## 📊 Supplier Summary (from last run)

| Supplier | Products | Total Units | Total Value |
|----------|----------|-------------|-------------|
| Apex Trade Group | 104 | 97,686 | $25,865,047 |
| BlueStar Logistics | 100 | 103,383 | $28,436,854 |
| EcoSource Inc. | 111 | 104,017 | $29,283,166 |
| FastTrack Wholesale | 95 | 94,240 | $28,150,913 |
| Global Parts Ltd. | 109 | 106,744 | $26,380,798 |
| NextGen Supply | 94 | 98,664 | $26,939,382 |
| Pinnacle Traders | 111 | 113,250 | $35,945,354 |
| Prime Distributors | 98 | 99,225 | $31,905,650 |
| TechSupplies Co. | 69 | 64,630 | $18,082,687 |
| Vertex Supply Chain | 109 | 103,867 | $24,747,148 |

---

*Built with Python 3 and openpyxl.*
