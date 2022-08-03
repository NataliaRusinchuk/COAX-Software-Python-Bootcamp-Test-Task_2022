"""
Make gif from TikTok video
Needs imageio and imageio-ffmpeg-0.4.7 to be installed
"""

import os, sys
import imageio
import urllib.request


def convertFile(video_path: str, output_path: str):
    """
    Function for creating gif from video via url\n
    PARAMETERS:\n
    video_path - string, contains url of the video\n
    output_path = string, contains path and name of output file
    """

    temp = "video.mp4"
    try:
        urllib.request.urlretrieve(video_path, temp)
    except:
        sys.exit("Invalid url") 
    try:
        writer = imageio.get_writer(output_path, fps=25)
    except:
        sys.exit("Invalid path for output file")
    for i, im in enumerate(imageio.imiter(temp)):
        writer.append_data(im)
    writer.close()
    os.remove(temp)

# Testing for some file
if __name__ == "main":
    url_link = "https://v16-webapp.tiktok.com/3630da5b3e0990a5706b12930f587856/62e84f38/video/tos/useast2a/tos-useast2a-pve-0068/68e17727aec140108911aa33dadef421/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1886&bt=943&btag=80000&cs=0&ds=3&ft=eXd.6HKvMyq8ZlE~1we2NFh4yl7Gb&mime_type=video_mp4&qs=0&rc=N2ZkaDtlZjQ8NTlkOWY6PEBpanc8NWg6ZnI5ZDMzNzczM0BhYzYxYmItXi8xLS01NWI1YSMybmM0cjRvbWlgLS1kMTZzcw%3D%3D&l=20220801160839010192166238254104D8"
    convertFile(url_link, 'task_2_animation.gif')
