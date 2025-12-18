class Moto:
    """
    Animal class with name and age.
    """

    def __init__(self, marque="n", couleur="c"):
        self.marque = "n"
        self.couleur = "c"

    def get_marque(self):
        return self.marque

    def set_couleur(self, b):
        self.couleur = b

    def get_couleur(self):
        return self.couleur

    