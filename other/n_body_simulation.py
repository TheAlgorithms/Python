"""
In physics and astronomy, a gravitational N-body simulation is a simulation of a
dynamical system of particles under the influence of gravity. The system
consists of a number of bodies, each of which exerts a gravitational force on all
other bodies. These forces are calculated using Newton's law of universal
gravitation. The Euler method is used at each time-step to calculate the change in
velocity and position brought about by these forces. Softening is used to prevent
numerical divergences when a particle comes too close to another (and the force
goes to infinity).
(Description adapted from https://en.wikipedia.org/wiki/N-body_simulation )
(See also http://www.shodor.org/refdesk/Resources/Algorithms/EulersMethod/ )
"""


from __future__ import annotations

import random

from matplotlib import animation  # type: ignore
from matplotlib import pyplot as plt


class Body:
    def __init__(
        self: Body,
        position_x: float,
        position_y: float,
        velocity_x: float,
        velocity_y: float,
        mass: float = 1.0,
        size: float = 1.0,
        color: str = "blue",
    ) -> None:
        """
        The parameters "size" & "color" are not relevant for the simulation itself,
        they are only used for plotting.
        """
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.mass = mass
        self.size = size
        self.color = color

    def update_velocity(
        self: Body, force_x: float, force_y: float, delta_time: float
    ) -> None:
        """
        Euler algorithm for velocity

        >>> body = Body(0.,0.,0.,0.)
        >>> body.update_velocity(1.,0.,1.)
        >>> body.velocity_x
        1.0
        """
        self.velocity_x += force_x * delta_time
        self.velocity_y += force_y * delta_time

    def update_position(self: Body, delta_time: float) -> None:
        """
        Euler algorithm for position

        >>> body = Body(0.,0.,1.,0.)
        >>> body.update_position(1.)
        >>> body.position_x
        1.0
        """
        self.position_x += self.velocity_x * delta_time
        self.position_y += self.velocity_y * delta_time


class BodySystem:
    """
    This class is used to hold the bodies, the gravitation constant, the time
    factor and the softening factor. The time factor is used to control the speed
    of the simulation. The softening factor is used for softening, a numerical
    trick for N-body simulations to prevent numerical divergences when two bodies
    get too close to each other.
    """

    def __init__(
        self: BodySystem,
        bodies: list[Body],
        gravitation_constant: float = 1.0,
        time_factor: float = 1.0,
        softening_factor: float = 0.0,
    ) -> None:
        self.bodies = bodies
        self.gravitation_constant = gravitation_constant
        self.time_factor = time_factor
        self.softening_factor = softening_factor

    def update_system(self: BodySystem, delta_time: float) -> None:
        """
        For each body, loop through all other bodies to calculate the total
        force they exert on it. Use that force to update the body's velocity.

        >>> body_system = BodySystem([Body(0,0,0,0), Body(10,0,0,0)])
        >>> body_system.update_system(1)
        >>> body_system.bodies[0].position_x
        0.01
        """
        for body1 in self.bodies:
            force_x = 0.0
            force_y = 0.0
            for body2 in self.bodies:
                if body1 != body2:
                    dif_x = body2.position_x - body1.position_x
                    dif_y = body2.position_y - body1.position_y

                    # Calculation of the distance using Pythagoras's theorem
                    # Extra factor due to the softening technique
                    distance = (dif_x ** 2 + dif_y ** 2 + self.softening_factor) ** (
                        1 / 2
                    )

                    # Newton's law of universal gravitation.
                    force_x += (
                        self.gravitation_constant * body2.mass * dif_x / distance ** 3
                    )
                    force_y += (
                        self.gravitation_constant * body2.mass * dif_y / distance ** 3
                    )

            # Update the body's velocity once all the force components have been added
            body1.update_velocity(force_x, force_y, delta_time * self.time_factor)

        # Update the positions only after all the velocities have been updated
        for body in self.bodies:
            body.update_position(delta_time * self.time_factor)


def plot(
    title: str,
    body_system: BodySystem,
    x_start: float = -1,
    x_end: float = 1,
    y_start: float = -1,
    y_end: float = 1,
) -> None:
    INTERVAL = 20  # Frame rate of the animation
    DELTA_TIME = INTERVAL / 1000  # Time between time steps in seconds

    fig = plt.figure()
    fig.canvas.set_window_title(title)

    # Set section to be plotted
    ax = plt.axes(xlim=(x_start, x_end), ylim=(y_start, y_end))

    # Each body is drawn as a patch by the plt-function
    patches = []
    for body in body_system.bodies:
        patches.append(
            plt.Circle((body.position_x, body.position_y), body.size, fc=body.color)
        )

    # Function called once at the start of the animation
    def init() -> list[patches.Circle]:  # type: ignore
        axes = plt.gca()
        axes.set_aspect("equal")

        for patch in patches:
            ax.add_patch(patch)
        return patches

    # Function called at each step of the animation
    def animate(i: int) -> list[patches.Circle]:  # type: ignore
        # Update the positions of the bodies
        body_system.update_system(DELTA_TIME)

        # Update the positions of the patches
        for patch, body in zip(patches, body_system.bodies):
            patch.center = (body.position_x, body.position_y)
        return patches

    anim = animation.FuncAnimation(  # noqa: F841
        fig, animate, init_func=init, interval=INTERVAL, blit=True
    )

    plt.show()


if __name__ == "__main__":
    # Example 1: figure-8 solution to the 3-body-problem
    position_x = 0.9700436
    position_y = -0.24308753
    velocity_x = 0.466203685
    velocity_y = 0.43236573

    bodies1 = [
        Body(position_x, position_y, velocity_x, velocity_y, size=0.2, color="red"),
        Body(-position_x, -position_y, velocity_x, velocity_y, size=0.2, color="green"),
        Body(0, 0, -2 * velocity_x, -2 * velocity_y, size=0.2, color="blue"),
    ]
    body_system1 = BodySystem(bodies1, time_factor=3)
    plot("Figure-8 solution to the 3-body-problem", body_system1, -2, 2, -2, 2)

    # Example 2: Moon's orbit around the earth
    moon_mass = 7.3476e22
    earth_mass = 5.972e24
    velocity_dif = 1022
    earth_moon_distance = 384399000
    gravitation_constant = 6.674e-11

    # Calculation of the respective velocities so that total impulse is zero,
    # i.e. the two bodies together don't move
    moon_velocity = earth_mass * velocity_dif / (earth_mass + moon_mass)
    earth_velocity = moon_velocity - velocity_dif

    moon = Body(-earth_moon_distance, 0, 0, moon_velocity, moon_mass, 10000000, "grey")
    earth = Body(0, 0, 0, earth_velocity, earth_mass, 50000000, "blue")
    body_system2 = BodySystem([earth, moon], gravitation_constant, time_factor=1000000)
    plot(
        "Moon's orbit around the earth",
        body_system2,
        -430000000,
        430000000,
        -430000000,
        430000000,
    )

    # Example 3: Random system with many bodies
    bodies = []
    for i in range(10):
        velocity_x = random.uniform(-0.5, 0.5)
        velocity_y = random.uniform(-0.5, 0.5)

        # Bodies are created pairwise with opposite velocities so that the
        # total impulse remains zero
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                velocity_x,
                velocity_y,
                size=0.05,
            )
        )
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                -velocity_x,
                -velocity_y,
                size=0.05,
            )
        )
    body_system3 = BodySystem(bodies, 0.01, 10, 0.1)
    plot("Random system with many bodies", body_system3, -1.5, 1.5, -1.5, 1.5)
