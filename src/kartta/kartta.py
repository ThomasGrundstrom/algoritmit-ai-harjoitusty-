class Kartta:

    # Määrittelee kartan reitinhakua varten.

    def __init__(self):
        self.taulukko = [[0 for i in range(180)] for j in range(100)]
        self.taulukko[0][0] = 1
        self.taulukko[99][179] = 2

#        for j in range(25):
#            if j != 0:
#                for i in range(179):
#                    self.taulukko[j*4][i] = 3
#        for j in range(1, 24):
#            for i in range(1, 180):
#                self.taulukko[j*4+2][i] = 3

#        for i in range(179):
#            self.taulukko[20][i] = 3

#        for j in range(25):
#            if j != 0:
#                for i in range(179):
#                    self.taulukko[j*4][i] = 3

#        for j in range(25):
#            for i in range(1, 179):
#                self.taulukko[j*4+2][i] = 3

#        for j in range(25):
#            if j != 0:
#                for i in range(1, 179):
#                    self.taulukko[j*2][i] = 3

#        for i in range(39):
#            self.taulukko[20][i] = 3
#        for i in range(20, 98):
#            self.taulukko[i][39] = 3

#        for j in range(1, 50):
#            for i in range(1, 90):
#                self.taulukko[j*2][i*2] = 3

#        for j in range(len(self.taulukko)):
#            self.taulukko[j][5] = 3

#        for i in range(39):
#            self.taulukko[20][i] = 3
#        for i in range(20, 98):
#            self.taulukko[i][39] = 3

#        for j in range(50):
#            for i in range(1, 179):
#                self.taulukko[j*2][i] = 3


kartta = Kartta()
