# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainpageComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()
    target = models.ForeignKey('MainpagePost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainpage_comment'


class MainpagePost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)
    text = models.TextField()
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.IntegerField()
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mainpage_post'


class MainpagePostRelationPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_post = models.ForeignKey(MainpagePost, models.DO_NOTHING)
    to_post = models.ForeignKey(MainpagePost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainpage_post_relation_posts'
        unique_together = (('from_post', 'to_post'),)


class MainpagePostTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(MainpagePost, models.DO_NOTHING)
    tag = models.ForeignKey('MainpageTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainpage_post_tags'
        unique_together = (('post', 'tag'),)


class MainpageReply(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()
    target = models.ForeignKey(MainpageComment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainpage_reply'


class MainpageTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'mainpage_tag'


class PollsSqltext(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    gseek_id = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_sqltext'


class PollsState(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    gseek_id = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_state'


class SqlText(models.Model):
    date = models.DateTimeField(primary_key=True)
    gseek_id = models.CharField(max_length=20)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sql_text'
        unique_together = (('date', 'gseek_id'),)


class State(models.Model):
    date = models.DateTimeField(primary_key=True)
    thread = models.CharField(max_length=20)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'
        unique_together = (('date', 'thread'),)
