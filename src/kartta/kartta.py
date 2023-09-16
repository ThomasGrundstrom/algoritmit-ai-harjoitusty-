class Kartta:

    # Määrittelee kartan reitinhakua varten.

    def __init__(self):
        self.taulukko = [[0 for i in range(40)] for j in range(40)]
        self.taulukko[0][0] = 1
        self.taulukko[39][39] = 2


kartta = Kartta()