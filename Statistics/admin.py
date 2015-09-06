from django.contrib import admin

class SquidLogsAdmin(admin.ModelAdmin):
    exclude = ('proxy_host', 'timestamp', 'date_day', 'date_time',
               'response_time', 'client_ip', 'squid_status', 'reply_size',
               'request_method', 'url', 'domain', 'username', 'squid_connect',
               'server_ip', 'mime_type', 'http_status')
