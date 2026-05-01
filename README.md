<pre>PAXER (PAth fiXER) V1.0-py
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

WHAT IS NEXT
------------

* Moving to C: For a maximum performance and zero overhead.</pre>