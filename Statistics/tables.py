import django_tables2 as tables
from Statistics.models import SquidLogs

class TopTenIPTable(tables.Table):
    occurances = tables.Column()

    class Meta:
        model = SquidLogs
        attrs = {"class": "paleblue"}
        fields = ('client_ip', 'occurances')

class TopTenDomainTable(tables.Table):
    domain = tables.Column()
    occurances = tables.Column()

    class Meta:
        model = SquidLogs
        attrs = {"class": "paleblue"}
        fields = ('domain', 'occurances')