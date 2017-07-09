from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.db import transaction
from Proxy.models import MAC
import re
import subprocess
import MySQLdb
from datetime import datetime


class DashBoard(models.Model):
    wan_image = models.CharField(max_length=16)
    lan1_image = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "Traffico Rete"

    def wan(self):
        data = subprocess.Popen('egrep Daily ' + settings.STATICFILES_DIRS[0] +
                                '/dashboard/localhost_' + self.wan_image +
                                '.html -A 20 | egrep td | awk \'{print $1, $2}\' | cut -d\'>\' -f2',
                                shell=True, stdout=subprocess.PIPE)
        values = []
        for item in data.stdout:
            values.append(item)
        return '<img src="../../../static/dashboard/localhost_' + self.wan_image + '-day.png"/><br>' + 'IN: ' + values[2] + 'OUT:' + values[5][:-1]

    wan.allow_tags = True
    wan.description = 'Traffico WAN'

    def lan1(self):
        data = subprocess.Popen('egrep Daily ' + settings.STATICFILES_DIRS[0] +
                                '/dashboard/localhost_' + self.lan1_image +
                                '.html -A 20 | egrep td | awk \'{print $1, $2}\' | cut -d\'>\' -f2',
                                shell=True, stdout=subprocess.PIPE)
        values = []
        for item in data.stdout:
            values.append(item)
        return '<img src="../../../static/dashboard/localhost_' + \
               self.lan1_image + '-day.png"/><br>' \
               + 'IN: ' + values[2] \
               + 'OUT:' + values[5][:-1]

    lan1.allow_tags = True
    lan1.description = 'Traffico LAN'


class AronLogs(models.Model):
    time_since_epoch = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    time_response = models.IntegerField(blank=True, null=True)
    ip_client = models.CharField(max_length=15, blank=True, null=True)
    ip_server = models.CharField(max_length=30, blank=True, null=True)
    http_status_code = models.CharField(max_length=10, blank=True, null=True)
    http_reply_size = models.IntegerField(blank=True, null=True)
    http_method = models.CharField(max_length=15, blank=True, null=True)
    http_url = models.CharField(max_length=200, blank=True, null=True)
    http_username = models.CharField(max_length=30, blank=True, null=True)
    http_mime_type = models.CharField(max_length=50, blank=True, null=True)
    squid_hier_status = models.CharField(max_length=30, blank=True, null=True)
    squid_request_status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aron_logs'
        verbose_name_plural = 'Logs'

    def data_traccia(self):
        fix_data = self.time_since_epoch
        return mark_safe(str(fix_data)[:-9])

    data_traccia.allow_tags = True
    data_traccia.show_description = 'Data traccia'

    def capacita_in_kb(self):
        if self.http_reply_size < 1024 * 1024:
            weight_kb = self.http_reply_size / 1024
            return mark_safe(str(weight_kb) + ' KB')
        else:
            weight_kb = self.http_reply_size / 1024 / 1024
            return mark_safe(str(weight_kb) + ' MB')

    capacita_in_kb.allow_tags = True
    capacita_in_kb.show_description = 'Capacit\'a nel disco'


class Cache(models.Model):
    class Meta:
        managed = False
        db_table = 'DashBoard_top'
        verbose_name_plural = 'Stato della Cache'

    def cache(self):
        graphic = chart(id='cache', title='Stato della Cache', opt3d='false', tooltip='Percento (%)')
        return mark_safe(graphic)

    cache.allow_tags = True
    cache.description = 'Stato della Cache'

    def tempo(self):
        graphic = chart(id='tempo', title='Tempo risposta in millisecondi', opt3d='false', tooltip='Percento (%)')
        return mark_safe(graphic)

    tempo.allow_tags = True
    tempo.description = 'Percentuale di tempo in (ms)'

    def used(self):
        graphic = chart_cache(id='used', title='Spazio utilizzato nella Cache', tooltip='Percento (%)')
        return mark_safe(graphic)

    used.allow_tags = True
    used.description = 'Percentuale di tempo in (ms)'


