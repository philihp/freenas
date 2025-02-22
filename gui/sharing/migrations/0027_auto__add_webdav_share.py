# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebDAV_Share'
        db.create_table(u'sharing_webdav_share', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webdav_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('webdav_comment', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('webdav_path', self.gf('freenasUI.freeadmin.models.fields.PathField')(max_length=255)),
            ('webdav_ro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('webdav_perm', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'sharing', ['WebDAV_Share'])


    def backwards(self, orm):
        # Deleting model 'WebDAV_Share'
        db.delete_table(u'sharing_webdav_share')


    models = {
        u'sharing.afp_share': {
            'Meta': {'ordering': "['afp_name']", 'object_name': 'AFP_Share'},
            'afp_allow': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'afp_comment': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'afp_deny': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'afp_dperm': ('django.db.models.fields.CharField', [], {'default': "'755'", 'max_length': '3'}),
            'afp_fperm': ('django.db.models.fields.CharField', [], {'default': "'644'", 'max_length': '3'}),
            'afp_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'afp_nodev': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'afp_nostat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'afp_path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'}),
            'afp_ro': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'afp_rw': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'afp_timemachine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'afp_umask': ('django.db.models.fields.CharField', [], {'default': "'000'", 'max_length': '3', 'blank': 'True'}),
            'afp_upriv': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sharing.cifs_share': {
            'Meta': {'ordering': "['cifs_name']", 'object_name': 'CIFS_Share'},
            'cifs_auxsmbconf': ('django.db.models.fields.TextField', [], {'max_length': '120', 'blank': 'True'}),
            'cifs_browsable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cifs_comment': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'cifs_default_permissions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cifs_guestok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cifs_guestonly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cifs_hostsallow': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cifs_hostsdeny': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cifs_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'cifs_path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'}),
            'cifs_recyclebin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cifs_ro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cifs_showhiddenfiles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sharing.nfs_share': {
            'Meta': {'object_name': 'NFS_Share'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nfs_alldirs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nfs_comment': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'nfs_hosts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nfs_mapall_group': ('freenasUI.freeadmin.models.fields.GroupField', [], {'default': "''", 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nfs_mapall_user': ('freenasUI.freeadmin.models.fields.UserField', [], {'default': "''", 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nfs_maproot_group': ('freenasUI.freeadmin.models.fields.GroupField', [], {'default': "''", 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nfs_maproot_user': ('freenasUI.freeadmin.models.fields.UserField', [], {'default': "''", 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nfs_network': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nfs_quiet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nfs_ro': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'sharing.nfs_share_path': {
            'Meta': {'ordering': "['path']", 'object_name': 'NFS_Share_Path'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paths'", 'to': u"orm['sharing.NFS_Share']"})
        },
        u'sharing.webdav_share': {
            'Meta': {'ordering': "['webdav_name']", 'object_name': 'WebDAV_Share'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'webdav_comment': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'webdav_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'webdav_path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'}),
            'webdav_perm': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'webdav_ro': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['sharing']