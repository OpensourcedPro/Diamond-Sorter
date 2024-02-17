import random
from random import randint as rint


def make_header() -> dict:
    headers = {}

    if bool(rint(0, 1)):
        headers.update({
            'Accept-Encoding': 'gzip, deflate, br'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Accept-Language': 'en-US;q=0.5,en;q=0.3'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Cache-Control': 'max-age=0'
        })

    if bool(rint(0, 1)):
        headers.update({
            'DNT': '1'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Upgrade-Insecure-Requests': '1'
        })

    headers.update({
        'Referer': 'https://%s' % random.choice(REFERERS)
    })

    if bool(rint(0, 1)):
        headers.update({
            'Pragma': 'no-cache'
        })

    return headers

REFERERS = (
    'www.google.com', 'youtube.com', 'apple.com', 'www.blogger.com',
    'microsoft.com', 'docs.google.com', 'play.google.com',
    'support.google.com', 'maps.google.com', 'plus.google.com',
    'adobe.com', 'cloudflare.com', 'linkedin.com', 'en.wikipedia.org',
    'wordpress.org', 'europa.eu', 'vimeo.com', 'youtu.be',
    'drive.google.com', 'sites.google.com', 'googleusercontent.com',
    'mozilla.org', 'accounts.google.com', 'facebook.com', 'vk.com',
    'github.com', 'istockphoto.com', 'bp.blogspot.com',
    'creativecommons.org', 'bbc.co.uk', 'medium.com', 'amazon.com',
    'line.me', 'es.wikipedia.org', 'w3.org', 'mail.google.com',
    'dropbox.com', 'live.com', 'policies.google.com', 'news.google.com',
    'feedburner.com', 'google.fr', 'nih.gov', 'jimdofree.com',
    'pt.wikipedia.org', 'fr.wikipedia.org', 't.me', 'uol.com.br',
    'myspace.com', 'google.co.jp', 'reuters.com', 'theguardian.com',
    'www.yahoo.com', 'google.co.uk', 'forbes.com', 'google.de',
    'wikimedia.org', 'buydomains.com', 'whatsapp.com', 'who.int',
    'bbc.com', 'nytimes.com', 'cnn.com', 'mail.ru', 'photos.google.com',
    'aliexpress.com', 'paypal.com', 'get.google.com', 'google.com.br',
    'developers.google.com', 'dailymotion.com', 'google.es',
    'gstatic.com', 'imdb.com', 'globo.com', 'slideshare.net',
    'hugedomains.com', 'msn.com', 'google.it', 'foxnews.com',
    'telegram.me', 'fandom.com', 'terra.com.br', 'cdc.gov',
    'code.google.com', 'amazon.co.uk', 'wikia.com', 'google.ru',
    'businessinsider.com', 'www.gov.uk', 'un.org', 'issuu.com',
    'ig.com.br', 'android.com', 'privacyshield.gov',
    'picasaweb.google.com', 'tinyurl.com', 'pinterest.com',
    'twitter.com', 'de.wikipedia.org', 'books.google.com',
    'id.wikipedia.org', 'lefigaro.fr', 'themeforest.net',
    'news.yahoo.com', 'usatoday.com', 'telegraph.co.uk',
    'independent.co.uk', 'aol.com', 'abril.com.br', 'scribd.com',
    'amazon.co.jp', 'draft.blogger.com', 'rt.com', 'bit.ly',
    'steampowered.com', 'hatena.ne.jp', 'ipv4.google.com',
    'huffingtonpost.com', 'rakuten.co.jp', 'fb.com',
    'myaccount.google.com', 'thesun.co.uk', 'abcnews.go.com',
    'tools.google.com', 'samsung.com', 'dan.com', 'amazon.de',
    'dailymail.co.uk', 'namecheap.com', 'archive.org', 'elpais.com',
    'ok.ru', 'plesk.com', 'nasa.gov', 'bloomberg.com', 'office.com',
    'booking.com', 'mediafire.com', 'translate.google.com', 'wsj.com',
    'mirror.co.uk', 'cpanel.net', 'ft.com',
    'marketingplatform.google.com', 'wired.com', 'aboutads.info',
    'washingtonpost.com', 'cnet.com', 'bing.com',
    'networkadvertising.org', 'cpanel.com', 'search.google.com',
    'gravatar.com', 'time.com', 'sedo.com', 'www.wix.com', 'webmd.com',
    'opera.com', 'files.wordpress.com', 'change.org',
    'youronlinechoices.com', 'goo.gl', 'ebay.com', 'harvard.edu',
    'berkeley.edu', 'ria.ru', 'guardian.co.uk', 'secureserver.net',
    'hp.com', 'www.weebly.com', 'scoop.it', 'ietf.org', 'nginx.org',
    'techcrunch.com', 'nhk.or.jp', 'gnu.org', 'amazon.es', 'oup.com',
    'stackoverflow.com', 'wp.com', 'depositfiles.com', 'addthis.com',
    'cbsnews.com', 'buzzfeed.com', 'm.wikipedia.org', 'bandcamp.com',
    'hm.com', 'e-recht24.de', 'enable-javascript.com', 'britannica.com',
    'walmart.com', 'ign.com', 'lemonde.fr', 'yahoo.co.jp', 'abc.net.au',
    'yelp.com', 'search.yahoo.com', 'amazon.fr', 'naver.jp',
    'imageshack.us', 'it.wikipedia.org', 'hollywoodreporter.com',
    'biglobe.ne.jp', 'trustpilot.com', 'cisco.com', 'akamaihd.net',
    'npr.org', 'kickstarter.com', 'tes.com', 'ibm.com', 'forms.gle',
    'columbia.edu', 'google.nl', 'whitehouse.gov', 'ja.wikipedia.org',
    'news.com.au', 'disqus.com', 'newsweek.com', 'ovh.net',
    'express.co.uk', 'economist.com', 'loc.gov', 'my.yahoo.com',
    'php.net', 'bt.com', 'netvibes.com', 'mystrikingly.com',
    'urbandictionary.com', 'latimes.com', 'digg.com', 'lg.com',
    'bloglovin.com', 'yale.edu', 'umich.edu', 'storage.googleapis.com',
    'netflix.com', 'instructables.com', 'smh.com.au', 'bitly.com',
    'pbs.org', 'imageshack.com', '000webhost.com', 'sciencemag.org',
    'nokia.com', 'groups.google.com', 'picasa.google.com', 'ovh.com',
    'soundcloud.com', 'unesco.org', 'usnews.com', 'mega.nz',
    'alibaba.com', 'detik.com', 'deezer.com', 'google.pl',
    'blackberry.com', 'nbcnews.com', 'ggpht.com', 'pixabay.com',
    'yandex.ru', 'dw.com', 'psychologytoday.com', 'playstation.com',
    'pl.wikipedia.org', '4shared.com', 'welt.de', 'pexels.com',
    'addtoany.com', 'disney.com', 'ted.com', 'list-manage.com',
    'google.com.tw', 'quora.com', 'eventbrite.com', 'wikihow.com',
    'stanford.edu', 'rambler.ru', 'gizmodo.com', 'vox.com', 'twitch.tv',
    'ox.ac.uk', 'gmail.com', 'over-blog-kiwi.com', 'researchgate.net',
    'nydailynews.com', 'instagram.com', 'thetimes.co.uk', 'weibo.com',
    'academia.edu', 'apache.org', 'nypost.com', 'mozilla.com',
    'engadget.com', 'channel4.com', 'princeton.edu', 'goo.ne.jp',
    'surveymonkey.com', 'noaa.gov', 'bp2.blogger.com', 'nvidia.com',
    'sciencedirect.com', 'nature.com', 'google.co.in',
    'www.wikipedia.org', 'cnbc.com', 'sfgate.com', 'godaddy.com',
    'shutterstock.com', 'wiley.com', 'wa.me', 'mit.edu',
    'indiatimes.com', 'sendspace.com', 'nginx.com', 'cbc.ca', 'abc.es',
    'ytimg.com', 'spotify.com', 'target.com', 'tripadvisor.com',
    'oracle.com', 'huffpost.com', 't.co', 'sapo.pt',
    'adssettings.google.com', 'xbox.com', 'washington.edu', 'dell.com',
    'nationalgeographic.com', 'icann.org', 'standard.co.uk',
    'gofundme.com', 'spiegel.de', 'ziddu.com', 'cornell.edu',
    'ovh.co.uk', 'mashable.com', 'amazon.it', 'fifa.com',
    'rapidshare.com', 'box.com', 'sciencedaily.com', 'sputniknews.com',
    'asus.com', 'theverge.com', 'about.com', 'theatlantic.com',
    'finance.yahoo.com', 'worldbank.org', 'metro.co.uk', 'elmundo.es',
    'goodreads.com', 'mysql.com', 'zendesk.com', 'ru.wikipedia.org',
    'www.over-blog.com', 'utexas.edu', 'variety.com', 'espn.com',
    'photobucket.com', 'yadi.sk', 'nikkei.com', 'doubleclick.net',
    'googleblog.com', 'naver.com', 'shopify.com', 'cambridge.org',
    'ea.com', 'google.co.id', 'google.ca', 'ikea.com',
    'www.livejournal.com', 'qq.com', 'epa.gov', 'm.me', 'so-net.ne.jp',
    'irs.gov', 'lycos.com', 'arstechnica.com', 'allaboutcookies.org',
    'corriere.it', 'springer.com', 'www.canalblog.com', 'axs.com',
    'sina.com.cn', 'nifty.com', 'zoom.us', 'ameblo.jp', 'oreilly.com',
    'rediff.com', 'stores.jp', 'megaupload.com', 'airbnb.com',
    'people.com', 'dreniq.com', 'prezi.com', 'consumerreports.org',
    'statista.com', 'kinja.com', 'pastebin.com', 'xinhuanet.com',
    'home.pl', 'politico.com', 'nps.gov', 'orange.fr', 'redhat.com',
    'photos1.blogger.com', '20minutos.es', 'calameo.com',
    'storage.canalblog.com', 'eff.org', 'e-monsite.com',
    'bp1.blogger.com', 'bp3.blogger.com', 'home.neustar',
    'lifehacker.com', 'theglobeandmail.com', 'techradar.com',
    'merriam-webster.com', 'digitaltrends.com', 'entrepreneur.com',
    'liveinternet.ru', 'calendar.google.com', 'zeit.de',
    'livescience.com', 'tmz.com', 'ucla.edu', 'fortune.com', 'slate.com',
    'discovery.com', 'thestar.com', 'discord.gg', 'usgs.gov',
    'blog.fc2.com', 'ieee.org', 'cocolog-nifty.com', 'video.google.com',
    'amazon.ca', 'foursquare.com', 'afternic.com', 'mixcloud.com',
    'histats.com', 'vchecks.me', 'thefreedictionary.com', 'thehill.com',
    'mayoclinic.org', 'nba.com', 'pcmag.com', 'a8.net', 'cmu.edu',
    'giphy.com', 'sedoparking.com', 'ssl-images-amazon.com',
    'boston.com', 'ibtimes.com', 'debian.org', 'weforum.org',
    'teamviewer.com', 'disney.go.com', 'archives.gov', 'house.gov',
    'state.gov', 'mail.yahoo.com', 'wattpad.com', 'vice.com',
    'pinterest.co.uk', 'google.com.au', 'alexa.com', 'behance.net',
    'newscientist.com', 'si.edu', 'dreamstime.com', 'cbslocal.com',
    'ndtv.com', 'example.com', 'jstor.org', 'upenn.edu', 'amzn.to',
    'greenpeace.org', 'ed.gov', 'ca.gov', 'csmonitor.com', 'iubenda.com',
    'gooyaabitemplates.com', 'ebay.co.uk', 'intel.com', 'apnews.com',
    'dribbble.com', 'bp0.blogger.com', 'chron.com', 'wiktionary.org',
    'plos.org', 'marriott.com', 'marketwatch.com', 'viagens.com.br',
    'com.com', 'newyorker.com', 'gamespot.com', 'khanacademy.org')
