from sys import stderr, stdout
from pathlib import Path
from os import getenv
from const import *
import argparse

__version__ = VERSION

def HandleArguments():
    parser = argparse.ArgumentParser(
        prog="PAXER (PAth fiXER)",
    )
    parser.add_argument("--path", "-p", default=getenv("PATH"))
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--silent", "-silent", action="store_true")
    return parser.parse_args()


def main(pathRaw: str):
    pathList = pathRaw.split(":")
    newPathList = []
    duplicationList = set()
    errorCount = 0
    for i in pathList:
        if not i.strip(): continue

        if i == ".":
            stderr.write(DANG.format(i=i) + "\n")
            errorCount += 1
            continue
        
        normalizedPath = Path(i).expanduser().absolute()
        normalizedStringPath = str(normalizedPath)

        if normalizedStringPath in duplicationList:
            stderr.write(DUP.format(i=i) + "\n")
            errorCount += 1
            continue
        
        if not normalizedPath.exists() or not normalizedPath.is_dir():
            stderr.write(NON.format(i=i) + "\n")
            errorCount += 1
            continue

        if normalizedStringPath in SYSTEM_DENY_LIST or str(normalizedPath.resolve()) in SYSTEM_DENY_LIST:
            stderr.write(SYS.format(i=i) + "\n")
            errorCount += 1
            continue

        newPathList.append(i)
        duplicationList.add(normalizedStringPath)
    if errorCount != 0:
        stderr.write(EXT.format(count=errorCount) + "\n")
    
    return ":".join(newPathList)

if __name__ == "__main__":
    if path := getenv("PATH"):
        stdout.write(main(path))