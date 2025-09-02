from fastapi import APIRouter, Body
from pydantic import conlist

from app.models.numbers import NumbersResponse
from app.services.numbers_service import analyze_numbers_service

router = APIRouter(prefix="/numbers", tags=["Numbers"])


@router.post("/positive-list",
             response_model=NumbersResponse,
             summary="Analyze numbers")
async def analyze_numbers(
        numbers: conlist(int, min_length=1) = Body(..., example=[1, 2, 3, 4, 5])
) -> NumbersResponse:
    """
    Analyze a list of integers provided as a raw JSON array.

    Example request body: `[1, 2, 3, 4, 5]`
    """
    return analyze_numbers_service(numbers)
