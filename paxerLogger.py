from const import LOG, MAX_LOG_SIZE
from datetime import datetime
from pathlib import Path
from sys import stderr
from os import stat

logLevel = 1
loggerFile = Path(LOG).expanduser().absolute() / "log.txt"
loggerFile.parent.mkdir(parents=True, exist_ok=True)
loggerFile.touch()

if loggerFile.exists() and stat(loggerFile).st_size > MAX_LOG_SIZE:
    backup = loggerFile.with_suffix(loggerFile.suffix + ".bak")
    loggerFile.replace(backup)

stream = open(loggerFile, "a")

def silent(message: str, outType: str):
    stream.write(f"[{outType}][ {datetime.now()} ] {message}\n")
    stream.flush()

def verbose(message: str, outType: str):
    trueMessage = f"[{outType}]{{time}} {message}\n"
    stderr.write(trueMessage.format(time=""))
    stderr.flush()
    stream.write(trueMessage.format(time=f"[ {datetime.now()} ]"))
    stream.flush()

pathUnusableError = lambda message: silent(message, "WARNING")
normalError = lambda message: verbose(message, " ERROR ")
normalLog = lambda message: verbose(message, "  LOG  ")

def setupLogger():
    global normalError, normalLog, pathUnusableError
    if logLevel < 1:
        normalError = lambda message: silent(message, outType="ERROR")
        normalLog = lambda message: silent(message, outType="LOG")
    elif logLevel > 1:
        pathUnusableError = lambda message: verbose(message, "WARNING")