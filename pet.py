class Pet():

    def __init__(self, name, animal_instance):
        self.name = name
        self.animal_type = animal_instance
        self.owner = "none"
    def __str__(self):
        return f'this is {self.name} owned by {self.owner}.  It has {str(self.animal_type.leg_num)} legs and and says {self.animal_type.saySomething()}.'

    def assign_owner(self, name):
         self.owner = name


       