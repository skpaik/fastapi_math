from fastapi import Body
from fastapi.routing import APIRouter
from pydantic import conlist

from app.models.numbers import NumbersResponse, ComparisonResponse, MathFunctionsResponse, \
    RandomResponse, TwoNumbersResponse, TwoNumbersRequest, MultipleNumbersResponse, MultipleNumbersRequest, \
    SingleNumberResponse, SingleNumberRequest, ComplexNumbersResponse, ComplexNumbersRequest, LogarithmResponse, \
    LogarithmRequest, ExponentiationResponse, ModulusResponse
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
@router.post("/single",
             response_model=SingleNumberResponse,
             summary="Operations on a single number")
async def single_number(
        request: SingleNumberRequest = Body(..., example={"number": 9})) -> SingleNumberResponse:
    n = request.number
    return numbers_service.single_number(n)


# ---------- Two inputs ----------
@router.post("/double",
             response_model=TwoNumbersResponse,
             summary="Operations on two numbers")
async def two_numbers(
        request: TwoNumbersRequest = Body(..., example={"a": 10, "b": 3})) -> TwoNumbersResponse:
    a, b = request.a, request.b

    return numbers_service.two_numbers(a, b)


# ---------- Multiple inputs ----------
@router.post("/multiple",
             response_model=MultipleNumbersResponse,
             summary="Operations on multiple numbers")
async def multiple_numbers(
        request: MultipleNumbersRequest = Body(..., example={"numbers": [2, 4, 6]})) -> MultipleNumbersResponse:
    numbers = request.numbers
    return numbers_service.multiple_numbers(numbers)


# ---------- Modulus ----------
@router.post("/modulus",
             response_model=ModulusResponse,
             summary="Modulus of two numbers")
async def modulus(
        request: TwoNumbersRequest = Body(..., example={"a": 10, "b": 3})) -> ModulusResponse:
    a, b = request.a, request.b
    return numbers_service.modulus(a, b)


# ---------- Exponentiation ----------
@router.post("/exponent",
             response_model=ExponentiationResponse,
             summary="Exponentiation (a^b)")
async def exponent(
        request: TwoNumbersRequest = Body(..., example={"a": 2, "b": 8})) -> ExponentiationResponse:
    a, b = request.a, request.b
    return numbers_service.exponent(a, b)


# ---------- Logarithms ----------
@router.post("/logarithm",
             response_model=LogarithmResponse,
             summary="Logarithm of a number")
async def logarithm(
        request: LogarithmRequest = Body(..., example={"number": 100, "base": 10})) -> LogarithmResponse:
    n, base = request.number, request.base
    return numbers_service.logarithm(n, base)


# ---------- Complex numbers ----------
@router.post("/complex",
             response_model=ComplexNumbersResponse,
             summary="Operations on a complex number")
async def complex_numbers(
        request: ComplexNumbersRequest = Body(..., example={"real": 3, "imag": 4})) -> ComplexNumbersResponse:
    z = complex(request.real, request.imag)
    return numbers_service.complex_numbers(z)
