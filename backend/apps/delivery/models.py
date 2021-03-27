from django.db import models
#/from address.models import AddressField
from .my_fields import DayOfTheWeekField
from ..membership.models import CoopMember
from django.utils.translation import ugettext_lazy as _
from .managers import BasketSubscriptionManager
from django.utils.translation import ugettext as __
from datetime import datetime, timedelta
from dateutil import rrule

#weekdays
MO,TU,WE,TH,FR,SA,SU = range(7)
WEEKDAYS = ((MO,__('Monday')),
            (TU,__('Tuesday')),
            (WE,__('Wednesday')),
            (TH,__('Thursday')),
            (FR,__('Friday')),
            (SA,__('Saturday')),
            (SU,__('Sunday')),
)

BASKET_STATUS = (('De',_('Delivered')),
                 ('Ch',_('Charged')),
                 ('Pl',_('Planned')),
                 ('Ca',_('Cancelled')),
)
# The lifecycle for a change request is the following: 
# The member ask for the change and the change is created with a 
# pending status. Then an approver (automatic or person) checks whether the 
# change is possible and either sets the status to approved or rejected. 
# If the basket the changes affects has already been programmed, then the basket change is made in the programme of the Delivery day. The next time a delivery day is programmed, all the approved request that are still valid are taken into account and the invalid ones are set into finalised. That way a change status can affect more than one basket, for instance for "non-active changes that usually occur on several continuous baskets". 

CHANGE_REQUEST_STATUS =(('Pe',_('Pending')),
                        ('Ap',_('Approved')),
                        ('Re',_('Rejected')),
                        ('Fi',_('Finalised')),
)

SUBSCRIPTION_STATUS = (('P',_('Pending')),
                       ('A',_('Active')),
                       ('I',_('Inactive')),
)
BASKET_PERIODICITY = (('We',_('Weekly')),
                      ('Ba',_('Biweekly (odd weeks)')),
                      ('Bb',_('Biweekly (even weeks)')),
)
# Each week is categorized as Odd week or Even Week 
# the Week 1 is the week of the 1st of August 2018.
FIRST_WEEK = datetime(2018,8,1)
WEEK_TYPE = (('A',_('Odd week')),
             ('B',_('Even week')),
)

class PickupPlace(models.Model):
    # This is the model to hold up information about pickup places
    title = models.CharField(_('title'),max_length=255)
    #address = AddressField(verbose_name=_('address'), on_delete= models.PROTECT)
    pickup_day = models.IntegerField(_('pickup day'),choices = WEEKDAYS)
    start_time = models.TimeField(_('start time'))
    duration = models.DurationField(_('duration'),
                                    default=timedelta(hours=3))
    def __str__(self):
        return self.title+" ("+dict(WEEKDAYS).get(self.pickup_day)+")"

    def add_occurrences(self, start_date = None, **rrule_params):
        '''
        Add one or more occurences to the event using a comparable API to
        ``dateutil.rrule``.
        If ``rrule_params`` does not contain a ``freq``, one will be defaulted
        to ``rrule.DAILY``.
        Because ``rrule.rrule`` returns an iterator that can essentially be
        unbounded, we need to slightly alter the expected behavior here in order
        to enforce a finite number of occurrence creation.
        If both ``count`` and ``until`` entries are missing from ``rrule_params``,
        only a single ``Occurrence`` instance will be created using the exact
        ``start_time`` and ``end_time`` values.
        '''
        if start_date is None:
            start_date = datetime.now
        start_time = datetime.combine (start_date,self.start_time)

        count = rrule_params.get('count')
        until = rrule_params.get('until')
        if not (count or until):
            self.occurrence_set.create(start_time=start_time, end_time=end_time)
        else:
            rrule_params.setdefault('freq', rrule.WEEKLY)
            occurrences = []
            for ev in rrule.rrule(dtstart=start_time, **rrule_params):
                occurrences.append(PickupDay(start_date=ev, end_time=ev + delta, event=self))
            self.occurrence_set.bulk_create(occurrences)
    class Meta:
        verbose_name = _('pickup place')
        verbose_name_plural = _('pickup places')

