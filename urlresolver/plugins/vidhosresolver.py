# 2016.01.05 11:59:00 Jerusalem Standard Time
#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts/script.module.urlresolver/lib/urlresolver/plugins/vidhosresolver.py
import re, json, urllib2
__name__ = 'videomail'

def supports(url):
    return not _regex(url) == None


def read_url2(url):
    try:
        p = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(url)
        return p.read()
    except:
        addDir('Download failed:', '', '', '')
        return None

    return None


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
        elif hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: %s' % e.reason


def read_url3(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        req.add_header('Host', 'www.vidhos.com')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Cookie', 'popNum=8; __atuvc=6%7C34%2C3%7C35; popundr=1; PHPSESSID=478ff84e532ad811df5d63854f4f0fe1; watched_video_list=MTgzNDY%3D')
        response = urllib2.urlopen(req)
        link = response.read()
        return link
    except:
        addDir('Download failed:' + str(e.reason), '', '', '')


def resolve(url):
    if True:
        print 'url', url
        data = read_url3(url)
        parts = data.split('|')
        regx = '<span id=\'vplayer\'><img src="(.+?)" style'
        ip = re.findall(regx, data, re.M | re.I)[0]
        ip = ip.split('i/')[0]
        link = None
        for i in range(1, len(parts)):
            if parts[i] == 'provider':
                link = parts[i + 1]
                if link.strip == '':
                    continue
            if parts[i] == 'flv':
                link = parts[i + 1]

        print 'js', link
        if link is not None:
            link = ip + link + '/v.flv?start=0'
        return link
    else:
        return
# okay decompyling I:\TSmediaTools\Kodi\scripts\script.module.urlresolver\lib\urlresolver\plugins\vidhosresolver.pyo 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.01.05 11:59:00 Jerusalem Standard Time
