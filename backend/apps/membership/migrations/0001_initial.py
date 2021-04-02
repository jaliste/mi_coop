# Generated by Django 3.0.5 on 2020-04-06 21:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SharePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoopMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('candidate', 'candidate'), ('accepted', 'accepted'), ('active', 'active'), ('inactive', 'inactive'), ('resigned', 'Resigned'), ('archived', 'archived'), ('lapsed', 'lapsed'), ('not_member', 'not a member')], default='candidate', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('members_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Members id')),
                ('national_id', models.CharField(max_length=255, verbose_name='National id')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('nationality', models.CharField(max_length=255, verbose_name='nationality')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='gender')),
                ('civil_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widow(ed)')], max_length=1, verbose_name='civil status')),
                ('occupation', models.CharField(blank=True, max_length=255, null=True, verbose_name='occupation')),
                ('contact_by_email', models.BooleanField(default=True, verbose_name='I authorize the Coop to contact me by email')),
                ('reasons_to_apply', models.TextField(blank=True)),
                ('referral', models.TextField(blank=True)),
                ('application_date', models.DateField(default=datetime.datetime.now, verbose_name='Application date')),
                ('affiliation_date', models.DateField(blank=True, null=True, verbose_name='Affiliation Date')),
                ('affiliation_notes', models.TextField(blank=True)),
                ('disaffiliation_date', models.DateField(blank=True, null=True, verbose_name='Disaffiliation Date')),
                ('disaffiliation_notes', models.TextField(blank=True)),
                ('reasons_for_disaffiliation', models.TextField(blank=True, verbose_name='Reasons for Disaffiliation ')),
                ('observations', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'membership',
                'verbose_name_plural': 'memberships',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone number')),
                ('phone_is_valid', models.BooleanField(default=True)),
                ('have_whatsapp', models.BooleanField(default=False, verbose_name='I use Whatsapp')),
                ('phone_is_whatsapp', models.BooleanField(default=True, verbose_name='My whatsapp number is the same as my phone number')),
                ('whatsapp_number', models.CharField(blank=True, max_length=255, verbose_name='Whatsapp number')),
                ('join_whatsapp_group', models.BooleanField(default=False, verbose_name='I want to join the Coop Whatsapp group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CapitalShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('subscribed', 'subscribed'), ('refunded', 'refunded'), ('payed', 'payed')], default='subscribed', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('number_of_shares', models.PositiveSmallIntegerField(default=1, verbose_name='Number of shares')),
                ('subscription_date', models.DateField(default=datetime.datetime.now, verbose_name='Subscription date')),
                ('payment_date', models.DateField(blank=True, verbose_name='Payment date')),
                ('refund_date', models.DateField(blank=True, verbose_name='Return date')),
                ('amount_payed', models.IntegerField(default=0, verbose_name='Amount payed')),
                ('observations', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.CoopMember')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
