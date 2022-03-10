"""
Garbled circuit is a cryptographic protocol that enables two-party secure computation
in which two mistrusting parties can jointly evaluate a function
over their private inputs without the presence of a trusted third party.
In the garbled circuit protocol, the function has to be described as a Boolean circuit.
Wikipedia reference: https://en.wikipedia.org/wiki/Garbled_circuit
"""

import random
from typing import Callable

from cryptograpic_algorithms.hashes.sha256 import SHA256
from cryptograpic_algorithms.transfer_protocol.oblivious_transfer import (
    Receiver,
    Sender,
)


def _generate_key(key_size: int) -> int:
    """Generate key with the size"""
    return random.randrange(2 ** (key_size - 1), 2 ** (key_size))


def _generate_label(label_size: int) -> int:
    """Generate key with the size"""
    return random.randrange(2 ** (label_size - 1), 2 ** (label_size))


def _enc(key: int, key_size: int = 128) -> int:
    """Fixed-key block cipher"""
    return int(SHA256(bytes(key)).hash, 16) % (2**key_size)


def _encrypt(keys: list[int], salt: int, secret: int, key_size: int = 128) -> int:
    """Encryption with keys and salt"""
    key = salt
    for index, subkey in enumerate(keys):
        key ^= subkey << index + 1
    key %= 2**key_size
    return _enc(key, key_size) ^ key ^ secret


def _decrypt(
    keys: list[int], salt: int, encoded_secret: int, key_size: int = 128
) -> int:
    """Decryption with keys and salt"""
    key = salt
    for index, subkey in enumerate(keys):
        key ^= subkey << index + 1
    key %= 2**key_size
    return _enc(key, key_size) ^ key ^ encoded_secret


