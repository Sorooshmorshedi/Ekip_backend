# Generated by Django 4.0.2 on 2022-02-26 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_expense_equal_share_alter_share_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='expense',
        ),
    ]
