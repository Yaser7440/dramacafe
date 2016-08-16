# 2014.11.21 08:42:25 Arabian Standard Time
#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts/script.module.urlresolver/lib/urlresolver/types.py
import urlresolver
from urlresolver import common


class HostedMediaFile:
    """
    This class represents a piece of media (file or stream) that is hosted 
    somewhere on the internet. It may be instantiated with EITHER the url to the
    web page associated with the media file, OR the host name and a unique 
    ``media_id`` used by the host to point to the media.
    
    For example::
    
        HostedMediaFile(url='http://youtube.com/watch?v=ABC123XYZ')
        
    represents the same piece of media as::
    
        HostedMediaFile(host='youtube.com', media_id='ABC123XYZ')
        
    ``title`` is a free text field useful for display purposes such as in
    :func:`choose_source`.
    
    .. note::
    
        If there is no resolver plugin to handle the arguments passed, 
        the resulting object will evaluate to ``False``. Otherwise it will 
        evaluate to ``True``. This is a handy way of checking whether
        a resolver exists::
            
            hmf = HostedMediaFile('http://youtube.com/watch?v=ABC123XYZ')
            if hmf:
                print 'yay! we can resolve this one'
            else:
                print 'sorry :( no resolvers available to handle this one.')
    
    .. warning::
        
        If you pass ``url`` you must not pass ``host`` or ``media_id``. You 
        must pass either ``url`` or ``host`` AND ``media_id``.
    """

    def __init__(self, url = '', host = '', media_id = '', title = ''):
        """
        Args:
            url (str): a URL to a web page that represents a piece of media.
            
            host (str): the host of the media to be represented.
            
            media_id (str): the unique ID given to the media by the host.
        """
        if not url and not (host and media_id) or url and (host or media_id):
            raise ValueError('Set either url, or host AND media_id. ' + 'No other combinations are valid.')
        self.resolver = None
        self._url = url
        self._host = host
        self._media_id = media_id
        print 'Here in types-py self._url =', self._url
        print 'Here in types-py self._host =', self._host
        print 'Here in types-py self._media_id =', self._media_id
        if 'billionuploads' in url or 'billionuploads' in host:
            from plugins.billionuploads import billionuploads
            self.resolver = billionuploads
        elif 'daclips' in url or 'daclips' in host:
            from plugins.daclips import DaclipsResolver
            self.resolver = DaclipsResolver
        elif 'movreel' in url or 'movreel' in host:
            from plugins.movreel import movreelResolver
            self.resolver = movreelResolver
        elif 'flashx' in url or 'flashx' in host:
            from plugins.flashx import FlashxResolver
            self.resolver = FlashxResolver
        elif 'gorillavid' in url or 'gorillavid' in host:
            from plugins.gorillavid import GorillavidResolver
            self.resolver = GorillavidResolver
        elif 'vidto' in url or 'vidto' in host:
            from plugins.vidto import vidto
            self.resolver = vidto
        elif 'divxstage' in url or 'divxstage' in host:
            from plugins.divxstage import DivxstageResolver
            self.resolver = DivxstageResolver
        elif 'movshare' in url or 'movshare' in host:
            from plugins.movshare import MovshareResolver
            self.resolver = MovshareResolver
        elif 'novamov' in url or 'novamov' in host:
            from plugins.novamov import NovamovResolver
            self.resolver = NovamovResolver
        elif 'nowvideo' in url or 'nowvideo' in host:
            from plugins.nowvideo import NowvideoResolver
            self.resolver = NowvideoResolver
        elif 'played' in url or 'played' in host:
            from plugins.played import playedResolver
            self.resolver = playedResolver
        elif 'mightyupload' in url or 'mightyupload' in host:
            from plugins.mightyupload import MightyuploadResolver
            self.resolver = MightyuploadResolver
        elif 'filenuke' in url or 'filenuke' in host:
            from plugins.filenuke import FilenukeResolver
            self.resolver = FilenukeResolver
        elif 'allmyvideos' in url or 'allmyvideos' in host:
            from plugins.allmyvideos import AllmyvideosResolver
            self.resolver = AllmyvideosResolver
        elif 'promptfile' in url or 'promptfile' in host:
            from plugins.promptfile import PromptfileResolver
            self.resolver = PromptfileResolver
        elif 'sharerepo' in url or 'sharerepo' in host:
            from plugins.sharerepo import SharerepoResolver
            self.resolver = SharerepoResolver
        elif 'sharesix' in url or 'sharesix' in host:
            from plugins.sharesix import SharesixResolver
            self.resolver = SharesixResolver
        elif 'streamcloud' in url or 'streamcloud' in host:
            from plugins.streamcloud import StreamcloudResolver
            self.resolver = StreamcloudResolver
        elif 'thefile' in url or 'thefile' in host:
            from plugins.thefile import TheFileResolver
            self.resolver = TheFileResolver
        elif 'uploadc' in url or 'uploadc' in host:
            from plugins.uploadc import UploadcResolver
            self.resolver = UploadcResolver
        elif 'vidbull' in url or 'vidbull' in host:
            from plugins.vidbull import VidbullResolver
            self.resolver = VidbullResolver
        elif 'videoweed' in url or 'videoweed' in host:
            from plugins.videoweed import VideoweedResolver
            self.resolver = VideoweedResolver
        elif 'bayfiles' in url or 'bayfiles' in host:
            from plugins.bayfiles import bayfilesResolver
            self.resolver = bayfilesResolver
        elif 'bestreams' in url or 'bestreams' in host:
            from plugins.bestreams import BestreamsResolver
            self.resolver = BestreamsResolver
        elif 'cheesestream' in url or 'cheesestream' in host:
            from plugins.cheesestream import FilenukeResolver
            self.resolver = FilenukeResolver
        elif 'clicktoview' in url or 'clicktoview' in host:
            from plugins.clicktoview import ClicktoviewResolver
            self.resolver = ClicktoviewResolver
        elif 'dailymotion' in url or 'dailymotion' in host:
            from plugins.dailymotion import DailymotionResolver
            self.resolver = DailymotionResolver
        elif 'donevideo' in url or 'donevideo' in host:
            from plugins.donevideo import DonevideoResolver
            self.resolver = DonevideoResolver
        elif 'entroupload' in url or 'entroupload' in host:
            from plugins.entroupload import EntrouploadResolver
            self.resolver = EntrouploadResolver
        elif 'filebox' in url or 'filebox' in host:
            from plugins.filebox import FileboxResolver
            self.resolver = FileboxResolver
        elif 'hostingbulk' in url or 'hostingbulk' in host:
            from plugins.hostingbulk import hostingbulkResolver
            self.resolver = hostingbulkResolver
        elif 'hostingcup' in url or 'hostingcup' in host:
            from plugins.hostingcup import HostingcupResolver
            self.resolver = HostingcupResolver
        elif 'jumbofiles' in url or 'jumbofiles' in host:
            from plugins.jumbofiles import JumbofilesResolver
            self.resolver = JumbofilesResolver
        elif 'lemuploads' in url or 'lemuploads' in host:
            from plugins.lemuploads import LemuploadsResolver
            self.resolver = LemuploadsResolver
        elif 'limevideo' in url or 'limevideo' in host:
            from plugins.limevideo import LimevideoResolver
            self.resolver = LimevideoResolver
        elif 'megarelease' in url or 'megarelease' in host:
            from plugins.megarelease import MegareleaseResolver
            self.resolver = MegareleaseResolver
        elif 'mega-vids' in url or 'mega-vids' in host:
            from plugins.megavids import AllmyvideosResolver
            self.resolver = AllmyvideosResolver
        elif 'movzap|zuzvideo' in url or 'movzap|zuzvideo' in host:
            from plugins.movzap import MovzapZuzVideoResolver
            self.resolver = MovzapZuzVideoResolver
        elif 'nosvideo' in url or 'nosvideo' in host:
            from plugins.nosvideo import NosvideoResolver
            self.resolver = NosvideoResolver
        elif '180upload' in url or '180upload' in host:
            from plugins.oneupload import OneeightyuploadResolver
            self.resolver = OneeightyuploadResolver
        elif 'playwire' in url or 'playwire' in host:
            from plugins.playwire import PlaywireResolver
            self.resolver = PlaywireResolver
        elif 'putlocker' in url or 'putlocker' in host:
            from plugins.putlocker import PutlockerResolver
            self.resolver = PutlockerResolver
        elif 'filedrive' in url or 'filedrive' in host:
            from plugins.putlocker import PutlockerResolver
            self.resolver = PutlockerResolver
        elif 'firedrive' in url or 'firedrive' in host:
            from plugins.putlocker import PutlockerResolver
            self.resolver = PutlockerResolver
        elif 'realdebrid' in url or 'realdebrid' in host:
            from plugins.realdebrid import RealDebridResolver
            self.resolver = RealDebridResolver
        elif 'sockshare' in url or 'sockshare' in host:
            from plugins.sockshare import sockshareResolver
            self.resolver = sockshareResolver
        elif 'vidhog' in url or 'vidhog' in host:
            from plugins.vidhog import VidhogResolver
            self.resolver = VidhogResolver
        elif 'vidxden' in url or 'vidxden' in host:
            from plugins.vidxden import VidxdenResolver
            self.resolver = VidxdenResolver
        elif 'vk' in url.lower() or 'vk' in host.lower():
            from plugins.vk import VKResolver
            self.resolver = VKResolver
        elif 'vodlocker' in url or 'vodlocker' in host:
            from plugins.vodlocker import FilenukeResolver
            self.resolver = FilenukeResolver
        elif 'xvidstage' in url or 'xvidstage' in host:
            from plugins.xvidstage import XvidstageResolver
            self.resolver = XvidstageResolver
        elif 'youwatch' in url or 'youwatch' in host:
            from plugins.youwatch import YouwatchResolver
            self.resolver = YouwatchResolver
        elif 'cloudy' in url or 'cloudy' in host:
            from plugins.cloudy import CloudyResolver
            self.resolver = CloudyResolver
        else:
            return
        if self.resolver is None:
            print 'No supported host'
            return
        else:
            if not host:
                res = self.resolver()
                self._hostandid = res.get_host_and_id(url)
                print 'Here in types-py self._hostandid =', self._hostandid
                self._host = self._hostandid[0]
                self._media_id = self._hostandid[1]
            elif not url:
                self._url = self.resolver().get_url(host, media_id)
            else:
                return
            print 'Here in types-py self._url B=', self._url
            print 'Here in types-py self._host B=', self._host
            print 'Here in types-py self._media_id B=', self._media_id
            if title:
                self.title = title
            else:
                self.title = self._host
            return

    def get_url(self):
        """
        Returns the URL of this :class:`HostedMediaFile`.
        """
        return self._url

    def get_host(self):
        """
        Returns the host of this :class:`HostedMediaFile`.
        """
        return self._host

    def get_media_id(self):
        """
        Returns the media_id of this :class:`HostedMediaFile`.
        """
        return self._media_id

    def resolve(self):
        """
        Resolves this :class:`HostedMediaFile` to a media URL. 
        
        Example::
            
            stream_url = HostedMediaFile(host='youtube.com', media_id='ABC123XYZ').resolve()
        
        .. note::
        
            This method currently uses just the highest priority resolver to 
            attempt to resolve to a media URL and if that fails it will return 
            False. In future perhaps we should be more clever and check to make 
            sure that there are no more resolvers capable of attempting to 
            resolve the URL first. 
        
        Returns:
            A direct URL to the media file that is playable by XBMC, or False
            if this was not possible. 
        """
        common.addon.log_debug('resolving using %s plugin' % self.resolver)
        res = self.resolver()
        media_url = res.get_media_url(self._host, self._media_id)
        print 'Here in types-py media_url =', media_url
        if 'unresolvable' in str(media_url):
            media_url = None
        return media_url

    def valid_url(self):
        """
        Returns True if the ``HostedMediaFile`` can be resolved.
        
        .. note::
            
            The following are exactly equivalent::
                
                if HostedMediaFile('http://youtube.com/watch?v=ABC123XYZ').valid_url():
                    print 'resolvable!'
        
                if HostedMediaFile('http://youtube.com/watch?v=ABC123XYZ'):
                    print 'resolvable!'
            
        """
        if self.resolver:
            return True
        return False

    def _find_resolvers(self):
        imps = []
        for imp in UrlResolver.implementors():
            if imp.valid_url(self.get_url(), self.get_host()):
                imps.append(imp)

        return imps

    def __nonzero__(self):
        return self.valid_url()

    def __str__(self):
        return "{'url': '%s', 'host': '%s', 'media_id': '%s'}" % (self._url, self._host, self._media_id)

    def __repr__(self):
        return self.__str__()
# okay decompyling I:\winKodi\Kodi\scripts\script.module.urlresolver\lib\urlresolver\types.pyo 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.11.21 08:42:26 Arabian Standard Time
