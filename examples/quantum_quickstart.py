"""Quick runnable examples for restored quantum modules."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from quantum.bb84 import bb84
from quantum.deutsch_jozsa import deutsch_jozsa
from quantum.quantum_entanglement import quantum_entanglement
from quantum.ripple_adder_classic import ripple_adder
from quantum.superdense_coding import superdense_coding


def main() -> None:
    print("BB84 key:", bb84(8, seed=0))
    print("Deutsch-Jozsa:", deutsch_jozsa(lambda bits: int(bits[0] == "1"), 3))
    print("Entanglement counts:", quantum_entanglement(10))
    print("Superdense coding:", superdense_coding(1, 1, shots=5))
    print("Ripple adder 9 + 6:", ripple_adder(9, 6))


if __name__ == "__main__":
    main()
