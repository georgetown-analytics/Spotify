import os
import time
kickout = []
header = ["artist-","trackid-","song"+"\n"]
path = "/volumes/Multimedia/FLAC/"

start = time.time()
with open("lowercase_Final.txt","w+") as source:
	for root, dirs, files in os.walk(path):
		try:
			for file in files:
				if file.endswith(".flac") and file[0].isalpha():
					trimmed_filename = file.replace(".flac","")
					lower_trimmed_filename = trimmed_filename.lower() 
					source.write(lower_trimmed_filename+'\n')
		except:
			continue
	end = time.time()

	duration = str((end - start))

	source.write('Duration: '+duration)