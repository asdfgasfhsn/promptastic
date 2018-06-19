from __future__ import print_function
# Python 2 and 3 compatibility: FileNotFoundError in Python 3, IOError in Python 2.
FileNotFoundError = getattr(__builtins__, 'FileNotFoundError', IOError)
input = getattr(__builtins__, 'raw_input', input)

import os
import re
import subprocess

from segments import Segment, theme
from utils import colors, glyphs


class GitRepo(Segment):
    def init(self):
        repo_name = self.get_repo_name()
        self.bg = colors.background(theme.GITREPO_BG)
        self.fg = colors.foreground(theme.GITREPO_FG)

        if not repo_name:
            self.active = False
            return

        self.text = ' ' + repo_name + ' '


    @staticmethod
    def get_repo_name():
        try:
            p = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()

            if 'not a git repo' in str(err).lower():
                raise FileNotFoundError
        except FileNotFoundError:
            return None

        return out.decode().split('/')[-1].strip() if out else '[ERR]'
