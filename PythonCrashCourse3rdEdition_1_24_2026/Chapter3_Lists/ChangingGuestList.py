guest_list = ["Twilight Sparkle", "Toshino Kyouko", "Shana"]

for guest in guest_list:
    print(f"You are invited to my party: {guest}. Please come.")

print(f"The following guest can't make it: {guest_list[1]}")

guest_list[1] = "Sakurako Ohmaro"

for guest in guest_list:
    print(f"You are invited to my party: {guest}. Please come.")