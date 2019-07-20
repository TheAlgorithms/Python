"""
Class to return properties of harmonic motion at x displacement.
This object can be used in game physics too.

python/black: True
"""
__authors__ = ["n0vice"]
__created__ = "2-14-2019"
__last_modified__ = "7-20-2019"

from numpy import sqrt, linspace, cos


class HarmonicOscillator:
    """
    Harmonic Oscillator object.
    Parameters:
    mass
    k                            ==> stifness of the oscillator
    angular_frequency ==>
    A                           ==> Amplitude
    """

    def __init__(self):
        self.mass = 1
        self.k = 1
        self.angular_frequency = sqrt(self.k / self.mass)
        self.AMPLITUDE = 6
        self.E = 0.5 * self.k * self.AMPLITUDE ** 2

    def force(self, x):
        return -self.k * x

    def position(self, t, A, phase):
        return A * cos(self.angular_frequency * t + phase)

    def kinetic_energy(self, x):
        return (0.5 * self.mass * self.angular_frequency ** 2) * (
            self.AMPLITUDE ** 2 - x ** 2
        )

    def potential_energy(self, x):
        return self.E - self.kinetic_energy(x)

    def hamiltonian(self, x):
        return self.potential_energy(x) + self.kinetic_energy(x)

    def lagrangian(self, x):
        return self.kinetic_energy(x) - self.potential_energy(x)

    def demo(self):
        import matplotlib.pyplot as plt

        oscillator = self
        # Displacement of oscillator
        x = linspace(-6, 6, 100)

        plt.title("Properties of Harmonic Oscillator")

        plt.subplot(2, 2, 1)
        plt.plot(oscillator.force(x), oscillator.potential_energy(x))
        plt.xlabel("Applied Force")
        plt.ylabel("Potential")

        plt.subplot(2, 2, 2)
        plt.plot(oscillator.force(x), oscillator.position(x, 1, 1))
        plt.xlabel("Applied Force")
        plt.ylabel("Position")

        plt.subplot(2, 2, 3)
        plt.plot(oscillator.potential_energy(x), label="Potential Energy")
        plt.plot(oscillator.kinetic_energy(x), label="Kinetic Energy")
        plt.xlabel("Displacement")
        plt.ylabel("Energy")
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(oscillator.hamiltonian(x), label="Hamiltonian")
        plt.plot(oscillator.lagrangian(x), label="Lagrangian")
        plt.xlabel("Displacement")
        plt.ylabel("Energy")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    HarmonicOscillator().demo()
