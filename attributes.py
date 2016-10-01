# order coffee in this order: (source: http://www.delish.com/food/a42014/17-secrets-of-a-starbucks-barista/)
#   Hot or iced
#   Size
#   Decaf
#   Number of shots (if any extra)
#   Number of pumps of syrup (if you're that specific)
#   Type of milk
#   Any extras (mo' whip, mo' deliciousness)
#   Drink type (latte, Frappuccino, etc.)

intro = [("How about a","?"), ("Why not try the","?"), ("Try a","!"), ("Check out a","!"), ("Nothing like a",".")]
temp = ["Hot", "Iced"]
size = ["Short", "Tall", "Grande", "Venti", "Trenta"]
attribute = ["","Non-Fat", "Iced", "Sugar Free", "Soy", "No Foam", "Triple", "Half Sweet", "Decaf", "Half-Caff" , "One-Pump", "Skinny", "Sugar-Free Syrup", "Light Ice", "No Whip", "Dolce Soy"]
multi = ["","Single", "Double", "Triple", "Quad"]
syrup_type = ["","With Extra Hot", " And Non-Fat", " On Half-Sweet", " Add One-Pump", "Add Ten-Pump", "And 4-Pump"]
syrup = ["", "Caramel", "Hazelnut", "Cinnamon", "Vanilla", "Chocolate"]
coffee = ["Espresso", "Espresso Macchiato", "Espresso con Panna", "Caffe Americano", "Cappuccino", "Caffe Latte", "Macchiato", "Caffe Mocha", "White Caffe Mocha", "Frappuccino", "Ristretto", "Chai Tea Latte", "Affogato"]
appendition = ["" ,"And An Extra Shot", " Plus Extra Whip", "With An Extra Shot And Cream", "At 120 Degrees", "With Extra Whipped Cream and Chocolate Sauce"]