class Cats:
    paws: 4
    eyes: 2
    tail: 1
    def __init__(self, colors, breed, years):
        self.color = colors
        self.breed = breed
        self.years = years

#colors

print ("1-black and white, 2-orange ,3-gray")

x1 = Cats("Siamese",1 ,2019)
x2 = Cats("British",3 ,2020)
x3 = Cats("Persian",2 ,2021)

print(x1.color)
print(x1.breed)
print(x1.years)

print(x2.color)
print(x2.breed)
print(x2.years)

print(x3.color)
print(x3.breed)
print(x3.years)


