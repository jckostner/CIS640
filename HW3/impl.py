class Network(object):

    def __init__(self):
        # constructor
        self.persons = []

    def create_person(self):
        # create a person in the network and return the person
        person = {}
        self.persons.append(person)
        return person

    def add_person_property(self, person, prop, value):
        # add property to a person
        if prop == "name" and type(value) == str:
            person[prop.lower()] = value
        else:
            raise TypeError

    def add_relation(self, person1, person2):
        # add a relation
        person1[person2['name']] = {}
        person2[person1['name']] = {}
        pass

    def add_relation_property(self, person1, person2, prop, value):
        # add property to the relation between person1 and person2
        person1[person2['name']][prop] = value
        person2[person1['name']][prop] = value


    def get_person(self, name):
        # get the person with given name
        for p in self.persons:
            personname = p.get('name', 0)
            if personname == name:
                break
        return p

    def friends_of_friends(self, name):
        # get a list of friends of friends of the person with given name
        friends = []
        friendsofnames = []
        friendsofexh = []
        friendsof = []
        for p in self.persons:
            personname = p.get('name', 0)
            if personname == name:
                break

        friendtest = {'friend': True}

        for key, value in p.items():
            if value == friendtest:
                friends.append(key)

        for n in friends:
            for p in self.persons:
                if p.get('name', 0) == n:
                    break
            for key, value in p.items():
                if value == friendtest:
                    friendsofnames.append(key)


        friendsof = set(friendsofnames)
        return friendsof

nw = Network()
person = nw.create_person()
nw.add_person_property(person, "name", "First Last")
nw.add_person_property(person, "name", "Last First")
print(nw.persons[0])