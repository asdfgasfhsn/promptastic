from os import path, access, W_OK, getenv

from segments import Segment
import colors
import glyphs


class CurrentDir(Segment):
    bg = colors.background(colors.DARK_GREY)
    fg = colors.foreground(colors.LIGHT_GREY)

    def init(self, cwd):
        home = path.expanduser('~')
        self.text = cwd.replace(home, '~')


class ReadOnly(Segment):
    bg = colors.background(colors.LIGHT_GREY)
    fg = colors.foreground(colors.RED)

    def init(self, cwd):
        self.text = ' {} '.format(glyphs.LOCK)

        if access(cwd, W_OK):
            self.active = False


class Venv(Segment):
    bg = colors.background(colors.SMERALD)
    fg = colors.foreground(colors.EXTRA_LIGHT_GREY)

    def init(self):
        env = getenv('VIRTUAL_ENV')
        if env is None:
            self.active = False
            return

        env_name = path.basename(env)
        self.text = '{} {}'.format(glyphs.VIRTUAL_ENV, env_name)