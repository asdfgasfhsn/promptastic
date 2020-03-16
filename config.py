# This is the configuration file which helps you customize your 'promptastic' installation.
# For instructions on how to use the promptastic.py script, see the README.

DIR_SHORTEN_LEN = 20
DIR_LIMIT_DEPTH = 2
ELLIPSIS = '...'

# Patched fonts are special fonts best suited for terminals
# True if the current terminal is using patched fonts available at:
# https://github.com/ryanoasis/nerd-fonts

PATCHED_FONTS = True

# The theme defines the colors used to draw individual segments.
# Themes are collected in the `themes` directory. Their names match their file name (w/o the file
# extension .py).
THEME = 'blues'

# Segments are the single elements which compose the Bash shell prompt.
# Enable or disable these segments to customize what you see on the shell prompt.
SEGMENTS = {
    # Seperate user/host info if desired.
    'user': False,
    'host': True,

    # Combined username @ machine's hostname.
    'userathost': False,

    # SSH tag when ssh-ing from another machine.
    'ssh': True,

    # AWS and Kubernetes Assume Role stuff.
    'ard': True,
    'ardtimer': True,
    'kubecontext': True,

    # Current directory path.
    'currentdir': True,

    # A padlock if the current user has read-only permissions on the current directory.
    'readonly': True,

    # A cross if the last command exited with a non-zero exit code.
    'exitcode': True,

    # Current git branch and status when the current directory is part of a git repo.
    'git': True,
    'gitrepo': True,

    # Name of the current virtual environment (see http://www.virtualenv.org/), if any.
    'venv': True,

    # Number of running jobs, if any.
    'jobs': False,

    # Current time.
    'time': False,

    # Current time but plain and on second line.
    'timeplain': True,
}
