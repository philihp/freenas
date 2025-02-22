#+
# Copyright 2010 iXsystems, Inc.
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#####################################################################
import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _

from freenasUI.directoryservice.forms import idmap_tdb_Form
from freenasUI.directoryservice.models import (
    idmap_tdb,
    DS_TYPE_CIFS
)
from freenasUI.directoryservice.views import get_directoryservice_status
from freenasUI.freeadmin.apppool import appPool
from freenasUI.freeadmin.views import JsonResp
from freenasUI.services import models
from freenasUI.services.forms import (
    servicesForm,
    CIFSForm
)

log = logging.getLogger("services.views")


def index(request):

    view = appPool.hook_app_index('sharing', request)
    view = filter(None, view)
    if view:
        return view[0]

    return render(request, 'services/index.html', {
        'toggleCore': request.GET.get('toggleCore'),
    })


def core(request):

    try:
        domaincontroller = models.DomainController.objects.order_by("-id")[0]
    except IndexError:
        domaincontroller = models.DomainController.objects.create()

    domaincontroller.onclick_enable = 'enable'
    ds_status = get_directoryservice_status()
    for key in ds_status:
        if ds_status[key] == True and key != 'dc_enable':
            domaincontroller.onclick_enable = 'disable'
            break

    try:
        afp = models.AFP.objects.order_by("-id")[0]
    except IndexError:
        afp = models.AFP.objects.create()

    try:
        cifs = models.CIFS.objects.order_by("-id")[0]
    except IndexError:
        cifs = models.CIFS.objects.create()

    try:
        dynamicdns = models.DynamicDNS.objects.order_by("-id")[0]
    except IndexError:
        dynamicdns = models.DynamicDNS.objects.create()

    try:
        lldp = models.LLDP.objects.order_by("-id")[0]
    except IndexError:
        lldp = models.LLDP.objects.create()

    try:
        nfs = models.NFS.objects.order_by("-id")[0]
    except IndexError:
        nfs = models.NFS.objects.create()

    try:
        ftp = models.FTP.objects.order_by("-id")[0]
    except IndexError:
        ftp = models.FTP.objects.create()

    try:
        tftp = models.TFTP.objects.order_by("-id")[0]
    except IndexError:
        tftp = models.TFTP.objects.create()

    try:
        rsyncd = models.Rsyncd.objects.order_by("-id")[0]
    except IndexError:
        rsyncd = models.Rsyncd.objects.create()

    try:
        smart = models.SMART.objects.order_by("-id")[0]
    except IndexError:
        smart = models.SMART.objects.create()

    try:
        snmp = models.SNMP.objects.order_by("-id")[0]
    except IndexError:
        snmp = models.SNMP.objects.create()

    try:
        ssh = models.SSH.objects.order_by("-id")[0]
    except IndexError:
        ssh = models.SSH.objects.create()

    try:
        ups = models.UPS.objects.order_by("-id")[0]
    except IndexError:
        ups = models.UPS.objects.create()

    try:
        webdav = models.WebDAV.objects.order_by("-id")[0]
    except IndexError:
	webdav = models.WebDAV.objects.create()

    srv = models.services.objects.all()
    return render(request, 'services/core.html', {
        'srv': srv,
        'cifs': cifs,
        'afp': afp,
        'lldp': lldp,
        'nfs': nfs,
        'rsyncd': rsyncd,
        'dynamicdns': dynamicdns,
        'snmp': snmp,
        'ups': ups,
        'ftp': ftp,
        'tftp': tftp,
        'smart': smart,
        'ssh': ssh,
        'domaincontroller': domaincontroller,
        'webdav': webdav
    })


def iscsi(request):
    gconfid = models.iSCSITargetGlobalConfiguration.objects.all().order_by(
        "-id")[0].id
    return render(request, 'services/iscsi.html', {
        'focus_tab': request.GET.get('tab', ''),
        'gconfid': gconfid,
    })


def servicesToggleView(request, formname):
    form2namemap = {
        'cifs_toggle': 'cifs',
        'afp_toggle': 'afp',
        'lldp_toggle': 'lldp',
        'nfs_toggle': 'nfs',
        'iscsitarget_toggle': 'iscsitarget',
        'dynamicdns_toggle': 'dynamicdns',
        'snmp_toggle': 'snmp',
        'httpd_toggle': 'httpd',
        'ftp_toggle': 'ftp',
        'tftp_toggle': 'tftp',
        'ssh_toggle': 'ssh',
        'ldap_toggle': 'ldap',
        'rsync_toggle': 'rsync',
        'smartd_toggle': 'smartd',
        'ups_toggle': 'ups',
        'plugins_toggle': 'plugins',
        'domaincontroller_toggle': 'domaincontroller',
        'webdav_toggle': 'webdav'
    }
    changing_service = form2namemap[formname]
    if changing_service == "":
        raise "Unknown service - Invalid request?"

    svc_entry = models.services.objects.get(srv_service=changing_service)
    if svc_entry.srv_enable:
        svc_entry.srv_enable = False
    else:
        svc_entry.srv_enable = True
    original_srv = svc_entry.srv_enable
    mf = servicesForm(instance=svc_entry, data={
        'srv_enable': svc_entry.srv_enable,
        'srv_service': changing_service,
    })
    if not mf.is_valid():
        return
    svc_entry = mf.save()
    events = []
    mf.done(request, events)

    error = False
    message = False
    if mf.started is True:
        status = 'on'
        if not original_srv:
            error = True
            message = _("The service could not be stopped.")

    elif mf.started is False:
        status = 'off'
        if original_srv:
            error = True
            message = _("The service could not be started.")
    else:
        if svc_entry.srv_enable:
            status = 'on'
        else:
            status = 'off'

    data = {
        'service': changing_service,
        'status': status,
        'error': error,
        'message': message,
        'enabled_svcs': mf.enabled_svcs,
        'disabled_svcs': mf.disabled_svcs,
        'events': events,
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def enable(request, svc):
    return render(request, "services/enable.html", {
        'svc': svc,
    })

def services_cifs(request):
    try:
        cifs = models.CIFS.objects.all()[0]
    except:
        cifs = models.CIFS()

    try:
        it = idmap_tdb.objects.get(
            idmap_ds_type=DS_TYPE_CIFS,
            idmap_ds_id=cifs.id
        )

    except Exception as e:
        it = idmap_tdb()

    if request.method == "POST":
        form = CIFSForm(request.POST, instance=cifs)
        if form.is_valid():
            form.save()
        else:
            return JsonResp(request, form=form)

        idmap_form = idmap_tdb_Form(request.POST, instance=it)
        if idmap_form.is_valid():
            idmap_form.save()
            return JsonResp(
                request,
                message=_("CIFS successfully updated.")
            )
        else:
            return JsonResp(request, form=idmap_form)

    else:
        form = CIFSForm(instance=cifs)
        idmap_form = idmap_tdb_Form(instance=it)

    idmap_form.fields['idmap_tdb_range_low'].label = "Idmap Range Low"
    idmap_form.fields['idmap_tdb_range_high'].label = "Idmap Range High"

    return render(request, 'services/cifs.html', {
        'form': form,
        'idmap_form': idmap_form
    })
