# -*- coding: utf8 -*-
##1.1.2 search hollowood added by mfaraj
try:import sys,syspath
except:pass
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from httplib import HTTP
from urlparse import urlparse
import StringIO
import httplib



__settings__ = xbmcaddon.Addon(id='plugin.video.dramacafe')
__icon__ = __settings__.getAddonInfo('icon')
__fanart__ = __settings__.getAddonInfo('fanart')
__language__ = __settings__.getLocalizedString
_thisPlugin = int(sys.argv[1])
_pluginName = (sys.argv[0])

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner
	
httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)

def GetCategories():
	#xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('WARNING','This addon is completely, Nobody has the right to charge you for this addon', 16000, 'https://pbs.twimg.com/profile_images/1908891822/R5MpO.gif'))
	url='http://www.online.dramacafe.in/index.html'
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	req.add_header('Host', 'www.online.dramacafe.in')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
	response = urllib2.urlopen(req)
	link=response.read()
	mylist=[]
	
	url_categories=(re.compile('<li class="topcat"><a href="(.+?)" class="topcat">(.+?)</a>').findall(link))
	url_categories_2=(re.compile('<li class=""><a href="(.+?)" class="">(.+?)</a>').findall(link))
	
	
	addDir('Search dramacafe','none',7,'')
	
	addDir('Recently added Hollywood movies','http://www.online.dramacafe.in/browse-NonArabicFilms-videos-1-date.html',5,'')
	addDir('Top rated Hollywood movies','http://www.online.dramacafe.in/browse-NonArabicFilms-videos-1-rating.html',15,'')
	addDir('Most viewed Hollywood movies','http://www.online.dramacafe.in/browse-NonArabicFilms-videos-1-views.html',115,'')
	
	addDir('Arabic movies','http://www.online.dramacafe.in/browse-ArabicMovies-videos-1-date.html',5,'')
	
        addDir('Bollywood movies','http://www.online.dramacafe.in/browse-Bollywood-videos-1-date.html',5,'')
        
        addDir('Non arabic series','http://www.online.dramacafe.in/browse-NonArabicSeries-videos-1-title.html',1115,'')
        addDir('Ramadan 2016 series','http://www.online.dramacafe.in/browse-Ramadan2016-videos-1-date.html',1115,'')
        addDir('Ramadan 2015 series','http://www.online.dramacafe.in/browse-Ramadan2015-videos-1-title.html',1115,'')
        addDir('Ramadan 2014 series','http://www.online.dramacafe.in/browse-Ramadan2014-videos-1-title.html',1115,'')
        addDir('Ramadan2013 series','http://www.online.dramacafe.in/browse-Ramadan2013-videos-1-title.html',1115,'')
        addDir('Ramadan2012 series','http://www.online.dramacafe.in/browse-Ramadan2012-videos-1-title.html',1115,'')
        addDir('Ramadan2011 series','http://www.online.dramacafe.in/browse-Ramadan2011-videos-1-title.html',1115,'')

        addDir('Eygptain Drama','http://www.online.dramacafe.in/browse-EgyptianDrama-videos-1-title.html',1115,'')
         
        addDir('Syrian Drama','http://www.online.dramacafe.in/browse-SyrianDrama-videos-1-title.html',1115,'')

        addDir('Lebanese Drama','http://www.online.dramacafe.in/browse-LebaneseDrama-videos-1-title.html',1115,'')

        addDir('Khaleeji series','http://www.online.dramacafe.in/browse-Khaleeji-videos-1-title.html',1115,'')

        addDir('IraqiDrama series','http://www.online.dramacafe.in/browse-IraqiDrama-videos-1-title.html',1115,'')
        
        addDir('Historical Bedwain series','http://www.online.dramacafe.in/browse-Historical-videos-1-title.html',1115,'')

        addDir('Asian Drama','http://www.online.dramacafe.in/browse-AsianDrama-videos-1-title.html',1115,'')

        addDir('Dubbed drama series','http://www.online.dramacafe.in/browse-DubbedDrama-videos-1-title.html',1115,'')

        
        addDir('Anime and Cartoon','http://www.online.dramacafe.in/browse-AnimeAndCartoon-videos-1-title.html',1115,'')
        addDir('Cartoon videos','http://www.online.dramacafe.in/browse-Cartoons-videos-1-title.html',1115,'')
        addDir('Anime movies','http://www.online.dramacafe.in/browse-AnimeMovies-videos-1-title.html',1115,'')
        
        
        
        
        

        
        addDir('Theatre','http://www.online.dramacafe.in/browse-Theatre-videos-1-title.html',1115,'')