class LFD(models.Model):
    class Meta:
        managed = False
        db_table = 'DashBoard_top'
        verbose_name_plural = 'Ultimi 15 giorni'

    def ultimi_15_giorni(self):
        graphic = lfd(id='lfd', title='Ultimi 15 gg', tooltip='Totale Richieste')
        return mark_safe(graphic)

    ultimi_15_giorni.allow_tags = True
    ultimi_15_giorni.description = 'Ultimi 15 giorni'


class Top(models.Model):
    top = models.CharField(max_length='1', default='', blank=True, null=True)

    class Meta:
        managed = False
        verbose_name_plural = 'Top IP/Dominio'

    def ip(self):
        graphic = chart(id='ip', title='Trafico per Origine', opt3d='true', tooltip='MegaBytes')
        return mark_safe(graphic)

    ip.allow_tags = True
    ip.description = 'Trafico per IP'

    def domain(self):
        graphic = chart(id='domain', title='Trafico per Destinazione', opt3d='true', tooltip='Richieste')
        return mark_safe(graphic)

    domain.allow_tags = True
    domain.description = 'Trafico per Dominio'


def chart(id='foo', title="Pie chart", opt3d="false", tooltip='hint'):
    with transaction.atomic():
        db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                             settings.DATABASES.values()[0]['USER'],
                             settings.DATABASES.values()[0]['PASSWORD'],
                             settings.DATABASES.values()[0]['NAME'])
        cursor = db.cursor()
        clean = 'DELETE FROM aron_logs WHERE ip_client IS NULL;'
        cursor.execute(clean)
        if id is 'tempo':
            sql_ctx = 'SELECT "0 a 0,5 sec" AS time_on_ms, COUNT(*) / (SELECT COUNT(*) FROM aron_logs) * 100 AS percentage ' \
                      'FROM aron_logs WHERE time_response >= 0 AND time_response < 500 UNION SELECT "0,5 a 1 sec", COUNT(*) / (SELECT COUNT(*) FROM aron_logs) * 100 AS percentage ' \
                      'FROM aron_logs WHERE time_response >= 500 AND time_response < 1000 UNION SELECT "1 a 2 sec", COUNT(*) / (SELECT COUNT(*) FROM aron_logs) * 100 AS percentage ' \
                      'FROM aron_logs WHERE time_response >= 1000 AND time_response < 2000 UNION  SELECT "piu\' di 2 sec", COUNT(*) / (SELECT COUNT(*) FROM aron_logs)*100 AS percentage ' \
                      'FROM aron_logs WHERE time_response >= 2000;'
        if id is 'cache':
            sql_ctx = 'SELECT squid_request_status, (COUNT(*)/(SELECT COUNT(*) FROM aron_logs) * 100) AS percentage FROM aron_logs WHERE time_since_epoch > CURDATE() - INTERVAL 1 DAY AND time_since_epoch < CURDATE() + INTERVAL 1 DAY GROUP BY squid_request_status ORDER BY 2 DESC;'
        if id is 'ip':
            sql_ctx = "SELECT ip_client, SUM(http_reply_size)/1024/1024 AS total_bytes FROM aron_logs WHERE time_since_epoch > CURDATE() - INTERVAL 1 DAY AND time_since_epoch < CURDATE() + INTERVAL 1 DAY GROUP BY 1 ORDER BY 2 DESC LIMIT 10;"
        if id is 'domain':
            sql_ctx = "select DISTINCT (SUBSTRING_INDEX((SUBSTRING_INDEX((SUBSTRING_INDEX(http_url, 'http://', -1)), '/', 1)), '.', -4)) as domain, count(SUBSTRING_INDEX((SUBSTRING_INDEX((SUBSTRING_INDEX(http_url, 'http://', -1)), '/', 1)), '.', -4)) AS request FROM aron_logs WHERE time_since_epoch > CURDATE() - INTERVAL 1 DAY AND time_since_epoch < CURDATE() + INTERVAL 1 DAY GROUP BY domain ORDER BY request desc limit 10;"
        cursor.execute(sql_ctx)
        r_db = cursor.fetchall()
        db.close()
    if len(r_db) is 0:
        graphic = '<script src=../../../static/admin/js/highcharts.js></script>' + \
                  '<script src=../../../static/admin/js/highcharts-3d.js></script>' + \
                  '<div id="graphic_' + str(id) + '" style="min-width: 825px; height: 310px; margin: 0 auto; position:absolute;"></div>' + \
                  '<br>' * 12
    else:
        graphic = '<script src=../../../static/admin/js/highcharts.js></script>' + \
                  '<script src=../../../static/admin/js/highcharts-3d.js></script>' + \
                  '<div id="graphic_' + str(id) + '" style="min-width: 825px; height: 310px; margin: 0 auto; position:absolute;"></div>' + \
                  '<script type="text/javascript">' + \
                  '  $(function () {' + \
                  '    $("#graphic_' + str(id) + '").highcharts({' + \
                  '      chart: {' + \
                  '        type: "pie",' \
                  '        options3d: { enabled: ' + str(opt3d) + ', alpha: 45 }' + \
                  '        },' + \
                  '      title: { text: "' + str(title) + '" },' \
                  '      plotOptions: {' \
                  '        pie: { innerSize: 100, depth: 45 }' \
                  '      },' \
                  '      series: [{' \
                  '        name: "' + str(tooltip) + '",' \
                  '        data: ['
        for i in range(0, len(r_db)):
            if str(r_db[i][0]) is None:
                pass
            else:
                mac = False
                if re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", r_db[i][0]):
                    arg = "arp -n | egrep %s | awk '{print $3}'" % str(r_db[i][0])
                    proc = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
                    for line in proc.stdout:
                        item = line.split()
                        if MAC.objects.filter(mac=item[0]).exists():
                            if i < len(r_db) - 1:
                                graphic += '          ["' + str(MAC.objects.filter(mac=item[0])[0].name) + '", ' + str(int(r_db[i][1])) + '], '
                                mac = True
                            else:
                                graphic += '          ["' + str(MAC.objects.filter(mac=item[0])[0].name) + '", ' + str(int(r_db[i][1])) + ']]}]});});</script>'
                                mac = True
                if mac is not True:
                    if i < len(r_db) - 1:
                        graphic += '          ["' + str(r_db[i][0]) + '", ' + str(int(r_db[i][1])) + '], '
                    else:
                        graphic += '          ["' + str(r_db[i][0]) + '", ' + str(int(r_db[i][1])) + ']]}]});});</script>'
        graphic += '<br>' * 12
    return graphic


