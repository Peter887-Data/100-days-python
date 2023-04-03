class Money:
  def __init__(self, value: float, currency: str) -> None:
    self.value = value
    self.currency = currency

  def __eq__(self, __value: object) -> bool:
    if not isinstance(__value, Money):
      return False
    if self.currency != __value.currency:
      return False
    return self.value == __value.value

  def __str__(self) -> str:
    return f"{self.value} {self.currency}"

  def __hash__(self) -> int:
    return self.value.__hash__() + 7 * self.currency.__hash__()
    

dollar1 = Money(100.0, "Dollar")
dollar2 = Money(100.0, "Dollar")
print(dollar1 == dollar2)
print(dollar1)

dollars = {
  dollar1: "1"
}

print(dollars.get(Money(100.0, "Euro")))