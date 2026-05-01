<pre>PAXER (PAth fiXER) V0.3-py
===========================
PAXER is a Unix utility to clean-up the $PATH variables from issues
that affects the performance of the shell you are using, while applying
to the current session.

!! WHAT IS NEW !!
-----------------
1. Added argument parsing
2. Added a better logging system
3. More support over symlinks
4. Optimization tweaks
5. Error counting for normal mode

Alongside, I'll start working on compiling the python code (Used tool: Nuitka).

WHAT DOES IT HANDLE
-------------------

* Deduplication
* Non-existing directories
* Dangerous paths (e.g. ".", " ")
* System-reserved directories (e.g. /dev, /etc)

INSTALLATION
------------

1. Python3 must be installed (python.org).

2. Move the files in your path
    - System Wide: /usr/local/bin/
    - User Specific: ~/.local/bin/

3. REQUIRED: Source the included .sh file in your shell's RC file

    Example for bash/zsh shells:
    source ~/.local/bin/paxer-setup.sh

    Note: The shell script does infact support the plain broune shell,
    use this command instead when putting it in the RC file:
    . ~/.local/bin/paxer-setup.sh

CAUTION: Ensure all files are put along to prevent errors

WHAT IS NEXT
------------

* Moving to C: For a maximum performance and zero overhead.</pre>