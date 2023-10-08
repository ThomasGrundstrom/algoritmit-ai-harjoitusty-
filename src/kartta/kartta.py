class Kartta:

    # Määrittelee kartan reitinhakua varten.

    def __init__(self):
        self.taulukko = [[0 for i in range(40)] for j in range(40)]
        self.taulukko[0][0] = 1
        self.taulukko[39][4] = 2
#        for j in range(50):
#            if j != 0:
#                for i in range(199):
#                    self.taulukko[j*4][i] = 3
#        for j in range(1, 49):
#            for i in range(1, 200):
#                self.taulukko[j*4+2][i] = 3

#        for i in range(199):
#            self.taulukko[20][i] = 3

#        for j in range(10):
#            if j != 0:
#                for i in range(39):
#                    self.taulukko[j*4][i] = 3

#        for j in range(10):
#            for i in range(1, 40):
#                self.taulukko[j*4+2][i] = 3

#        for j in range(20):
#            if j != 0:
#                for i in range(1, 39):
#                    self.taulukko[j*2][i] = 3

        for i in range(39):
            self.taulukko[20][i] = 3


kartta = Kartta()
