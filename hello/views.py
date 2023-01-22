import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.error("Test!!")
    return HttpResponse("Hello logging world.")
