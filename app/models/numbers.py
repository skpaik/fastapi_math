from typing import List, Optional

from pydantic import BaseModel, Field, conlist


class NumbersResponse(BaseModel):
    input: List[int]
    sum: int
    product: int
    min: int
    max: int
    average: float


class NumbersResponse(BaseModel):
    input: List[int]
    total_sum: int = Field(..., example=20)
    even_sum: int = Field(..., example=6)
    odd_sum: int = Field(..., example=14)
    average: float = Field(..., example=2.857)
    max: int = Field(..., example=5)
    min: int = Field(..., example=1)
    median: float = Field(..., example=3)
    mode: List[int] = Field(..., example=[2, 3])
    std_dev: float = Field(..., example=1.676)
    count: int = Field(..., example=7)

    class Config:
        json_schema_extra = {
            "example": {
                "input": [1, 2, 6, 9],
                "total_sum": 20,
                "even_sum": 6,
                "odd_sum": 14,
                "average": 2.857,
                "max": 5,
                "min": 1,
                "median": 3,
                "mode": [2, 3],
                "std_dev": 1.676,
                "count": 7,
            }
        }


class NumbersRequest(BaseModel):
    numbers: conlist(int, min_length=1)


class ComparisonResponse(BaseModel):
    input: List[int]
    greater_than_zero: List[int]
    even_numbers: List[int]
    odd_numbers: List[int]


class MathFunctionsResponse(BaseModel):
    input: List[int]
    square_roots: List[float]
    squares: List[int]
    ceilings: List[int]
    floors: List[int]


class RandomResponse(BaseModel):
    random_int: int
    random_float: float


# ---------- Single input ----------
class SingleNumberRequest(BaseModel):
    number: int


class SingleNumberResponse(BaseModel):
    input: int
    square: int
    cube: int
    sqrt: float


# ---------- Two inputs ----------
class TwoNumbersRequest(BaseModel):
    a: int
    b: int


class TwoNumbersResponse(BaseModel):
    a: int
    b: int
    sum: int
    difference: int
    product: int
    quotient: float
    modulus: int
    power: int


# ---------- Multiple inputs ----------
class MultipleNumbersRequest(BaseModel):
    numbers: conlist(int, min_length=1)


class MultipleNumbersResponse(BaseModel):
    input: List[int]
    sum: int
    average: float
    min: int
    max: int
    product: int


# ---------- Modulus & Exponentiation ----------
class TwoNumbersRequest(BaseModel):
    a: int
    b: int


class ModulusResponse(BaseModel):
    a: int
    b: int
    modulus: Optional[int]


class ExponentiationResponse(BaseModel):
    a: int
    b: int
    result: int


# ---------- Logarithms ----------
class LogarithmRequest(BaseModel):
    number: float
    base: Optional[float] = None  # default = natural log


class LogarithmResponse(BaseModel):
    input: float
    base: Optional[float]
    result: float


# ---------- Complex numbers ----------
class ComplexNumbersRequest(BaseModel):
    real: float
    imag: float


class ComplexNumbersResponse(BaseModel):
    input: complex
    conjugate: complex
    magnitude: float
    phase: float
