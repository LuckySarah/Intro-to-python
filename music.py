# create a dictionary what to do
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=hga8EEbnwpc'])

#How to install ffmpeg
# justpaste.it/iq3it
# windows
# winget install --id Gyan.FFmpeg -e
#   'ffmpeg_location': r'c:/ffmpeg/bin' ,