guest_list = ["Twilight Sparkle", "Toshino Kyouko", "Shana"]

for guest in guest_list:
    print(f"You are invited to my party: {guest}. Please come.")

print(f"The following guest can't make it: {guest_list[1]}")

guest_list[1] = "Sakurako Ohmaro"

for guest in guest_list:
    print(f"You are invited to my party: {guest}. Please come.")

print("We found a bigger table, more guests can be accomodated!")

guest_list.insert(0,"Brent")
guest_list.insert(1,"Phil")
guest_list.append("Pop Step")

for guest in guest_list:
    print(f"You are invited to my party: {guest}. Please come.")