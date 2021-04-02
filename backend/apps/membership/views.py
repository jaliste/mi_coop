from django.shortcuts import render
from django.views import generic
from viewflow.flow.views import StartFlowMixin, FlowViewMixin
from .forms import MemberForm, ContactInfoForm, UserUpdateForm, AcceptConditionsForm
from formtools.wizard.views import SessionWizardView
from django.forms import Form
from rest_framework import viewsets
#from .serializers import CoopMemberSerializer
from .models import CoopMember

CONTACT_WIZARD_TEMPLATES = {"user": "membership/user_data.html",
                            "usercoop": "membership/user_coop_data.html",
                            "contact" : "membership/contact_data.html",
                            "conditions": "membership/accept_conditions.html",
                            "preview": "membership/preview.html",
                            }


class SubmitApplicationView(StartFlowMixin, generic.UpdateView):
    form_class = MemberForm

    def get_object(self):
        return self.activation.process.member

    def activation_done(self, form):
        member = form.save()
        self.activation.process.member = member
        super(StartView, self).activation_done(form)

class CandidateMemberViewSet(viewsets.ModelViewSet):
    queryset = CoopMember.objects.filter(status="candidate").order_by("-application_date")
    serializer_class = CoopMemberSerializer
    
class CoopMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CoopMember.objects.exclude(status="candidate").order_by("-application_date")
    
    serializer_class = CoopMemberSerializer

