"""
Qiskit framework'ü kullanarak istenen sayıda kuantum bit için kuantum Fourier dönüşümünü (QFT) oluşturur. 
Bu deney, IBM Q simülatöründe 10000 deneme ile çalıştırılır. 
Bu devre, kuantum hesaplamada Shor algoritmasını tasarlamak için bir yapı taşı olarak kullanılabilir. 
Ayrıca, kuantum faz tahmini gibi diğer uygulamalar için de kullanılabilir.

Organiser: K. Umut Araz
.
Referanslar:
https://en.wikipedia.org/wiki/Quantum_Fourier_transform
https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html
"""

import math
import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def kuantum_fourier_donustur(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    """
    # >>> kuantum_fourier_donustur(2)
    # {'00': 2500, '01': 2500, '11': 2500, '10': 2500}
    # number_of_qubits = 3 için kuantum devresi:
                                               ┌───┐
    qr_0: ──────■──────────────────────■───────┤ H ├─X─
                │                ┌───┐ │P(π/2) └───┘ │
    qr_1: ──────┼────────■───────┤ H ├─■─────────────┼─
          ┌───┐ │P(π/4)  │P(π/2) └───┘               │
    qr_2: ┤ H ├─■────────■───────────────────────────X─
          └───┘
    cr: 3/═════════════════════════════════════════════
    Args:
        n : kuantum bit sayısı
    Returns:
        qiskit.result.counts.Counts: dağıtılmış sayımlar.

    >>> kuantum_fourier_donustur(2)
    {'00': 2500, '01': 2500, '10': 2500, '11': 2500}
    >>> kuantum_fourier_donustur(-1)
    Traceback (most recent call last):
        ...
    ValueError: kuantum bit sayısı 0'dan büyük olmalıdır.
    >>> kuantum_fourier_donustur('a')
    Traceback (most recent call last):
        ...
    TypeError: kuantum bit sayısı bir tam sayı olmalıdır.
    >>> kuantum_fourier_donustur(100)
    Traceback (most recent call last):
        ...
    ValueError: kuantum bit sayısı simüle etmek için çok büyük(>10).
    >>> kuantum_fourier_donustur(0.5)
    Traceback (most recent call last):
        ...
    ValueError: kuantum bit sayısı tam sayı olmalıdır.
    """
    if isinstance(number_of_qubits, str):
        raise TypeError("Kuantum bit sayısı bir tam sayı olmalıdır.")
    if number_of_qubits <= 0:
        raise ValueError("Kuantum bit sayısı 0'dan büyük olmalıdır.")
    if math.floor(number_of_qubits) != number_of_qubits:
        raise ValueError("Kuantum bit sayısı tam sayı olmalıdır.")
    if number_of_qubits > 10:
        raise ValueError("Kuantum bit sayısı simüle etmek için çok büyük(>10).")

    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")

    kuantum_devre = QuantumCircuit(qr, cr)

    counter = number_of_qubits

    for i in range(counter):
        kuantum_devre.h(number_of_qubits - i - 1)
        counter -= 1
        for j in range(counter):
            kuantum_devre.cp(np.pi / 2 ** (counter - j), j, counter)

    for k in range(number_of_qubits // 2):
        kuantum_devre.swap(k, number_of_qubits - k - 1)

    # tüm kuantum bitlerini ölç
    kuantum_devre.measure(qr, cr)
    # 10000 deneme ile simüle et
    backend = Aer.get_backend("qasm_simulator")
    job = execute(kuantum_devre, backend, shots=10000)

    return job.result().get_counts(kuantum_devre)


if __name__ == "__main__":
    print(
        f"Kuantum Fourier dönüşüm durumu için toplam sayım: \
    {kuantum_fourier_donustur(3)}"
    )
