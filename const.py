DANG = "Dangerous path `{i}`, skipping\n"
DUP = "Duplicated path `{i}`, skipping\n"
NON = "Non-existing path or not a directory `{i}`, skipping\n"
SYS = "System-reserved path or pointed to it `{i}`, skipping\n"
EXT = "Exited with {i} issues"

SYSTEM_DENY_LIST = {
    "/", "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}