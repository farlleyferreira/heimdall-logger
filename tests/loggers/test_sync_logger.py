from heimdall_logger.loggers.sync_logger import SyncLogger
from heimdall_logger.handlers.handle_data import FileDataLog, ApiSendLog

def test_sync_logger_instance():
    sync_logger = SyncLogger(
        "heimdall"
    )
    assert isinstance(sync_logger, SyncLogger)


def test_sync_logger_log_if_file_data_way():
    
    log_file_data = FileDataLog(
        log_name="logfile",
        log_path=""
    )
    sync_logger = SyncLogger(
        "heimdall",
        file_data=log_file_data
    )
    sync_logger.log("teste", "input")
    assert open("logfile.log", "r")


def test_sync_logger_log_if_call_api_way():
    api_caller_data = ApiSendLog(
        api_method="POST",
        api_route="http://www.google.com.br"        
    )
        
    sync_logger = SyncLogger(
        "heimdall",
        api_callback=api_caller_data
    )
    
    sync_logger.log("teste", "input")    
