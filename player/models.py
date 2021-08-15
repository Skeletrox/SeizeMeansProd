from django.db import models


SECRET_POLICE_RANKS = [
    "Sergeant",
    "Lieutenant",
    "Major",
    "Lieutenant Colonel",
    "Colonel",
    "Commissioner General",
    "General Secretary"
]

# Create your models here.
class Player(models.Model):
    # TODO: replace alL external model references with actual models
    name = models.CharField(max_length=64)
    owned_cash = models.IntegerField(default=0)
    owned_properties = []

    # TODO: add behavior to methods

    # roll a 6-sided die
    def roll_die(self):
        pass

    # purchase a property
    def purchase_property(self, property):
        pass

    # modify property
    def modify_property(self, property, action):
        pass


class SecretPolice(Player):
    rank = models.IntegerField(default=1)

    # promote player
    def promote(self):
        pass

    # demote player
    def demote(self):
        pass


class Citizen(Player):
    is_hero = models.BooleanField(default=False)