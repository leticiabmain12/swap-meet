from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, name="", condition=0,): #age=None
        super().__init__(name, condition, category = "Clothing")

    def __str__(self):
        return "The finest clothing you could wear."
    