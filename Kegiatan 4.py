import shelve

data = shelve.open("Ganno")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