class Garbler:
    def generate_label(
        self,
        garbler_input_size: int,
        evaluator_input_size: int,
        function: Callable[..., int],
        label_size: int = 128,
    ) -> tuple[tuple[int, ...], int]:
        self._garbler_label = tuple(
            (_generate_label(label_size), _generate_label(label_size))
            for _ in range(garbler_input_size)
        )
        self._evaluator_label = tuple(
            (_generate_label(label_size), _generate_label(label_size))
            for _ in range(evaluator_input_size)
        )
        salt = _generate_key(label_size)
        _output_label: list[int] = [-1, -1]
        garbled_table: list[int] = []
        for garbler_input in range(2 ** len(self._garbler_label)):
            input_labels: list[int] = []
            input_values: list[int] = []
            input_: str = (
                bin(garbler_input)
                .removeprefix("0b")
                .ljust(len(self._garbler_label), "0")
            )
            input_values += [int(inp_) for inp_ in input_]
            input_labels += [
                self._garbler_label[i][inp] for i, inp in enumerate(input_values)
            ]
            for evaluator_input in range(2 ** len(self._evaluator_label)):
                input_ = (
                    bin(evaluator_input)
                    .removeprefix("0b")
                    .ljust(len(self._evaluator_label), "0")
                )
                input_values += [int(inp_) for inp_ in input_]
                input_labels += [
                    self._evaluator_label[i][inp] for i, inp in enumerate(input_values)
                ]

                output = function(*input_values)
                output_label = function(*input_labels)
                _output_label[output] = output_label
                garbled_table.append(_encrypt(input_labels, salt, output_label))
        if any(label < 0 for label in _output_label):
            raise Exception(
                f"The function does not depends on the input \
                (always return {str(bool(function(0,0)))})"
            )
        self._output_label: tuple[int, int] = (_output_label[0], _output_label[1])
        random.shuffle(garbled_table)
        return (tuple(garbled_table), salt)

    def get_encrypted_secret(self, secret: int) -> list[int]:
        input_labels: list[int] = []
        input_: str = (
            bin(secret).removeprefix("0b").ljust(len(self._garbler_label), "0")
        )
        input_labels += [
            self._garbler_label[i][int(inp_)] for i, inp_ in enumerate(input_)
        ]
        return input_labels

    def get_secret_label_send_message(
        self, key_size: int, index: int
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        self._label_sender = Sender()
        self._label_sender.set_secrets(self._evaluator_label[index])
        public_key = self._label_sender.generate_key(key_size)
        random_messages_ = self._label_sender.generate_random_message()
        random_messages = (random_messages_[0], random_messages_[1])
        return (public_key, random_messages)

    def get_secret_label_encrypt_secret(self, encrypted_choice: int) -> tuple[int, int]:
        return self._label_sender.encrypt_secret(encrypted_choice)

    def get_output_label(self) -> tuple[int, int]:
        return self._output_label

    def get_output(self, output_labels: tuple[int, ...]) -> bool:
        result: bool
        try:
            output_labels.index(self._output_label[0])
            result = False
        except ValueError:
            pass
        try:
            output_labels.index(self._output_label[1])
            result = True
        except ValueError:
            pass
        return result


class Evaluator:
    def set_secret(self, secret: int, evaluator_input_size: int):
        self._secret = secret
        self._secret_label: list[int] = [-1 for _ in range(evaluator_input_size)]

    def get_secret_label_set_choice(self, index: int):
        self.index = index
        self._label_receiver = Receiver()
        self._label_receiver.set_choice((self._secret >> self.index) & 1)

    def get_secret_label_encrypt_choice(
        self, public_key: tuple[int, int], random_messages: tuple[int, int]
    ):
        return self._label_receiver.encrypt_choice(public_key, random_messages)

    def get_secret_label_decrypt_secrets(self, encrypted_secret: tuple[int, int]):
        self._secret_label[self.index] = self._label_receiver.decrypt_choice(
            encrypted_secret
        )

    def get_output_label(
        self,
        garbled_table: tuple[int, ...],
        garbler_input_label: list[int],
        salt: int,
        label_size: int = 128,
    ) -> tuple[int, ...]:
        output_label_: list[int] = []
        for encrypted_value in garbled_table:
            output_label_.append(
                _decrypt(
                    garbler_input_label + self._secret_label,
                    salt,
                    encrypted_value,
                    label_size,
                )
            )
        random.shuffle(output_label_)
        self._output_label = tuple(output_label_)
        return self._output_label

    def get_output(self, output_labels: tuple[int, int]) -> bool:
        result: bool
        try:
            self._output_label.index(output_labels[0])
            result = False
        except ValueError:
            pass
        try:
            self._output_label.index(output_labels[1])
            result = True
        except ValueError:
            pass
        return result


def main():
    ALICE_INPUT_BITS = 4
    BOB_INPUT_BITS = 4
    LABEL_SIZE = 128
    KEY_SIZE = 128  # Must be more than or equal to LABEL_SIZE

    lookup_table = [
        random.randrange(1) for _ in range(2 ** (ALICE_INPUT_BITS + BOB_INPUT_BITS))
    ]

    def function(*args: int) -> int:
        out = 0
        for inp in range(2 ** (ALICE_INPUT_BITS + BOB_INPUT_BITS)):
            input_value: list[int] = []
            input_: str = (
                bin(inp)
                .removeprefix("0b")
                .ljust(len(ALICE_INPUT_BITS + BOB_INPUT_BITS), "0")
            )
            input_value += [int(inp_) for inp_ in input_]
            ctrl = lookup_table(inp)
            for i, tf in enumerate(input_value):
                ctrl &= args[i] if tf else ~args[i]
                if not ctrl:
                    continue
            out |= ctrl
        return out

    alice_value = random.randrange(2**ALICE_INPUT_BITS)
    bob_value = random.randrange(2**BOB_INPUT_BITS)

    alice = Garbler()
    bob = Evaluator()

    garbled_table, salt = alice.generate_label(
        ALICE_INPUT_BITS, BOB_INPUT_BITS, function, LABEL_SIZE
    )

    garbler_label = alice.get_encrypted_secret(alice_value)

    bob.set_secret(bob_value, BOB_INPUT_BITS)
    for i in range(BOB_INPUT_BITS):
        bob.get_secret_label_set_choice(i)
        public_key, random_messages = alice.get_secret_label_send_message(KEY_SIZE, i)
        encrypted_choice = bob.get_secret_label_encrypt_choice(
            public_key, random_messages
        )
        encrypted_secrets = alice.get_secret_label_encrypt_secret(encrypted_choice)
        bob.get_secret_label_decrypt_secrets(encrypted_secrets)

    value_a = alice.get_output(
        bob.get_output_label(garbled_table, garbler_label, salt, LABEL_SIZE)
    )
    value_b = bob.get_output(alice.get_output_label())

    assert (
        value_a == value_b == function(alice_value, bob_value)
    ), "The algorithm failed to correctly evaluate the function."
