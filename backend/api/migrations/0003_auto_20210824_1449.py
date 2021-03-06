# Generated by Django 3.2.6 on 2021-08-24 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210821_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champions',
            name='key',
            field=models.CharField(db_index=True, default='empty', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='champion_match_performance',
            name='championId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.champions', to_field='key'),
        ),
        migrations.AlterField(
            model_name='champions',
            name='blurb',
            field=models.TextField(default='empty'),
        ),
        
    ]
