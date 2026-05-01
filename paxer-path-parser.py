import paxerLogger as pxl
from pathlib import Path
from sys import stderr
from os import getenv
from const import *
import argparse

__version__ = VERSION

def HandleArguments():
    parser = argparse.ArgumentParser(
        prog="PAXER (PAth fiXER)",
    )
    parser.add_argument("--path", "-p", default=getenv("PATH"), type=str)
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--silent", "-s", action="store_true")
    return parser.parse_args()

def main():
    data = HandleArguments()
    
    if data.silent: pxl.logLevel = 0
    elif data.verbose: pxl.logLevel = 2
    pxl.setupLogger()

    if data.path is None:
        pxl.normalError("Path is None")
        return
    
    pathList = data.path.split(":")
    newPathList = []
    dupCheckSet = set()

    errorCount = 0

    for path in pathList:
        if not path.strip(): continue
        if path == ".":
            pxl.pathUnusableError(DANG.format(i=path))
            errorCount += 1
            continue

        normPath = Path(path).expanduser().absolute()
        normStringPath = str(normPath)

        if normStringPath in dupCheckSet:
            pxl.pathUnusableError(DUP.format(i=path))
            errorCount += 1
            continue
        dupCheckSet.add(normStringPath)

        if normPath.is_symlink():
            realPath = normPath.readlink().resolve()
            realStringPath = str(realPath)

            if realStringPath == ".":
                pxl.pathUnusableError(DANG.format(i=path, real=realStringPath))
                errorCount += 1
                continue

            realPath = realPath.expanduser().absolute()
            realStringPath = str(realPath)

            if realPath in dupCheckSet:
                pxl.pathUnusableError(SYM_DUP.format(i=path, real=realStringPath))
                errorCount += 1
                continue
            dupCheckSet.add(realPath)
            
            if not realPath.is_dir():
                pxl.pathUnusableError(SYM_NON.format(i=path, real=realStringPath))
                errorCount += 1
                continue

            if realStringPath in SYSTEM_DENY_LIST:
                pxl.pathUnusableError(SYM_SYS.format(i=path, real=realStringPath))
                errorCount += 1
                continue

        else:
            if not normPath.is_dir():
                pxl.pathUnusableError(NON.format(i=path))
                errorCount += 1
                continue

            if normStringPath in SYSTEM_DENY_LIST:
                pxl.pathUnusableError(SYS.format(i=path))
                errorCount += 1
                continue
        
        newPathList.append(path)
    if errorCount != 0:
        pxl.normalError(EXT.format(count=errorCount) + "\n")
    
    print(":".join(newPathList), end="")

if __name__ == "__main__":
    main()