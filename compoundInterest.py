# interest = P [(1 + i)**n – 1]
# P = principal
# i = nominal annual interest rate in percentage terms
# n = number of compounding periods


def get_compound_interest(principal, interest_rate, period) -> int:
    """calculates compound interest given principal, interest rate and period of time"""
    rate_calculation = (1 + interest_rate) ** period
    interest = principal * (rate_calculation - 1)
    return interest

print(get_compound_interest(10000, 0.05, 3))