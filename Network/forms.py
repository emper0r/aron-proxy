from django import forms
from django.contrib import messages
from Network.models import IP
import iptools
from netaddr import IPAddress, IPNetwork

class NetworkForm(forms.Field):
    ip_wan = IP.objects.all().values()[0]['ip_wan']
    netmask_wan = IP.objects.all().values()[0]['mask_wan']
    gateway = IP.objects.all().values()[0]['gateway']
    iptools.ipv4.validate_ip(ip_wan)
    iptools.ipv4.validate_netmask(netmask_wan)
    iptools.ipv4.validate_ip(gateway)
    if IPAddress(gateway) not in IPNetwork(ip_wan+'/'+netmask_wan):
        pass
