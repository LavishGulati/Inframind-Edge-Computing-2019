# Generated by Django 2.2.6 on 2019-10-06 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('TotalAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('Contact', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Cost', models.IntegerField()),
                ('FinalCost', models.IntegerField()),
                ('orders', models.ManyToManyField(to='home.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BillingTo', to='home.User'),
        ),
    ]
