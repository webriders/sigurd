# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Info'
        db.create_table('web_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('web', ['Info'])


    def backwards(self, orm):
        
        # Deleting model 'Info'
        db.delete_table('web_info')


    models = {
        'web.application': {
            'Meta': {'object_name': 'Application'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'web.applicationconfig': {
            'Meta': {'unique_together': "(('application', 'slug'),)", 'object_name': 'ApplicationConfig'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Application']"}),
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3096', 'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 7, 31, 17, 55, 28, 673886)'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'supported_versions': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'web.downloaditem': {
            'Meta': {'object_name': 'DownloadItem'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'web.info': {
            'Meta': {'object_name': 'Info'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['web']
