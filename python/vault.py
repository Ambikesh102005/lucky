class Vault:
    def __init__(self, gelleons=0, sickles=0, knuts=0):
        self.gelleons = gelleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.gelleons} Gelleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.gelleons + other.gelleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
