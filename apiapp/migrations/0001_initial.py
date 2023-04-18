# Generated by Django 3.2.2 on 2023-04-15 20:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

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
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('address', models.CharField(max_length=255, unique=True)),
                ('signature', models.CharField(blank=True, max_length=255)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('wage', models.FloatField(blank=True, default=5000)),
                ('next_paycheck_date', models.DateTimeField(auto_now=True)),
                ('last_paycheck_date', models.DateTimeField(auto_now=True)),
                ('is_whitelisted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('type_field', models.CharField(choices=[('DAO', 'DAO'), ('Co', 'Co'), ('FDN', 'Foundation')], max_length=10)),
                ('workers', models.ManyToManyField(related_name='workers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_paycheck_date', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(default='ETH', max_length=255)),
                ('borrowing_amount', models.FloatField(blank=True, default=0)),
                ('repayment_date', models.DateTimeField(auto_now=True)),
                ('is_payed', models.BooleanField(default=False)),
                ('LTV', models.FloatField(default=30)),
                ('APR', models.FloatField(default=20)),
                ('accrued_interest', models.FloatField(blank=True, default=0)),
                ('max_borrowing_amount', models.FloatField(blank=True, default=0)),
                ('org_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='orgs',
            field=models.ManyToManyField(related_name='org', to='apiapp.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
