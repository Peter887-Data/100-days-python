import decimal

if __name__ == "__main__":

    bill = input("Total bill amount in $:")
    persons = input("How many people?:")
    tip = input("percentage of tip?")

    bill = decimal.Decimal(bill)
    persons = int(persons)
    tip = decimal.Decimal(tip)/100

    total_bill = bill*(1+tip)/persons
    print(f"{total_bill:10.2f}")


