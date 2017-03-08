import pytest
from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent


class TestAuthenticationComponent:

    def setup_method(self):
        self.ds = MockDataStore()
        self.au = AuthenticationComponent(self.ds)
        self.default_un = "username"
        self.default_pw = "password"

    def test_create_user_successfully_creates_user_with_correct_parameters(self):
        assert self.au.create_user(self.default_un, self.default_pw)

    def test_create_user_only_stores_username_and_password(self):
        self.au.create_user(self.default_un, self.default_pw)
        assert self.ds.num_of_stored == 1

    def test_create_user_meets_minimal_data_store_method_calls(self):
        minimum_calls = 1
        self.au.create_user(self.default_un, self.default_pw)
        assert minimum_calls == self.ds.num_of_calls

    def test_create_user_honors_unique_user_names(self):
        self.au.create_user(self.default_un, self.default_pw)
        with pytest.raises(RuntimeError, message="Expected RuntimeError due to duplicate user names."):
            self.au.create_user(self.default_un, self.default_pw)

    def test_login_user_successfully_logs_in(self):
        self.au.create_user(self.default_un, self.default_pw)
        assert self.au.login_user(self.default_un, self.default_pw)

    def test_login_user_minimal_data_store_method_calls(self):
        minimum_calls = 1
        self.au.


class MockDataStore(DataStore):

    def __init__(self):
        self.num_of_stored = 0
        self.num_of_calls = 0

    def create(self, name, value):
        assert isinstance(name, str)
        assert isinstance(value, str)
        if self.num_of_stored == 1:
            raise RuntimeError
        self.num_of_stored += 1
        self.num_of_calls += 1
        return True

    def read(self, name):
        assert isinstance(name, str)
        self.num_of_calls += 1

    def update(self, name, value):
        assert isinstance(name, str)
        assert isinstance(value, str)
        self.num_of_calls += 1

    def delete(self, name):
        assert isinstance(name, str)
        self.num_of_stored -= 1
        self.num_of_calls += 1