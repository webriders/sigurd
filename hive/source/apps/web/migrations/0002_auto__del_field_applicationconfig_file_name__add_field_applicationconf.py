# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'ApplicationConfig.file_name'
        db.delete_column('web_applicationconfig', 'file_name')

        # Adding field 'ApplicationConfig.archive'
        db.add_column('web_applicationconfig', 'archive', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'ApplicationConfig.file_name'
        raise RuntimeError("Cannot reverse this migration. 'ApplicationConfig.file_name' and its values cannot be restored.")

        # Deleting field 'ApplicationConfig.archive'
        db.delete_column('web_applicationconfig', 'archive')


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
            'archive': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3096', 'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
