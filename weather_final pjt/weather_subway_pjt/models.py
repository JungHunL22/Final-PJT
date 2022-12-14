# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    user_no = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ForecastPm(models.Model):
    fp_idx = models.BigAutoField(primary_key=True)
    fw_idx = models.BigIntegerField()
    pm10 = models.CharField(max_length=30)
    pm25 = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'forecast_pm'


class ForecastWeather(models.Model):
    fw_idx = models.BigAutoField(primary_key=True)
    day = models.DateField()
    time = models.CharField(max_length=30)
    ondo = models.FloatField()
    humn = models.BigIntegerField()
    sky = models.BigIntegerField()
    windd = models.BigIntegerField()
    winds = models.FloatField()
    rain = models.FloatField()
    snow = models.FloatField()

    class Meta:
        managed = False
        db_table = 'forecast_weather'


class MyPlace(models.Model):
    mp_idx = models.BigAutoField()
    id = models.CharField(max_length=30)
    station_name = models.CharField(max_length=30)
    t_name = models.CharField(max_length=100)
    cate = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'my_place'


class Subway(models.Model):
    s_idx = models.BigAutoField()
    station_name = models.CharField(primary_key=True, max_length=30)
    gu = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subway'


class Tourism(models.Model):
    t_idx = models.BigAutoField(primary_key=True)
    station_name = models.CharField(max_length=100)
    t_name = models.CharField(max_length=100)
    cate = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourism'


class Weight(models.Model):
    station_name = models.CharField(max_length=40, blank=True, null=True)
    w = models.FloatField(blank=True, null=True)
    gu = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight'
