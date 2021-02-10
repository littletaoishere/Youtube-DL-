import moviepy.editor as mp
clip = mp.VideoFileClip(r"南山南.mp4")
clip.audio.write_audiofile(r"南山南.mp3")
