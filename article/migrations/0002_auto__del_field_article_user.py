# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.user'
        db.delete_column(u'article_article', 'user_id')


    def backwards(self, orm):
        # Adding field 'Article.user'
        db.add_column(u'article_article', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=10, to=orm['auth.User'], unique=True),
                      keep_default=False)


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'del_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kvalitetskrav': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['article']