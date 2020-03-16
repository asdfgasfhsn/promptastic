# Colors
WHITE = 15
BLACK = 0
BLACKISH = 232

DARKEST_BLUE = 8

NEARLY_WHITE_GREY = 254
EXTRA_LIGHT_GREY = 252
LIGHT_GREY = 250
MID_GREY = 240
MID_DARK_GREY = 238
DARK_GREY = 237
DARKER_GREY = 235
EXTRA_DARK_GREY = 234
DARKEST_GREY = 232  # or 16.

BLUEISH = 31

LIGHT_ORANGE = 202
MID_ORANGE = 166
MID_ORANGE_3 = 172
MID_ORANGE_1 = 9
MID_ORANGE_4 = 202
MID_ORANGE_2 = 208

DARK_PURPLE = 60
PINKISH_RED = 161
LIGHTER_RED = 196
LIGHT_RED = 160
RED = 124
RED_2 = 9

PISTACHIO = 184
LIGHT_GREEN = 148
MID_GREEN = 35
SMERALD = 29
DARK_GREEN = 22
GREEN = 2

GOLD = 94
LIGHT_GOLD = 3
LIGHTER_GOLD = 178

BROWN = 130

# bg = #141C21
BG_1 = 16
# fg = #D9DBDF
FG_1 = 188
# fg-alt = #141C21
FG_ALT = 16

# shade1 = #1976D2
# shade2 = #1E88E5
BLUE_SHADE_1 = 32
BLUE_SHADE_2 = 32

# shade3 = #2196F3
BLUE_SHADE_3 = 33
# shade4 = #42A5F5
# shade5 = #64B5F6
BLUE_SHADE_4 = 75
BLUE_SHADE_5 = 75
# shade6 = #90CAF9
BLUE_SHADE_6 = 117

# heart
RED_SHADE = 167

def foreground(color):
    return '\[$(tput setaf {})\]'.format(color)


def background(color):
    return '\[$(tput setab {})\]'.format(color)


def reset():
    return '\[$(tput sgr0)\]'


def bold():
    return '\[$(tput bold)\]'


def underline_start():
    return '\[$(tput smul)\]'


def underline_end():
    return '\[$(tput rmul)\]'
