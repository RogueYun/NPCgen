from tools import *

class Age(object):
	def __init__(self):
		self.age_title = "none"
		self.age = 0
		self.lot_age = {"Infant":1, "Toddler":1, "Child":8, "Youth":8, "Young Adult":8, "Adult":8, "Elder":6 }

	def menu_age_select(self):
		age_var = raw_input("Please select the character's age:\n\n\t[a] Infant\n\t[b] Toddler\n\t[c] Child\n\t[d] Youth\n\t[e] Young Adult\n\t[f] Adult\n\t[g] Elder\n\t[r] Random\n\n>>: ")
		if age_var.lower() == "a":
			self.age_title = "Infant"
		elif age_var.lower() == "b":
			self.age_title = "Toddler"
		elif age_var.lower() == "c":
			self.age_title = "Child"
		elif age_var.lower() == "d":
			self.age_title = "Youth"
		elif age_var.lower() == "e":
			self.age_title = "Young Adult"
		elif age_var.lower() == "f":
			self.age_title = "Adult"
		elif age_var.lower() == "g":
			self.age_title = "Elder"
		elif age_var.lower() == "r":
			self.age_title = lot(self.lot_age)


x = Age()
x.menu_age_select()

print x.age_title

n = names_male = ['Althalos', 'Arthur', 'Asher', 'Barda', 'Benedict', 'Berinon', 'Borin', 'Brom', 'Bryce', 'Carac', 'Cassius', 'Cedric', 'Charles', 'Cornwallis', 'Crewe', 'Dain', 'Derwinter', 'Destrian', 'Donald', 'Doran', 'Drake', 'Edmund', 'Falk', 'Favian', 'Fendrel', 'Forthwind', 'Frederick', 'Gavin', 'Geoffrey', 'Gorvenal', 'Gregory', 'Hadrian', 'Hardin', 'Henry', 'Janshai', 'Jarin', 'John', 'Josef', 'Joseph', 'McKinnon', 'Leo', 'Leofrick', 'Letholdus', 'Lief', 'Merek', 'Montagu', 'Oliver', 'Peter', 'Peyton', 'Quinn', 'Robin', 'Roger', 'Ronald', 'Rowan', 'Rulf', 'Sadon', 'Simon', 'Clifton', 'Terrin', 'Terryn', 'Terrowin', 'Thomas', 'Tristan', 'Tybalt', 'Ulric', 'Walter', 'William', 'Xalvador', 'Zane']

n.sort()

print n