class Aiuto(models.Model):
    class Meta:
        managed = False
        db_table = 'DashBoard_top'
        verbose_name_plural = 'Legenda'

    def cache_codes(self):
        return '<b>IMS</b>  - E\' una tecnica che viene utilizzata dalla webcache quando un oggetto perde la sua consistenza.<br>Se un oggetto non viene piu\' ritenuto consistente verra\' verificato con una richiesta di If-Modified-Since (IMS), tale richiesta serve per determinarne la reale consistenza dell\'oggetto e se lo stesso risultasse realmente modificato la cache si occupera\' di richiedere al server di origine una copia aggiornata</br>' \
               '<b>TCP_HIT</b> - E\' stata trovata una copia valida dell\'oggetto nella cache.</br>' \
               '<b>TCP_MISS</b> - L\'oggetto richiesto non e\' presente nella cache.</br>' \
               '<b>TCP_REFRESH_HIT</b> - L\'oggetto e\' presente nella cache ma si tratta di un\'oggetto vecchio (STALE). La query IMS relativa all\'oggetto e\' "304 not modified".</br>' \
               '<b>TCP_REF_FAIL_HIT</b> - L\'oggetto e\' presente nella cache ma si tratta di una copia vecchia. La query IMS fallisce se l\'oggetto viene trasportato</br>' \
               '<b>TCP_REFRESH_MISS</b> - L\'oggetto e\' presente nella cache ma si tratta di una copia vecchia. La query IMS ritorna un nuovo oggetto.</br>' \
               '<b>TCP_CLIENT_REFRESH_MISS</b> - Il client annuncia un messaggio "no-cache" pragma, la richiesta dell\'oggetto visualizza dei messaggi di controllo della cache, la cache deve aggiornare l\'oggetto.</br>' \
               '<b>TCP_IMS_HIT</b> - Il client annuncia una richiesta IMS per un oggetto che e\' presente nella cache e non e\' scaduto.</br>' \
               '<b>TCP_SWAPFAIL_MISS</b> - L\'oggetto era nella cache ma non e\' piu\' accessibile. </br>' \
               '<b>TCP_NEGATIVE_HIT</b> - Si tratta di una richiesta per un oggetto non presente nella cache, il messaggio e\' "404 not found", la cache pensa che questo oggetto sia inaccessibile.</br>' \
               '<b>TCP_MEM_HIT</b> - Una copia valida dell\'oggetto richiesto e\' sia nella cache che nella memoria, con questo messaggio indica che l\'accesso al disco e\' stato evitato. </br>' \
               '<b>TCP_DENIED</b> - L\'accesso viene bloccato per questo tipo di richiesta.</br>' \
               '<b>TCP_OFFLINE_HIT</b> - L\'oggetto richiesto e\' stato reperito direttamente dalla cache durante la modalita\' off-line. Questo tipo di modalita\' non valida nessun oggetto.</br>' \
               '<b>UDP_HIT</b> - Esiste una copia valida dell\'oggetto nella cache.</br>' \
               '<b>UDP_MISS</b> - L\'oggetto richiesto non e\' nella cache.</br>' \
               '<b>UDP_DENIED</b> - Per questo tipo di richiesta l\'accesso e\' stato negato.</br>' \
               '<b>UDP_INVALID</b> - E\' stata ricevuta una richiesta non valida.</br>' \
               '<b>UDP_MISS_NOFETCH</b> - Se l\'avviamento del Proxy viene richiamato con il comando -Y (se la vostra cache e\' di tipo child ed usa il protocollo ICP, questa opzione consente una rigenerazione veloce della cache), nel caso si dovessero verificare degli errori frequenti, la cache ritornera\' questo codice o dei codici UDP_HIT.</br>' \
               '<b>NONE</b> - Si verifica con gli errori sulle richieste effettuate dal cache manager.</br>'

    cache_codes.allow_tags = True
    cache_codes.description = 'Legenda'

    def http_status_code(self):
        return '<b>100 Continue:</b> Il server ha ricevuto l\'header della richiesta e il client deve procedere ad inviare il corpo della richiesta (solitamente nelle richieste di tipo POST).</br>' \
               '<b>101 Switching Protocols:</b> Il richiedente ha richiesto di cambiare il protocollo in uso e il server e\' a conoscenza di ci\'o che dovr\'a fare.</br>' \
               '<b>200 OK:</b> Risposta standard per le richieste HTTP andate a buon fine.</br>' \
               '<b>201 Created:</b> - </br>' \
               '<b>202 Accepted:</b> La richiesta di elaborazione \'e stata accettata ma non \'e ancora terminata.</br>' \
               '<b>203 Non-Authoritative Information:</b> - </br>' \
               '<b>204 No Content:</b> - </br>' \
               '<b>205 Reset Content:</b> - </br>' \
               '<b>206 Partial Content:</b> - </br>' \
               '<b>207 Multi-Status:</b> In caso di risposte XML, quando pi\'u azioni possono essere richieste, i dettagli dei singoli stati sono dati nel corpo della risposta. Vedi WebDAV (RFC 4918) per le specifiche associate. </br>' \
               '<b>300 Multiple Choices:</b> - </br>' \
               '<b>301 Moved Permanently:</b> Questa e tutte le future richieste andranno dirette ad un altro URI (specificato nell\'header Location). </br>' \
               '<b>302 Found:</b> Questo \'e il codice pi\'u usato ma anche un classico esempio di non aderenza agli standard nella pratica quotidiana. Infatti, le specifiche di HTTP/1.0 (RFC 1945) richiederebbero che il client esegua redirezioni temporanee (la descrizione originale era "Moved Temporarily"), ma i pi\'u diffusi browser l\'hanno implementata come 303 descritta di seguito. Perci\'o, HTTP/1.1 ha aggiunto i codici di stato 303 e 307 per distinguere tra i due comportamenti. Comunque, la maggior parte delle applicazioni e dei framework web ancora usano il codice di stato 302 come se fosse il 303. </br>' \
               '<b>303 See Other (da HTTP/1.1):</b> La risposta alla richiesta pu\'o essere trovata sotto un\'altra URI usando il metodo GET.' \
               '<b>304 Not Modified:</b> -</br>' \
               '<b>305 Use Proxy (da HTTP/1.1):</b> Molti client HTTP (come Mozilla ed Internet Explorer) non gestiscono correttamente le risposte con questo codice di stato.</br>' \
               '<b>306 Switch Proxy:</b> Non pi\'u usato.</br>' \
               '<b>307 Temporary Redirect (da HTTP/1.1):</b> In quest\'occasione, la richiesta dovrebbe essere ripetuta con un\'altra URI, ma successive richieste possono essere ancora dirette a quella originale. In contrasto con 303, la richiesta di POST originale deve essere reiterata con un\'altra richiesta di tipo POST.</br>' \
               '<b>308 Permanent Redirect (approvato come RFC sperimentale):</b> Questa richiesta e le future dovrebbero essere fatte verso un altro URI. Le risposte 307 e 308 (come proposta) dovrebbero comportarsi similmente alla 302 e la 301, ma non prevedono un cambiamento di metodo.</br>' \
               '<b>400 Bad Request:</b> La richiesta non puo\' essere soddisfatta a causa di errori di sintassi.</br>' \
               '<b>401 Unauthorized:</b> Simile a 403/Forbidden, ma pensato per essere usato quando l\'autenticazione \'e possibile ma \'e fallita o non pu\'o essere fornita. Vedi anche basic access authentication e digest access authentication.</br>' \
               '<b>402 Payment Required:</b> L\'intendimento originale prevedeva un suo utilizzo per realizzare meccanismi di digital cash/micropagamento, ma questo non si \'e mai verificato ed il codice non \'e mai stato utilizzato.</br>' \
               '<b>403 Forbidden:</b> La richiesta \'e legittima ma il server si rifiuta di soddisfarla. Contrariamente al codice 401 Unauthorized, l\'autenticazione non ha effetto.</br>' \
               '<b>404 Not Found:</b> La risorsa richiesta non \'e stata trovata ma in futuro potrebbe essere disponibile.</br>' \
               '<b>405 Method Not Allowed:</b> La richiesta \'e stata eseguita usando un metodo non permesso. Ad esempio questo accade quando si usa il metodo GET per inviare dati da presentare con un metodo POST.</br>' \
               '<b>406 Not Acceptable:</b> La risorsa richiesta \'e solo in grado di generare contenuti non accettabili secondo la header Accept inviato nella richiesta.</br>' \
               '<b>407 Proxy Authentication Required:</b> Errore richiesta d\'autenticazione.</br>' \
               '<b>408 Request Timeout:</b> Il tempo per inviare la richiesta \'e scaduto e il server ha terminato la connessione.</br>' \
               '<b>409 Conflict:</b> La richiesta non pu\'o essere portata a termine a causa di un conflitto con lo stato attuale della risorsa. Questo codice \'e permesso solo nei casi in cui ci si aspetta che l\'utente possa risolvere il conflitto e ripetere la richiesta. Il corpo della risposta dovrebbe contenere abbastanza informazioni per individuare la causa del conflitto.</br>' \
               '<b>410 Gone:</b> Indica che la risorsa richiesta non \'e pi\'u disponibile e non lo sar\'a pi\'u in futuro.</br>' \
               '<b>411 Length Required:</b> La richiesta non specifica la propria dimensione come richiesto dalla risorsa richiesta.</br>' \
               '<b>412 Precondition Failed:</b> -</br>' \
               '<b>413 Request Entity Too Large:</b> La richiesta \'e pi\'u grande di quanto il server possa gestire.</br>' \
               '<b>414 Request-URI Too Long:</b> L\'URI richiesto \'e troppo grande per essere processato dal server.</br>' \
               '<b>415 Unsupported Media Type:</b> L\'entita\'a della richiesta \'e di un tipo non accettato dal server o dalla risorsa richiesta.</br>' \
               '<b>416 Requested Range Not Satisfiable:</b> -</br>' \
               '<b>417 Expectation Failed:</b> -</br>' \
               '<b>418 I\'m a teapot:</b> Questo \'e un tipico pesce d\'aprile dell\'IETF (RFC 2324). Non si aspettano implementazioni in alcun server HTTP.</br>' \
               '<b>422 Unprocessable Entity:</b> Il server comprende il tipo di contenuto dell\'entit\'a richiesta e la sintassi della richiesta \'e corretta, ma non \'e in grado di processare le istruzioni contenute nella richiesta.</br>' \
               '<b>426 Upgrade Required:</b> Il client dovrebbe cambiare il protocollo ed usare ad esempio il TLS/1.0.</br>' \
               '<b>449 Retry With:</b> Estensione di Microsoft: The request should be retried after doing the appropriate action.</br>' \
               '<b>451 Unavailable For Legal Reasons (Approvato da Internet Engineering Steering Group IESG):</b> Stato non obbligatorio utilizzato quando l\'accesso alla risorsa \'e limitato per ragioni legali come censura o mandati governativi. Probabilmente fa riferimento al romanzo distopistico Fahrenheit 451.</br>' \
               '<b>500 Internal Server Error:</b> Messaggio di errore generico senza alcun dettaglio.</br>' \
               '<b>501 Not Implemented:</b> Il server non \'e in grado di soddisfare il metodo della richiesta.</br>' \
               '<b>502 Bad Gateway:</b> -</br>' \
               '<b>503 Service Unavailable:</b> Il server non \'e al momento disponibile. Generalmente \'e una condizione temporanea.</br>' \
               '<b>504 Gateway Timeout:</b> -</br>' \
               '<b>505 HTTP Version Not Supported:</b> Il server non supporta la versione HTTP della richiesta.</br>' \
               '<b>509 Bandwidth Limit Exceeded:</b> Questo codice di stato, bench\'e usato da molti server, non \'e un codice di stato ufficiale in quanto non \'e specificato in alcuna RFC.'

    http_status_code.allow_tags = True
    http_status_code.description = 'Legenda'


