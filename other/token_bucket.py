# Implementation of Token Bucket Algorithm
# Token `rate` is added to the bucket every `frequency` in seconds.
# The bucket can hold tokens up to `capacity` (full).
# The bucket starts full.
# Each request consume one token.
# If a token arrives when the bucket is full, token is discarded.
# If a request arrives when bucket is empty, request will be discarded.
# If bucket has tokens available, requests will pass.
# https://en.wikipedia.org/wiki/Token_bucket
import threading
import time


class TokenBucketRateLimiter:
    def __init__(self, rate: int, capacity: int, frequency: int) -> None:
        """
        Initialize a Token Bucket rate limiter.

        :param rate: Number of tokens added to the bucket per refill
        :param capacity: Maximum number of tokens the bucket can hold.
        :param frequency: Frequency of refill in seconds
        >>> bucket = TokenBucketRateLimiter(4, 4, 60)
        >>> bucket.tokens
        4
        >>> bucket.capacity
        4
        >>> bucket.frequency
        60
        """
        self.rate = rate  # Tokens added per refill
        self.capacity = capacity  # Maximum capacity of the bucket
        self.frequency = frequency  # Frequency tokens are refilled
        self.tokens = capacity  # Current tokens in the bucket
        self.last_checked = time.time()  # Time when tokens were last checked
        self.lock = threading.Lock()  # To make the rate limiter thread-safe

    def _add_tokens(self) -> None:
        """
        Refill tokens only when a full minute has passed.
        >>> bucket = TokenBucketRateLimiter(1, 4, 60)
        >>> bucket.tokens  # Initially has 4 token (rate)
        4
        >>> bucket._add_tokens()
        >>> bucket.tokens  # Bucket already full
        4
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_checked

        if elapsed_time >= self.frequency:
            minutes_passed = int(elapsed_time // self.frequency)

            # Add tokens based on rate
            added_tokens = minutes_passed * self.rate
            self.tokens = min(self.capacity, self.tokens + added_tokens)

            # Update the last checked time
            self.last_checked += minutes_passed * self.frequency

    def allow_request(self) -> bool:
        """
        Check if a request is allowed.
        If there are enough tokens, it consumes one token.
        :return: True if the request is allowed, False otherwise.
        >>> bucket = TokenBucketRateLimiter(1, 2, 60)
        >>> bucket.allow_request()  # Token is available, request passes
        True
        >>> bucket.allow_request()  # Token is available, request passes
        True
        >>> bucket.allow_request()  # No token left, request is dropped
        False
        """
        with self.lock:
            self._add_tokens()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Allow 4 requests per minute, capacity of 4")
    bucket = TokenBucketRateLimiter(4, 4, 60)
    total_requests = 10
    delay_in_seconds = 10
    print("Simulate 1 request per 10 seconds...")
    for i in range(total_requests):
        result = "pass" if bucket.allow_request() else "dropped"
        print(
            f"Request {i+1}/{total_requests} \
            timeline: {i*delay_in_seconds} seconds = {result}"
        )
        time.sleep(delay_in_seconds)
