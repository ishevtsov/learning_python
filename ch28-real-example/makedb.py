from person import Person, Manager
import shelve

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	tom = Manager('Tom Jones', 50000)

	db = shelve.open('persondb')
	for obj in (bob, sue, tom):
		db[obj.name] = obj
	db.close()