def lfd(id='foo', title="Pie chart", tooltip='hint'):
    with transaction.atomic():
        db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                             settings.DATABASES.values()[0]['USER'],
                             settings.DATABASES.values()[0]['PASSWORD'],
                             settings.DATABASES.values()[0]['NAME'])
        cursor = db.cursor()
        clean = 'DELETE FROM aron_logs WHERE ip_client IS NULL;'
        cursor.execute(clean)
        if id is 'lfd':
            sql_ctx = 'SELECT DATE(time_since_epoch) AS date_day, COUNT(*) AS num_of_requests FROM aron_logs GROUP BY date_day ORDER BY date_day DESC LIMIT 15;'
        cursor.execute(sql_ctx)
        r_db = cursor.fetchall()
        db.close()
    if len(r_db) is 0:
        graphic = '<script src=../../../static/admin/js/highcharts.js></script>' + \
                  '<script src=../../../static/admin/js/highcharts-3d.js></script>' + \
                  '<div id="graphic_' + str(id) + '" style="min-width: 825px; height: 310px; margin: 0 auto; position:absolute;"></div>' + \
                  '<br>' * 12
    else:
        graphic = '<script src=../../../static/admin/js/highcharts.js></script>' + \
                  '<script src=../../../static/admin/js/highcharts-3d.js></script>' + \
                  '<div id="graphic_' + str(id) + '" style="min-width: 886px; height: 310px; margin: 0 auto; position:absolute;"></div>' + \
                  '<script type="text/javascript">' + \
                  '  $(function () {' + \
                  '    $("#graphic_' + str(id) + '").highcharts({' + \
                  '      chart: {' + \
                  '        type: "spline"' \
                  '        },' + \
                  '      title: { text: "' + str(title) + '" },' \
                  '      xAxis: {' \
                  '        type: "category",' \
                  '        labels: {' \
                  '          rotation: 0,' \
                  '          overflow: \'justify\',' \
                  '          style: {' \
                  '            fontSize: "13px",' \
                  '            fontFamily: "Verdana, sans-serif"' \
                  '          }' \
                  '        }' \
                  '      },' \
                  '      yAxis: {' \
                  '        min: 0,' \
                  '        title: { text: "Richieste" }' \
                  '      },' \
                  '      legend: { enabled: true },' \
                  '      series: [{' \
                  '        name: "' + str(tooltip) + '",' \
                  '        data: ['
        for i in range(0, len(r_db)):
            if i is len(r_db) - 1:
                if str(r_db[i][0]) is None:
                    pass
                else:
                    graphic += '          ["' + str(datetime.strftime(datetime.strptime(str(r_db[i][0]), "%Y-%m-%d"), "%b %d")) + '", ' + str(int(r_db[i][1])) + ']],' \
                               '          dataLabels: {' \
                               '            enabled: true,' \
                               '            rotation: 0,' \
                               '            color: "#FFFFFF",' \
                               '            align: "center",' \
                               '            format: "{point.y}",' \
                               '            y: 10,' \
                               '            style: {' \
                               '              fontSize: "13px",' \
                               '              fontFamily: "Verdana, sans-serif"' \
                               '            }' \
                               '          }' \
                               '}]});});</script>'
                    graphic += '<br>' * 12
            else:
                if str(r_db[i][0]) is None:
                    pass
                else:
                    graphic += '          ["' + str(datetime.strftime(datetime.strptime(str(r_db[i][0]), "%Y-%m-%d"), "%b %d")) + '", ' + str(int(r_db[i][1])) + '], '
    return graphic


