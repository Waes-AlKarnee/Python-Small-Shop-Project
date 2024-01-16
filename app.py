# 1. How Many Product Does We Have
# 2. Buy A Product (100tk per Product)
# 3. exit the program

class SHOP:
    def __init__(self, Avalible_Product):
        self.Avalible_Products = Avalible_Product

    def DesplayProducts(self):
        print("Available Products: ",self.Avalible_Products)

    def BuyProduct(self, quantity):
        if quantity<=0:
            print("Enter More Then 0")
        elif quantity>self.Avalible_Products:
            print("Not Have Enough Products")
        else:
            self.Avalible_Products = self.Avalible_Products-quantity
            print("You Bought", quantity, "Products")
            print("Total Price", quantity*100)
            print("Now We Have ", self.Avalible_Products ," Available Products")

Product = SHOP(50)
while True:
    userInput = int(input('''
1. Check Our Stock
2. Buy A Product
3. Exit
'''))
    if userInput == 1:
        Product.DesplayProducts()
    elif userInput == 2:
        userQuentity = int(input("How many Poducts Do You Want To Buy"))
        Product.BuyProduct(userQuentity)
    else:
        break