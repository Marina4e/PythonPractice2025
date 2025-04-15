flat_number = 20

entrance_number = (flat_number -1) //20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print("подъезд №" + str(entrance_number))
print("квартира №" + str(floor_number))