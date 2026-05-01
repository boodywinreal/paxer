VERSION = "1.0-py"

LOG = "~/.paxer/logs"
MAX_LOG_SIZE = 5 * 1024 * 1024

DANG = "Dangerous path `{i}`, skipping"
DUP = "Duplicated path or symlink `{i}`, skipping"
NON = "Non-existing path or not a directory `{i}`, skipping"
SYS = "System-reserved path `{i}`, skipping"
SYM_DANG = "Symlink `{i}` poins to dangerous path `{real}`, skipping"
SYM_DUP = "Symlink `{i}` points to an already existing path `{real}`, skipping"
SYM_NON = "Symlink `{i}` points to non-existing directory `{real}`, skipping"
SYM_SYS = "Symlink `{i}` points to a system-reserved path `{real}`, skipping"
EXT = "Finished with {count} issues, see " + LOG + "/log.txt" + " for more output"

SYSTEM_DENY_LIST = {
    "/", "/root", "/tmp", "/var/tmp", "/dev", "/sys", "/proc", 
    "/etc", "/var/log", "/dev/shm"
}