# Generated by Django 2.1.5 on 2022-01-01 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20220101_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('house_name', models.CharField(max_length=100, verbose_name='House Name')),
                ('aadhar_no', models.BigIntegerField(verbose_name='Aadhar Number')),
                ('image', models.FileField(max_length=300, upload_to='Images', verbose_name='Image')),
                ('case_file', models.FileField(max_length=300, upload_to='CaseFile', verbose_name='Case File')),
                ('casr_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CaseType')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.City')),
            ],
        ),
    ]