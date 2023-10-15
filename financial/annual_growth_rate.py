def calculate_annual_growth_rate(initial_value, final_value, num_years):
    if initial_value <= 0 or final_value <= 0 or num_years <= 0:
        raise ValueError(
            "Initial value, final value, and number of years must be positive numbers."
        )

    annual_growth_rate = ((final_value / initial_value) ** (1 / num_years)) - 1
    return annual_growth_rate


# Example usage:
initial_value = 1000  # Initial value
final_value = 1500  # Final value after a certain number of years
num_years = 5  # Number of years

growth_rate = calculate_annual_growth_rate(initial_value, final_value, num_years)
print(f"The annual growth rate is {growth_rate:.2%}")
