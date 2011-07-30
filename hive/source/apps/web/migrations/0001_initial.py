# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Application'
        db.create_table('web_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=256, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('web', ['Application'])

        # Adding model 'ApplicationConfig'
        db.create_table('web_applicationconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Application'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=3096, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=128, null=True, blank=True)),
            ('supported_versions', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('file_name', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('downloads', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_master', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('web', ['ApplicationConfig'])


    def backwards(self, orm):
        
        # Deleting model 'Application'
        db.delete_table('web_application')

        # Deleting model 'ApplicationConfig'
        db.delete_table('web_applicationconfig')


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
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3096', 'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'supported_versions': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['web']
