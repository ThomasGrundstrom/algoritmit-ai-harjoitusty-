class Kartta:

    # Määrittelee kartan reitinhakua varten.

    def __init__(self):
        self.taulukko = [[0 for i in range(40)] for j in range(40)]
        self.taulukko[0][0] = 1
        self.taulukko[39][4] = 2
        for i in range(39):
            self.taulukko[20][i] = 3


kartta = Kartta()