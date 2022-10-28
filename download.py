import pytube

def error():
    print("Error Downloading :(")

class SearchDownload:
    def __init__(self,query):
        self.query = query
        self.results = pytube.Search(query)
    
    def get_data(self):
        for result in self.results.results:
            return result.video_id,result.title, result.author , result.length
    
class PlaylistDownload:
    def __init__(self,link):
        self.link = link
        self.yt = pytube.Playlist(self.link)
        self.title = self.yt.title

    def download_video_default(self):
        for video in self.yt.videos:
            video.streams.get_highest_resolution().download()

    def download_audio_default(self):
        for video in self.yt.videos:
            video.streams.filter(abr="128kbps",progressive=False).first().download()

class SingleDownload:
    def __init__(self,link):
        self.link = link
        self.yt = pytube.YouTube(self.link)
        self.title = self.yt.title
        self.author = self.yt.author
        self.date = self.yt.publish_date.strftime("%Y-%m-%d")
        self.length = self.yt.length
          
    def download_video_default(self):
        self.yt.streams.get_highest_resolution().download(filename=f"'{self.title}'.mp4")
    
    def download_audio_default(self):
        self.yt.streams.filter(abr="128kbps",progressive=False).first().download(filename=f"'{self.title}'.mp3")
    
