import os


def clear():
    #if os.name == "nt":
    #    cmd = "cls"
    #else:
    #    cmd = "clear"
    #os.system(cmd)
    os.system("cls" if os.name == "nt" else "clear")


bidders = {}
add_bidder = True
while add_bidder:
    bidder = input("Enter your name: ")
    value = input("value of your bid in $: ")

    bidders[bidder] = float(value)

    another_bidder = input("Is there another bidder? yes or no: ")

    clear()

    if another_bidder != "yes":
        add_bidder = False

max_bidder = max(bidders, key=bidders.get)
max_value = bidders[max_bidder]
print(f"{max_bidder} gets the auction for {max_value}$")