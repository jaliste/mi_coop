from django.db import models
#from address.models import AddressField
from ..accounts.models import CustomUser as User
from django.utils.translation import ugettext as _
from datetime import datetime
from model_utils.models import StatusModel, TimeFramedModel
from model_utils import Choices

GENDER_CHOICES = (
        ('M',_('Male')),
        ('F',_('Female')),
        ('O',_('Other')),
)

CIVIL_STATUS = (
    ('S', _('Single')),
    ('M', _('Married')),
    ('D', _('Divorced')),
    ('W', _('Widow(ed)')),
)




class Coop(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    # we need contact info for other users or persons, not only for 
    # members
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    phone_number = models.CharField(_("phone number"),max_length=255, blank=True)
    phone_is_valid = models.BooleanField(default=True)
    have_whatsapp = models.BooleanField(_("I use Whatsapp"), default=False)
    phone_is_whatsapp = models.BooleanField(_("My whatsapp number is the same as my phone number"),
            default=True)
    whatsapp_number = models.CharField(_("Whatsapp number"), max_length=255,blank=True)
    join_whatsapp_group = models.BooleanField(_("I want to join the Coop Whatsapp group"), default=False)

#   address = AddressField()

  

class CoopMember(StatusModel):

    STATUS = Choices(
    	('candidate', _('candidate')), # Lleno el formulario de inscripcion
    	('accepted', _('accepted')),   # fue aceptado como socio pero aun faltan
    	('active', _('active')),       # socio activo.
    	('inactive', ('inactive')),    # socio inactivo
    	('resigned', _('Resigned')),   # socio presento la renuncia.
    	('archived', _('archived')),   
    	('lapsed', _('lapsed')),
        ('not_member',_('not a member')), # ya no es socio.
    )

    # Every member has a number
    #coop = models.ForeignKey(Coop, on_delete = models.CASCADE)
    members_id = models.IntegerField(_('Members id'), unique = True, null = True, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # Basic personal information is saved in the User model
    # (First name, last name and email)

    # Personal information required for the 
    # Libro de Registro de Socios
    # by the Ley General de Cooperativas in Chile
    
    national_id = models.CharField(_("National id"), max_length=255)
    birthdate = models.DateField(_("birth date"),blank=True, null=True)
    nationality = models.CharField(_("nationality"), max_length=255)
    gender = models.CharField(_("gender"), max_length=1, choices = GENDER_CHOICES)
    civil_status = models.CharField(_("civil status"), max_length=1, choices = CIVIL_STATUS)
    occupation = models.CharField(_("occupation"), blank=True,null=True, max_length=255)
    
    # terms and conditions
    contact_by_email = models.BooleanField(_("I authorize the Coop to contact me by email"),default=True)
    reasons_to_apply = models.TextField(blank=True)
    referral = models.TextField(blank=True)

    application_date = models.DateField(_("Application date"),
                                        default = datetime.now)
    # Coop information
    affiliation_date = models.DateField(_("Affiliation Date"), blank=True, null=True)
    affiliation_notes = models.TextField(blank=True)
    disaffiliation_date = models.DateField(_("Disaffiliation Date"),
                                           blank=True, null=True)
    disaffiliation_notes = models.TextField(blank=True)
    reasons_for_disaffiliation = models.TextField(_("Reasons for Disaffiliation "),
                                                  blank=True)
    observations = models.TextField(blank=True)
    # Coop shared_capital
    #is_membership = fields.Boolean(string="Is Membership", compute='get_is_membership', readonly=True)

    def accept(self, date=datetime.now, notes=None):
        if self.status != CoopMember.STATUS.candidate:
            # TODO: Do error
            return
        self.status = CoopMember.STATUS.accepted
        self.affilation_date = date
        self.affiliation_notes =notes
        self.save()
        share_number = 2
        # Subscribe shares. 
        price = SharePrice.timeframed.get(date)
        shares = self.capitalshare_set.create(
            number_of_shares=share_number,
            subscription_date=date,
            amount_payed=price*share_number
        )


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + "(RUT:" + self.national_id +")"
    
    class Meta:
        verbose_name = _("membership")
        verbose_name_plural = _("memberships")

class SharePrice (TimeFramedModel):
    price = models.IntegerField(_("price"))

class CapitalShare (StatusModel):
    STATUS = (
        ('subscribed', _('subscribed')),
        ('refunded', _('refunded')),
        ('payed', _('payed')),
    )

    number_of_shares = models.PositiveSmallIntegerField(_("Number of shares"),
                        default = 1)
    subscription_date = models.DateField(_("Subscription date"), default = datetime.now)
    payment_date = models.DateField(_("Payment date"), blank=True)
    refund_date = models.DateField(_("Return date"), blank=True)
    owner = models.ForeignKey(CoopMember, on_delete = models.CASCADE)
    amount_payed = models.IntegerField(_("Amount payed"),default=0)
    observations = models.TextField(blank=True)
    
    def set_payed(self, amount_really_payed, when=datetime.now):
        if self.amount_really_payed!= self.amount_payed:
            #TODO error
            return
        self.payment_date=when
        self.status=CapitalShare.STATUS.payed
        self.saved()


