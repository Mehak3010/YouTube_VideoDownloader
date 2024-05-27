from pytube import YouTube

url  = input("Enter your link here:: ")

directory = input("Enter file path to store your video:: ")

link = YouTube(url)

video = link.streams.filter(progressive=True).get_highest_resolution() # Use this to download video with heighest resolution

video = link.streams.filter(progressive=True).get_lowest_resolution()  # Use this to download video with lowest resolution


video.download(directory)
