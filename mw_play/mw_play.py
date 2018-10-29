#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)


VIDEO_1_PATH = "/home/pirate/test/lushtest1.mlp"
#SUBTITLE_1_PATH = "/home/pirate/test/lushtest1.srt"
#VIDEO_1_PATH = "/home/pirate/test/lushtest2.mp4"
player_log = logging.getLogger("Player 1")

player = OMXPlayer(VIDEO_1_PATH, 
        dbus_name='org.mpris.MediaPlayer2.omxplayer1')
player.playEvent += lambda _: player_log.info("Play")
player.pauseEvent += lambda _: player_log.info("Pause")
player.stopEvent += lambda _: player_log.info("Stop")

#player.select_subtitle(SUBTITLE_1_PATH)

print(dir(player))

#print(player.list_subtitles())

# it takes about this long for omxplayer to warm up and start displaying a picture on a rpi3
sleep(2.5)

player.set_position(5)
player.pause()

sleep(2)

#player.set_aspect_mode('stretch')
#player.set_video_pos(0, 0, 200, 200)
player.play()
#print(player.list_subtitles())

sleep(10)

player.quit()
