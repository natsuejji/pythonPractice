import sys
from pytube import YouTube
from pytube import Playlist
from pytube import StreamQuery as sq
filterKey = ['1080p','720p','360p']

def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    percent = (100*(stream.filesize-remaining))/stream.filesize
    sys.stdout.write("\r    downloading... %2d%%" % percent)
    sys.stdout.flush()

def download_YT_audio(url):
    yt = YouTube(url,on_progress_callback=progress_Check)
    print ('current video title : ',yt.title)
    """
    for y in yt.streams.all():
        print(y)

    """
    for k in filterKey:
        st = yt.streams.filter(resolution=k,audio_codec='mp4a.40.2')
        print ('    current resolution : ',k)
        if st.first()!=None:        
            break
    content = st.first()
    try:
        content.download('video')
        print ('\ndone')
    except:
        print ('\n找不到目標檔案')
    
def usage_print():
    print ("usage: ", sys.argv[0], "<id type> <id>")
    print ("id type:\n")
    print ("            v = video")
    print ("            l = playlist")

def download_YT_audio_list(id):
    url = 'https://www.youtube.com/playlist?list=' + id
    pl = Playlist(url)
    for val in pl.parse_links():
        download_YT_audio(val)
    
def main():
    if len(sys.argv) < 2 and len(sys.argv) >2:
        usage_print()
    else:
        if sys.argv[1] == 'v':
            url = 'https://www.youtube.com/watch?v='+sys.argv[2]
            download_YT_audio(url)
        elif sys.argv[1] == 'l':
            download_YT_audio_list(sys.argv[2])
        else:
            usage_print()
    sys.exit(0)

if  __name__ == "__main__":
    main()