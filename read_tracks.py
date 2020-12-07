import os


format = "ffprobe -i bbb_final.mp4 -v quiet -show_entries format=format_name"
if(format):
    print(os.system(format))
else:
    print("ERROR")


