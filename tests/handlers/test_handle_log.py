import asyncio
import traceback

from faker import Faker
from heimdall_logger.handlers.handle_log import HandleLog

faker = Faker(0)

def test_sync_handle_logger_instance():
    handle_log = HandleLog(
        pattern="",
        message=faker.pystr(),
        transaction=faker.pystr(),
        class_name=faker.file_name(),
        project_name=faker.pystr(),
        function_name=faker.pystr(),
        level=faker.pystr(),
        error=Exception(faker.pydict())
    )
    assert isinstance(handle_log, HandleLog)
    
    
def test_sync_handle_logger_get_log_extension():
    handle_log = HandleLog(
        pattern="",
        message="",
        transaction="",
        class_name="",
        project_name="",
        function_name="",
        level="INFO"
    )
    assert handle_log.get_formated_log_file() == "\x1b[38;5;12m\x1b[0m"
    
def test_sync_handle_logger_get_log_with_exception():
    
    _error = _error=Exception(faker.pydict())
    handle_log = HandleLog(
        pattern="",
        message="",
        transaction="",
        class_name="",
        project_name="",
        function_name="",
        level="INFO",
        error=_error
    )
    
    _traceback = "".join(traceback.TracebackException.from_exception(_error).format())    
    assert handle_log.get_formated_log_file() == "\x1b[38;5;12m\x1b[0m" + f": \n{_traceback}"
    
def test_sync_handle_logger_get_txt_extension():
    
    handle_log = HandleLog(
       pattern="",
       message="",
       transaction="",
       class_name="",
       project_name="",
       function_name="",
       level="INFO",

    )
   
    assert handle_log.get_formated_txt_file() == "" 
    
def test_sync_handle_logger_get_txt_with_exception():
    
    _error = _error=Exception(faker.pydict())
    handle_log = HandleLog(
        pattern="",
        message="",
        transaction="",
        class_name="",
        project_name="",
        function_name="",
        level="INFO",
        error=_error
    )
    
    _traceback = "".join(traceback.TracebackException.from_exception(_error).format())    
    assert handle_log.get_formated_txt_file() == "" + f": \n{_traceback}"
    
def test_sync_handle_logger_get_json_extension():
    
    handle_log = HandleLog(
        pattern="",
        message=faker.pystr(),
        transaction=faker.pystr(),
        class_name=faker.file_name(),
        project_name=faker.pystr(),
        function_name=faker.pystr(),
        level="INFO",

    )
   
    assert type(handle_log.get_formated_json_file()) == dict
    
def test_sync_handle_logger_get_json_with_exception():
    
    _error=Exception(faker.pydict())
    handle_log = HandleLog(
        pattern="",
        message=faker.pystr(),
        transaction=faker.pystr(),
        class_name=faker.file_name(),
        project_name=faker.pystr(),
        function_name=faker.pystr(),
        level="INFO",
        error=_error
    )    
    _log = handle_log.get_formated_json_file()
    _traceback = "".join(traceback.TracebackException.from_exception(_error).format())    
    assert "traceback" in _log
    assert _log["traceback"] == _traceback
    