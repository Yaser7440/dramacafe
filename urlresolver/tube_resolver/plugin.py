# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/resources/tube_resolver/plugin.py

import sys,os
print "sys.argv(2)",sys.argv[2]
drive=os.path.dirname(os.path.abspath(__file__))[:2]
videofile=drive+"/TSmediaTools/tmp/video.txt"
def getvideo(url = None):
    error = None
    url=url.replace("'","")
    print 'plugin7url', url
    
    url=url.strip()
    video_id = get_youtube_video_id(url)
    print 'plugin9video_id', url
    
    try:
        ql = str(config.plugins.tstube.vidqual.value)
    except:
        ql = '4'

    
    
    from youtubedl.YouTubeVideoUrl import YouTubeVideoUrl
    ytdl = YouTubeVideoUrl()

    
    if ql=='0':
        quality='17'

    elif ql=='1':
        quality='5'
    elif ql=='2':
        quality='18'
    elif ql=='3':
       quality='22'
    elif ql=='4':
       quality='22'
    elif ql=='5':
       quality='37'
    elif ql=='6':    
       quality='38'
    print "ql,quality",ql,quality
    video_url = ytdl.extract(video_id,quality)
 
    print 'video_url',video_url
    afile=open(videofile,"w")
    afile.write(video_url)
    afile.close()
    import webbrowser
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    
    webbrowser.open(video_url,new=new)  
    if video_url is not None and video_url.startswith('http'):
        return (video_url, None)
    else:
        return (None, video_url)
        return


def get_youtube_video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    print "value",value
    
    if value.startswith('plugin:') or "plugin:" in value:
        print "value2",value
        return value.split('=')[1]
    from urlparse import urlparse, parse_qs
    if 'youtu' not in value:
        return value
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return value
getvideo(sys.argv[2])
