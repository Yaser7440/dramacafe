'''
    Vimeo plugin for Kodi
    Copyright (C) 2010-2012 Tobias Ussing And Henrik Mosgaard Jensen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import urllib
import re
import os.path
import datetime
import time
from xml.dom.minidom import parseString

try: import simplejson as json
except ImportError: import json
import xbmc,xbmcgui ,xbmcplugin,xbmcvfs
if True:



    import CommonFunctions as common
   

class VimeoPlayer():

    # Vimeo Playback Feeds
    urls = {}
    urls['embed_stream'] = "http://player.vimeo.com/play_redirect?clip_id=%s&sig=%s&time=%s&quality=%s&codecs=H264,VP8,VP6&type=moogaloop_local&embed_location="

    def __init__(self):
        self.xbmc = xbmc
        self.xbmcgui = xbmcgui
        self.xbmcplugin = xbmcplugin
        self.xbmcvfs = xbmcvfs

        
        
        
       
        
        self.common = common
        
       
        
        
        #self.storage = sys.modules["__main__"].storage

    # ================================ Video Playback ====================================
    def playVideo(self, params={}):
        self.common.log("")
        get = params.get
        (video, status) = self.getVideoObject(params)
        if status != 200:
            self.common.log("construct video url failed, contents of video item " + repr(video))
            
            return False

        listitem = self.xbmcgui.ListItem(label=video['Title'], iconImage=video['thumbnail'], thumbnailImage=video['thumbnail'], path=video['video_url'])
        listitem.setInfo('Video', {'infoLabels': 'video'})

        self.common.log("Playing video: " + video['Title'] + " - " + get('videoid') + " - " + video['video_url'])

        self.xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listitem)
        #self.storage.storeValue("vidstatus-" + get('videoid'), "7")

    def scrapeVideoInfo(self, params):
        get = params.get
        try:
          result = self.common.fetchPage({"link": "http://www.vimeo.com/%s" % get("videoid")})
          result = str(result).replace('\n','')
          rurl = re.compile('data-config-url="(.+?)"').search(result).group(1)
          rurl = rurl.replace('&amp;','&')
          result = self.common.fetchPage({"link":rurl})
        except:
          result = self.common.fetchPage({"link": "http://player.vimeo.com/video/%s/config?type=moogaloop&referrer=&player_url=player.vimeo.com&v=1.0.0&cdn_url=http://a.vimeocdn.com" % get("videoid")})
        collection = {}
        if result["status"] == 200:
            html = result["content"]
            #print repr(html)
            #html = html[html.find('{config:{'):]
            #html = html[:html.find('}}},') + 3]
            #html = html.replace("{config:{", '{"config":{') + "}"
            collection = json.loads(html)
        return collection
    def addDir(name,url,mode,iconimage,page=0):
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&page="+str(page)
            ok=True
            liz=self.xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            ok=self.xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
            return ok
    def getVideoInfo(self, params):
        self.common.log("")
        get = params.get

        collection = self.scrapeVideoInfo(params)
        print 'collection',collection
        sys.exit(0)
        video = {}
        if collection.has_key("config"):
            video['videoid'] = get("videoid")
            title = collection["config"]["video"]["title"]
            if len(title) == 0:
                title = "No Title"
            title = self.common.replaceHTMLCodes(title)
            video['Title'] = title
            video['Duration'] = collection["config"]["video"]["duration"]
            video['thumbnail'] = collection["config"]["video"]["thumbnail"]
            video['Studio'] = collection["config"]["video"]["owner"]["name"]
            video['request_signature'] = collection["config"]["request"]["signature"]
            video['request_signature_expires'] = collection["config"]["request"]["timestamp"]

            isHD = collection["config"]["video"]["hd"]
            if str(isHD) == "1":
                video['isHD'] = "1"
        elif collection.has_key("request"):
            video['videoid'] = get("videoid")
            try:
               title = collection["video"]["title"]
            except:
               title = "" #collection["config"]["video"]["title"]
            if len(title) == 0:
                title = "No Title"
            title = self.common.replaceHTMLCodes(title)
            video['Title'] = title
            try:
               h264 = collection["request"]["files"]["h264"]
            except:
               h264 = collection["request"]["files"]["vp6"]
            video['Duration'] = "0"
            video['thumbnail'] = ""
            video['Studio'] = ""
            video['request_signature'] = ""
            video['request_signature_expires'] = ""
            video['urls'] = h264
            #print "video[urls] = "+str(video['urls'])
            print "video",video

            print 'video',video['urls']['mobile']['url']
            playlink(video['urls']['mobile']['url'])
        

        self.common.log("Done")
        return (video, 200)


    def getVideoObject(self, params):
        self.common.log("")
        get = params.get
        
        (video, status) = self.getVideoInfo(params)

        #Check if file has been downloaded locally and use that as a source instead


        get = video.get
        if not video:
            # we need a scrape the homepage fallback when the api doesn't want to give us the URL
            self.common.log("getVideoObject failed because of missing video from getVideoInfo")
            return ("", 500)

        quality = self.selectVideoQuality(params, video)
        
        if ('apierror' not in video):
            #video_url =  self.urls['embed_stream'] % (get("videoid"), video['request_signature'], video['request_signature_expires'], quality)
            #result = self.common.fetchPage({"link": video_url, "no-content": "true"})
            #print repr(result)
            #video['video_url'] = result["new_url"]
	    if quality in video["urls"]: video['video_url'] = video["urls"][quality]["url"]
            self.common.log("Done")
            return (video, 200)
        else:
            self.common.log("Got apierror: " + video['apierror'])
            return (video['apierror'], 303)

    def selectVideoQuality(self, params, video):
        self.common.log("" + repr(params) + " - " + repr(video))
        get = params.get
        vget = video.get

        quality = "sd"

        
        quality = "hd"
        
        

        
        return quality

    def userSelectsVideoQuality(self, params):
        items = [("hd", "720p"),("sd", "SD")]
        choices = []
                
        if len(items) > 1:             
            for (quality, message) in items:
                choices.append(message)
    
            dialog = self.xbmcgui.Dialog()
            selected = dialog.select(self.language(30518), choices)

            if selected > -1:
                (quality, message) = items[selected]
                return quality
        
        return "sd"
def playlink(url):
            print "m2",url
            import xbmcgui,xbmcplugin
            listItem = xbmcgui.ListItem(path=str(url))
            xbmcplugin.setResolvedUrl(1, True, listItem)
