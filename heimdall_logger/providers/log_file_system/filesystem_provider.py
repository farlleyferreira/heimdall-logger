import aiofiles
from pathlib import Path
from heimdall_logger.constants.log_output_format import Extension


class File(object):

    def __init__(
        self,
        file_path: str,
    ) -> None:
        """
        [summary]

        Args:
            file_path (str): [description]
        """

        self.file_path = file_path

    def write_file(self, data: str) -> None:
        """
        [summary]

        Args:
            data (tuple): [description]
        """
        _path: str = self.file_path
        print("path:   ", _path)
        print("data:   ", data)
        with open(file=_path, mode="a") as out:
            out.write(data)
            out.write("\n")
            out.flush()
            out.close()

    async def async_write_file(self, data: str) -> None:
        """
        [summary]

        Args:
            data (tuple): [description]
        """
        _path: str = self.file_path

        async with aiofiles.open(file=_path, mode="a") as out:
            await out.writelines(data)
            await out.writelines("\n")
            await out.flush()
            await out.close()
