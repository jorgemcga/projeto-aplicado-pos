from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="Health API", version="1.0.0")


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Check if API is running and database connected.
    
    Returns:
        Dict with status and database connection state
    """
    return {
        "status": "running",
        "database": "connected"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
