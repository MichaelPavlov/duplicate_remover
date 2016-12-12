import os
import subprocess
from shlex import split

from django.conf import settings


def save_file(f, name):
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return destination


def collect_unique_lines():
    return os.system('sort %s/* | uniq -u > %s/result.txt' % (settings.MEDIA_ROOT, settings.MEDIA_ROOT))
    print(result)
    # p1 = subprocess.run('pwd', cwd=settings.MEDIA_ROOT)
    # p1 = subprocess.run(split('sort file-*'), stdout=subprocess.PIPE, cwd=settings.MEDIA_ROOT)
    # p2 = subprocess.Popen(split('uniq -u > result.txt'), stdin=p1.stdout, cwd=settings.MEDIA_ROOT)
    pass
