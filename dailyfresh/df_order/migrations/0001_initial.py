# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('orderid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='df_order.OrderMain'),
        ),
    ]
