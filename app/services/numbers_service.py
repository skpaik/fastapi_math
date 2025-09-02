import statistics

from app.models.numbers import NumbersResponse


def analyze_numbers_service(numbers: list[int]) -> NumbersResponse:
    """
    Business logic for analyzing numbers.
    """
    numbers_len = len(numbers)
    numbers_sum = sum(numbers)
    even_sum = sum(n for n in numbers if n % 2 == 0)

    return NumbersResponse(
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
