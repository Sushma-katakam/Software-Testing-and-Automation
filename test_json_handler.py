""" Importing from pytest"""
import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(req_id):
    """ This is a decorator function to assign id"""
    def decorator(function):
        function.requirement = req_id
        return function
    return decorator

@pytest.fixture
def json_handler_fixture():
    """ pytest fixture for jsonhandler"""
    return JsonHandler()

@pytest.fixture
def temp_file_fixture(tmp_path):
    """ pytest fixture for file temporary path"""
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler_fixture, temp_file_fixture):
    """ This is a test for readjson """
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    read_data = json_handler_fixture.read_json(temp_file_fixture)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_fixture, temp_file_fixture):
    """ This is a test for writejson """
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    read_data = json_handler_fixture.read_json(temp_file_fixture)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_fixture):
    """ This is a test for check key"""
    data = {"test": "data"}
    assert json_handler_fixture.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_fixture, temp_file_fixture):
    """ This is a test for Update json"""
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    json_handler_fixture.update_json("test", "new data", temp_file_fixture)
    updated_data = json_handler_fixture.read_json(temp_file_fixture)
    assert updated_data["test"] == "new data"
