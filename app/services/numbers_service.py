import math
import random
import statistics

from app.models.numbers import NumbersResponse, ComparisonResponse, MathFunctionsResponse, RandomResponse


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
