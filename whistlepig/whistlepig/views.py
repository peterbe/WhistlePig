import commonware

from django.shortcuts import render

log = commonware.log.getLogger('whistlepig')


def home(request, template='whistlepig/home.html'):
    """Main landing page for whistlepig"""
    data = {}
    log.debug("The WhistlePig lives!!")
    return render(request, template, data)
