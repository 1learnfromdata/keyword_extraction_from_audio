# pip install ffmpeg moviepy

import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"last_part.mp4")
my_clip.audio.write_audiofile(r"my_result.wav")
