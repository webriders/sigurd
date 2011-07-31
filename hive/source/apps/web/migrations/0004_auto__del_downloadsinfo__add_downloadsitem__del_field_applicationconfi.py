# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'DownloadsInfo'
        db.delete_table('web_downloadsinfo')

        # Adding model 'DownloadsItem'
        db.create_table('web_downloadsitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2048)),
            ('archive', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('web', ['DownloadsItem'])

        # Deleting field 'ApplicationConfig.views'
        db.delete_column('web_applicationconfig', 'views')

        # Adding field 'ApplicationConfig.publish_date'
        db.add_column('web_applicationconfig', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 7, 31, 11, 57, 10, 892594)), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'DownloadsInfo'
        db.create_table('web_downloadsinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archive', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2048)),
        ))
        db.send_create_signal('web', ['DownloadsInfo'])

        # Deleting model 'DownloadsItem'
        db.delete_table('web_downloadsitem')

        # Adding field 'ApplicationConfig.views'
        db.add_column('web_applicationconfig', 'views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'ApplicationConfig.publish_date'
        db.delete_column('web_applicationconfig', 'publish_date')


    models = {
        'web.application': {
            'Meta': {'object_name': 'Application'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'web.applicationconfig': {
            'Meta': {'object_name': 'ApplicationConfig'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Application']"}),
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3096', 'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 7, 31, 11, 57, 10, 892594)'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'supported_versions': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'web.downloadsitem': {
            'Meta': {'object_name': 'DownloadsItem'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['web']
