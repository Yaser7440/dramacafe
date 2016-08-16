"""
streamcloud urlresolver plugin
Copyright (C) 2012 Lynx187

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import re
from urlresolver import common
from urlresolver.resolver import UrlResolver, ResolverError
def geturl(html):
        
     
        form_values = {}
        match = re.compile('<input.*?name="(.*?)".*?value="(.*?)">', re.DOTALL | re.IGNORECASE).findall(schtml)
        for name, value in match:
            form_values[name] = value.replace("download1","download2")
       
        newscpage = postHtml(streamcloudurl, form_data=form_values)
        videourl = re.compile('file: "(.+?)",', re.DOTALL | re.IGNORECASE).findall(newscpage)[0]
        return videourl
class StreamcloudResolver(UrlResolver):
    name = "streamcloud"
    domains = ["streamcloud.eu"]
    pattern = '(?://|\.)(streamcloud\.eu)/([0-9a-zA-Z]+)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        import sys
        web_url=sys.argv[len(sys.argv)-1]
        web_url=common.web_url()
        #web_url = self.get_url(host, media_id)
        resp = self.net.http_GET(web_url)
        html = resp.content
        print geturl(html)
        sys.exit(0)
        
        post_url = resp.get_url()
        if re.search('>(File Not Found)<', html):
            raise ResolverError('File Not Found or removed')

        form_values = {}
        for i in re.finditer('<input.*?name="(.*?)".*?value="(.*?)">', html):
            form_values[i.group(1)] = i.group(2).replace("download1", "download2")
        html = self.net.http_POST(post_url, form_data=form_values).content

        r = re.search('file: "(.+?)",', html)
        if r:
            return r.group(1)
        else:
            raise ResolverError('File Not Found or removed')

    def get_url(self, host, media_id):
        return 'http://streamcloud.eu/%s' % (media_id)

    def get_host_and_id(self, url):
        r = re.search(self.pattern, url)
        if r:
            return r.groups()
        else:
            return False

    def valid_url(self, url, host):
        return re.search(self.pattern, url) or self.name in host
