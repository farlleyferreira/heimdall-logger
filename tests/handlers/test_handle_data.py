import pytest

from faker import Faker
from heimdall_logger.constants.log_output_format import Extension
from heimdall_logger.constants.log_level import Level
from heimdall_logger.handlers.handle_log import HandleLog
from heimdall_logger.handlers.handle_data import ApiCallerData, LogFileData

faker = Faker(0)

handle_log = HandleLog(
        message="teste 123",
        transaction="input data",
        class_name="main",
        project_name="heimdall",
        function_name="call_api",
        level=Level.INFO.name,
        error=Exception(faker.pydict())
    )

def test_sync_handle_data_file_instance():
    log_file_data = LogFileData(
       log_extension=Extension.TXT,
       log_name="file",
       log_path=""
    )
    assert isinstance(log_file_data, LogFileData)
    
def test_sync_handle_api_caller_instance():
    api_caller_data = ApiCallerData(
       api_route="https://www.google.com",
       api_method="GET",
       api_headers={"Authorize": "1541505a4sd4asdas5d4as78d4as4d85a4sd7a4sd4as8d7a"}
    )
    assert isinstance(api_caller_data, ApiCallerData)
    
def test_sync_handle_data_file_write_file():
    log_file_data = LogFileData(
       log_extension=Extension.LOG,
       log_name="logfile",
       log_path=""
    )
    
    log_file_data.write_file(handle_log)    
 
@pytest.mark.asyncio
async def test_async_handle_data_file_write_async_file():
    log_file_data = LogFileData(
       log_extension=Extension.JSON,
       log_name="file",
       log_path=""
    )
    await log_file_data.write_async_file(handle_log)   
    
def test_sync_handle_data_file_get_full_path():
    log_file_data = LogFileData(
       log_extension=Extension.LOG,
       log_name="logfile",
       log_path=""
    )
    assert open(log_file_data.get_full_path())

@pytest.mark.asyncio    
async def test_async_handle_api_call_async():
    
    api_caller_data = ApiCallerData(
       api_route="https://www.google.com.br",
       api_method="GET"       
    )
    
    await api_caller_data.call_async_api(handle_log)

def test_sync_handle_api_call_sync():
    api_caller_data = ApiCallerData(
       api_route="https://www.google.com",
       api_method="GET",
       api_headers={"Authorize": "1541505a4sd4asdas5d4as78d4as4d85a4sd7a4sd4as8d7a"}
    )
    api_caller_data.call_api(handle_log)

