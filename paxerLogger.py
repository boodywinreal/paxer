from sys import stderr, stdout
from pathlib import Path
from const import LOG, MAX_LOG_SIZE
from os import stat

loggerFile = Path(LOG).expanduser().absolute() / "/paxer.log"

if loggerFile.exists() and stat(loggerFile).st_size > MAX_LOG_SIZE:
    backup = loggerFile.with_suffix(loggerFile.suffix + ".1")
    loggerFile.replace(backup)

def verboseCurrent(message: str): pass

def verboseNormal(message: str):
    pass
    