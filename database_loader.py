import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_to_warehouse(df, db_name='ecommerce_insights.db', table_name='review_analysis'):
    """
    Loads the AI-processed data into a structured SQLite Data Warehouse.
    """
    if df is None or df.empty:
        logging.warning("No data to load.")
        return

    logging.info(f"Connecting to Data Warehouse: {db_name}")
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        # Save to SQL, replace if it exists for this demo, usually we append
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        logging.info(f"Successfully loaded {len(df)} structured records into '{table_name}'.")
    except Exception as e:
        logging.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
