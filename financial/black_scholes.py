"""
Description:

The Black-Scholes model, also known as the Black-Scholes-Merton (BSM) model,
is one of the most important concepts in modern financial theory.
This mathematical equation estimates the theoretical value of derivatives based on other investment instruments,
taking into account the impact of time and other risk factors.
Developed in 1973, it is still regarded as one of the best ways for pricing an options contract.

Read more:
https://www.investopedia.com/terms/b/blackscholes.asp
"""
import numpy as np
from scipy.stats import norm

N = norm.cdf

"""
    black_scholes_nondiv(): Implementation of Black-Scholes formula for non-dividend paying options
    :param S: Current asset price
    :type S: float
    :param K: Strike price of the option
    :type K: float
    :param T: Time until option expiration
    :type T: float
    :param r: Risk-free interest rate.
    :type r: float
    :param sigma: Annualized volatility of the asset's returns
    :type sigma: float
    :param call_value: Takes input as "call", "put", "both"
    :type call_value: string
    :return: Price of the options
    :rtype: float. Returns a dictionary when call_value is set to "both"
"""


def black_scholes_nondiv(
    S: float, K: float, T: float, r: float, sigma: float, call_value="both"
) -> dict:
    """
    >>> black_scholes_nondiv(100, 100, 1, 0.05, 0.2, "call")
    {'call': 10.450583572185565}
    >>> black_scholes_nondiv(100, 100, 1, 0.05, 0.2, "put")
    {'put': 5.573526022256971}
    >>> black_scholes_nondiv(100, 100, 1, 0.05, 0.2, "both")
    {'put': 5.573526022256971, 'call': 10.450583572185565}
    """

    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    value = 0

    if call_value == "both":
        value_call = S * N(d1) - K * np.exp(-r * T) * N(d2)
        value_put = K * np.exp(-r * T) * N(-d2) - S * N(-d1)
        return {"put": value_put, "call": value_call}

    if call_value == "call":
        value = S * N(d1) - K * np.exp(-r * T) * N(d2)
        return {"call": value}

    elif call_value == "put":
        value = K * np.exp(-r * T) * N(-d2) - S * N(-d1)
        return {"put": value}

    return None


"""
    black_scholes_div(): Implementation of Black-Scholes formula for Dividend paying options
    :param S: Current asset price
    :type S: float
    :param K: Strike price of the option
    :type K: float
    :param T: Time until option expiration
    :type T: float
    :param r: Risk-free interest rate.
    :type r: float
    :param q: The dividend rate of the asset.
    :type q: float
    :param sigma: Annualized volatility of the asset's returns.
    :type sigma: float
    :param call_value: Takes input as "call", "put", "both"
    :type call_value: string
    :return: Price of the options
    :rtype: float. Returns a dictionary when call_value is set to "both"
"""


def black_scholes_div(
    S: float, K: float, T: float, r: float, q: float, sigma: float, call_value="both"
) -> dict:
    """
    >>> black_scholes_div(100, 100, 1, 0.05, 0.02, 0.2, "call")
    {'call': 9.227005508154036}
    >>> black_scholes_div(100, 100, 1, 0.05, 0.02, 0.2, "put")
    {'put': 6.330080627549918}
    >>> black_scholes_div(100, 100, 1, 0.05, 0.02, 0.2, "both")
    {'put': 6.330080627549918, 'call': 9.227005508154036}
    """

    d1 = (np.log(S / K) + (r - q + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    value = 0

    if call_value == "both":
        value_put = K * np.exp(-r * T) * N(-d2) - S * np.exp(-q * T) * N(-d1)
        value_call = S * np.exp(-q * T) * N(d1) - K * np.exp(-r * T) * N(d2)
        return {"put": value_put, "call": value_call}

    if call_value == "call":
        value = S * np.exp(-q * T) * N(d1) - K * np.exp(-r * T) * N(d2)
        return {"call": value}

    elif call_value == "put":
        value = K * np.exp(-r * T) * N(-d2) - S * np.exp(-q * T) * N(-d1)
        return {"put": value}

    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
