from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print
bids = []
type_input = "yes"

while type_input == "yes":
  name_input = input("What is your name?: ")
  bid_input = input("What's your bid?: $")
  new_bid = {
    "name": name_input,
    "bid": bid_input
  }
  bids.append(new_bid)

  type_input = input("Are there are any other bidders? Type 'yes' or 'no' ")
  
  if type_input == 'no':
    max = 0
    name = ""
    for index in range(len(bids)):
      if max < int(bids[index]["bid"]):
        max = int(bids[index]["bid"])
        name = bids[index]["name"]
    print(f"{name} won a bid of ${max}")
  else:
    clear()