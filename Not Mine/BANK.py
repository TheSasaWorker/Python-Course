import time


class Coins:
    def __init__(self,name,value,weight,colour,diameter,mintage,composition):
        self.name = name
        self.value = value
        self.weight = weight 
        self.colour = colour
        self.diameter = diameter 
        self.mintage = mintage
        self.composition = composition 

    def data(self):
        return "This coin is a {} that is worth {}, which weighs {}, it has a {} colour, a diameter of {}, a total of {} copies, and it is made of {}.".format(self.name, self.value, self.weight, self.colour, self.diameter, self.mintage, self.composition)

coin_1 = Coins("1793 large cent",
               "12,908$",
               "13.48 grams",
               "bronze",
               "26 mm",
               "36.103",
               "copper",
              )

coin_2 = Coins("1959 flying eagle cent",
               "406$",
               "4.67 grams",
               "bronze",
               "19 mm",
               "23,600,000",
               "88% copper, 12% nickel"
              )

coin_3 = Coins("Lincoln Wheat Back Penny",
               "5 cents",
               "3.11 grams",
               "light bronze",
               "19 mm",
               "22,000,000",
               "95% copper, 5% tin and zinc"
              )

coin_4 = Coins("1913 Buffalo Nickel",
               "1,750$",
               "5 grams",
               "silver",
               "21.2 mm",
               "37,000,530",
               "75% copper, 25% nickel"
              )

coin_5 = Coins("1794 Half Dime",
               "1,883$",
               "1.35 grams",
               "bronze",
               "17.5 mm",
               "1500",
               ".8924 silver, .1076 copper"
              )


print(coin_1.data())
print(coin_2.data())
print(coin_3.data())
print(coin_4.data())
print(coin_5.data())

time.sleep(30)