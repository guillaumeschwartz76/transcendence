from tables_core.models import CustomUser, Player, Match
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware

class UpdateLastAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)

        try:
            u = CustomUser.objects.get(user__pk=request.user.pk)
            aware_datetime = make_aware(datetime.now())
            u.last_access = datetime.now(tz=aware_datetime.tzinfo)
            u.save()
            print ("last_access: ", u.last_access)
        except:
            pass

        return response