def search(mainurl=None):
        
        
         
        search_entered = ''
        debug=True
        if debug:
               keyboard = xbmc.Keyboard(search_entered, 'Search 1channel')
               keyboard.doModal()
               if keyboard.isConfirmed():
                   search_entered = keyboard.getText() .replace(' ','+')  
                   print "mfarajx3",search_entered
                   
        else:
             print "search error"
            
        
        
        if mainurl=='none':
           url='http://www.online.dramacafe.in/search.php?keywords='+search_entered
            
        else:
          url=mainurl  
         
        print "mfarajx4_url",url
        indexFilmHollywood_search( "Search",url,1) 
        

def indexSerie(url,page):
    mainurl=url
    firstPart=str(url).split('videos')[0]
    nameList=[]
    secPart='videos-'
    lastPart='-date.html'
    counter=page
    debug=True
    if debug:
        counter=counter+1
        url=str(firstPart)+secPart+str(counter)+(lastPart)
        print "url",url,counter,page
        
        if checkUrl(url):
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            req.add_header('Host', 'www.online.dramacafe.in')
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
            response = urllib2.urlopen(req)
            link=response.read()
            target= re.findall(r'<span class="pm-video-li-thumb-info">(.*?)\s(.*?) <div class="pm-video-attr">', link, re.DOTALL)
            finalSerieImage=''
            for items in target:
                if str( items[1].split('</span>')[1]):
                    myPath=str( items[1].split('</span>')[1])
                    entirePath=str( myPath).replace("str( items[1].split('</span>')[1])", ' deLiM ').replace('" class="pm-thumb-fix pm-thumb-145"><span class="pm-thumb-fix-clip"><img src="',' deLiM ').replace('" alt="',' deLiM ').replace('" width="',' deLiM ')
                    entirePath=str(entirePath).split(' deLiM ')
                    try:
                        finalSerieImage=str( entirePath[1]).strip()
                    except:
                        finalSerieImage=''
                    if len(entirePath)>1:
                        finalSeriePath=str( entirePath[0]).replace('<a href="', '').strip()
                        finalSerieName=str( entirePath[2]).strip()
                        serieName=finalSerieName# str(finalSerieName).split('-')[0]
                        serieName=str(serieName).strip()
                        serieName=serieName.replace("&amp;","and")
                        if ('شارة' and 'الافلام' and 'افلام' and 'المسرحيات ' ) not in serieName:
                            if serieName not in nameList:
                                print "serieName",serieName
                                nameList.append(serieName)
                                addDir(serieName,finalSeriePath,2,finalSerieImage)
            addDir('next page>>',mainurl,1,'',page=counter)                    
								

def indexFilm(url,page):
    mainurl=url
    firstPart=str(url).split('videos')[0]
    nameList=[]
    secPart='videos-'
    lastPart='-date.html'
    counter=page
    debug=True
    if debug:
        counter=counter+1
        url=str(firstPart)+secPart+str(counter)+(lastPart)
        print url
        if checkUrl(url):
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            req.add_header('Host', 'www.online.dramacafe.in')
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
            response = urllib2.urlopen(req)
            link=response.read()
            target= re.findall(r'<span class="pm-video-li-thumb-info">(.*?)\s(.*?) <div class="pm-video-attr">', link, re.DOTALL)
            finalSerieImage=''
            for items in target:
                if str( items[1].split('</span>')[1]):
                    myPath=str( items[1].split('</span>')[1])
                    entirePath=str( myPath).replace("str( items[1].split('</span>')[1])", ' deLiM ').replace('" class="pm-thumb-fix pm-thumb-145"><span class="pm-thumb-fix-clip"><img src="',' deLiM ').replace('" alt="',' deLiM ').replace('" width="',' deLiM ')
                    entirePath=str(entirePath).split(' deLiM ')
                    try:
                        finalSerieImage=str( entirePath[1]).strip()
                    except:
                        finalSerieImage=''
                    if len(entirePath)>1:
                        finalSeriePath=str( entirePath[0]).replace('<a href="', '').strip()
                        finalSerieName=str( entirePath[2]).strip()
                        serieName= str(finalSerieName).split('-')[0]
                        serieName=str(serieName).strip()
                        serieName=serieName.replace("&amp;","and")
                        if ('شارة' and 'الافلام' and 'افلام' and 'المسرحيات ' ) not in serieName:
                            if serieName not in nameList:
                                nameList.append(serieName)
                                addLink(serieName,finalSeriePath,3,finalSerieImage)
            addDir('next page>>',mainurl,1,'',page=counter)


