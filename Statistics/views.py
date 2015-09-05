from django.shortcuts import render
from django.db.models import Count
from django_tables2 import RequestConfig
from Statistics.tables import TopTenUsersTable
from Statistics.models import SquidLogs

def statistics(request):
    top_ten_users = TopTenUsersTable(SquidLogs.objects.values('domain').annotate(occurances=Count('domain')).order_by('-occurances'))
    RequestConfig(request, paginate={"per_page": 10}).configure(top_ten_users)
    return render(request, "statistics.html", {"top_ten_users": top_ten_users})
