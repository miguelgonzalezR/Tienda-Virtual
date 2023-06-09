# Generated by Django 3.0.8 on 2020-08-13 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200813_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=40, verbose_name='Estdo de las orden')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]
