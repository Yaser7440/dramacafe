#!/usr/bin/python
# -*- coding: utf-8 -*-
try:import sys,syspath
except:pass
import xbmc,xbmcaddon,xbmcplugin,xbmcgui,urllib,urllib2,re,os
import json

pluginhandle = int(sys.argv[1])


default_params="&order=date"  
        
print "defaultParams",default_params

KEYV3 = 'AIzaSyDn2w07I3D8xNQ9D-QcY5t3n0JZ7RW8J8c'


def read_url2(url):
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            print 'URL: '+url
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code
                #xbmc.executebuiltin("XBMC.Notification(musichcannels,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: %s' %e.reason
                #xbmc.executebuiltin("XBMC.Notification(LiveStreams,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")

def getchannelid(chusername):
    url = 'https://www.googleapis.com/youtube/v3/channels?part=id&forUsername=%s&key=%s' % (chusername, KEYV3)
    content = read_url2(url)
   
    list1 = []
    
    if content:
        
            data = json.loads(content)
            channelId = str(data['items'][0]['id'])
            #url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId=' + channelId + '&maxResults=12'+ '&key=' + KEYV3 
            return channelId

def mainmenu(list1):
  for item in list1:
    try:mode=item[2]
    except:mode=1001
    
    addDir(item[0],item[1] ,mode,"",'')      
    
  
def submenu(name,chid,page=''):
  url='https://www.googleapis.com/youtube/v3/search?part=snippet&type=playlist&channelId='+chid+'&maxResults=11'+default_params+'&key='+KEYV3
  addDir('Playlists',url ,1002,"",'')
  url='https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId='+chid+'&maxResults=11'+default_params+'&key='+KEYV3
  addDir('Videos',url ,1002,"",'')
  

def getviedoList(name1, urlmain,page=''):
               
               print "page",page
               
               
               if page=='':
                  #&paged=2
                  #http://www.aflamy.com/portal/category/aflam-ajnaby/page/2/
                  #urlmain='https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId='+urlmain+'&maxResults=11'+default_params+'&key='+KEYV3     
                  url_page=urlmain
                  
               else:
                #http://www.dardarkom.com/filme-enline/filme-gharbi/page/2/
                      url_page=urlmain+"&pageToken="+page
               print "url_page",url_page
               
               content = read_url2(url_page)
               if content is None:
                  addDir('Error:downoad error','',1,'','')
                  return
	       data = json.loads(content)
	       c4_browse_ajax = str(data.get('nextPageToken', ''))               
               
	       a = 0
               l = len(data)

               if l<1:
                       addDir('No contents / results found!','',1,'','')
                       return
                       
	       list_item = 'ItemList' in data['kind']
	       for item in data.get('items', {}):
				if not list_item:
					kind = item['id']['kind']
				else:
					kind = item['kind']
				if kind:
					title = item['snippet']['title'].encode('utf-8')
					#title=title.decode('utf-8').encode('ascii','ignore')
					desc = item['snippet']['description'].encode('utf-8','ignore').replace("&","_").replace(";","")
					
					
					if kind.endswith('#video'):
						try:
							url = str(item['id']['videoId'])
							img = str(item['snippet']['thumbnails']['default']['url'])
							print "url",url
							stream_link = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
							addDir( title,stream_link,1004, img,desc,'')
						except:
							continue
						
						
					elif kind.endswith('#playlistItem'):
						try:
							url = str(item['snippet']['resourceId']['videoId'])
							img = str(item['snippet']['thumbnails']['default']['url'])
							url='plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
							addDir( title, url,1004, img,desc,'')
						except:
							pass
						
							
					elif kind.endswith('#channel'):
						url = str(item['id']['channelId'])
						img = str(item['snippet']['thumbnails']['default']['url'])
						#self.filmliste.append(('', title, url, img, desc, 'CV3', ''))
						url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId='+url+ '&maxResults=11'+default_params+'&key='+KEYV3
						
						addDir( title, url,1002, img,desc,'')
					elif kind.endswith('#playlist'):
						url = str(item['id']['playlistId'])
						img = str(item['snippet']['thumbnails']['default']['url'])
						#self.filmliste.append(('', title, url, img, desc, 'PV3', ''))
						url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+url+ '&maxResults=11'+default_params+'&key='+KEYV3
						
						addDir( title, url,1002, img,desc,'')
              
               if not c4_browse_ajax=='':
                  addDir( 'next page>', urlmain,1002, img,'',c4_browse_ajax)
