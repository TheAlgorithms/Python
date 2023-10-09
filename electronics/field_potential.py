from typing import List, Tuple


def calculate_electric_field(
    charges: List[Tuple[float, Tuple[float, float, float]]],
    point: Tuple[float, float, float],
) -> Tuple[float, Tuple[float, float, float]]:
    """
    Calculate the electric field and potential at a given point due to charges.

    Args:
        charges (List[Tuple[float, Tuple[float, float, float]]]): List of charge
            magnitude (in Coulombs) and position of charges (x, y, z).
        point (Tuple[float, float, float]): Position (x, y, z) to calculate the
            electric field and potential.

    Returns:
        Tuple[float, Tuple[float, float, float]]: Electric field magnitude (N/C)
        and electric field vector (Ex, Ey, Ez) at the given point.

    Formula:
        Electric Field (E) at a point due to charge Q at position (x_q, y_q, z_q):
        E = k * Q / r^2

        Electric Potential (V) at a point due to charge Q at position (x_q, y_q, z_q):
        V = k * Q / r

        where
        k = 8.99 * 10^9 N m^2/C^2 (Coulomb's constant)
        r = distance from the charge to the point (x, y, z)

    Example:
    >>> charges = [(1e-6, (0.0, 0.0, 0.0)), (2e-6, (1.0, 0.0, 0.0))]
    >>> point = (2.0, 0.0, 0.0)
    >>> calculate_electric_field(charges, point)
    (1798722.37, (1798722.37, 0.0, 0.0))
    """
    k = 8.99e9  # Coulomb's constant (N m^2/C^2)

    electric_field = [0.0, 0.0, 0.0]

    for charge in charges:
        charge_magnitude, charge_position = charge
        dx, dy, dz = (
            point[0] - charge_position[0],
            point[1] - charge_position[1],
            point[2] - charge_position[2],
        )
        r = (dx**2 + dy**2 + dz**2) ** 0.5

        electric_field[0] += k * charge_magnitude * dx / r**3
        electric_field[1] += k * charge_magnitude * dy / r**3
        electric_field[2] += k * charge_magnitude * dz / r**3

    electric_field_magnitude = (
        electric_field[0] ** 2 + electric_field[1] ** 2 + electric_field[2] ** 2
    ) ** 0.5

    return electric_field_magnitude, tuple(electric_field)


def main() -> None:
    """
    Main function to calculate electric field and potential at a given point.
    """
    try:
        n = int(input("Enter the number of charges: "))
        charges = []

        for i in range(n):
            charge_magnitude = float(
                input(f"Enter charge magnitude (in Coulombs) for charge {i+1}: ")
            )
            position = tuple(
                float(coord)
                for coord in input(
                    f"Enter position (x, y, z) for charge {i+1} (comma-separated): "
                ).split(",")
            )
            charges.append((charge_magnitude, position))

        point = tuple(
            float(coord)
            for coord in input(
                "Enter the point (x, y, z) where electric field and potential are to be calculated (comma-separated): "
            ).split(",")
        )

        electric_field_magnitude, electric_field_vector = calculate_electric_field(
            charges, point
        )

        print("\nElectric Field and Potential at the Given Point:")
        print(f"Electric Field Magnitude: {electric_field_magnitude} N/C")
        print(f"Electric Field Vector (Ex, Ey, Ez): {electric_field_vector}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
