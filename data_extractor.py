import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_ecommerce_reviews():
    """
    Simulates extracting customer reviews from an E-Commerce platform.
    In a real scenario, this would connect to an API or scrape a website.
    """
    logging.info("Extracting customer reviews from E-commerce source...")
    
    # Simulating raw extracted data
    raw_data = [
        {"review_id": "R101", "product": "Wireless Headphones", "rating": 2, "text": "The sound is okay but the battery dies after 2 hours. Very disappointed."},
        {"review_id": "R102", "product": "Smart Watch", "rating": 5, "text": "Amazing product, tracks my heart rate perfectly and delivery was fast."},
        {"review_id": "R103", "product": "Wireless Headphones", "rating": 1, "text": "Stopped charging completely after 1 week. Worst purchase."},
        {"review_id": "R104", "product": "Gaming Mouse", "rating": 3, "text": "Good response time, but the packaging was damaged when it arrived."},
        {"review_id": "R105", "product": "Smart Watch", "rating": 1, "text": "The screen cracked on day 2 without dropping it. Build quality is poor."},
        {"review_id": "R106", "product": "Gaming Mouse", "rating": 5, "text": "Best mouse ever. Smooth and ergonomic."}
    ]
    
    df = pd.DataFrame(raw_data)
    logging.info(f"Successfully extracted {len(df)} reviews.")
    return df

if __name__ == "__main__":
    df = extract_ecommerce_reviews()
    print(df.head())