def getplayList(name1, urlmain,page=''):
               print "mahmou1",urlmain
               print "page",page
               
               
               if page=='':
                  #&paged=2
                  #http://www.aflamy.com/portal/category/aflam-ajnaby/page/2/
                  urlmain='https://www.googleapis.com/youtube/v3/search?part=snippet&type=playlist&channelId='+urlmain+'&maxResults=11'+default_params+'&key='+KEYV3     
                  url_page=urlmain
                  
               else:
                #http://www.dardarkom.com/filme-enline/filme-gharbi/page/2/
                      url_page=urlmain+"&pageToken="+page
               print "url_page",url_page
               
               content = read_url2(url_page)
               if content is None:
                  addDir('Error:downoad error','',1,'','')
                  return
	       data = json.loads(content)
	       c4_browse_ajax = str(data.get('nextPageToken', ''))               
               
	       a = 0
               l = len(data)

               if l<1:
                       addDir('No contents / results found!','',1,'','')
                       return
                       
	       list_item = 'ItemList' in data['kind']
	       for item in data.get('items', {}):
				if not list_item:
					kind = item['id']['kind']
				else:
					kind = item['kind']
				if kind:
					title = item['snippet']['title'].encode('utf-8')
					desc = item['snippet']['description'].encode('utf-8').replace("&","_").replace(";","")
					
					if kind.endswith('#video'):
						try:
							url = str(item['id']['videoId'])
							img = str(item['snippet']['thumbnails']['default']['url'])
							print "url",url
							stream_link = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
							addDir( title+"_"+desc,stream_link,1004, img,desc,'')
						except:
							continue
						
						
					elif kind.endswith('#playlistItem'):
						try:
							url = str(item['snippet']['resourceId']['videoId'])
							img = str(item['snippet']['thumbnails']['default']['url'])
							url='plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
							addDir( title, url,1004, img,desc,'')
						except:
							pass
						
							
					elif kind.endswith('#channel'):
						url = str(item['id']['channelId'])
						img = str(item['snippet']['thumbnails']['default']['url'])
						#self.filmliste.append(('', title, url, img, desc, 'CV3', ''))
						url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId='+url+ '&maxResults=12'+default_params+'&key='+KEYV3
						
						addDir( title, url,1002, img,desc,'')
					elif kind.endswith('#playlist'):
						url = str(item['id']['playlistId'])
						img = str(item['snippet']['thumbnails']['default']['url'])
						#self.filmliste.append(('', title, url, img, desc, 'PV3', ''))
						url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+url+ '&maxResults=12'+default_params+'&key='+KEYV3
						
						addDir( title, url,1002, img,desc,'')
              
               if not c4_browse_ajax=='':
                  addDir( 'next page>', urlmain,1002, img,desc,c4_browse_ajax)



                  
def addDir(name,url,mode,iconimage,desc='',page=''):
        if not page=='':
           u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&desc="+urllib.quote_plus(desc)+"&pageToken="+str(page)
        else:
           u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name) +"&desc="+urllib.quote_plus(desc)+"&pageToken="  
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def playlink(url):
            print "m2",url
	    listItem = xbmcgui.ListItem(path=str(url))
	    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listItem)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        print "input,output",paramstring,param
        return param
def process_mode(list1=[]):
      params=get_params()
      url=None
      name=None
      mode=None
      page=''

              
      try:
              url=urllib.unquote_plus(params["url"])
      except:
              pass
      try:
              name=urllib.unquote_plus(params["name"])
      except:
              pass
      try:
              mode=int(params["mode"])
      except:
              pass
      try:
              page=str(params["pageToken"])
      except:
              pass
      print "Mode: "+str(mode)
      print "URL: "+str(url)
      print "Name: "+str(name)
      print "page: "+str(page)

      if type(url)==type(str()):
        url=urllib.unquote_plus(url)

      if mode==None:
               
        mainmenu(list1)
      elif mode == 1001:
          
          submenu(name,url,'')  
      elif mode == 1002:
          print "url",url
          
          getviedoList(name,url,page)
      elif mode == 1003:
          
          getplayList(name,url,page)
      elif mode == 1004:
          playlink(url)
      elif mode == 1005:
          #url ='https://www.googleapis.com/youtube/v3/channels?part=id&forUsername='+url+'&maxResults=12&relevanceLanguage=en&key=AIzaSyBPEkhZzAvfYQZYLmIQcOsklbZbTbymjb0'
          print "",url
          chid=getchannelid(url)
          submenu(name,chid,page='')
          #getvideoList(name,url,'')
      elif mode == 1006:##playlist
          print "url",url
          url='https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+url+'&maxResults=11&order=date&key='+KEYV3
          name='playlist'
          page=''
          getviedoList(name,url,page)
      elif mode == 1007:#play video
          if not url.startswith("plugin://"):
             url='plugin://plugin.video.youtube/?action=play_video&videoid='+url
          playlink(url)     
                   
#https://www.googleapis.com/youtube/v3/search?part=snippet&type=playlist&channelId=UCQH0vhD4yny1ZE3eDzYVSXA&maxResults=11&order=date&key=AIzaSyDn2w07I3D8xNQ9D-QcY5t3n0JZ7RW8J8c


