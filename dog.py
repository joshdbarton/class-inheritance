from animal import Animal 

class Dog(Animal):
    
    def __init__(self, breed):
        self.breed = breed
        super().__init__("dog", leg_num=4, domesticated=True)
    
    def __str__(self):
        return f'This is a {self.breed}.  It is a {self.species} and has {str(self.leg_num)} legs.'
