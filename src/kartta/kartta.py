class Kartta:

    # Määrittelee kartan reitinhakua varten.

    def __init__(self):
        self.taulukko = [[0 for i in range(40)] for j in range(40)]
        self.taulukko[0][0] = 1
        self.taulukko[39][0] = 2
#        for j in range(10):
#            if j != 0:
#                for i in range(39):
#                    self.taulukko[j*4][i] = 3
#        for j in [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]:
#            for i in range(1, 40):
#                self.taulukko[j][i] = 3
        for i in range(39):
            self.taulukko[20][i] = 3


kartta = Kartta()
