# Generated by Django 3.0.6 on 2020-06-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, choices=[('lo', 'love'), ('bu', 'business'), ('cu', 'culture'), ('li', 'lifestyle'), ('te', 'tech'), ('sp', 'sports'), ('po', 'politics'), ('tr', 'travel'), ('fu', 'fun'), ('fe', 'feeling'), ('fa', 'fashion'), ('ed', 'education'), ('he', 'health'), ('na', 'nature'), ('ot', 'others')], max_length=2, null=True),
        ),
    ]