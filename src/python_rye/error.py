def add_numbers(a: int, b: int) -> int:
    """Add"""
    error_point = "error"
    return a + b


# pyright check error
result = add_numbers(10, "20")
