import os
from pydub import AudioSegment


class Lab3:

    def mp4container(self): # funció on s'executa el codi de l'exercici 1&2
        # we cut the first minute out of the bbb video
        os.system("ffmpeg -ss 00:00:00 -i bbb_original.mp4 -c copy -t 00:01:00 bbb_minute.mp4")
        # we get the mono audio track
        os.system("ffmpeg -i bbb_minute.mp4 -ac 1 bbb_mono.mp3")
        # we get the audio from the 1 minute clip
        sound = AudioSegment.from_file("bbb_minute.mp4")
        # export the sound to a different bitrate
        sound.export("bbb_bitrate", format="mp3", bitrate="128k")
        # we add the subtitles to the 1 minute clip
        os.system("ffmpeg -i bbb_minute.mp4 -i subtitles.srt -c copy -c:s mov_text bbb_subtitles.mp4")
        # we combine the last tracks and clips into a .mp4
        os.system("ffmpeg -i bbb_subtitles.mp4 -i bbb_mono.mp3 -c copy bbb_final.mp4")

    def test(format): # funció que executa el codi dels exercicis 3&4
        if (format):
            print(os.system(format))
        else:
            print("ERROR")


