import math
import cmath  # for complex numbers
import random
import statistics

from app.models.numbers import NumbersResponse, ComparisonResponse, MathFunctionsResponse, RandomResponse, \
    SingleNumberResponse, TwoNumbersResponse, MultipleNumbersResponse, ModulusResponse, ExponentiationResponse, \
    LogarithmResponse, ComplexNumbersResponse


class NumbersService:
    def analyze_numbers(self, numbers: list[int]) -> NumbersResponse:
        """
        Business logic for analyzing numbers.
        """
        numbers_len = len(numbers)
        numbers_sum = sum(numbers)
        even_sum = sum(n for n in numbers if n % 2 == 0)

        return NumbersResponse(
            input=numbers,
            total_sum=numbers_sum,
            even_sum=even_sum,
            odd_sum=numbers_sum - even_sum,
            average=numbers_sum / numbers_len,
            max=max(numbers),
            min=min(numbers),
            median=statistics.median(numbers),
            mode=statistics.multimode(numbers),
            std_dev=statistics.stdev(numbers) if numbers_len > 1 else 0.0,
            count=numbers_len,
        )

    def compare_numbers(self, numbers: list[int]) -> ComparisonResponse:
        """
        Business logic for analyzing numbers.
        """
        return ComparisonResponse(
            input=numbers,
            greater_than_zero=[n for n in numbers if n > 0],
            even_numbers=[n for n in numbers if n % 2 == 0],
            odd_numbers=[n for n in numbers if n % 2 != 0]
        )

    def math_functions(self, numbers: list[int]) -> MathFunctionsResponse:
        return MathFunctionsResponse(
            input=numbers,
            square_roots=[math.sqrt(n) for n in numbers],
            squares=[n ** 2 for n in numbers],
            ceilings=[math.ceil(n + 0.1) for n in numbers],  # just example adjustment
            floors=[math.floor(n + 0.9) for n in numbers]
        )

    def random_numbers(self) -> RandomResponse:
        return RandomResponse(
            random_int=random.randint(1, 100),
            random_float=random.random()
        )

    def single_number(self, n) -> SingleNumberResponse:
        return SingleNumberResponse(
            input=n,
            square=n ** 2,
            cube=n ** 3,
            sqrt=math.sqrt(n) if n >= 0 else float("nan")
        )

    def two_numbers(self, a, b) -> TwoNumbersResponse:
        return TwoNumbersResponse(
            a=a,
            b=b,
            sum=a + b,
            difference=a - b,
            product=a * b,
            quotient=a / b if b != 0 else float("inf"),
            modulus=a % b if b != 0 else None,
            power=a ** b
        )

    def multiple_numbers(self, numbers) -> MultipleNumbersResponse:
        total = sum(numbers)
        product = 1

        for n in numbers:
            product *= n

        return MultipleNumbersResponse(
            input=numbers,
            sum=total,
            average=total / len(numbers),
            min=min(numbers),
            max=max(numbers),
            product=product
        )

    def modulus(self, a, b) -> ModulusResponse:
        return ModulusResponse(
            a=a,
            b=b,
            modulus=a % b if b != 0 else None
        )

    def exponent(self, a, b) -> ExponentiationResponse:
        return ExponentiationResponse(a=a, b=b, result=a ** b)

    def logarithm(self, n, base) -> LogarithmResponse:
        if n <= 0:
            result = float("nan")
        elif base is None:
            result = math.log(n)  # natural log
        else:
            result = math.log(n, base)

        return LogarithmResponse(input=n, base=base, result=result)

    def complex_numbers(self, z) -> ComplexNumbersResponse:
        return ComplexNumbersResponse(
            input=z,
            conjugate=z.conjugate(),
            magnitude=abs(z),
            phase=cmath.phase(z)
        )
