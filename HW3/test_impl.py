import pytest
import impl

class TestNetwork:
    def setup_method(self):
        self.nw = impl.Network()

    def test_create_person_returns_person(self):
        try:
            person = self.nw.create_person()
        except:
            assert False

    def test_add_person_property_name_prop_takes_str_val(self):
        try:
            person = self.nw.create_person()
            self.nw.add_person_property(person, "name", "First Last")
        except:
            assert False

    def test_add_person_property_name_prop_takes_only_str_val(self):
        try:
            person = self.nw.create_person()
            self.nw.add_person_property(person, "name", 1234)
            self.nw.add_person_property(person, "name", False)
            assert False
        except TypeError:
            assert True

    def test_add_person_property_overwrites_existing_property(self):
        try:
            person = self.nw.create_person()
            prop = "name"
            val1 = "First Last"
            val2 = "Last First"
            self.nw.add_person_property(person, prop, val1)
            self.nw.add_person_property(person, prop, val2)
        except:
            assert False

    def test_add_person_property_fails_on_invalid_person(self):
        try:
            self.nw.add_person_property(None, "name", "First Last")
            assert False
        except:
            assert True

    def test_add_relation_doesnt_allow_multiple_relations_between_two_people(self):
        try:
            person1 = self.nw.create_person()
            person2 = self.nw.create_person()
            self.nw.add_relation(person1, person2)
            self.nw.add_relation(person1, person2)
            assert False
        except ValueError:
            assert True

    def test_add_relation_fails_on_nonexistent_person1(self):
        try:
            person2 = self.nw.create_person()
            self.nw.add_relation(None, person2)
            assert False
        except:
            assert True

    def test_add_relation_fails_on_nonexistent_person2(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_relation(person1, None)
            assert False
        except:
            assert True

    def test_add_relation_fails_on_adding_relation_to_same_person(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_relation(person1, person1)
            assert False
        except:
            assert True

    def test_add_relation_property_overwrites_existing_prop(self):
        try:
            person1 = self.nw.create_person()
            person2 = self.nw.create_person()
            rprop = "friend"
            val1 = True
            val2 = False
            self.nw.add_relation(person1, person2)
            self.nw.add_relation_property(person1, person2, rprop, val1)
            self.nw.add_relation_property(person1, person2, rprop, val2)
        except:
            assert False

    def test_add_relation_property_fails_on_no_relation(self):
        try:
            person1 = self.nw.create_person()
            person2 = self.nw.create_person()
            self.nw.add_relation_property(person1, person2, "friend", True)
            assert False
        except RuntimeError:
            assert True

    def test_add_relation_property_fails_on_person1_not_existing(self):
        try:
            person2 = self.nw.create_person()
            self.nw.add_relation_property(None, person2, "friend", "First Last")
            assert False
        except:
            assert True

    def test_add_relation_property_fails_on_person2_not_existing(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_relation_property(person1, None, "friend", "First Last")
            assert False
        except:
            assert True

    def test_get_person_raises_error_on_nonexistent_name(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_person_property(person1, "name", "First Last")
            self.nw.get_person("not First Last")
            assert False
        except RuntimeError:
            assert True

    def test_get_person_only_accepts_strings(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_person_property(person1, "name", "First Last")
            self.nw.get_person(1234)
            self.nw.get_person(False)
            assert False
        except TypeError:
            assert True

    def test_get_person_fails_if_no_people_exist(self):
        # needs finished
        pass

    def test_get_person_returns_person(self):
        try:
            person1 = self.nw.create_person()
            name = "First Last"
            self.nw.add_person_property(person1, "name", name)
            person = self.nw.get_person(name)
        except:
            assert False

    def test_friends_of_friends_fails_on_nonexistent_name(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_person_property(person1, "name", "First Last")
            self.nw.friends_of_friends("not First Last")
            assert False
        except RuntimeError:
            assert True

    def test_friends_of_friends_only_accepts_strings(self):
        try:
            person1 = self.nw.create_person()
            self.nw.add_person_property(person1, "name", "First Last")
            self.nw.friends_of_friends(1234)
            self.nw.friends_of_friends(False)
            assert False
        except TypeError:
            assert True




