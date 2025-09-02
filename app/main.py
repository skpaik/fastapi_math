from fastapi import FastAPI

from app.api import numbers

app = FastAPI(
    title="Number Analyzer API",
    description="API to analyze a list of integers and return useful statistics.",
    version="1.0.0",
)

# Register routers
app.include_router(numbers.router)


@app.get("/", summary="Home")
async def home():
    return {"Hello": "Open the docs links"}


@app.get("/health", summary="Health check")
async def health():
    return {"status": "ok"}
