# encoding=utf-8

from pytz.gae import pytz

import settings
import util
import datetime

def uurlencode(value):
    return util.uurlencode(value)


def pageurl(value):
    return util.pageurl(value)


def labelurl(value):
    return util.get_label_url(value)


def hostname(value):
    host = value.split('/')[2]
    if host.startswith('www.'):
        host = host[4:]
    return host


def nonestr(value):
    if value is None:
        return ''
    return value


def markdown(text):
    return util.parse_markdown(text)


def wikify(text, page_title=None):
    return util.wikify_filter(text, page_name=page_title)


def wikify_page(page):
    return util.wikify_filter(page.body, page_name=page.title)


def cleanup_summary(text):
    return util.cleanup_summary(text)


def timezone(date, tz=None):
    if not tz:
        tz = settings.get("timezone", "UTC")
    if tz:
        return date.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone(tz))
    return date


def breadcrumbs(pagename):
    crumbs = pagename.split('/')[:-1]
    return util.wikify_filter(''.join(
        '[[%s|%s]] &raquo; ' % ('/'.join(crumbs[0:n+1]), crumb)
        for (n, crumb) in zip(xrange(len(crumbs)), crumbs)
        ))


def datev(dt, format='%Y/%m/%d %H:%M:%S'):
    # dt is provided as a datetime object
    try:
      return dt.strftime(format)
    except Exception, e:
      return dt


def load_filters(env):
  env.filters['uurlencode'] = uurlencode
  env.filters['pageurl'] = pageurl
  env.filters['labelurl'] = labelurl
  env.filters['hostname'] = hostname
  env.filters['nonestr'] = nonestr
  env.filters['markdown'] = markdown
  env.filters['wikify'] = wikify
  env.filters['wikify_page'] = wikify_page
  env.filters['cleanup_summary'] = cleanup_summary
  env.filters['timezone'] = timezone
  env.filters['breadcrumbs'] = breadcrumbs
  env.filters['date'] = datev