class PickupDay(models.Model):
    # Each time we deliver baskets, we create one pickup occurrence to 
    # group all the baskets that are to be picked up at a certain place
    # and date.
    # We repeat pickup_day, start_time and duration as the ones
    # in PickupPlace are intended for bulk-creation of 
    # Ocurrences, but these can change for one particular ocurrence, 
    # in particular, if the usual pickup day falls into a holiday and then 
    # the coop chooses to move the pickup day to the next working-day. 
    pickup_place = models.ForeignKey(
                PickupPlace,
                verbose_name=_('pickup place'),
                on_delete=models.CASCADE,
                null=True,
            )
    start_date = models.DateTimeField(_('start date'))
    duration = models.DurationField(_('duration'),default = timedelta(hours=3))
    status = models.CharField(max_length=100)
    week_type = models.CharField(max_length=1,choices = WEEK_TYPE, default='A') 
    def __str__(self):
        return self.start_date.strftime("%d-%m-%Y") + " ("+ self.pickup_place.title +")"

    class Meta:
        verbose_name = _('pickup occurrence')
        verbose_name_plural = _('pickup occurrences')
    def program_baskets(self):

        # This method programs all the baskets for this Pickup Ocurrence. 
        pass

class SubscriptionPeriodicity(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('periodicity')
        verbose_name_plural = _('periodicities')
        
class ProduceUnit(models.Model):
    #A Produce Unit
    name = models.CharField(max_length=255)
    unit_fee = models.DecimalField(_('Unit fee'), max_digits=8, decimal_places=2)
    def __str__(self):
        return self.name


class BasketSubscription(models.Model):
    # This models represent the basket subscription the user has. 
    # That is to which "fichas" or ProduceTypes  the member is 
    # subscribed. One time produce orders are saved in another model.
    # When a member wants to change permanently his/her "fichas", 
    # a new subscription must be created...
    # At anytime, only one active subscription per member 
    # is permitted. one subscription per member?
    # and the old subscription must ge given a valid_until date value. 
    #user wants to change its subscription, it must be accepted
    # by a manager, since we need to make sure 
    # the change can be fullfilled before the next delivery. 
    member = models.ForeignKey(CoopMember,
                               verbose_name=_("member"),
                               on_delete = models.CASCADE)
    pickup_place = models.ForeignKey(PickupPlace,
                                     verbose_name = _("pickup place"),
                                     on_delete = models.CASCADE)
    status = models.CharField(max_length=1,
                              choices = SUBSCRIPTION_STATUS,
                              default = 'P')
    valid_from = models.DateTimeField(_('Valid from'), default=datetime.now)
    valid_until = models.DateTimeField(_('Valid until'), blank=True, null=True)
    periodicity = models.ForeignKey(SubscriptionPeriodicity,
                                    verbose_name = _('periodicity'),
                                    on_delete = models.PROTECT)
    admin_fee = models.DecimalField(_('Admin fee'), max_digits=8, decimal_places=2)
    advance_fee = models.DecimalField(_('Advance fee'), max_digits=8, decimal_places=2)
    total_fee = models.DecimalField(_('Total fee'), max_digits=8, decimal_places=2, null=True)

    #contents = models.ManyToManyField(ProduceUnit,through='BasketSubscriptionItem')
    objects = BasketSubscriptionManager()    
    class Meta:
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")

class BasketSubscriptionItem(models.Model):
    subscription = models.ForeignKey(BasketSubscription, related_name="chips", on_delete = models.CASCADE)
    produce = models.ForeignKey(ProduceUnit,
                                verbose_name = _("produce"),
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"))
    fee = models.DecimalField(_('fee'), max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.produce)
    class Meta:
        verbose_name = _("basket subscription item")
        verbose_name_plural = _("basket subscription items")

class Basket(models.Model):
    # a Basket  belongs to a PickupDay object
    # since it can only be picked up at a Pickup Day. 
    # so if we want to move the day where a basket will be picked up, 
    # we need to change its parent pickup Ocurrence object. 
    pickup_day = models.ForeignKey(
                    PickupDay,
                    verbose_name = _('Pickup day'),
                    on_delete = models.CASCADE
                )
    member = models.ForeignKey(CoopMember,
                on_delete = models.PROTECT
            )
    status = models.CharField(max_length = 2, choices = BASKET_STATUS, default ='Pl')
    
    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

class BasketContents(models.Model):
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE)
    produce = models.ForeignKey(ProduceUnit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_fee = models.DecimalField(max_digits=8, decimal_places=2)

class BasketChangeRequest(models.Model):
    member = models.ForeignKey(CoopMember,
                 on_delete = models.PROTECT
                 )
    
    status = models.CharField(max_length = 2, choices = CHANGE_REQUEST_STATUS, default = 'Pe')
    


