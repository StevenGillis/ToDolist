import weakref
import sqlite3
conn = sqlite3.connect('todo.db')
c = conn.cursor()
conn.commit()

class newitems:
    def __init__(self, description, urgency):
        self.__class__.instances.append(weakref.proxy(self))
        self.description = description
        self.urgency = urgency

    @classmethod
    def createInstances(cls, item, urgency):
        c.execute("INSERT INTO item VALUES(?, ?)", (item, urgency))

    @classmethod
    def printInstances(cls):
        list = c.execute("select description FROM item")
        for item in list:
            print(item[0])

while True:
    item = input("to do:")
    #  command s to show the list
    if item[0] == "s" and len(item) == 1:
        newitems.printInstances()
    #  d command to remove items from the list by list index
    elif item[0] == "d" and len(item) == 1:
        del_number = int(input("Which item is done?"))
        del list[del_number]
        newitems.printInstances()
    else:
        newitems.createInstances(item=str(item), urgency="high")
        newitems.printInstances()

conn.close()

