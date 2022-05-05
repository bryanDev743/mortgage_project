# Generated by Django 4.0.3 on 2022-05-03 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('states', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=9)),
                ('routing_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('passw', models.CharField(max_length=50)),
                ('states', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_n', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User_has_Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.loan')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.user')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('credit_score', models.IntegerField()),
                ('credit_line', models.IntegerField()),
                ('income', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('debts', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bank_offers_Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.bank')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.loan')),
            ],
        ),
    ]