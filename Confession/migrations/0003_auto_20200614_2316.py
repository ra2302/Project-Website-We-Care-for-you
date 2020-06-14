# Generated by Django 3.0.3 on 2020-06-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Confession', '0002_confessionpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confessionpost',
            name='category',
            field=models.CharField(choices=[('TR', 'Truth'), ('FA', 'Fantasy'), ('DR', 'Dream'), ('GU', 'Guilt'), ('LI', 'Lie'), ('PA', 'Pain'), ('RA', 'Random Feeling'), ('FE', 'First Experience'), ('WI', 'Wild Experience')], max_length=2),
        ),
    ]