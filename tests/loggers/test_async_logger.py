import pytest
import asyncio
from heimdall_logger.loggers.async_logger import AsyncLogger
from heimdall_logger.handlers.handle_data import LogFileData, ApiCallerData


class TestASyncLogger(object):

    @pytest.fixture 
    def event_loop(self): 
        asyncio.sleep(2)
        loop = asyncio.new_event_loop() 
        yield loop 
        loop.close() 

    def test_sync_logger_instance(self):
        sync_logger = AsyncLogger(
            "heimdall"
        )
        assert isinstance(sync_logger, AsyncLogger)


    def test_sync_logger_log_if_file_data_way(self):
        
        log_file_data = LogFileData(
            log_name="logfile",
            log_path=""
        )
        
        sync_logger = AsyncLogger(
            "heimdall",
            file_data=log_file_data
        )
            
        asyncio.run(
            sync_logger.async_log("teste", "input")
        )
        assert open("logfile.log", "r")

    def test_sync_logger_log_if_call_api_way(self):
        api_caller_data = ApiCallerData(
            api_method="POST",
            api_route="http://www.google.com.br"        
        )
            
        sync_logger = AsyncLogger(
            "heimdall",
            api_callback=api_caller_data
        )
        
        asyncio.run(
            sync_logger.async_log("teste", "input")
        )
