import logging

import os
import urllib2
from datetime import datetime


logger = logging.getLogger(__name__)

TEAM = []

TEAMS = [
    'nwe', 'lar', 'buf', 'mia', 'nyj', 'bal',
    'cin', 'cle', 'pit', 'hou', 'ind', 'jac',
    'ten', 'phi', 'was', 'chi', 'det', 'gnb',
    'min',
]

POSITIONS = [
    'Running Back',
    'Wide Receiver 2',
    'Wide Receiver 1',
    'Right Offensive Guard',
    'Fullback',
    'Right Offensive Tackle',
    'Left Offensive Tackle',
    'Tight End',
    'Left Offensive Guard',
    'Quarterback',
    'Center',
]

CACHE_FOLDER = '.cache/'

def cache_file(method, id, include_time=False):
    cache_dir = '%s%s' % (CACHE_FOLDER, method)

    if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    if include_time:
        now_dir = str(datetime.now()).split()[0]
        cache_dir = '%s/%s' % (cache_dir, now_dir)

        if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)

    return '%s/%s' % ( cache_dir, id )


def fetch(url):
    cache_f = cache_file('fetch-url', url.replace('/', '-'), True)


    if os.path.exists(cache_f):
        logger.info('cache: {url}'.format(url=url))
        fp = open(cache_f, 'r')
        resp = fp.read()
    else:
        logger.info( 'fetching: {url}'.format(url=url))
        fp = open(cache_f, 'w')
        resp = urllib2.urlopen(url).read()
        fp.write(resp)

    fp.close()

    return resp
