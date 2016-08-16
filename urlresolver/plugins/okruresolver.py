# 2016.01.05 11:58:56 Jerusalem Standard Time
#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts/script.module.urlresolver/lib/urlresolver/plugins/okruresolver.py
import urllib2, re, os, sys, urllib, json
import xbmcgui, xbmcplugin

def read_url(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data
    except urllib2.URLError as e:
        print 'URL: ' + url
        if hasattr(e, 'code'):
            print 'We failed with error code - %s.' % e.code
            addDir('Download failed:' + str(e.code), '', '', '')
        elif hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: %s' % e.reason
            addDir('Download failed:' + str(e.reason), '', '', '')


def http_req(url, getCookie = False):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    req.add_header('Accept', ACCEPT)
    req.add_header('Cache-Control', 'no-transform')
    response = urllib2.urlopen(req)
    source = response.read()
    response.close()
    if getCookie:
        cookie = response.headers.get('Set-Cookie')
        return {'source': source,
         'cookie': cookie}
    return source


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

def _okru_to_res(string):
    string = string.strip()
    resolution = string
    if string == 'full':
        resolution = '1080p'
    elif string == 'hd':
        resolution = '720p'
    elif string == 'sd':
        resolution = '480p'
    elif string == 'low':
        resolution = '360p'
    elif string == 'lowest':
        resolution = '240p'
    elif string == 'mobile':
        resolution = '144p'
    return resolution


def ok_ru(url):
    sources = []
    list1 = []
    print 'id', url
    if True:
        id = re.search('\\d+', url).group(0)
        jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
        jsonSource = json.loads(http_req(jsonUrl))
        print 'jsonSource ', jsonSource['videos']
        for source in jsonSource['videos']:
            name = '%s %s' % ('', source['name'])
            duzenleyici = re.search('sig.+', source['url']).group(0)
            url = 'http://m.ok.ru/dk?st.cmd=moviePlaybackRedirect&st.' + duzenleyici
            addDir(name, url, 1, '', 1)
            list1.append((name, url))

        return list1


def resolve(url, urllist = False):
    web_url = url
    urllist = ok_ru(web_url)
    return
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    id = re.search('\\d+', url).group(0)
    json_url = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
    req = urllib2.Request(json_url, headers=HEADERS)
    response = urllib2.urlopen(req)
    source = response.read()
    response.close()
    json_source = json.loads(source)
    sources = []
    for source in json_source['videos']:
        name = _okru_to_res(source['name'])
        link = '%s|User-Agent=%s&Accept=%s'
        link = link % (source['url'], HEADERS['User-Agent'], HEADERS['Accept'])
        item = (name, link)
        sources.append(item)

    return sources


def addDir(name, url, mode, iconimage, page = 0):
    u = sys.argv[0] + '?url=' + urllib.quote_plus(url) + '&mode=' + str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz, isFolder=False)
    return ok


def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)
    return ok
# okay decompyling I:\TSmediaTools\Kodi\scripts\script.module.urlresolver\lib\urlresolver\plugins\okruresolver.pyo 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.01.05 11:58:56 Jerusalem Standard Time
