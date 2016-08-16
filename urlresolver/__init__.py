# 2014.11.21 08:42:18 Arabian Standard Time
#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts/script.module.urlresolver/lib/urlresolver/__init__.py
"""
This module provides the main API for accessing the urlresolver features.

For most cases you probably want to use :func:`urlresolver.resolve` or 
:func:`urlresolver.choose_source`.

.. seealso::
        
        :class:`HostedMediaFile`


"""
#from types import HostedMediaFile
import xbmcgui
def HostedMediaFile(url):
    resolve(url)
def resolve(web_url,urllist=False):
    """
    Resolve a web page to a media stream.
    
    It is usually as simple as::
        
        import urlresolver
        media_url = urlresolver.resolve(web_url) 
        
    where ``web_url`` is the address of a web page which is associated with a 
    media file and ``media_url`` is the direct URL to the media. 
    
    Behind the scenes, :mod:`urlresolver` will check each of the available 
    resolver plugins to see if they accept the ``web_url`` in priority order 
    (lowest priotity number first). When it finds a plugin willing to resolve 
    the URL, it passes the ``web_url`` to the plugin and returns the direct URL 
    to the media file, or ``False`` if it was not possible to resolve.
    
        .. seealso::
                
                :class:`HostedMediaFile`
    
    Args:
        web_url (str): A URL to a web page associated with a piece of media
        content.
        
    Returns:
        If the ``web_url`` could be resolved, a string containing the direct 
        URL to the media file, if not, returns ``False``.    
    """
    from tsmresolver import resolve
    return resolve(web_url,urllist=urllist)


def filter_source_list(source_list):
    """
    Takes a list of :class:`HostedMediaFile`s representing web pages that are 
    thought to be associated with media content. If no resolver plugins exist 
    to resolve a :class:`HostedMediaFile` to a link to a media file it is 
    removed from the list.
    
    Args:
        urls (list of :class:`HostedMediaFile`): A list of 
        :class:`HostedMediaFiles` representing web pages that are thought to be 
        associated with media content.
        
    Returns:
        The same list of :class:`HostedMediaFile` but with any that can't be 
        resolved by a resolver plugin removed.
    
    """
    return [ source for source in source_list if source ]


def choose_source(sources):
    """
    Given a list of :class:`HostedMediaFile` representing web pages that are 
    thought to be associated with media content this function checks which are 
    playable and if there are more than one it pops up a dialog box displaying 
    the choices.
    
    Example::
    
        sources = [HostedMediaFile(url='http://youtu.be/VIDEOID', title='Youtube [verified] (20 views)'),
                   HostedMediaFile(url='http://putlocker.com/file/VIDEOID', title='Putlocker (3 views)')]
                source = urlresolver.choose_source(sources)
                if source:
                        stream_url = source.resolve()
                        addon.resolve_url(stream_url)
                else:
                        addon.resolve_url(False)
    
    Args:
        sources (list): A list of :class:`HostedMediaFile` representing web 
        pages that are thought to be associated with media content.
        
    Returns:
        The chosen :class:`HostedMediaFile` or ``False`` if the dialog is 
        cancelled or none of the :class:`HostedMediaFile` are resolvable.    
        
    """
    sources = filter_source_list(sources)
    if len(sources) > 1:
        dialog = xbmcgui.Dialog()
        titles = []
        for source in sources:
            titles.append(source.title)

        index = dialog.select('Choose your stream', titles)
        if index > -1:
            return sources[index]
        else:
            return False
    else:
        if len(sources) == 1:
            return sources[0]
        common.addon.log_error('no playable streams found')
        return False
# okay decompyling I:\winKodi\Kodi\scripts\script.module.urlresolver\lib\urlresolver\__init__.pyo 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.11.21 08:42:20 Arabian Standard Time
