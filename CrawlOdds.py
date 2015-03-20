import urllib2


class CrawlOdds(object):
    def __init__(self):
        # open html page with url
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                            'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]


