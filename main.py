import sqlite3
import pandas as pd

# -----------------------------
# Database connection
# -----------------------------
conn = sqlite3.connect("data.sqlite")


# -----------------------------
# Helper function (very important)
# -----------------------------
def run_query(query):
    """Executes SQL query and returns DataFrame"""
    return pd.read_sql_query(query, conn)