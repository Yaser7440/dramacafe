# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para Google Video
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# ------------------------------------------------------------
# modify by DrZ3r0

import urllib2,re,os,sys,urllib,json
import xbmcgui,xbmcplugin

from t0mm0.common.net import Net
net=Net()
fmt_value = {
    5: "240p h263 flv",
    18: "360p h264 mp4",
    22: "720p h264 mp4",
    26: "???",
    33: "???",
    34: "360p h264 flv",
    35: "480p h264 flv",
    37: "1080p h264 mp4",
    36: "3gpp",
    38: "720p vp8 webm",
    43: "360p h264 flv",
    44: "480p vp8 webm",
    45: "720p vp8 webm",
    46: "520p vp8 webm",
    59: "480 for rtmpe",
    78: "400 for rtmpe",
    82: "360p h264 stereo",
    83: "240p h264 stereo",
    84: "720p h264 stereo",
    85: "520p h264 stereo",
    100: "360p vp8 webm stereo",
    101: "480p vp8 webm stereo",
    102: "720p vp8 webm stereo",
    120: "hd720",
    121: "hd1080"
    }


# Returns an array of possible video url's from the page_url
def get_video_url(page_url, premium=False, user="", password="", video_password=""):
  
    video_urls = []

    data =net.http_GET(page_url,headers={}).content #scrapertools.cache_page(page_url)

    #fmt_stream_map = scrapertools.find_single_match(data, r'\["fmt_stream_map","([^"]+)"\]')
    fmt_stream_map=re.findall(r'\["fmt_stream_map","([^"]+)"\]',data)[0]
    #print "fmt_stream_map",fmt_stream_map
    
    if fmt_stream_map[0] != '':
        fmt_stream_map = fmt_stream_map.replace(r'\u0026', '&').replace(r'\u003d', '=')
        for vdata in fmt_stream_map.split(','):
            vdata_split = vdata.split('|')
            name=fmt_value[int(vdata_split[0])]
            url= vdata_split[1]              
            video_urls.append(["[%s googledrive]" % fmt_value[int(vdata_split[0])], vdata_split[1]])
            addDir(name,url,1,'',1)
        #for video_url in video_urls:
            #logger.info("[googledrive.py] %s - %s" % (video_url[0], video_url[1]))
    print "video_urls",video_urls
    #sys.exit(0)
    return None


# Encuentra v�deos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    patronvideos = r'.google.com/file/d/([a-zA-Z0-9_-]+)'
    logger.info("[googledrive.py] find_videos #" + patronvideos + "#")

    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    for media_id in matches:
        titulo = "[googledrive]"
        url = 'https://drive.google.com/file/d/%s/preview' % media_id
        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'googledrive'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    return devuelve
def addDir(name,url,mode,iconimage,page=0):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty("IsPlayable","true");
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    return ok
