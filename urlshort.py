#! /usr/bin/env python
from pyshorteners import Shortener
import click

@click.command()
@click.option('--service',
              default='Isgd',
              help='Service to use, Isgd at the tim@e')
@click.argument('url')
def url_shorten(service, url):

    supported_services = ['Isgd']
    url = url if url.startswith('http') else ('http://%s' % url)

    if service not in supported_services:
        print 'Service "{}" is not supported, supported services are: {}'\
            .format(service, supported_services)
        return
    try:
        shortener = Shortener(service)
        print shortener.short(url)
    except ValueError:
        print 'Invalid url given'
    except Exception as e:
        print 'Unable to shorten the url'


if __name__ == '__main__':
    url_shorten()
