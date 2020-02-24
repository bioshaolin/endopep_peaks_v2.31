import os
import sys
import argparse
import subprocess
import re
import glob
import shlex
import operator
import textwrap
from collections import defaultdict
import pandas as pd
import numpy as np



'''
from ffpyplayer.player import MediaPlayer
video_path="endopep_peaks/test_vid.mp4"
def PlayVideo(video_path):
	video=cv2.VideoCapture(video_path)
	player = MediaPlayer(video_path)
	while True:
		grabbed, frame=video.read()
		audio_frame, val = player.get_frame()
		if not grabbed:
			print("End of video")
			break
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
		cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
		subprocess.call("ffplay ~/endopep_peaks/scripts/py_dir/vid_dir/run_final_edit.mp4", shell=True)
#		cv2.resizeWindow("Video", 1600,900)
		cv2.imshow("Video", frame)
		if val != 'eof' and audio_frame is not None:
            #audio
			img, t = audio_frame
	video.release()
	cv2.destroyAllWindows()
PlayVideo(video_path)
'''

subprocess.call("ffplay ~/endopep_peaks/scripts/py_dir/vid_dir/run_final_edit.mp4", shell=True)
