init -1 python:
    def beep(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/callback/beep44.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")

