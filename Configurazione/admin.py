from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
from singlemodeladmin import SingleModelAdmin
from django.contrib import messages
from django.db import transaction
from License import bf
from web import settings
import gzip
import os
import MySQLdb


@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': context.get('show_save_and_add_another', ctx['show_save_and_add_another']),
        'show_save_and_continue': context.get('show_save_and_continue', ctx['show_save_and_continue']),
        'show_save': context.get('show_save', ctx['show_save']),
        'show_save_as_new': context.get('show_save_as_new', ctx['show_save_as_new']),
        'show_delete_link': context.get('show_save_and_add_another', ctx['show_delete_link']),
        })
    return ctx


class ImportConfigAdmin(SingleModelAdmin):
    list_display = 'filename',

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ImportConfigAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ImportConfigAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if request.FILES['filename'].name == "config.aron.prx":
            try:
                save_file(request.FILES['filename'])
                load_f = gzip.open(str(settings.STATICFILES_DIRS[0]) + '/' + request.FILES['filename'].name, 'rb')
                ctx = bf.decrypt(load_f.read())
                with transaction.atomic():
                    db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                                         settings.DATABASES.values()[0]['USER'],
                                         settings.DATABASES.values()[0]['PASSWORD'],
                                         settings.DATABASES.values()[0]['NAME'])
                    cursor = db.cursor()
                    cursor.execute(ctx)
                    db.close()
                    load_f.close()
                    os.unlink(str(settings.STATICFILES_DIRS[0]) + '/' + str(request.FILES['filename']))
                    messages.set_level(request, messages.SUCCESS)
                    messages.info(request, 'File importato correttamente')
            except:
                messages.set_level(request, messages.ERROR)
                messages.error(request, 'Errore. Il file \'e dannegiato.')
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'Errore nell\'Import')


class ExportConfigAdmin(SingleModelAdmin):
    readonly_fields = ('config',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ExportConfigAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ExportConfigAdmin, self).add_view(request, form_url, extra_context=extra_context)


def save_file(file):
    filename = file._get_name()
    fd = open('%s/%s' % (str(settings.STATICFILES_DIRS[0]) + '/', filename), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
