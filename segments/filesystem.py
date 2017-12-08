import os
import config
from segments import Segment, theme
from utils import colors, glyphs


class CurrentDir(Segment):
    bg = colors.background(theme.CURRENTDIR_BG)
    fg = colors.foreground(theme.CURRENTDIR_FG)

    def init(self, cwd):

        home = os.path.expanduser('~')
        cwd = cwd.replace(home, '~')

        dir_shorten_len=config.DIR_SHORTEN_LEN
        dir_limit_depth=config.DIR_LIMIT_DEPTH
        ellipsis=config.ELLIPSIS

        cwd_split = cwd.split(os.sep)
        cwd_split_len = len(cwd_split)
        cwd = [i[0:dir_shorten_len] if dir_shorten_len and i else i for i in cwd_split[:-1]] + [cwd_split[-1]]
        if dir_limit_depth and cwd_split_len > dir_limit_depth + 1:
            del(cwd[0:-dir_limit_depth])
            if ellipsis is not None:
                cwd.insert(0, ellipsis)
        if len(cwd) != 1:
            cwd_segemented = ' '
            count = 1
            for cwd_segement in cwd:
                cwd_segemented += cwd_segement + ' '
                if count <= len(cwd) - 1:
                    cwd_segemented += glyphs.DIVIDER_THIN + ' '
                count += 1
        else:
            cwd_segemented = ' ' + ''.join(cwd) + ' '
        self.text = cwd_segemented

class ReadOnly(Segment):
    bg = colors.background(theme.READONLY_BG)
    fg = colors.foreground(theme.READONLY_FG)

    def init(self, cwd):
        self.text = ' ' + glyphs.WRITE_ONLY + ' '

        if os.access(cwd, os.W_OK):
            self.active = False


class Venv(Segment):
    bg = colors.background(theme.VENV_BG)
    fg = colors.foreground(theme.VENV_FG)

    def init(self):
        env = os.getenv('VIRTUAL_ENV')
        if env is None:
            self.active = False
            return

        env_name = os.path.basename(env)
        self.text = ' ' + glyphs.VIRTUAL_ENV + ' ' + env_name + ' '


class Ard(Segment):
    bg = colors.background(theme.ARD_BG)
    fg = colors.foreground(theme.ARD_FG)

    def init(self):
        env = os.getenv('ARD_TARGET_PROFILE')
        ard_only = os.getenv('ARD_ONLY')
        if ard_only is None:
            self.active = False
            return

        self.text = ' {} '.format(env)

class ArdTimer(Segment):
    bg = colors.background(theme.ARDTIMER_BG)
    fg = colors.foreground(theme.ARDTIMER_FG)

    def init(self):
        env = os.getenv('ARD_TARGET_PROFILE')
        if env is None:
            self.active = False
            return

        import datetime
        time_remaing = 60 - ((int(datetime.datetime.now().strftime("%s")) - int(os.getenv('ARD_START_TIME'))) / 60)
        self.text = ' {} '.format(time_remaing)

class KubeContext(Segment):
    bg = colors.background(theme.KUBE_BG)
    fg = colors.foreground(theme.KUBE_FG)

    def init(self):
        env = os.getenv('KUBE_CONTEXT')
        if env is None:
            self.active = False
            return

        self.text = ' {} '.format(env)
