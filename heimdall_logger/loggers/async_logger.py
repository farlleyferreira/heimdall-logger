
import inspect

from heimdall_logger.utils.probe import Probe
from heimdall_logger.constants.log_level import Level
from heimdall_logger.format_log.template import Pattern
from heimdall_logger.handlers.handle_log import HandleLog
from heimdall_logger.handlers.handle_data import LogFileData, ApiCallerData

log_pattern = Pattern().default()


class AsyncLogger():
    """[summary]
    """

    def __init__(
        self,
        project_name: str,
        file_data: LogFileData = None,
        api_callback: ApiCallerData = None,
        pattern: str = log_pattern,
    ) -> None:
        """[summary]

        Args:
            project_name (str): [description]
            custom_pattern (str, optional): [description]. 
            Defaults to [{level}][{datetime}] - {transaction} - {project_name}.{class_name}.{function_name} - _message: traceback
        """
        self.project_name = project_name
        self.api_callback = api_callback
        self.file_data = file_data
        self.pattern = pattern

    async def async_log(
        self,
        message: str,
        transaction: str,
        level: Level = Level.INFO,
        error: Exception = None
    ):
        """[summary]

        Args:
            message (str): [description]
            transaction (str): [description]
            level (Level, optional): [description]. Defaults to Level.INFO.
            error (Exception, optional): [description]. Defaults to None.
        """

        stack = inspect.stack()

        _level = level
        _error = error
        _message = message
        _transaction = transaction
        _pattern = self.pattern
        _project_name = self.project_name
        _class_name, _function_name = Probe.inspect_namespaces_from(stack)

        _log = HandleLog(
            pattern=_pattern,
            message=_message,
            transaction=_transaction,
            class_name=_class_name,
            project_name=_project_name,
            function_name=_function_name,
            level=_level.name,
            error=_error
        )

        if self.file_data:
            await self.file_data.write_async_file(_log)

        if self.api_callback:
            await self.api_callback.call_async_api(_log)

        print(_log.get_formated_log_file())
