class Solmu:

    # Luokka, joka määrittelee verkossa olevan solmun rakenteen.

    def __init__(self, koordinaatit, tyyppi):
        self.koordinaatit = koordinaatit
        self.etaisyys = float("inf")
        self.tyyppi = tyyppi
        self.kasitelty = False
        self.naapurit = []
        self.edellinen = None
        self.keossa = False
