import pytest, random, string
from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent


class TestAuthenticationComponent:

    @pytest.fixture
    def random_pw(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(5, 10))

    @pytest.fixture
    def random_un(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(5, 10))

    def setup_method(self):
        self.ds = MockStubDataStore()
        self.au = AuthenticationComponent(self.ds)
        self.default_un = "username"
        self.default_pw = "password"

    def test_create_user_successfully_creates_user_with_correct_parameters(self, random_un, random_pw):
        assert self.au.create_user(random_un, random_pw)

    def test_create_user_only_stores_username_and_password(self, random_un, random_pw):
        self.au.create_user(random_un, random_pw)
        assert self.ds.num_of_stored == 1

    def test_create_user_meets_minimal_data_store_method_calls(self):
        minimum_calls = 1

        self.au.create_user(self.default_un, self.default_pw)
        assert minimum_calls == self.ds.num_of_calls

    def test_create_user_honors_unique_user_names(self):
        self.ds.return_value_bool = False

        self.au.create_user(self.default_un, self.default_pw)
        assert not self.au.create_user(self.default_un, self.default_pw)

    def test_login_user_successfully_logs_in(self):
        self.ds.return_value = self.default_pw

        self.au.create_user(self.default_un, self.default_pw)
        assert self.au.login_user(self.default_un, self.default_pw)

    def test_login_user_minimal_data_store_method_calls(self):
        minimum_calls = 1

        self.au.create_user(self.default_un, self.default_pw)
        create_user_calls = self.ds.num_of_calls
        self.au.login_user(self.default_un, self.default_pw)
        assert minimum_calls == self.ds.num_of_calls - create_user_calls

    def test_login_user_fails_on_non_existent_user(self, random_un, random_pw):
        self.ds.cause_error = True

        assert not self.au.login_user(random_un, random_pw)

    def test_login_user_fails_on_invalid_password(self):
        self.au.create_user(self.default_un, self.default_pw)
        assert not self.au.login_user(self.default_un, "notpassword")

    def test_login_user_does_not_store_in_data_store(self):
        self.au.create_user(self.default_un, self.default_pw)
        current_store = self.ds.num_of_stored
        self.au.login_user(self.default_un, self.default_pw)
        assert current_store == self.ds.num_of_stored

    def test_change_password_fails_on_non_existent_user(self, random_un, random_pw):
        self.ds.return_value_bool = False

        assert not self.au.change_password(random_un, random_pw)

    def test_change_password_successfully_changes_password(self, random_pw):
        self.au.create_user(self.default_un, self.default_pw)
        assert self.au.change_password(self.default_un, random_pw)

    def test_change_password_meets_minimal_data_store_method_calls(self, random_pw):
        minimum_calls = 1

        self.au.create_user(self.default_un, self.default_pw)
        create_user_calls = self.ds.num_of_calls
        self.au.change_password(self.default_un, random_pw)
        assert minimum_calls == self.ds.num_of_calls - create_user_calls

    def test_change_password_does_not_store_in_data_store(self, random_pw):
        self.au.create_user(self.default_un, self.default_pw)
        current_store = self.ds.num_of_stored
        self.au.change_password(self.default_un, random_pw)
        assert current_store == self.ds.num_of_stored

    def test_rename_user_succeeds_on_existent_user(self, random_un):
        self.au.create_user(self.default_un, self.default_pw)
        assert self.au.rename_user(self.default_un, random_un)

    def test_rename_user_fails_on_non_existent_user(self, random_un):
        self.ds.cause_error = True
        self.ds.return_value_bool = False

        assert not self.au.rename_user(self.default_un, random_un)

    def test_rename_user_meets_minimal_method_calls(self, random_un):
        minimum_calls = 3

        self.au.create_user(self.default_un, self.default_pw)
        create_user_calls = self.ds.num_of_calls
        self.au.rename_user(self.default_un, random_un)
        assert minimum_calls == self.ds.num_of_calls - create_user_calls

    def test_rename_user_doesnt_store_additional_data_to_data_store(self, random_un):
        self.au.create_user(self.default_un, self.default_pw)
        current_store = self.ds.num_of_stored
        self.au.rename_user(self.default_un, random_un)
        assert current_store == self.ds.num_of_stored


class MockStubDataStore(DataStore):

    def __init__(self):
        self.num_of_stored = 0
        self.num_of_calls = 0
        self.return_value_bool = True
        self.cause_error = False
        self.return_value_str = "password"

    def create(self, name, value):
        assert isinstance(name, str)
        assert isinstance(value, str)
        self.num_of_stored += 1
        self.num_of_calls += 1
        return self.return_value_bool

    def read(self, name):
        assert isinstance(name, str)
        if self.cause_error:
            raise RuntimeError
        self.num_of_calls += 1
        return self.return_value_str

    def update(self, name, value):
        assert isinstance(name, str)
        assert isinstance(value, str)
        self.num_of_calls += 1
        return self.return_value_bool

    def delete(self, name):
        assert isinstance(name, str)
        self.num_of_stored -= 1
        self.num_of_calls += 1
        return self.return_value_bool
