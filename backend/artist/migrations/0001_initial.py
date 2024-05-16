# Generated by Django 5.0.6 on 2024-05-15 22:57

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=20)),
                ('total_visits', models.IntegerField(default=0)),
                ('total_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_visit_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSegments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_name', models.CharField(max_length=255)),
                ('criteria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Integrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WhatsApp', 'WhatsApp'), ('SMS', 'SMS'), ('Payment Gateway', 'Payment Gateway'), ('Quick Books', 'Quick Books'), ('Mailchimp', 'Mailchimp')], max_length=20)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
            ],
        ),
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
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('ADM', 'Admin'), ('Staff', 'Staff'), ('MNG', 'Manager')], max_length=5)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='CustomerSegmentMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.customer')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.customersegments')),
            ],
        ),
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.customersegments')),
            ],
        ),
        migrations.CreateModel(
            name='GiftVouchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeemable_at_locations', models.TextField()),
                ('issued_by_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.location')),
            ],
        ),
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_locations', models.TextField()),
                ('sold_at_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.network'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.location')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCredits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SMS', 'SMS'), ('WhatsApp', 'WhatsApp')], max_length=10)),
                ('total_credits', models.IntegerField()),
                ('remaining_credits', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.location')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.customer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.location')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.products')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.sales')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.services')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Technician', 'Technician')], max_length=10)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.location')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('No Show', 'No Show')], max_length=10)),
                ('remarks', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.customer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.location')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.services')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.staff')),
            ],
        ),
    ]
