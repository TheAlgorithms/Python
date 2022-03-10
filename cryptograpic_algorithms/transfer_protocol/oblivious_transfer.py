"""
In cryptography,
an oblivious transfer protocol is a type of protocol in which a sender transfers
one of potentially many pieces of information to a receiver,
but remains oblivious as to what piece (if any) has been transferred.
Wikipedia reference: https://en.wikipedia.org/wiki/Oblivious_transfer
"""

import random

from cryptograpic_algorithms.ciphers.rsa_key_generator import generateKey


class Sender:
    def set_secrets(self, secrets: tuple[int, ...]) -> None:
        """Set message to be sent"""
        self._secret = secrets

    def generate_key(self, keySize: int) -> tuple[int, int]:
        """Generate RSA key pair and send public portion"""
        self.public_key, self._private_key = generateKey(keySize)
        return self.public_key

    def generate_random_message(self) -> tuple[int, ...]:
        """Generate random message and send"""
        n, e = self.public_key
        self.random_messages = tuple(random.randrange(n) for _ in self._secret)
        return self.random_messages

    def encrypt_secret(self, encrypted_choice: int) -> tuple[int, ...]:
        """Send all encrypted secret"""
        n, d = self._private_key
        salt = [
            (encrypted_choice - random_message) ** d % n
            for random_message in self.random_messages
        ]  # Unblind the salt with the random message
        return tuple(
            secret + salt for secret, salt in zip(self._secret, salt)
        )  # Blind the secret with the salt


class Receiver:
    def set_choice(self, index: int) -> None:
        self._choice = index

    def encrypt_choice(
        self, public_key: tuple[int, int], random_messages: tuple[int, ...]
    ) -> int:
        """Send the encryption of a random salt blinded with the random message"""
        n, e = public_key
        self._salt = random.randrange(n)  # Generate salt
        return (
            random_messages[self._choice] + self._salt**e
        ) % n  # Encrypt the salt and blind with the selected random message

    def decrypt_secret(self, encrypted_secrets: tuple[int, ...]) -> int:
        """Decrypt the message according to the choice selected"""
        return (
            encrypted_secrets[self._choice] - self._salt
        )  # Unblind the secret with the salt


def main():
    CHOICES = 2
    KEY_SIZE = 10

    secrets = tuple(
        random.randrange(2 ** (KEY_SIZE - 1)) for _ in range(CHOICES)
    )  # Generate secrets that is safe with the KEY_SIZE
    choice = random.randrange(CHOICES)

    alice = Sender()
    bob = Receiver()

    alice.set_secrets(secrets)
    bob.set_choice(choice)

    # Bob can do this algorithms for several times to receive more secrets

    public_key = alice.generate_key(KEY_SIZE)
    random_messages = alice.generate_random_message()
    encrypted_choice = bob.encrypt_choice(public_key, random_messages)
    encrypted_secrets = alice.encrypt_secret(encrypted_choice)
    secret = bob.decrypt_secret(encrypted_secrets)

    assert (
        secret == secret[choice]
    ), "The algorithm failed to correctly transfer the data."
