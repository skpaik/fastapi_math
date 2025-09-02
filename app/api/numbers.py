from fastapi import Body
from fastapi.routing import APIRouter
from pydantic import conlist

from app.models.numbers import NumbersResponse, ComparisonResponse, MathFunctionsResponse, \
    RandomResponse
from app.services.numbers_service import NumbersService

router = APIRouter(prefix="/numbers", tags=["Numbers"])

numbers_service = NumbersService()


# ----------------- Arithmetic -----------------
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
    return numbers_service.analyze_numbers(numbers)


# ----------------- Comparisons -----------------
@router.post("/compare-numbers",
             response_model=ComparisonResponse,
             summary="Number comparisons")
async def compare_numbers(numbers: conlist(int, min_length=1) = Body(..., example=[-2, 0, 5, 8])) -> ComparisonResponse:
    return numbers_service.compare_numbers(numbers)


# ----------------- Math functions -----------------
@router.post("/math-functions",
             response_model=MathFunctionsResponse,
             summary="Math functions on numbers")
async def math_functions(
        numbers: conlist(int, min_length=1) = Body(..., example=[1, 4, 9, 16])) -> MathFunctionsResponse:
    return numbers_service.math_functions(numbers)


# ----------------- Random numbers -----------------
@router.get("/random-number",
            response_model=RandomResponse,
            summary="Generate random numbers")
async def random_numbers():
    return numbers_service.random_numbers()
