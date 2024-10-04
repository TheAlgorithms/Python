def calculate_rsi(prices, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given list of prices.
    
    RSI is a momentum oscillator that measures the speed and change of price movements.
    It is typically used to identify overbought or oversold conditions in a market.
    
    Args:
        prices (list of float): A list of prices for a financial asset.
        period (int): The number of periods to use in the calculation (default is 14).
        
    Returns:
        list of float: A list of RSI values corresponding to the input price data.
    """
    
    # Initialize lists to store gains and losses
    gains = []
    losses = []
    
    # Loop through the prices starting from the second one (since we compare prices[i] with prices[i-1])
    for i in range(1, len(prices)):
        # Calculate the price difference from the previous day
        delta = prices[i] - prices[i - 1]
        
        # If delta is positive, it's a gain. Otherwise, it's a loss.
        if delta > 0:
            gains.append(delta)   # Positive change is a gain
            losses.append(0)      # No loss on this day
        else:
            gains.append(0)       # No gain on this day
            losses.append(abs(delta))  # Negative change becomes a loss

    # Calculate the initial average gain and loss for the first 'period' number of data points
    # This is the simple moving average (SMA) for the first 'period' values
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    # Initialize a list to store the RSI values that we will calculate
    rsi_values = []

    # Calculate the first RSI value:
    # RSI is 100 if there's no loss (i.e., avg_loss == 0), otherwise, it's based on RS (Relative Strength)
    if avg_loss == 0:
        rsi = 100  # If there's no loss, RSI is set to 100 (overbought condition)
    else:
        rs = avg_gain / avg_loss  # Relative Strength (RS)
        rsi = 100 - (100 / (1 + rs))  # RSI formula

    # Add the first RSI value to the list
    rsi_values.append(rsi)

    # Now, we calculate RSI for the rest of the data using the smoothed moving average technique
    for i in range(period, len(prices) - 1):
        # Calculate the price change from the previous day
        delta = prices[i] - prices[i - 1]

        # Calculate the gain and loss for this day
        gain = max(0, delta)  # Gain is positive changes only
        loss = max(0, -delta)  # Loss is the absolute value of negative changes

        # Smooth the average gain and average loss over time (using previous averages)
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

        # Calculate the RSI based on the updated averages
        if avg_loss == 0:
            rsi = 100  # If avg_loss is zero, RSI is 100 (overbought)
        else:
            rs = avg_gain / avg_loss  # Calculate the new Relative Strength
            rsi = 100 - (100 / (1 + rs))  # Calculate the new RSI value

        # Append the RSI value to our list of results
        rsi_values.append(rsi)

    return rsi_values


# Example usage:
if __name__ == "__main__":
    # Example list of daily closing prices for a financial asset (e.g., stock or currency pair)
    prices = [44, 44.15, 44.09, 44.20, 44.30, 44.25, 44.40, 44.35, 44.50, 44.60, 44.55, 44.75, 44.80, 44.70, 44.85]

    # Call the RSI calculation function with the list of prices
    rsi = calculate_rsi(prices)

    # Print the calculated RSI values
    print("RSI Values:", rsi)
