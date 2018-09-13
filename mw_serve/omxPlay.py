#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from time import sleep

AUDIO_PATH_MLP = "/opt/02_Planets_Part1_Treatment.mlp"
AUDIO_PATH_TEST = "/opt/demo_5ch/ChID-BLITS-EBU-Narration441-16b.wav"

player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

seconds = [2, 3, 4, 10]

for sec in seconds:
        sleep(sec)
        print(player.playback_status())
        print(player.position())
