# Diligent E-Commerce Data Project

This repository was created as part of the Diligent A-SDLC Test Activity.

It includes:
- Synthetic e-commerce dataset (5 CSV files)
- Python loader script to create SQLite database
- SQL schema and join query examples

## How to Run

### 1. Install dependencies
pip install pandas

### 2. Load data into SQLite
python load_data.py

Produces:
ecommerce.db

### 3. Run SQL queries
sqlite3 ecommerce.db < sample_query.sql
