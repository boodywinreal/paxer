import paxerLogger as pxl
from pathlib import Path
from sys import stderr
from os import getenv
from const import *
import argparse

__version__ = VERSION

def PrintHelp(parser, file):
    parser._print_message(parser.format_help(), file)
    exit(1)


def HandleArguments():
    parser = argparse.ArgumentParser(
        prog="PAXER (PAth fiXER)"
    )
    parser.add_argument("--path", "-p", default=getenv("PATH"), type=str, help="Give a custom path to handle")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all hidden warnings and errors")
    parser.add_argument("--silent", "-s", action="store_true", help="Runs the tool silently")
    parser.print_help = lambda file=stderr: PrintHelp(parser, file)

    return parser.parse_args()

def main():
    data = HandleArguments()
    
    if data.silent: pxl.logLevel = 0
    elif data.verbose: pxl.logLevel = 2
    pxl.setupLogger()

    if data.path is None:
        pxl.normalError("Path is None")
        print(getenv("PATH"), end="")
        exit(1)
    
    paths = [Path(i.strip()) for i in data.path.split(":") if i.strip()]
    newest = []
    duplication = set()

    errors = 0

    for raw in paths:
        if raw == Path("."):
            pxl.pathUnusableError(DANG.format(raw))
            errors += 1
            continue
        if raw == Path("/"):
            pxl.pathUnusableError(SYS.format(raw))
            errors += 1
            continue

        normal = raw.expanduser().absolute()
        if normal in duplication:
            pxl.pathUnusableError(DUP.format(raw))
            errors += 1
            continue
        duplication.add(normal)

        if normal.is_symlink():
            real = (normal.parent / normal.readlink()).resolve()
            if real in duplication:
                pxl.pathUnusableError(SYM_DUP.format(raw, real))
                errors += 1
                continue
            duplication.add(real)

            if not real.is_dir():
                pxl.pathUnusableError(SYM_NON.format(raw, real))
                errors += 1
                continue

            forbidden = (
                real in SYSTEM_DENY_LIST
                or any(parent in SYSTEM_DENY_LIST for parent in real.parents)
            )
            
            if forbidden:
                pxl.pathUnusableError(SYM_SYS.format(raw))
                errors += 1
                continue
        else:
            if not normal.is_dir():
                pxl.pathUnusableError(NON.format(raw))
                errors += 1
                continue
            
            forbidden = (
                normal in SYSTEM_DENY_LIST
                or any(parent in SYSTEM_DENY_LIST for parent in normal.parents)
            )

            if forbidden:
                pxl.pathUnusableError(SYS.format(raw))
                errors += 1
                continue
        newest.append(raw)
    
    if errors != 0: pxl.normalError(EXT.format(count=errors) + "\n")
    print(":".join(newest), end="")
    exit(0)

if __name__ == "__main__":
    main()