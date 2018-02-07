all:
	ffmpeg -i output1.avi -vcodec copy -acodec copy video1.mp4
	ffmpeg -i output2.avi -vcodec copy -acodec copy video2.mp4
	ffmpeg -i output3.avi -vcodec copy -acodec copy video3.mp4
