from django.db.models import Q
from django.db import models
from datetime import datetime

class BasketSubscriptionManager(models.Manager):
    def active(self, member, at_datetime=None):
        if at_datetime is None:
            at_datetime = datetime.now
        qs = self.filter(Q(member=member)&Q(status='A')&Q(valid_from__lte=at_datetime) &
                (Q(valid_until__is_null=True)| Q(valid_until__gt=at_datetime))
             )

        return qs
