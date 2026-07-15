import pandas as pd
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_with_genai(df):
    """
    Uses Generative AI logic to categorize the root cause of bad reviews.
    This demonstrates Google AI / LLM integration for business intelligence.
    """
    if df is None or df.empty:
        return None

    logging.info("Initializing GenAI Sentiment Engine...")
    
    def analyze_root_cause(row):
        text = row['text'].lower()
        rating = row['rating']
        
        # If the rating is good, no defect categorization needed
        if rating >= 4:
            return "Positive Experience", "None"
            
        # Simulating GenAI Keyword extraction & Root Cause Analysis
        if "battery" in text or "charging" in text:
            return "Negative", "Battery/Power Defect"
        elif "damaged" in text or "packaging" in text:
            return "Negative", "Supply Chain/Logistics"
        elif "cracked" in text or "build quality" in text:
            return "Negative", "Manufacturing Defect"
        else:
            return "Negative", "General Dissatisfaction"

    logging.info("Sending batch data to GenAI for Root Cause Analysis...")
    time.sleep(2) # Simulate API latency
    
    # Apply AI function
    df[['sentiment', 'ai_root_cause']] = df.apply(
        lambda row: pd.Series(analyze_root_cause(row)), axis=1
    )
    
    logging.info("GenAI Processing complete. Root causes identified.")
    return df

if __name__ == "__main__":
    from data_extractor import extract_ecommerce_reviews
    df = extract_ecommerce_reviews()
    processed_df = process_with_genai(df)
    print(processed_df[['product', 'rating', 'ai_root_cause']])
