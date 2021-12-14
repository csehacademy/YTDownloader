from pytube import YouTube

link = input("enter your YouTube url : ")
yt = YouTube(link)
videos = yt.streams.all()
# This will stream all the format available for the video

video = list(enumerate(videos))
# This will be index all the format in list starting with zero
for i in video:
    print(i)
    # This will print all the available format of video with proper index

print ("enter the desired option to download the format")
dn_option = int(input(" enter the option : "))
# Ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download()

print("Download succesfully")