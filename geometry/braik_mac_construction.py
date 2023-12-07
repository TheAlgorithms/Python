from __future__ import annotations
import math
from dataclasses import dataclass, field
from numpy import array, linalg

# braikenridge_maclaurin_construction
# https://mathworld.wolfram.com/ConicSection.html
# 5 Points define a conic section on a 2D normal
# orthogonal plane using this technique

