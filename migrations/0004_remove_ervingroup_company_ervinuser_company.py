# Generated by Django 4.0.2 on 2022-03-26 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ervin', '0003_company_remove_ervingroup_custom_logo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ervingroup',
            name='company',
        ),
        migrations.AddField(
            model_name='ervinuser',
            name='company',
            field=models.ForeignKey(blank=True, help_text="What is this user's company", null=True, on_delete=django.db.models.deletion.SET_NULL, to='ervin.company'),
        ),
    ]
