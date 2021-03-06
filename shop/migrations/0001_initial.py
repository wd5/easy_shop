# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('shop_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('shop', ['Product'])

        # Adding model 'ClientType'
        db.create_table('shop_clienttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('shop', ['ClientType'])

        # Adding model 'Client'
        db.create_table('shop_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('shop', ['Client'])

        # Adding M2M table for field client_type on 'Client'
        db.create_table('shop_client_client_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('client', models.ForeignKey(orm['shop.client'], null=False)),
            ('clienttype', models.ForeignKey(orm['shop.clienttype'], null=False))
        ))
        db.create_unique('shop_client_client_type', ['client_id', 'clienttype_id'])

        # Adding model 'ClientProduct'
        db.create_table('shop_clientproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Client'])),
            ('price_in', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('price_out', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal('shop', ['ClientProduct'])

        # Adding model 'Document'
        db.create_table('shop_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent', to=orm['shop.Client'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received', to=orm['shop.Client'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('shop', ['Document'])

        # Adding model 'DocumentProduct'
        db.create_table('shop_documentproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Document'])),
            ('price_in', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('price_out', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal('shop', ['DocumentProduct'])

        # Adding model 'Sheet'
        db.create_table('shop_sheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('shop', ['Sheet'])

        # Adding M2M table for field sales on 'Sheet'
        db.create_table('shop_sheet_sales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sheet', models.ForeignKey(orm['shop.sheet'], null=False)),
            ('document', models.ForeignKey(orm['shop.document'], null=False))
        ))
        db.create_unique('shop_sheet_sales', ['sheet_id', 'document_id'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('shop_product')

        # Deleting model 'ClientType'
        db.delete_table('shop_clienttype')

        # Deleting model 'Client'
        db.delete_table('shop_client')

        # Removing M2M table for field client_type on 'Client'
        db.delete_table('shop_client_client_type')

        # Deleting model 'ClientProduct'
        db.delete_table('shop_clientproduct')

        # Deleting model 'Document'
        db.delete_table('shop_document')

        # Deleting model 'DocumentProduct'
        db.delete_table('shop_documentproduct')

        # Deleting model 'Sheet'
        db.delete_table('shop_sheet')

        # Removing M2M table for field sales on 'Sheet'
        db.delete_table('shop_sheet_sales')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.client': {
            'Meta': {'object_name': 'Client'},
            'client_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['shop.ClientType']", 'symmetrical': 'False'}),
            'contacts': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.clientproduct': {
            'Meta': {'object_name': 'ClientProduct'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_in': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'price_out': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'})
        },
        'shop.clienttype': {
            'Meta': {'object_name': 'ClientType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.document': {
            'Meta': {'object_name': 'Document'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received'", 'to': "orm['shop.Client']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent'", 'to': "orm['shop.Client']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'shop.documentproduct': {
            'Meta': {'object_name': 'DocumentProduct'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_in': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'price_out': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.sheet': {
            'Meta': {'object_name': 'Sheet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['shop.Document']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['shop']