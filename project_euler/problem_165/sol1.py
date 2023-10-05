"""
Project Euler Problem [165]: [https://projecteuler.net/problem=165]
<p>A segment is uniquely defined by its two endpoints.<br> By considering two line segments in plane geometry there are three possibilities:<br> 
the segments have zero points, one point, or infinitely many points in common.</p>
<p>Moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.<br>
We will call a common point $T$ of two segments $L_1$ and $L_2$ a true intersection point of $L_1$ and $L_2$ if $T$ is the only common point of $L_1$ and $L_2$ and $T$ is an interior point of both segments.
</p>
<p>Consider the three segments $L_1$, $L_2$, and $L_3$:</p>
<ul style="list-style-type:none;">
<li>$L_1$: $(27, 44)$ to $(12, 32)$</li>
<li>$L_2$: $(46, 53)$ to $(17, 62)$</li>
<li>$L_3$: $(46, 70)$ to $(22, 40)$</li></ul>
<p>It can be verified that line segments $L_2$ and $L_3$ have a true intersection point. We note that as the one of the end points of $L_3$: $(22,40)$ lies on $L_1$ this is not considered to be a true point of intersection. $L_1$ and $L_2$ have no common point. So among the three line segments, we find one true intersection point.</p>
<p>Now let us do the same for $5000$ line segments. To this end, we generate $20000$ numbers using the so-called "Blum Blum Shub" pseudo-random number generator.</p>
\begin{align}
s_0 &amp;= 290797\\
s_{n + 1} &amp;= s_n \times s_n \pmod{50515093}\\
t_n &amp;= s_n \pmod{500}
\end{align}
<p>To create each line segment, we use four consecutive numbers $t_n$. That is, the first line segment is given by:</p>
<p>$(t_1, t_2)$ to $(t_3, t_4)$.</p>
<p>The first four numbers computed according to the above generator should be: $27$, $144$, $12$ and $232$. The first segment would thus be $(27,144)$ to $(12,232)$.</p>
<p>How many distinct true intersection points are found among the $5000$ line segments?</p>

"""

import random

def blum_blum_shub(seed, n):
    # Initialize Blum Blum Shub PRNG
    x = seed
    random_numbers = []
    
    for _ in range(4 * n):
        x = (x * x) % 2147483647
        random_numbers.append(x)
    
    return random_numbers

def create_line_segment(a, b, c, d):
    return ((a, b), (c, d))

def is_true_intersection(segment1, segment2):
    (x1, y1), (x2, y2) = segment1
    (x3, y3), (x4, y4) = segment2

    # Check if segments share a common point that is an interior point
    if x1 == x2 == x3 == x4 and min(y1, y2) < y3 < max(y1, y2):
        return True

    return False

def count_true_intersections(segments):
    count = 0
    n = len(segments)

    for i in range(n):
        for j in range(i + 1, n):
            if is_true_intersection(segments[i], segments[j]):
                count += 1

    return count

# Number of line segments to generate
n = 100
seed = 42  # Initial seed for the PRNG

# Generate random numbers using Blum Blum Shub
random_numbers = blum_blum_shub(seed, n)

# Create line segments from the random numbers
segments = [create_line_segment(random_numbers[i], random_numbers[i + 1], random_numbers[i + 2], random_numbers[i + 3]) for i in range(0, len(random_numbers), 4)]

# Count distinct true intersection points
intersection_count = count_true_intersections(segments)

print("Distinct true intersection points:", intersection_count)
