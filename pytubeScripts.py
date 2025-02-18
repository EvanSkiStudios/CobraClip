from pytubefix import YouTube
from pytubefix.cli import on_progress


def downloadmp4(link, output):
    yt = YouTube(link, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=output)


def downloadAudio(link, output):
    yt = YouTube(link, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download(output_path=output)
