# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'data_users_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'data_users', ['Country'])

        # Adding model 'City'
        db.create_table(u'data_users_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'data_users', ['City'])

        # Adding model 'MedicalEspecialty'
        db.create_table(u'data_users_medicalespecialty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'data_users', ['MedicalEspecialty'])

        # Adding model 'ProfileUser'
        db.create_table(u'data_users_profileuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('medical_specialty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_users.MedicalEspecialty'], null=True, blank=True)),
            ('medical_emphasis', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('professional_abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('patient_abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('date_birth', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_users.Country'], null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_users.City'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='registration/img/profile/avatar-default-user.png', max_length=100, null=True, blank=True)),
            ('whatsapp', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('professional_register', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('medical_consultation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_blood', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_date_birth', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_patient_abstract', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_nationality', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_message', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('you_tube', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('google_plus', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('instagram', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'data_users', ['ProfileUser'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'data_users_country')

        # Deleting model 'City'
        db.delete_table(u'data_users_city')

        # Deleting model 'MedicalEspecialty'
        db.delete_table(u'data_users_medicalespecialty')

        # Deleting model 'ProfileUser'
        db.delete_table(u'data_users_profileuser')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'relationships': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_to'", 'symmetrical': 'False', 'through': u"orm['relationships.Relationship']", 'to': u"orm['auth.User']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'data_users.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'data_users.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'data_users.medicalespecialty': {
            'Meta': {'object_name': 'MedicalEspecialty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'data_users.profileuser': {
            'Meta': {'object_name': 'ProfileUser'},
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_users.City']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_users.Country']", 'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'flag_blood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_date_birth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_message': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_nationality': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_patient_abstract': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'google_plus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'registration/img/profile/avatar-default-user.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'medical_consultation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medical_emphasis': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medical_specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_users.MedicalEspecialty']", 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'patient_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'professional_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'professional_register': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'whatsapp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'you_tube': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'relationships.relationship': {
            'Meta': {'ordering': "('created',)", 'unique_together': "(('from_user', 'to_user', 'status', 'site'),)", 'object_name': 'Relationship'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_users'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'relationships'", 'to': u"orm['sites.Site']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relationships.RelationshipStatus']"}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_users'", 'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '1.0', 'null': 'True', 'blank': 'True'})
        },
        u'relationships.relationshipstatus': {
            'Meta': {'ordering': "('name',)", 'object_name': 'RelationshipStatus'},
            'from_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'symmetrical_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['data_users']