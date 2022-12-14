# Generated by Django 4.1 on 2022-09-04 21:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('classic_tracker', '0001_initial'), ('classic_tracker', '0002_user_subject_count_user_time_usage_ratio'), ('classic_tracker', '0003_alter_user_email'), ('classic_tracker', '0004_alter_day_day_of_week'), ('classic_tracker', '0005_alter_day_day_of_week'), ('classic_tracker', '0006_alter_day_day_of_week'), ('classic_tracker', '0007_alter_stage_name_alter_subject_name'), ('classic_tracker', '0008_alter_user_options_alter_day_study_time_and_more'), ('classic_tracker', '0009_alter_day_worktime'), ('classic_tracker', '0010_alter_day_end_next_day_alter_day_worktime_and_more'), ('classic_tracker', '0011_alter_day_end_next_day_alter_session_end_next_day'), ('classic_tracker', '0012_alter_day_stage_alter_session_day_and_more'), ('classic_tracker', '0013_alter_user_options_and_more'), ('classic_tracker', '0014_alter_day_worktime')]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('total_usable_time', models.PositiveBigIntegerField(default=0)),
                ('total_study_time', models.PositiveBigIntegerField(default=0)),
                ('total_work_time', models.PositiveBigIntegerField(default=0)),
                ('stage_count', models.PositiveSmallIntegerField(default=0)),
                ('day_count', models.PositiveSmallIntegerField(default=0)),
                ('session_count', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('subject_count', models.PositiveIntegerField(default=0)),
                ('time_usage_ratio', models.DecimalField(decimal_places=4, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Easy to remember, 20 characters max', max_length=20)),
                ('description', models.TextField(blank=True, help_text='100 characters max', max_length=100, null=True)),
                ('total_study_time', models.PositiveBigIntegerField(default=0)),
                ('session_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Easy to remember, 20 characters max', max_length=20)),
                ('description', models.TextField(blank=True, help_text='100 characters max', max_length=100, null=True)),
                ('day_count', models.PositiveSmallIntegerField(default=0)),
                ('session_count', models.PositiveIntegerField(default=0)),
                ('total_usable_time', models.PositiveBigIntegerField(default=0)),
                ('total_study_time', models.PositiveBigIntegerField(default=0)),
                ('total_work_time', models.PositiveBigIntegerField(default=0)),
                ('time_usage_ratio', models.DecimalField(decimal_places=4, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('day_of_week', models.SmallIntegerField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')])),
                ('session_count', models.PositiveSmallIntegerField(default=0)),
                ('worktime', models.DecimalField(decimal_places=1, default=0, help_text='Time spent in school/office, may leave it 0 and update later', max_digits=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('start', models.TimeField()),
                ('end', models.TimeField(blank=True, help_text='May be completed later', null=True)),
                ('end_next_day', models.BooleanField(blank=True, default=False, help_text='May be completed later', null=True)),
                ('usable_time', models.PositiveIntegerField(default=0)),
                ('study_time', models.PositiveIntegerField(default=0)),
                ('time_usage_ratio', models.DecimalField(decimal_places=4, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('comment', models.TextField(blank=True, help_text='100 characters max', max_length=100, null=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classic_tracker.stage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField(blank=True, help_text='May be completed later', null=True)),
                ('end_next_day', models.BooleanField(blank=True, default=False, help_text='May be completed later', null=True)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classic_tracker.day')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classic_tracker.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='day',
            constraint=models.UniqueConstraint(fields=('user', 'day'), name='user_day_uniqueness'),
        ),
        migrations.AddConstraint(
            model_name='day',
            constraint=models.CheckConstraint(check=models.Q(('time_usage_ratio__range', (0, 1))), name='day_time_usage_ratio_range'),
        ),
        migrations.AddConstraint(
            model_name='stage',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='user_stage_uniqueness'),
        ),
        migrations.AddConstraint(
            model_name='stage',
            constraint=models.CheckConstraint(check=models.Q(('time_usage_ratio__range', (0, 1))), name='stage_time_usage_ratio_range'),
        ),
        migrations.AddConstraint(
            model_name='subject',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='user_subject_uniqueness'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(check=models.Q(('time_usage_ratio__range', (0, 1))), name='user_time_usage_ratio_range'),
        ),
        migrations.AlterField(
            model_name='day',
            name='worktime',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='day',
            name='end_next_day',
            field=models.BooleanField(blank=True, help_text='May be completed later', null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='worktime',
            field=models.PositiveIntegerField(default=0, help_text='Time spent in school/office, may leave it 0 and update later'),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_next_day',
            field=models.BooleanField(blank=True, help_text='May be completed later', null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='end_next_day',
            field=models.BooleanField(blank=True, default=False, help_text='May be completed later', null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_next_day',
            field=models.BooleanField(blank=True, default=False, help_text='May be completed later', null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classic_tracker.stage'),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classic_tracker.day'),
        ),
        migrations.AlterField(
            model_name='session',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classic_tracker.subject'),
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='stage',
            name='stage_time_usage_ratio_range',
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='user_time_usage_ratio_range',
        ),
        migrations.AlterField(
            model_name='day',
            name='worktime',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Time spent in school/office, may leave it 0 and update later'),
        ),
    ]
