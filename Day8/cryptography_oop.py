from typing import Protocol
import string


class CryptographyAlgorithm(Protocol):
  def encode(self, text: str) -> str:
    ...
  def decode(self, text: str) -> str:
    ...


class CaeserCryptographyAlgorithm(CryptographyAlgorithm):
  def __init__(self, shift: int):
    self.shift = shift

  def encode(self, text: str) -> str:
    return CaeserCryptographyAlgorithm(-self.shift).decode(text)

  def decode(self, text: str) -> str:
    new_word = ""
    for letter in text:
        pos = string.printable.find(letter)
        pos = pos - self.shift
        offset = pos // len(string.printable)
        pos -= offset * len(string.printable)
        new_letter = string.printable[pos]
        new_word += new_letter
    return new_word


class NoOpCryptographyAlgorithm(CryptographyAlgorithm):
  def encode(self, text: str) -> str:
    return text

  def decode(self, text: str) -> str:
    return text


def fancy_stuff(algorithm: CryptographyAlgorithm):
  encoded = algorithm.encode("Hallo Peter")
  print(f"Encoded: {repr(encoded)}")
  decoded = algorithm.decode(encoded)
  print(f"Decoded: {repr(decoded)}")

if __name__ == "__main__":
  algorithm1 = CaeserCryptographyAlgorithm(3)
  algorithm2 = NoOpCryptographyAlgorithm()

  fancy_stuff(algorithm1)
  fancy_stuff(algorithm2)
