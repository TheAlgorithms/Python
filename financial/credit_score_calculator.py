# Import necessary libraries
import math


# Define a function to calculate the credit score
def calculate_credit_score():
    # Gather information from the user
    age = int(input("Enter your age: ").strip())
    credit_history_months = int(input("Enter your credit history in months: ").strip())
    annual_income = float(input("Enter your annual income: $").strip())
    total_debt = float(input("Enter your total debt: $").strip())
    outstanding_credit = float(input("Enter your outstanding credit amount: $").strip())
    recent_delinquencies = int(
        input("Enter recent delinquencies (last 12 months): ".strip())
    )
    credit_utilization = float(
        input("Enter your credit utilization ratio (0-1): ").strip()
    )

    # Define weight factors for each category
    age_weight = 0.1
    credit_history_weight = 0.2
    income_weight = 0.15
    debt_weight = 0.15
    recent_delinquencies_weight = 0.1
    credit_utilization_weight = 0.2
    outstanding_credit_weight = 0.1

    # Calculate a base score (scaled to a maximum of 850)
    base_score = 500  # A base score for a person with average characteristics
    base_score += age * age_weight
    base_score += (credit_history_months / 12) * credit_history_weight
    base_score += (math.log(annual_income) / 10) * income_weight
    base_score -= (total_debt / annual_income) * debt_weight
    base_score -= recent_delinquencies * recent_delinquencies_weight
    base_score -= (1 - credit_utilization) * credit_utilization_weight
    base_score += (outstanding_credit / annual_income) * outstanding_credit_weight

    # Adjust the base score to be within the range 300-850
    base_score = max(300, min(850, base_score))

    return base_score


if __name__ == "__main__":
    credit_score = calculate_credit_score()
    print(f"Your credit score is: {credit_score:.2f}")