def checkUrl(url):
	p = urlparse(url)
	conn = httplib.HTTPConnection(p.netloc)
	conn.request('HEAD', p.path)
	resp = conn.getresponse()
	return resp.status < 400
								
def getEpos(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	req.add_header('Host', 'www.online.dramacafe.in')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
	response = urllib2.urlopen(req)
	link=response.read()
	target= re.findall(r'<span class="pm-video-li-thumb-info">(.*?)\s(.*?)<h3 dir=', link, re.DOTALL)
	for items in target:
		myItems=str( items[1]).split('</span>')[1]
		myItems=str(myItems).replace('<a href="', ' DELIM ').replace('" class="pm-thumb-fix pm-thumb-74"><span class="pm-thumb-fix-clip"><img src="', ' DELIM ').replace('" alt="', ' DELIM ').replace('" width="74"><span class="vertical-align">', ' DELIM ')
		myItems=str(myItems).split(' DELIM ')
		myPath=str( myItems[1]).strip()
		myImage=str( myItems[2]).strip()
		myName=str( myItems[3]).strip()
		if '|' not in myName:
			addLink(myName,myPath,3,myImage)


def playContent(url):
        print "mfaraj3",url
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	req.add_header('Host', 'www.online.dramacafe.in')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
	response = urllib2.urlopen(req)
	link=response.read()
	url_video=(re.compile('<iframe frameborder="0" width="560" height="317" src="(.+?)"></iframe>').findall(link))
	try:
		url_video=str(url_video).split('video/')
		url_video=str(url_video[1]).split('?syndication=')[0]
		url_video=str(url_video).strip()
		playback_url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url='+ str(url_video)
		listItem = xbmcgui.ListItem(path=str(playback_url))
		xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
	except:
		addLink('No video was found !','',334,'http://portal.aolcdn.com/p5/forms/4344/2af553bd-0f81-41d1-a061-8858924b83ca.jpg')
#######################
def indexFilmHollywood_search(name,url,page):
               
  
                
                    req = urllib2.Request(url)
                    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                    req.add_header('Host', 'www.online.dramacafe.in')
                    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                    req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
                    response = urllib2.urlopen(req)
                    link=response.read()
                    
                    regx='<h3 dir="ltr"><a href="(.*?)" class=".*?" title="(.*?)</a></h3>'
                    done=True
                    if done:

                            
                            match1 = re.findall(regx,link, re.S)
                            print "match1mfaraj",match1
                            i=0
                            for href,name in match1:
                                
                                #href="http://www.online.dramacafe.in/embed/"+href
                                print href
                                name=name.replace("&amp;","and")
                                try:name=name.decode('unicode_escape').encode('ascii','ignore').split("|")[1]
                                
                                except:pass                                
                                addDir(name,href,6,"",0)
                                                 
                                 
        
                            
                    else:
                               return None
                           
                
                    addDir('next page>>',mainurl,5,'',page=counter)		
def indexFilmHollywood(name,url,page):
                mainurl=url
                firstPart=str(url).split('videos')[0]
                nameList=[]
                secPart='videos-'
                lastPart='-date.html'
                counter=page
                debug=True
                if debug:
                    counter=counter+1
                    url=str(firstPart)+secPart+str(counter)+(lastPart)
                    print url
                    if checkUrl(url):
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        req.add_header('Host', 'www.online.dramacafe.in')
                        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
                        response = urllib2.urlopen(req)
                        link=response.read()
                    
                    regx='<h3 dir="ltr"><a href="(.*?)" class=".*?" title="(.*?)</a></h3>'
                    done=True
                    if done:

                            
                            match1 = re.findall(regx,link, re.S)
                            print "match1mfaraj",match1
                            i=0
                            for href,name in match1:
                                
                                #href="http://www.online.dramacafe.in/embed/"+href
                                print href
                                name=name.replace("&amp;","and").replace("|","_").replace("مترجم بجودة عالية","").replace("كامل بجودة عالية","")
                                try:name=name.decode('unicode_escape').encode('ascii','ignore').split("|")[1]
                                
                                except:pass
                                name=name.replace("&amp","_")
                                addDir(name,href,6,"",0)
                                                 
                                 
        
                            
                    else:
                               return None
                           
                
                    addDir('next page>>',mainurl,5,'',page=counter)
def indextopFilmHollywood(name,url,page):
                mainurl=url
                firstPart=str(url).split('videos')[0]
                nameList=[]
                secPart='videos-'
                lastPart='-rating.html'
                counter=page
                debug=True
                if debug:
                    counter=counter+1
                    url=str(firstPart)+secPart+str(counter)+(lastPart)
                    print url
                    if checkUrl(url):
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        req.add_header('Host', 'www.online.dramacafe.in')
                        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
                        response = urllib2.urlopen(req)
                        link=response.read()
                    
                    regx='<h3 dir="ltr"><a href="(.*?)" class=".*?" title="(.*?)</a></h3>'
                    done=True
                    if done:

                            
                            match1 = re.findall(regx,link, re.S)
                            print "match1mfaraj",match1
                            i=0
                            for href,name in match1:
                                
                                #href="http://www.online.dramacafe.in/embed/"+href
                                print href
                                name=name.replace("&amp;","and")
                                try:name=name.decode('unicode_escape').encode('ascii','ignore').split("|")[1]
                                
                                except:pass
                                
                                addDir(name,href,6,"",0)
                                                 
                                 
        
                            
                    else:
                               return None
                           
                
                    addDir('next page>>',mainurl,5,'',page=counter)

def indexviewsFilmHollywood(name,url,page):
                mainurl=url
                firstPart=str(url).split('videos')[0]
                nameList=[]
                secPart='videos-'
                lastPart='-views.html'
                counter=page
                debug=True
                if debug:
                    counter=counter+1
                    url=str(firstPart)+secPart+str(counter)+(lastPart)
                    print url
                    if checkUrl(url):
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        req.add_header('Host', 'www.online.dramacafe.in')
                        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
                        response = urllib2.urlopen(req)
                        link=response.read()
                    
                    regx='<h3 dir="ltr"><a href="(.*?)" class=".*?" title="(.*?)</a></h3>'
                    done=True
                    if done:

                            
                            match1 = re.findall(regx,link, re.S)
                            print "match1mfaraj",match1
                            i=0
                            for href,name in match1:
                                
                                #href="http://www.online.dramacafe.in/embed/"+href
                                print href
                                name=name.replace("&amp;","and")
                                try:name=name.decode('unicode_escape').encode('ascii','ignore').split("|")[1]
                                
                                except:pass                                
                                addDir(name,href,6,"",0)
                                                 
                                 
        
                            
                    else:
                               return None
                           
                
                    addDir('next page>>',mainurl,5,'',page=counter)
def indextitleFilmHollywood(name,url,page):
                mainurl=url
                firstPart=str(url).split('videos')[0]
                nameList=[]
                secPart='videos-'
                lastPart='-title.html'
                counter=page
                debug=True
                if debug:
                    counter=counter+1
                    url=str(firstPart)+secPart+str(counter)+(lastPart)
                    print url
                    if checkUrl(url):
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        req.add_header('Host', 'www.online.dramacafe.in')
                        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
                        response = urllib2.urlopen(req)
                        link=response.read()
                    
                    regx='<h3 dir="ltr"><a href="(.*?)" class=".*?" title="(.*?)</a></h3>'
                    done=True
                    if done:

                            
                            match1 = re.findall(regx,link, re.S)
                            print "match1mfaraj",match1
                            i=0
                            for href,name in match1:
                                
                                #href="http://www.online.dramacafe.in/embed/"+href
                                print href
                                name=name.replace("&amp;","and")
                                try:name=name.decode('unicode_escape').encode('ascii','ignore').split("|")[1]
                                
                                except:pass                                
                                addDir(name,href,6,"",0)
                                                 
                                 
        
                            
                    else:
                               return None
                           
                
                    addDir('next page>>',mainurl,5,'',page=counter)  


                    
def get_play_link(name, url,page):
    if True:
        print 'now get the GGG url'
        print "m1",url
        videoid = re.findall('-video_(.*?).html', url)
        print "videoid",videoid
        url = 'http://www.online.dramacafe.in/ajax.php?p=video&do=getplayer&vid=' + videoid[0] + '&aid=4&player=detail'
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link = response.read()
        target = re.findall('src="(.+?)"', link)
        print "target-mfaraj",target[0]
        if 'dailymotion.com' in str(target[0]):
            from urlresolver import resolve
        
            final_urls=resolve(str(target[0]),True)
            
            for item in final_urls:
                
               addDir(item[0],item[1],10,"",0)
	elif "openload" in target[0] or 'up2stream' in target[0]:
            from urlresolver import resolve
        
            final_url=resolve(str(target[0]),False)
            playlink(final_url)
            return
	    
        else:
            print "m12",target[0]
            vurl=target[0]
            if not vurl.startswith("http"):
                vurl="http:"+vurl
            req1 = urllib2.Request(vurl)
            req1.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            req1.add_header('Referer', 'http://www.online.dramacafe.in/')
            try:
                response = urllib2.urlopen(req1)
            except urllib2.HTTPError as e:
                print e.fp.read()
                return None
                #self.session.open(MessageBox, _('Stream is private'), MessageBox.TYPE_INFO, timeout=3)

            link1 = response.read()
            
            #self.session.open(MessageBox, _('Stream is private'), MessageBox.TYPE_INFO, timeout=3)
            regxori='"hd":{"profile"\\:113,"origin"\\:"ns3\\.pdl","url"\\:"(.+?)","height"'
            regx='"profile":116,"origin":"gcs","url":"https://s.vimeocdn.com/vimeo-prod-skyfire-std-us/01/2182/5/135911377/402464149.mp4?token=55d5da48_0x6efa977ec6d931f41c62ee072fce404506b0b1e0","cdn"'
            regx='"profile":116,"origin":"gcs","url":"(.+?)","cdn"'

            regx='"url":"(.+?)",".+?"'
            parts=link1.split('"profile":')
            for i in range(1,len(parts)):
                print "parts",parts[i]
                url=parts[i].split(",")[2].replace('"url":','').replace('"','')
                if i==1:
                    quality='Medium resolution'

                elif i==2:
                    quality='High resolution'
                elif i==3:
                    quality='Low resolution'
                
                addDir(quality,url,10,"",0)

            return    
            #regx='"profile"\\:116,"origin"\\:"gcs","url"\\:"(.+?)","cdn"'
            #regx='"hd":{"profile"\\:113,"origin":"ns3\\.pdl-secure","url":"https://pdlvimeocdn-a.akamaihd.net/46586/021/397243300.mp4?token2=1440075943_54f73c4eb063f707d15ef688188ca5c3&aksessionid=28104c656cf8c20f","height"'
            #regx='''"hd":{"profile"\\:113,"origin"\\:"gcs","url"\\:"(.+?)","cdn"'''
            #regx='''"hd":{"profile"\\:113,"origin"\\:"ns3\\.pdl","url":"(.+?)","height"'''
            #regx='''"hd":{"profile":113,"origin"\\:"gcs","url":"https://s.vimeocdn.com/vimeo-prod-skyfire-std-us/01/2165/5/135829560/402147637.mp4?token=55d5d048_0x8bc353e94490ce42f3b9c5f1bddb67f1ef13b4b3","cdn"'''
            hdLink = re.findall(regx, link1,re.S)
            print "m2",final_url
            final_url = str(hdLink[0])
            #xbmc.player().play(final_url)
            xbmc.Player().play(final_url)
            sys.exit(0)
	    listItem = xbmcgui.ListItem(path=str(final_url))
	    xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
    else:
            return None
            
		
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

def playlink(url):
            print "m2",url
            xbmc.Player().play(url)
            sys.exit(0)
	    listItem = xbmcgui.ListItem(path=str(url))
	    xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)

