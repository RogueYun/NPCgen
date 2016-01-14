from tools import *

class Occupation(object):
	def __init__(self):
		self.lot_adventurer_class = {"Barbarian":1, "Bard":1, "Cleric":1, "Druid":1, "Fighter":1, "Monk":1, "Paladin":1, "Ranger":1, "Rogue":1, "Sorcerer":1, "Warlock":1, "Wizard":1}
		self.lot_primitive_occ = {"Hunter":10, "Fisherman":10, "Gatherer":10, "Warrior":4, "Shaman":2, "Basketweaver":2, "Craftsman":2, "Cheif":1}
		self.lot_nomad_occ = {"Herder":20, "Hunter":4, "Warrior":4, "Craftsman":2, "Merchant":2, "Shaman":1, "Herbalist":1, "Tentmaker":1, "Weapon Master":1, "Sage":1, "Horsemaster":1, "Entertainer":1}

x = Occupation()

print lot(x.lot_primitive_occ)

print "/n/n"

print lot(x.lot_nomad_occ)
