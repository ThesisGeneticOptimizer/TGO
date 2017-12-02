guest = []
table = []

from Guests import Guest
from Tables import Table
from gen_al import GeneticAlgorithm

guest.append(Guest("Jude"))
guest.append(Guest("Jane"))
guest.append(Guest("Ace"))
guest.append(Guest("Prince"))
guest.append(Guest("Kent"))
guest.append(Guest("Harvey"))
guest.append(Guest("Stephen"))
guest.append(Guest("Christian"))
guest.append(Guest("Pammy"))
guest.append(Guest("Edwin"))
guest.append(Guest("Cris"))
guest.append(Guest("Joel"))

table.append(Table("1"))
table.append(Table("2"))

GeneticAlgorithm.initialization(guest, table)

