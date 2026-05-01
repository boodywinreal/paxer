VERSION = "0.3-py"

LOG = "~/.paxer/logs"
MAX_LOG_SIZE = 5 * 1024 * 1024

DANG = "Dangerous path `{i}`, skipping"
DUP = "Duplicated path `{i}`, skipping"
NON = "Non-existing path or not a directory `{i}`, skipping"
SYS = "System-reserved path or pointed to it `{i}`, skipping"
EXT = "Exited with {count} issues"

SYSTEM_DENY_LIST = {
    "/", "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}