from os import getenv
from pathlib import Path
from sys import stderr, stdout

__version__ = "0.2-poc"

SYSTEM_DENY_LIST = {
    "/", "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}

def main(pathRaw: str):
    pathList = pathRaw.split(":")
    newPathList = []
    duplicationList = set()
    for i in pathList:
        if not i.strip(): continue

        if i == ".":
            stderr.write(f"Dangerous path `{i}`, skipping\n")
            continue
        
        normalizedPath = Path(i).expanduser().absolute()
        normalizedStringPath = str(normalizedPath)

        if normalizedStringPath in duplicationList:
            stderr.write(f"Duplicated path `{i}`, skipping\n")
            continue
        
        if not normalizedPath.exists() or not normalizedPath.is_dir():
            stderr.write(f"Non-existing path or not a directory `{i}`, skipping\n")
            continue

        if normalizedStringPath in SYSTEM_DENY_LIST or str(normalizedPath.resolve()) in SYSTEM_DENY_LIST:
            stderr.write(f"System-reserved path or pointed to it `{i}`, skipping\n")
            continue

        newPathList.append(i)
        duplicationList.add(normalizedStringPath)

    return ":".join(newPathList)


if __name__ == "__main__":
    if path := getenv("PATH"):
        stdout.write(main(path))