from fastapi import Body
from fastapi.routing import APIRouter
from pydantic import conlist

from app.models.numbers import NumbersResponse, ComparisonResponse, MathFunctionsResponse, \
    RandomResponse, TwoNumbersResponse, TwoNumbersRequest, MultipleNumbersResponse, MultipleNumbersRequest, \
    SingleNumberResponse, SingleNumberRequest
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


# ---------- Single input ----------
@router.post("/single", response_model=SingleNumberResponse, summary="Operations on a single number")
async def single_number(request: SingleNumberRequest) -> SingleNumberResponse:
    n = request.number
    return numbers_service.single_number(n)


# ---------- Two inputs ----------
@router.post("/double", response_model=TwoNumbersResponse, summary="Operations on two numbers")
async def two_numbers(request: TwoNumbersRequest) -> TwoNumbersResponse:
    a, b = request.a, request.b

    return numbers_service.two_numbers(a, b)


# ---------- Multiple inputs ----------
@router.post("/multiple", response_model=MultipleNumbersResponse, summary="Operations on multiple numbers")
async def multiple_numbers(request: MultipleNumbersRequest) -> MultipleNumbersResponse:
    numbers = request.numbers
    return numbers_service.multiple_numbers(numbers)
