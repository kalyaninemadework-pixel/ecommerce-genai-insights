import logging
from data_extractor import extract_ecommerce_reviews
from genai_sentiment_processor import process_with_genai
from database_loader import load_to_warehouse

# Configure master logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("genai_pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("GenAI_Orchestrator")

def run():
    logger.info("==================================================")
    logger.info("🚀 Starting Universal E-Commerce GenAI Pipeline...")
    logger.info("==================================================")
    
    # Phase 1
    logger.info("[PHASE 1] Data Extraction")
    raw_data = extract_ecommerce_reviews()
    
    # Phase 2
    logger.info("[PHASE 2] AI Transformation & Sentiment Analysis")
    structured_data = process_with_genai(raw_data)
    
    # Phase 3
    logger.info("[PHASE 3] Loading to Data Warehouse")
    load_to_warehouse(structured_data)
    
    logger.info("==================================================")
    logger.info("✅ Pipeline Execution Complete. Data is ready for BI.")
    logger.info("==================================================")

if __name__ == "__main__":
    run()
