import art
print(art.logo)

def highest_bidder(bid):
    bidder = ""
    highest = 0
    for names in bid:
        if bid[names] > highest:
            highest = bid[names]
            bidder = names

    print(f"The highest bidder is {bidder} with a value of ${highest}.")

bids = {}
more_inputs = True
# TODO-1: Ask the user for input
while more_inputs:
    name = input("Please enter your name:\n")
    value = int(input("Please Enter your Bid Value: $"))
# TODO-2: Save data into dictionary {name: price}
    bids[name]=value
# TODO-3: Whether if new bids need to be added
    more_bids = input("More people to bid, if yes type 'yes'. Otherwise 'no").lower()
    if more_bids == 'no':
        print("\n"*100)
        more_inputs = False
        highest_bidder(bids)
    else:
        print("\n" * 100)
        more_inputs = True
# TODO-4: Compare bids in dictionary