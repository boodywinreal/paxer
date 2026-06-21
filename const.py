from pathlib import Path

VERSION = "1.0-py"

LOG = "~/.paxer/logs"
MAX_LOG_SIZE = 5 * 1024 * 1024

DANG = "Dangerous path `{}`, skipping"
DUP = "Duplicated path or symlink `{}`, skipping"
NON = "Non-existing path or not a directory `{}`, skipping"
SYS = "System-reserved path `{}`, skipping"
SYM_DANG = "Symlink `{}` poins to dangerous path `{}`, skipping"
SYM_DUP = "Symlink `{}` points to an already existing path `{}`, skipping"
SYM_NON = "Symlink `{}` points to non-existing directory `{}`, skipping"
SYM_SYS = "Symlink `{}` points to a system-reserved path `{}`, skipping"
EXT = "Finished with {} issues, see " + LOG + "/log.txt" + " for more output"

SYSTEM_DENY_LIST = {Path(i) for i in {
    "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}}