import asyncio
from heimdall_logger import (Extension,Level,FileDataLog,SyncLogger,AsyncLogger)


async def demo_function():

    _log_file_data = FileDataLog(
        log_extension=Extension.LOG,
        log_name="logfile",
        log_path=""
    )

    sync_logger = SyncLogger(
        project_name="heimdall-logger",
        file_data=_log_file_data
    )

    async_logger = AsyncLogger(
        project_name="heimdall-logger",
        file_data=_log_file_data 
    )

    sync_logger.log(level=Level.CRITICAL,message="exemple sync",transaction="start log sync")
    await async_logger.async_log(level=Level.CRITICAL,message="exemple async",transaction="start log async")

    sync_logger.log(level=Level.FATAL,message="exemple sync",transaction="close log sync")
    await async_logger.async_log(level=Level.FATAL,message="exemple async",transaction="close log async")

    sync_logger.log(level=Level.ERROR,message="exemple sync",transaction="start log sync")
    await async_logger.async_log(level=Level.ERROR,message="exemple async",transaction="start log async")

    sync_logger.log(level=Level.WARNING,message="exemple sync",transaction="close log sync")
    await async_logger.async_log(level=Level.WARNING,message="exemple async",transaction="close log async")

    sync_logger.log(level=Level.NOTICE,message="exemple sync",transaction="start log sync")
    await async_logger.async_log(level=Level.NOTICE,message="exemple async",transaction="start log async")

    sync_logger.log(level=Level.TRACE,message="exemple sync",transaction="close log sync")
    await async_logger.async_log(level=Level.TRACE,message="exemple async",transaction="close log async")

    sync_logger.log(level=Level.INFO,message="exemple sync",transaction="start log sync")
    await async_logger.async_log(level=Level.INFO,message="exemple async",transaction="start log async")

    sync_logger.log(level=Level.DEBUG,message="exemple sync",transaction="close log sync")
    await async_logger.async_log(level=Level.DEBUG,message="exemple async",transaction="close log async")

    sync_logger.log(level=Level.DEBUG,message="exemple sync",transaction="start log sync")
    await async_logger.async_log(level=Level.DEBUG,message="exemple async",transaction="start log async")

    
if __name__ == "__main__":
    asyncio.run(demo_function())