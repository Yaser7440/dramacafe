# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts/script.module.urlresolver/lib/urlresolver/tsmresolver.py
import os, sys, urllib

def gethostname(url):
    try:
        return url.split('/')[2].replace('www.', '').replace('embed.', '').split('.')[0]
    except:
        return url


def get_linkid(web_url):
    parts = web_url.split('/')
    if parts:
        web_url = web_url.split('/')[len(parts) - 1]
    return web_url


def resolve(web_url = None, host = None, media_id = None, urllist = False):
    if host is None and web_url is not None:
        host = gethostname(web_url)
    stream_url = None
    done = True
    try:
        host = host.lower()
    except:
        pass

    print '16host,web_url', host, web_url
    sys.argv.append(web_url)
    debug = True
    if debug:
        print 'web_url', web_url
        if web_url is not None and media_id is None:
            media_id = get_linkid(web_url)
            if '.' in media_id:
                media_id = media_id.split('.')[0]
            print 'extracted_media_id', media_id
###############pelisresolver
        if 'fastvideo' in host or 'fastvideo' in web_url:
                import pelisresolver
                from pelisresolver.servers.fastvideo import get_video_url 
                
                host='fastvideo'
               
                stream_url = get_video_url(web_url)
                print "stream_url",stream_url
                if urllist==True:
                    return stream_url
                else:
                    return stream_url[0]
        if 'openload' in host or 'openload' in web_url:
            from urlresolver.plugins.openload import OpenLoadResolver as Resolver
            
            host = 'openload'
                
        '''if 'openload' in host or 'openload' in web_url:#ok
                             import pelisresolver
                             from pelisresolver.servers.openload import get_video_url
                             host = 'openload'
                             stream_url = get_video_url(web_url)
                             print 'stream_urlstm', stream_url
                             if urllist == True:
                                 return stream_url
                             else:
                                 return stream_url[0][1]'''
        '''if 'youwatch' in host or 'youwatch' in web_url:#ok
                import pelisresolver
                from pelisresolver.servers.youwatch import get_video_url 
                
               
                stream_url = get_video_url(web_url)
                print "stream_url-tm",stream_url
                if urllist==True:
                    return stream_url
                else:
                    return stream_url'''
   
        if host == 'hqq' or 'hqq' in web_url or  'netutv' in web_url:
                import pelisresolver
                from pelisresolver.servers.netutv import get_video_url 
                
               
                stream_url = get_video_url(web_url)
                print "stream_url-tm",stream_url
                if urllist==True:
                    return stream_url
                else:
                    return stream_url  
