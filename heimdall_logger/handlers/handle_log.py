
import traceback
import traceback
from typing import Optional
from datetime import datetime as dt

from dataclasses import dataclass
from heimdall_logger.constants.log_level import Level
from heimdall_logger.constants.log_level import LevelColors
from heimdall_logger.format_log.template import Pattern


@dataclass
class HandleLog:
    pattern: str = Pattern.default()
    message: str = ""
    transaction: str = ""
    class_name: str = ""
    project_name: str = ""
    function_name: str = ""
    level: str = ""
    datetime: dt = dt.utcnow()
    error: Optional[Exception] = None

    def get_formated_log_file(self):

        _log = self.pattern.format(
            level=self.level,
            message=self.message,
            datetime=self.datetime,
            class_name=self.class_name,
            transaction=self.transaction,
            project_name=self.project_name,
            function_name=self.function_name
        )

        output_log = f"{LevelColors[self.level]}{_log}{LevelColors[Level.UNSET.name]}"

        if self.error:
            _traceback = "".join(traceback.TracebackException.from_exception(self.error).format())
            output_log += f": \n{_traceback}"

        return output_log

    def get_formated_txt_file(self):

        _log = self.pattern.format(
            level=self.level,
            message=self.message,
            datetime=self.datetime,
            class_name=self.class_name,
            transaction=self.transaction,
            project_name=self.project_name,
            function_name=self.function_name
        )

        output_log = _log

        if self.error:
            _traceback = "".join(traceback.TracebackException.from_exception(self.error).format())
            output_log += f": \n{_traceback}"

        return output_log

    def get_formated_json_file(self):

        output_log = {
            "level": self.level,
            "datetime": self.datetime.isoformat(),
            "class_name": self.class_name,
            "project_name": self.project_name,
            "function_name": self.function_name,
            "transaction": self.transaction,
            "message": self.message
        }

        if self.error:
            _traceback = "".join(traceback.TracebackException.from_exception(self.error).format())
            output_log["traceback"] = _traceback

        return output_log
