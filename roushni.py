print('Content-type:text/html\r\n\r\n')

import pytube
from pytube.streams import Stream
import cgi
form = cgi.FieldStorage()
url = form.getvalue("url")
def downloadVideo(url):
	'''
    utility to download YouTube video 
    '''
	youTube = pytube.YouTube(url)
	stream = youTube.streams.get_highest_resolution()
	stream.download()

# pass the youtube video link to download
downloadVideo(url)
