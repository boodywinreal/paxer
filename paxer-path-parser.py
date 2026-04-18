from os import getenv
from os.path import isdir, normpath, expanduser, realpath
from sys import stderr, stdout

SYSTEM_DENY_LIST = {
    "/", "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}

def main(path: str):
    dirs = path.split(":")
    new_dirs = []
    for i in dirs:
        if i == "." or not i.strip():
            stderr.write(f"Dangerous path `{i}`, skipping\n")
            continue
        
        norm = normpath(expanduser(i))
        if norm.startswith("//") and not norm.startswith("///"):
            norm = "/" + norm.lstrip("/")
        
        if norm in new_dirs:
            stderr.write(f"Duplicated path `{i}`, skipping\n")
            continue
        
        if norm in SYSTEM_DENY_LIST:
            stderr.write(f"System-reserved path `{i}`, skipping\n")
            continue

        if not isdir(norm):
            stderr.write(f"Non-existing path or not a directory `{i}`, skipping\n")
            continue

        if realpath(norm) in SYSTEM_DENY_LIST:
            stderr.write(f"Pointed to a system-reserved path `{i}`, skipping\n")
            continue

        new_dirs.append(norm)
    return ":".join(new_dirs)


if __name__ == "__main__":
    if path := getenv("PATH"):
        stdout.write(main(path))