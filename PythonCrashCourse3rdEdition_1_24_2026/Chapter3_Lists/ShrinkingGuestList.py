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

print("The new table won't arrive to accommodate all guest, only 2 can come. Sorry!")

count = 0
while count < 4:
    removed_guest = guest_list.pop()
    print(f"Sorry you cannot come: {removed_guest}")
    count += 1

for guest in guest_list:
    print(f"You are still invited: {guest}")

print(guest_list)

del guest_list[1]
del guest_list[0]

print(f"All guests have been removed: {guest_list}")

