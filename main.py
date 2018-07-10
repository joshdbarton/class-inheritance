from dog import Dog
from pet import Pet


spot = Pet("Spot", Dog("bulldog"))

print(spot)

spot.assign_owner("Josh")

print(spot)