def chart_cache(id='foo', title="Pie chart", tooltip='hint'):
    values = []
    if id is 'used':
        data = subprocess.Popen('sudo squidclient mgr:storedir | egrep -i capacity | awk "{print \$4, \$6}"', shell=True, stdout=subprocess.PIPE)
        for item in data.stdout:
            values.append(item)
    graphic = '<script src=../../../static/admin/js/highcharts.js></script>' \
              '<script src=../../../static/admin/js/highcharts-3d.js></script>' \
              '<div id="graphic_' + str(id) + '" style="min-width: 825px; height: 310px; margin: 0 auto; position:absolute;"></div>' \
              '<script type="text/javascript">' \
              '  $(function () {' \
              '    $("#graphic_' + str(id) + '").highcharts({' \
              '      chart: {' \
              '        plotBackgroundColor: null,' \
              '        plotBorderWidth: 0,' \
              '        plotShadow: false' \
              '      },' \
              '      title: { text: "' + str(title) + '",' \
              '        align: "center",' \
              '        verticalAlign: "middle",' \
              '        y: 40' \
              '      },' \
              '      tooltip: {' \
              '        pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"' \
              '      },' \
              '      plotOptions: {' \
              '        pie: {' \
              '          dataLabels: {' \
              '          enabled: true,' \
              '          distance: -50,' \
              '            style: {' \
              '              fontWeight: "bold",' \
              '              color: "white",' \
              '              textShadow: "0px 1px 2px black" }' \
              '        },' \
              '      startAngle: -90,' \
              '      endAngle: 90,' \
              '      center: ["50%", "60%"]' \
              '      }},' \
              '      series: [{' \
              '        type: "pie",' \
              '        name: "' + str(tooltip) + '",' \
              '        innerSize: "50%",' \
              '        data: [' \
              '          [ "USATO",' + str(values[0].split(' ')[0][:2]) + '], ' \
              '          [ "LIBERO",' + str(values[0].split(' ')[1][:2]) + '], ' \
              '          { name: "Proprietary or Undetectable", ' \
              '             y: 0.2,' \
              '             dataLabels: {' \
              '             enabled: false }}]}]});});</script>'
    graphic += '<br>' * 12
    return graphic
