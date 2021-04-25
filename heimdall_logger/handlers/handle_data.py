import json
import asyncio
from dataclasses import dataclass
from heimdall_logger.constants.log_output_format import Extension
from heimdall_logger.providers.log_file_system.filesystem_provider import File
from heimdall_logger.providers.api.async_callback_provider import Api
from heimdall_logger.handlers.handle_log import HandleLog


@dataclass
class FileDataLog:
    log_path: str = "."
    log_name: str = "logfile"
    log_extension: Extension = Extension.LOG

    def get_full_path(self) -> str:
        return f"{self.log_path}{self.log_name}.{self.log_extension.value}"

    def get_writable_data(self, data: HandleLog):
        _data = ""

        if self.log_extension == Extension.TXT or self.log_extension == Extension.LOG:
            _data = data.get_formated_txt_file()

        if self.log_extension == Extension.JSON:
            _data_dict = data.get_formated_json_file()
            _data = json.dumps(_data_dict)

        return _data

    def write_file(self, data: HandleLog):
        _data = self.get_writable_data(data)
        _path = self.get_full_path()

        file = File(_path)
        file.write_file(data=_data)

    async def write_async_file(self, data: HandleLog):
        _data = self.get_writable_data(data)
        _path = self.get_full_path()

        file = File(_path)
        await file.async_write_file(data=_data)


@dataclass
class ApiSendLog:
    api_route: str = ""
    api_method: str = ""
    api_headers: object = None

    def call_api(self, data: HandleLog):
        _data = data.get_formated_json_file()
        api = Api(self.api_method, self.api_route)
        asyncio.run(api.async_call_api(_data, self.api_headers))

    async def call_async_api(self, data: HandleLog):
        _data = data.get_formated_json_file()
        api = Api(self.api_method, self.api_route)
        await api.async_call_api(_data, self.api_headers)
