import os


def test(format):
    if(format):
        print(os.system(format))
    else:
        print("ERROR")

# ex1 = "ffprobe -i bbb_final.mp4 -v quiet -show_entries format=format_name"
# test(ex1)
# ex2 = "ffprobe -i bbb_mono.mp3 -v quiet -show_entries format=format_name"
# test(ex2)
ex3 = "ffprobe -i resized.jpg -v quiet -show_entries format=format_name"
test(ex3)


