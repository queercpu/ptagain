init python:

    renpy.music.register_channel("nature", "sfx", loop=True)
    renpy.music.register_channel("looper", "sfx", loop=True)
    renpy.music.register_channel("beep", "sfx", loop=True)
    renpy.music.register_channel("sfx1", "sfx", loop=False)
    renpy.music.register_channel("sfx2", "sfx", loop=False)
    renpy.music.register_channel("sfx3", "sfx", loop=False)


    config.end_splash_transition = dissolve


