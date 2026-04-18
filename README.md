<pre>PAXER (PAth fiXER) V0.1-poc
===========================
PAXER is a Unix utility to clean-up the $PATH variables from issues
that affects the performance of the shell you are using, while applying
to the current session.

WARNING: PAXER in this state is still a Proof Of Concept (POC),
expect instabiliy or slowness, issue reporting is recommended.

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

CAUTION: Ensure all files are put along to prevent errors

WHAT IS NEXT
------------

* Moving to C: For a maximum performance and zero overhead.
* User Customizability: Adding flags to toggle specific settings.</pre>