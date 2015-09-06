from __future__ import unicode_literals
from django.db import models


class SquidLogs(models.Model):
    proxy_host = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    date_day = models.DateField(blank=True, null=True)
    date_time = models.TimeField(blank=True, null=True)
    response_time = models.IntegerField(blank=True, null=True)
    client_ip = models.CharField(max_length=15, blank=True, null=True)
    squid_status = models.CharField(max_length=30, blank=True, null=True)
    http_status = models.CharField(max_length=10, blank=True, null=True)
    reply_size = models.IntegerField(blank=True, null=True)
    request_method = models.CharField(max_length=15, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    domain = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    squid_connect = models.CharField(max_length=20, blank=True, null=True)
    server_ip = models.CharField(max_length=15, blank=True, null=True)
    mime_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics_plog'
        verbose_name_plural = 'Proxy'