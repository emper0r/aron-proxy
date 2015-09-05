import django_tables2 as tables
from Statistics.models import SquidLogs

class TopTenUsersTable(tables.Table):
    domain = tables.Column()
    occurances = tables.Column()

    class Meta:
        model = SquidLogs
        attrs = {"class": "paleblue"}
        fields = ('domain', 'occurances')

class TopTenDomainTable(tables.Table):
    class Meta:
        model = SquidLogs
        attrs = {"class": "paleblue"}