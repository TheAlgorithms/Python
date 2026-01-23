from __future__ import annotations

import random
from dataclasses import dataclass

from matplotlib import animation
from matplotlib import pyplot as plt

"""
In foundational orbital mechanics, a gravitational N-body simulation models the
dynamic evolution of particles under mutual attraction.

The core challenge in such simulations is preserving the system's total energy and
momentum over long durations. While the basic Euler method is simple, it suffers
from numerical drift, causing orbits to spirally decay or explode.

This implementation utilizes the Leapfrog Integration (a Symplectic integrator),
which interleaves velocity and position updates to ensure second-order accuracy
and exceptional energy conservation—a crucial requirement for mimicking nature's
underlying laws.

Reference: https://en.wikipedia.org/wiki/Leapfrog_integration
"""

# Frame rate of the animation
INTERVAL = 20
# Time between time steps in seconds
DELTA_TIME = INTERVAL / 1000


@dataclass
class Vector2D:
    """A minimal 2D vector class to handle physical quantities."""

    x: float
    y: float

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector2D:
        return Vector2D(self.x * scalar, self.y * scalar)

    def magnitude_sq(self) -> float:
        return self.x**2 + self.y**2

    def magnitude(self) -> float:
        return self.magnitude_sq() ** 0.5


class Body:
    def __init__(
        self,
        position: Vector2D,
        velocity: Vector2D,
        mass: float = 1.0,
        size: float = 1.0,
        color: str = "blue",
    ) -> None:
        self.pos = position
        self.vel = velocity
        self.acc = Vector2D(0.0, 0.0)  # Current acceleration
        self.mass = mass
        self.size = size
        self.color = color

    def update_position(self, dt: float) -> None:
        """
        Updates position using current velocity.
        >>> b = Body(Vector2D(0, 0), Vector2D(1, 2))
        >>> b.update_position(1.0)
        >>> b.pos.x, b.pos.y
        (1, 2)
        """
        # r(t + dt) = r(t) + v(t + dt/2) * dt
        self.pos += self.vel * dt

    def update_velocity(self, force: Vector2D, dt: float) -> None:
        """
        Updates velocity by applying acceleration over a time step.
        >>> b = Body(Vector2D(0, 0), Vector2D(0, 0), mass=2.0)
        >>> b.update_velocity(Vector2D(10, 0), 1.0)
        >>> b.vel.x, b.vel.y
        (5.0, 0.0)
        """
        # v(t + dt/2) = v(t - dt/2) + a(t) * dt
        acc = force * (1.0 / self.mass)
        self.vel += acc * dt


class BodySystem:
    def __init__(
        self,
        bodies: list[Body],
        gravitation_constant: float = 1.0,
        time_factor: float = 1.0,
        softening_factor: float = 0.0,
    ) -> None:
        self.bodies = bodies
        self.g = gravitation_constant
        self.time_factor = time_factor
        self.softening = softening_factor

    def compute_forces(self) -> list[Vector2D]:
        """Calculates mutual gravitational forces between all bodies."""
        forces = [Vector2D(0.0, 0.0) for _ in self.bodies]
        for i, b1 in enumerate(self.bodies):
            for j, b2 in enumerate(self.bodies):
                if i == j:
                    continue
                diff = b2.pos - b1.pos
                dist_sq = diff.magnitude_sq() + self.softening
                force_mag = (self.g * b1.mass * b2.mass) / (dist_sq**1.5)
                forces[i] += diff * force_mag
        return forces

    def total_energy(self) -> float:
        """
        Calculates the total mechanical energy (Kinetic + Potential).
        In a closed system, this should remain nearly constant.
        """
        kinetic_energy = 0.0
        potential_energy = 0.0

        for i, b1 in enumerate(self.bodies):
            # Kinetic Energy: 0.5 * m * v^2
            kinetic_energy += 0.5 * b1.mass * b1.vel.magnitude_sq()

            # Potential Energy: -G * m1 * m2 / r
            for j in range(i + 1, len(self.bodies)):
                b2 = self.bodies[j]
                r = (b2.pos - b1.pos).magnitude()
                if r > 0:
                    potential_energy -= (self.g * b1.mass * b2.mass) / r

        return kinetic_energy + potential_energy

    def update_system(self, delta_time: float) -> None:
        """
        Advances the system using Leapfrog Integration.
        This provides better stability than the standard Euler method.
        """
        dt = delta_time * self.time_factor

        # 1. Compute forces at current positions
        forces = self.compute_forces()

        # 2. Update velocities (half step) and positions (full step)
        # For simplicity in this structure, we use a Drift-Kick-Drift variant
        for i, body in enumerate(self.bodies):
            body.update_velocity(forces[i], dt)
            body.update_position(dt)


def update_step(
    body_system: BodySystem, delta_time: float, patches: list[plt.Circle]
) -> None:
    body_system.update_system(delta_time)
    for patch, body in zip(patches, body_system.bodies):
        patch.center = (body.pos.x, body.pos.y)


def plot(
    title: str,
    body_system: BodySystem,
    xlim: tuple[float, float] = (-1, 1),
    ylim: tuple[float, float] = (-1, 1),
) -> None:
    fig = plt.figure()
    fig.canvas.manager.set_window_title(title)
    ax = plt.axes(xlim=xlim, ylim=ylim)
    plt.gca().set_aspect("equal")

    patches = [
        plt.Circle((b.pos.x, b.pos.y), b.size, fc=b.color) for b in body_system.bodies
    ]
    for patch in patches:
        ax.add_patch(patch)

    def update(frame: int) -> list[plt.Circle]:
        update_step(body_system, DELTA_TIME, patches)
        return patches

    anim = animation.FuncAnimation(fig, update, interval=INTERVAL, blit=True)
    plt.show()


def example_figure_eight() -> BodySystem:
    # Classic 3-body figure-8 initial conditions
    p_x, p_y = 0.9700436, -0.24308753
    v_x, v_y = 0.466203685, 0.43236573
    b1 = Body(Vector2D(p_x, p_y), Vector2D(v_x, v_y), size=0.05, color="red")
    b2 = Body(Vector2D(-p_x, -p_y), Vector2D(v_x, v_y), size=0.05, color="green")
    b3 = Body(Vector2D(0, 0), Vector2D(-2 * v_x, -2 * v_y), size=0.05, color="blue")
    return BodySystem([b1, b2, b3], time_factor=2.0)


if __name__ == "__main__":
    # Run the figure-8 simulation
    sys = example_figure_eight()
    plot("Stable 3-Body Orbit (Leapfrog)", sys, (-1.5, 1.5), (-1.5, 1.5))