def addLink(name,url,mode,iconimage):
    u=_pluginName+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty("IsPlayable","true");
    ok=xbmcplugin.addDirectoryItem(handle=_thisPlugin,url=u,listitem=liz,isFolder=False)
    return ok
	


def addDir(name,url,mode,iconimage,page=0):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&page="+str(page)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

              
params=get_params()
url=None
name=None
mode=None
page=0

	
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
        page=int(params["page"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "page: "+str(page)

if mode==None or url==None or len(url)<1:
        print ""
        GetCategories()
       
elif mode==1:
        print ""+url
        indexSerie(url,page)
	
elif mode==2:
		print ""+url
		#getEpos(url)
		#playContent(url)
		get_play_link(name,url,page)	
elif mode==3:
	print ""+url
	playContent(url)
	
elif mode==4:
	print ""+url
	
	indexFilm(url,page)
elif mode==5:
	print "mfaraj"+url
	indexFilmHollywood(name,url,page)
	#getvideopage(url,page)
elif mode==15:
	print "mfaraj"+url
	indextopFilmHollywood(name,url,page)
	#getvideopage(url,page)
elif mode==115:
	print "mfaraj"+url
	indexviewsFilmHollywood(name,url,page)
elif mode==1115:
	print "mfaraj"+url
	indextitleFilmHollywood(name,url,page)	
	#getvideopage(url,page)	
elif mode==6:
	print "mfaraj"+url
	
	get_play_link(name,url,page)
elif mode==7:

    search(mainurl=url)
elif mode==10:

    playlink(url)	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
