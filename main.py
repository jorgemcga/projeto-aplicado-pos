import os
import logging
from fastapi import FastAPI
from typing import Dict
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Carregar variáveis do .env
load_dotenv()

app = FastAPI(title="Health API", version="1.0.0")

logger = logging.getLogger("uvicorn")

# Configurar conexão PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = None
if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
else:
    logger.warning("DATABASE_URL not configured")


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Check if API is running and database connected.
    
    Returns:
        Dict with status and database connection state
    """
    database_status = "disconnected"
    
    if engine:
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            database_status = "connected"
            logger.info("Database connection successful")
        except Exception as e:
            database_status = f"disconnected: {str(e)}"
            logger.error(f"Database connection failed: {str(e)}")
    else:
        database_status = "not_configured"
        logger.warning("Database not configured")
    
    return {
        "status": "running",
        "database": database_status
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
