ponies = ["twilight sparkle", "pinkie pie", "applejack", "rainbow dash", "rarity", "fluttershy"]

print(f"Here is the apple pone: {ponies[2]}")

print(f"Here is the leader of the group: {ponies[0].title()}")

print("Applejack had to go on adventure, Limestone will take her place as guardian pone")
ponies[2] = "limestone pie"

print(ponies)

print("Applejack came back, add her back to the ponies group.")

ponies.append("applejack")
print(ponies)
print(f"Here are the number of ponies in the group: {len(ponies)}")

print("Marble Pie is lonely, she wants to be added next to her sisters.")
ponies.insert(3,"marble pie")
print(ponies)
print(f"Here are the number of ponies in the group: {len(ponies)}")

wonderbolts = []

print("Rainbow Dash and Fluttershy exit the group to join the Wonderbolts")
wonderbolts.append(ponies.pop(4))
wonderbolts.append(ponies.pop(5))

print(f"The current group of wonderbolts: {wonderbolts}")
print(f"The current group of ponies: {ponies}")

print("Rarity wants to leave the group since she wants to relax")
ponies.remove("rarity")
print(ponies)


ponies.sort()
print(ponies)

wonderbolts.append("big mac")
wonderbolts.append("hoity toity")
print(wonderbolts)
print(sorted(wonderbolts))
wonderbolts.reverse()
print(wonderbolts)