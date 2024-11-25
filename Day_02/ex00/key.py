class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"

    def __len__(self):
        return 1337

    def __getitem__(self, item):
        return 3

    def __gt__(self, other):
        return other >= 9000

    def __str__(self):
        return 'GeneralTsoKeycard'

    @property
    def passphrase(self):
        return self.__passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        self.__passphrase = passphrase
