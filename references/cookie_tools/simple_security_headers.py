#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import re
import requests
import argparse
import collections
from urllib.parse import urlparse
from validator_collection import checkers
from bs4 import BeautifulSoup
from huepy import bold, info, run, que, bad, good, red


requests.packages.urllib3.disable_warnings()


def valid_url(url: str) -> bool:
    """Check that the URL is well formatted."""
    parsed_url = urlparse(url)
    if not (checkers.is_url(parsed_url.geturl()) or checkers.is_ip_address(parsed_url.geturl())):
        # prepend http if missing
        parsed_url = parsed_url._replace(**{"scheme": "http"})
        parsed_url = parsed_url._replace(**{"netloc": parsed_url[2]})  # move path to netloc
        parsed_url = parsed_url._replace(**{"path": ""})
        # check again with fixed url
        if not (checkers.is_url(parsed_url.geturl()) or checkers.is_ip_address(parsed_url.geturl())):
            return False
    return True


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', metavar='URL', required=True, help='URL https://example.com')
    parser.add_argument('--verify', action='store_true', default=False, help='Verify the SSL certificate. Default is set to False.')
    parser.add_argument('--description', action='store_true', help='Print header description')

    args = parser.parse_args()
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Cache-control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'close'
    })

    # prepend http if missing
    args.url = 'http://' + args.url if not args.url.startswith('http') else args.url
    if not valid_url(args.url):
        parser.print_help()
        exit()

    try:
        response = session.get(url=args.url, verify=args.verify)
    except requests.exceptions.ConnectionError as e:
        print(bold(bad(f"{bold(red('connection error'))}: {e}")))
        print(bold(bad(f'{args.url}')))
        exit()
    except Exception:
        print(bold(bad(bold(red('connection error')))))
        print(bold(bad(f'{args.url}')))
        exit()

    headers = response.headers
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    wappalyzer_json_url = "https://raw.githubusercontent.com/AliasIO/wappalyzer/master/src/technologies.json"

    check_headers = [
        'X-Content-Type-Options',
        'X-Frame-Options',
        'X-XSS-Protection',
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'Referrer-Policy',
        'Feature-Policy'
    ]

    descriptions = {}
    descriptions['X-Content-Type-Options'] = que('X-Content-Type-Options stops a browser from trying to MIME-sniff the content type and forces it to stick with the declared content-type. The only valid value for this header is "X-Content-Type-Options: nosniff".')
    descriptions['X-Frame-Options'] = que('X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking.')
    descriptions['X-XSS-Protection'] = que('X-XSS-Protection sets the configuration for the XSS Auditor built into older browser. The recommended value was "X-XSS-Protection: 1; mode=block" but you should now look at Content Security Policy instead.')
    descriptions['Strict-Transport-Security'] = que('HTTP Strict Transport Security is an excellent feature to support on your site and strengthens your implementation of TLS by getting the User Agent to enforce the use of HTTPS.')
    descriptions['Content-Security-Policy'] = que('Content Security Policy is an effective measure to protect your site from XSS attacks. By whitelisting sources of approved content, you can prevent the browser from loading malicious assets. Analyse this policy in more detail. You can sign up for a free account on Report URI to collect reports about problems on your site.')
    descriptions['Referrer-Policy'] = que('Referrer-Policy Referrer Policy is a new header that allows a site to control how much information the browser includes with navigations away from a document and should be set by all sites.')
    descriptions['Feature-Policy'] = que('Feature Policy is a new header that allows a site to control which features and APIs can be used in the browser.')

    cookie_checks = [
        'Expires',
        'HttpOnly',
        'Secure',
        'Path=/',
    ]

    print(info(f"{bold('Request URL')}: {args.url}"))
    print(info(f"{bold('Response status code')}: {response.status_code}"))

    print(info(bold('Request headers:')))
    print(json.dumps(dict(session.headers), indent=2, sort_keys=True))

    print(info(bold('Response headers:')))
    print(json.dumps(dict(headers), indent=2, sort_keys=True))

    print(f"\n{run(bold('Checking security headers...'))}")
    for check_head in check_headers:
        if check_head.lower() in headers:
            print(good(f'{check_head} found'))
        else:
            print(bad(f'{check_head} not found'))
            if args.description:
                if check_head in descriptions.keys():
                    print(descriptions[check_head])

    print(f"\n{run(bold('Checking cookies...'))}")
    if 'set-cookie' in headers:
        cookies = headers['Set-Cookie'].split(',')
        for cookie in cookies:
            print(f"{bold('cookie: ')} {cookie}")
            for cookie_check in cookie_checks:
                if cookie_check.lower() in cookie.lower():
                    print(good(f'{cookie_check} found'))
                else:
                    print(bad(f'{cookie_check} not found'))
    else:
        print(info('not found'))

    print(f"\n{run(bold('Checking Wappalyzer Regular Expressions...'))}")

    # Prepare wappalyzer data
    wappalyzer_json_file = requests.get(wappalyzer_json_url)
    if wappalyzer_json_file.ok:
        try:
            wappalyzer_json = json.loads(wappalyzer_json_file.text)
        except json.decoder.JSONDecodeError as e:
            print(bold(bad(f"{bold(red('JSONDecodeError'))}: {e}")))
            exit()
    else:
        print(bold(bad(f"{bold(red(f'Unable to get wappalyzer json file {wappalyzer_json_url}'))}")))
        exit()

    wappalyzer_categories = wappalyzer_json['categories']
    saved_apps = {}
    for k, v in wappalyzer_categories.items():
        name = wappalyzer_categories[k]['name']
        saved_apps[name] = set()

    wappalyzer_tech = wappalyzer_json['technologies']
    wappalyzer_names = {}
    for app_name, details in wappalyzer_tech.items():
        wappalyzer_names[app_name] = set()
        if 'cats' in details.keys():
            for ca in details['cats']:
                wappalyzer_names[app_name].add(ca)

    # Parse meta data
    metas = []
    for meta in soup.findAll('meta'):
        meta_object = list(meta.attrs.keys()) + list(meta.attrs.values())
        metas.append(meta_object)

    for app_name, details in wappalyzer_tech.items():
        found = False
        try:
            # Check meta
            if 'meta' in details.keys():
                for k, v in details['meta'].items():
                    for meta in metas:
                        if k in meta and re.search(v, ' '.join(meta)):
                            for cat in details['cats']:
                                name = wappalyzer_categories[str(cat)]['name']
                                saved_apps[name].add(app_name)
                                found = True
            # Check headers
            if 'headers' in details.keys():
                for k, header in details['headers'].items():
                    if k in headers and re.search(headers[k], header):
                        for cat in details['cats']:
                            name = wappalyzer_categories[str(cat)]['name']
                            saved_apps[name].add(app_name)
                            found = True
            # Check html and script
            search_in_html = []
            if 'html' in details.keys():
                if isinstance(details['html'], list):
                    search_in_html += details['html']
                if isinstance(details['html'], str):
                    search_in_html.append(details['html'])
            if 'script' in details.keys():
                if isinstance(details['script'], list):
                    search_in_html += details['script']
                if isinstance(details['script'], str):
                    search_in_html.append(details['script'])
            for regex in search_in_html:
                if re.search(regex, html):
                    for cat in details['cats']:
                        name = wappalyzer_categories[str(cat)]['name']
                        saved_apps[name].add(app_name)
                        found = True
            if found and 'implies' in details.keys():
                if isinstance(details['implies'], list):
                    techs = details['implies']
                elif isinstance(details['implies'], str):
                    techs = [details['implies']]
                else:
                    techs = []
                for tech in techs:
                    subcats = wappalyzer_names[tech]
                    for subcat in subcats:
                        subcat_category = wappalyzer_categories[str(subcat)]['name']
                        saved_apps[subcat_category].add(tech)
        except re.error:
            # print(warn(f'regex error: {regex}'))
            pass

    wappalyzer_found = False
    for category, app_names in saved_apps.items():
        if app_names:
            wappalyzer_found = True
            output = info(f"{category}: {', '.join(map(str, app_names))}")
            print(output)
    if not wappalyzer_found:
        print(info('not found'))


if __name__ == '__main__':
    main()