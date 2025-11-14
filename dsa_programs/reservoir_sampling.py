"""Reservoir sampling for streaming data."""

import random
from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def reservoir_sample(stream: Iterable[T], k: int, rng: Optional[random.Random] = None) -> List[T]:
    if k <= 0:
        raise ValueError("Sample size must be positive")
    rand = rng or random.Random()
    reservoir: List[T] = []
    for idx, item in enumerate(stream):
        if idx < k:
            reservoir.append(item)
        else:
            replace_at = rand.randint(0, idx)
            if replace_at < k:
                reservoir[replace_at] = item
    if len(reservoir) < k:
        raise ValueError("Stream shorter than requested sample size")
    return reservoir
