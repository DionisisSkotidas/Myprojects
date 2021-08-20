def auction():
    auction_dict = {}
    top_bid = 0
    top_bidder = ''

    while True:
        name = str(input("Who is you?\n"))
        bid = float(input('How many money you give?\n'))
        auction_dict[name] = bid

        yes_or_no = input('yes or no?').lower()
        if yes_or_no == 'no':
            break
    for bidder in auction_dict:
        money = auction_dict[bidder]
        if money > top_bid:
            top_bid = money
            top_bidder = bidder
    announcement = 'The to bidder was {} with the bid of {}' \
        .format(top_bidder, top_bid)

    return announcement


if __name__ == "__main__":
    trial = auction()
    print(trial)