###############end pelisresolver
        if 'drive.google' in host or 'drive.google' in web_url or 'docs.google' in host or 'docs.google' in web_url:
                #from pelisresolver.servers.googledrive import get_video_url 
                from urlresolver.plugins.googledrive import get_video_url
                host='googledrive'
                
                stream_url = get_video_url(web_url)
                if urllist==True:
                    return stream_url
                else:
                    return stream_url[0][1]        
        if 'google' in host or 'google' in web_url:
                #from pelisresolver.servers.googledrive import get_video_url 
                from urlresolver.plugins.googlevideo import GoogleResolver as Resolver
                host='googlevideo'
                
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return

        print "web_url44",host,web_url

        if host == 'up2stream' or 'up2stream' in web_url:
                from urlresolver.plugins.up2stream import Up2StreamResolver as Resolver
                
                host = 'up2stream'                    
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return stream_url        
        if host == 'keeload' or 'keeload' in web_url:
                from urlresolver.plugins.keeload import keeloadResolver as Resolver
                
                host = 'keeload'                    
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return stream_url
        if host == 'vidag' or 'vid.ag' in web_url:
                from urlresolver.plugins.vidag import VidAgResolver as Resolver
               
                host = 'vidag'                    
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return stream_url
            
        if host == 'videorev' or 'videorev' in web_url:
                from urlresolver.plugins.videorev import VideoRevResolver as Resolver
               
                host = 'videorev'                    
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return stream_url
            
        if host == 'uptobox' or 'uptostream' in web_url:
                from urlresolver.plugins.uptobox import UpToBoxResolver as Resolver
               
                host = 'uptobox'                    
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                return stream_url
        if 'moevideos' in host or 'moevideos' in web_url:
            from pelisresolver.servers.moevideos import get_video_url
            host = 'moevideos'
            stream_url = get_video_url(web_url)
            print 'stream_urls', stream_url
            if urllist == True:
                return stream_url
            else:
                return stream_url[0][1]
        if 'dailymotion' in host or 'dailymotion' in web_url:
            from urlresolver.plugins.dailymotion import DailymotionResolver as Resolver
           
            host = 'dailymotion'
            resolver = Resolver()
            stream_url = resolver.get_media_url(host, media_id)
            if urllist == True:
                return stream_url
            else:
                return stream_url[0]
        else:
           
            if host == 'allvid' or 'allvid' in web_url:
                from urlresolver.plugins.allvid import AllVidResolver  as Resolver
                
                print "web_urlxx",web_url
                
                host = 'allvid'            
                resolver = Resolver()
                stream_url = resolver.get_media_url(host, media_id)
                print "stream_url"
                return stream_url            
           
            if host == 'hqq' or 'hqq' in web_url:
                from urlresolver.plugins.hqqresolver import resolve
                host = 'hqq'
                stream_url = resolve(web_url)
                if stream_url is None:
                    stream_url = 'unresolvable'
                return stream_url
            if host == 'vidhos' or 'vidhos' in web_url:
                from urlresolver.plugins.vidhosresolver import resolve
                host = 'vidhos'
                stream_url = resolve(web_url)
                if stream_url is None:
                    stream_url = 'unresolvable'
                return stream_url
            if host == 'movpod' or 'movpod' in web_url:
                from urlresolver.plugins.movpod import MovpodResolver as Resolver
                
                host = 'movpod'
                
                return stream_url
            if host == 'cloudy' or 'cloudy' in web_url:
                from urlresolver.plugins.cloudy import CloudyResolver as Resolver
                
                host = 'cloudy'                
            elif host == 'vidup' or 'vidup' in web_url:
                from urlresolver.plugins.vidup_org import VidUpResolver as Resolver
                
                host = 'vidup'
            elif host == 'daclips' or 'daclips' in web_url:
                from urlresolver.plugins.daclips import DaclipsResolver as Resolver
                
                host = 'movpod'
            else:
                if host == 'filepup' or 'filepup' in web_url:
                        from urlresolver.plugins.filepup import FilePupResolver  as Resolver
                        
                        print "web_urlxx",web_url
                        
                        host = 'filepup'            
                        resolver = Resolver()
                        stream_url = resolver.get_media_url(host, media_id)
                        print "stream_url"
                        return stream_url 
             
            
                if host == 'videoapi' or 'videoapi' in web_url or host == 'mail' or 'mail' in web_url:
                    from urlresolver.plugins.mailru import MailRuResolver as Resolver
                    host = 'mail.ru'
                    resolver=Resolver()
                    stream_url = resolver.get_media_url(host, media_id)
                    print "stream_url"
                    return stream_url 
                if host == 'hqq' or 'hqq' in web_url:
                    from urlresolver.plugins.hqqresolver import resolve
                    host = 'shared'
                    stream_url = resolve(web_url)
                    if stream_url is None:
                        stream_url = 'unresolvable'
                    return stream_url
                if host == 'shared' or 'shared.sx' in web_url:
                    from urlresolver.plugins.sharedsx import SharedsxResolver as Resolver
                    
                    host = 'shared'
                elif host == 'vidspot' or 'vidspot' in web_url:
                    from urlresolver.plugins.vidspot import VidSpotResolver as Resolver
                    
                    host = 'vidspot'
                elif host == 'mrfile' or 'mrfile' in web_url:
                    from urlresolver.plugins.mrfile import mrfileResolver as Resolver
                    
                    host = 'mrfile'
                elif host == 'letwatch' or 'letwatch' in web_url:
                    from urlresolver.plugins.letwatch import LetwatchResolver as Resolver
                    
                    host = 'letwatch'
                elif host == 'primeshare' or 'primeshare' in web_url:
                    from urlresolver.plugins.primeshare import PrimeshareResolver as Resolver
                    
                    host = 'primeshare'
                elif host == 'video.tt' or 'video.tt' in web_url:
                    from urlresolver.plugins.videott import VideoTTResolver as Resolver
                    
                    host = 'video.tt'
                elif (host == 'vshare' or 'vshare' in web_url) and 'movshare' not in web_url:
                    from urlresolver.plugins.vshare import VshareResolver as Resolver
                    
                    host = 'vshare.io'
                elif host == 'realvid' or 'realvid' in web_url:
                    from urlresolver.plugins.realvid import RealvidResolver as Resolver
                    
                    host = 'realvid'
                elif host == 'cloudyvideos' or 'cloudyvideos' in web_url:
                    from urlresolver.plugins.cloudyvideos import CloudyvideosResolver as Resolver
                    
                    host = 'cloudyvideos'
                elif host == 'streamin' or 'streamin' in web_url:
                    from urlresolver.plugins.streaminto import StreamintoResolver as Resolver
                    
                    host = 'streamin.to'
                elif host == 'videomega' or 'videomega' in web_url:
                    from urlresolver.plugins.videomega import VideomegaResolver as Resolver
                    
                    host = 'videomega'

                elif host == 'watchers' or 'watchers' in web_url:
                    from urlresolver.plugins.watchers import WatchersResolver as Resolver
                    
                    host = 'watchers'                    
                elif host == 'exashare' or 'exashare' in web_url:
                    from urlresolver.plugins.exashare import ExashareResolver as Resolver
                    
                    host = 'exashare'
                elif host == 'vidxden' or 'vidxden' in web_url:
                    from urlresolver.plugins.vidxden import VidxdenResolver as Resolver
                    
                    host = 'vidxden'
                elif host == 'vidzi' or 'vidzi' in web_url:
                    from urlresolver.plugins.vidzi import vidziResolver as Resolver
                    if '-' in web_url:
                        media_id = web_url.split('-')[1]
                    
                    host = 'vidzi'
                elif host == 'srvid' or 'shrvid' in web_url:
                    from urlresolver.plugins.shrvid import AllmyvideosResolver as Resolver
                    
                    host = 'shrvid'
                else:
                    if host == 'vimeo' or 'vimeo' in web_url:
                        from urlresolver.plugins.vimeo import VimeoResolver as Resolver
                        resolver = Resolver()
                        stream_url = resolver.get_media_url(host, media_id)
                        print "stream_url"
                        return stream_url                         
                    if host == 'vidbull' or 'vidbull' in web_url:
                        from urlresolver.plugins.vidbull import VidbullResolver as Resolver
                        
                        host = 'vidbull'
                    elif host == 'bestreams' or 'bestreams' in web_url:
                        from urlresolver.plugins.bestreams import BestreamsResolver as Resolver
                        host = 'bestreams'
                    elif host == 'vodlocker' or 'vodlocker' in web_url:
                        from urlresolver.plugins.vodlocker import VodlockerResolver as Resolver
                        host = 'vodlocker'
                        
                    elif host == 'vidgg' or 'vidgg' in web_url:
                        from urlresolver.plugins.vidgg import VidggResolver as Resolver
                        
                        host = 'vidgg'                        
                    elif host == 'thevideo' or 'thevideo' in web_url:
                        from urlresolver.plugins.thevideo import TheVideoResolver as Resolver
                        
                        host = 'thevideo.me'
                    elif host == 'gorillavid' or 'gorillavid' in web_url:
                        if web_url.endswith('.flv'):
                            return web_url
                        from urlresolver.plugins.gorillavid import GorillavidResolver as Resolver
                        host = 'gorillavid'
                    elif 'firedrive' in host or 'putlocker' in host or 'sockshare' in host or 'putlocker' in web_url or 'sockshare' in web_url or 'firedrive' in host:
                        if 'sockshare' in host or 'sockshare' in web_url:
                            from urlresolver.plugins.sockshare import sockshareResolver as Resolver
                            host = 'sockshare'
                        else:
                            from urlresolver.plugins.putlocker import PutlockerResolver as Resolver
                            host = 'putlocker'
                        print 'myresolver33putlocker', web_url
                    elif 'facebook' in host.lower() or 'facebook' in web_url:
                        from urlresolver.plugins.facebook import FacebookResolver as Resolver
                        host = 'facebook'
                    elif 'stagevu' in host.lower() or 'stagevu' in web_url:
                        from urlresolver.plugins.stagevu import StagevuResolver as Resolver
                        host = 'stagevu'
                    elif 'mightyupload' in host.lower() or 'mightyupload' in web_url or'mightyload' in host.lower() or 'mightyload' in web_url:
                        from urlresolver.plugins.mightyupload import MightyuploadResolver as Resolver
                        
                        host = 'mightyupload.com'
                    elif 'sharerepo' in host.lower() or 'sharerepo' in web_url:
                        from urlresolver.plugins.sharerepo import SharerepoResolver as Resolver
                        
                        host = 'sharerepo'
                    elif 'thefile' in host.lower() or 'thefile' in web_url:
                        from urlresolver.plugins.thefile import TheFileResolver as Resolver
                        host = 'thefile'
                    elif host.lower() == 'vidto' or 'vidto' in web_url:
                        from urlresolver.plugins.vidto import VidtoResolver as Resolver
                        
                        host = 'vidto.me'
                    elif host == 'clicktoview' or 'clicktoview' in web_url:
                        from urlresolver.plugins.clicktoview import ClicktoviewResolver as Resolver
                        host = 'clicktoview'
                    elif host == 'xvidstage' or 'xvidstage' in web_url:
                        from urlresolver.plugins.xvidstage import XvidstageResolver as Resolver
                        
                        host = 'xvidstage'
                    elif host == 'nowvideo' or 'nowvideo' in web_url:
                        from urlresolver.plugins.nowvideo import NowvideoResolver as Resolver
                        host = 'nowvideo'
                        if '=' in web_url:
                            media_id = web_url.split('=')[1]
                    elif 'divxstage' in host or 'divxstage' in web_url or 'cloudtime' in host or 'cloudtime' in web_url:
                        from urlresolver.plugins.divxstage import DivxstageResolver as Resolver
                        web_url = web_url.replace('divxstage', 'cloudtime')
                        
                        host = 'divxstage'
                    elif host == 'ok' or 'ok.ru' in web_url:
                            from urlresolver.plugins.okruresolver import resolve
               
                            host='okru'
                            print "web_url",web_url
                
                            stream_url = resolve(web_url)
                            if urllist==True:
                                return stream_url
                            else:
                                return stream_url[0] 
                    elif 'vk' in host.lower() or '.vk' in web_url or 'video_ext.php' in web_url:
                        from urlresolver.plugins.vk import VKResolver as Resolver
                        
                        host = 'vk'
                    elif 'vidspot' in host or 'allmyvideos' in host or 'allmyvideos' in web_url:
                        from urlresolver.plugins.allmyvideos import AllmyvideosResolver as Resolver
                        if 'vidspot' in host:
                            host = 'vidspot'
                        else:
                            host = 'allmyvideos'
                        
                    elif 'bayfiles' in host or 'bayfiles' in web_url:
                        from urlresolver.plugins.bayfiles import bayfilesResolver as Resolver
                        try:
                            web_url = os.path.basename(web_url)
                        except:
                            pass

                        host = 'bayfiles'
                    elif 'nosvideo' in host or 'nosvideo' in web_url:
                        from urlresolver.plugins.nosvideo import NosvideoResolver as Resolver
                        
                        host = 'nosvideo'
                    elif 'filenuke' in host or 'filenuke' in web_url:
                        from urlresolver.plugins.filenuke import FilenukeResolver as Resolver
                        
                        host = 'filenuke'
                    elif 'flashx' in host or 'flashx' in web_url:
                        from urlresolver.plugins.flashx import FlashxResolver as Resolver
                        

                        host = 'flashx'
                    elif 'hugefiles' in web_url or 'hugefiles' in web_url:
                        from urlresolver.plugins.hugefiles import HugefilesResolver as Resolver
                        host = 'hugefiles'
                    elif 'movshare' in host.lower() or 'movshare' in web_url:
                        from urlresolver.plugins.movshare import MovshareResolver as Resolver
                        
                        print 'movshare', web_url
                        host = 'movshare'
                    elif 'neodrive' in host.lower() or 'neodrive' in web_url:
                        from urlresolver.plugins.neodrive import neodriveResolver as Resolver
                        
                        host = 'newdrive'
                    elif 'zalaa' in host.lower() or 'zalaa' in web_url:
                        from urlresolver.plugins.zalaa import ZalaaResolver as Resolver
                        
                        try:
                            media_id = web_url.split('/')[3] + '/' + web_url.split('/')[4]
                        except:
                            pass

                        host = 'zalaa'
                    else:
                        if 'youtube' in host or 'youtube' in web_url:
                            print 'myresolver84', web_url
                            
                            from tube_resolver.plugin import getvideo 
                            host = 'youtube'
                            print 'myresolver85', host
                            stream_url, error = getvideo(web_url)
                            print 'myresolver86', stream_url, error
                            return (stream_url, error)
                        if 'vidhog' in host or 'vidhog' in web_url:
                            from urlresolver.plugins.vidhog import VidhogResolver as Resolver
                            host = 'vidhog'
                        elif 'videoweed' in host or 'videoweed' in web_url:
                            from urlresolver.plugins.videoweed import VideoweedResolver as Resolver
                            
                            host = 'videoweed'
                        elif 'openload' in host or 'openload' in web_url:
                            from urlresolver.plugins.openload import OpenLoadResolver as Resolver
                            
                            host = 'openload'
                        elif 'videowood' in host or 'videowood' in web_url:
                            from urlresolver.plugins.videowood import VideowoodResolver as Resolver
                            host = 'videowood'
                            
                        elif 'novamov' in host or 'novamov' in web_url:
                            from urlresolver.plugins.novamov import NovamovResolver as Resolver
                            media_id = get_linkid(web_url)
                            host = 'novamov'
                        elif 'veehd' in host or 'veehd' in web_url:
                            from urlresolver.plugins.veeHD import VeeHDResolver as Resolver
                            host = 'veehd.com'
                        elif 'uploadc' in host or 'uploadc' in web_url:
                            from urlresolver.plugins.uploadc import UploadcResolver as Resolver
                            
                            host = 'uploadc'

                        elif 'streamcloud' in host or 'streamcloud' in web_url:
                            from urlresolver.plugins.streamcloud import StreamcloudResolver as Resolver
                            
                            host = 'streamcloud'
                        elif 'zstream' in host or 'zstream' in web_url:
                            from urlresolver.plugins.zstream import ZstreamResolver as Resolver
                            
                            host = 'zstream.to'                        
                        elif 'sharesix' in host or 'sharesix' in web_url:
                            from urlresolver.plugins.sharesix import SharesixResolver as Resolver
                            
                            host = 'sharesix.com'
                        elif 'purevid' in host or 'purevid' in web_url:
                            from urlresolver.plugins.purevid import purevidResolver as Resolver
                            host = 'purevid'
                        elif 'promptfile' in host or 'promptfile' in web_url:
                            from urlresolver.plugins.promptfile import PromptfileResolver as Resolver
                            
                            host = 'promptfile'
                        elif 'movreel' in host or 'movreel' in web_url:
                            from urlresolver.plugins.movreel import movreelResolver as Resolver
                            
                            web_url = web_url.replace('http://', '')
                            parts = web_url.split('/')
                            if parts:
                                media_id = web_url.split('/')[len(parts) - 1]
                            host = 'movreel'
                            print 'host', host, media_id
                        elif 'youwatch' in host or 'youwatch' in web_url:
                            from urlresolver.plugins.youwatch import YouWatchResolver as Resolver
                            
                            host = 'youwatch'
                        elif 'played' in host or 'played' in web_url:
                            from urlresolver.plugins.played import playedResolver as Resolver
                            host = 'played'
                        elif '180upload' in host or '180upload' in web_url:
                            from urlresolver.plugins.one80upload import OneeightyuploadResolver as Resolver
                            web_url = web_url.replace('http://', '')
                            parts = web_url.split('/')
                            if parts:
                                media_id = web_url.split('/')[len(parts) - 1]
                            host = '180upload'
                        elif 'billionuploads' in host or 'billionuploads' in web_url:
                            from urlresolver.plugins.billionuploads import billionuploads as Resolver
                            
                        else:
                            print 'No supported host'
                            return 'unresolvable link,No supported host'
        resolver = Resolver()
        stream_url = resolver.get_media_url(host, media_id)
        print 'stream_url', stream_url
        try:
            if '"' in stream_url:
                stream_url = stream_url.split('"')[0]
        except:
            pass

        print 'stream_url-176', stream_url
    else:
        print 'error in resolving url'
        return 'unresolvable link,Error in resolving url'
    if stream_url is not None:
        try:
            if '|' in stream_url:
                try:
                    stream_url = stream_url.split('|')[0]
                except:
                    pass

        except:
            pass

    print 'Stream_url/myresolver/176', str(stream_url) + ':' + host
    print '186', str(stream_url)
    stream_url = str(stream_url)
    if 'unresolvable' in stream_url or 'None' in stream_url:
        stream_url = 'unresolvable:unable to resolve link'
    return stream_url
