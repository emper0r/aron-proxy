from django.shortcuts import render
from django.db.models import Count
from django_tables2 import RequestConfig
from Statistics.tables import TopTenIPTable
from Statistics.tables import TopTenDomainTable
from Statistics.models import SquidLogs

def statistics(request):
    top_10_ip = TopTenIPTable(SquidLogs.objects.values('client_ip').annotate(occurances=Count('client_ip')).order_by('-occurances'))
    top_10_domains = TopTenDomainTable(SquidLogs.objects.values('domain').annotate(occurances=Count('domain')).order_by('-occurances'))
    RequestConfig(request, paginate={"per_page": 10}).configure(top_10_ip)
    RequestConfig(request, paginate={"per_page": 10}).configure(top_10_domains)
    return render(request, "statistics.html",
                  {"top_10_ip": top_10_ip,
                   "top_10_domains": top_10_domains},
                  )
