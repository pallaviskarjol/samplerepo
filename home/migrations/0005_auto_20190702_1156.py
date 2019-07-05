# Generated by Django 2.2.2 on 2019-07-02 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, choices=[('CSE', 'Computer Science'), ('ISE', 'Information Science')], max_length=30, null=True, verbose_name='Name')),
                ('HOD', models.CharField(max_length=30, null=True, verbose_name='Head Of Dept')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.AddField(
            model_name='details',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Student'),
        ),
        migrations.AddField(
            model_name='link',
            name='reg_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.details'),
        ),
        migrations.AddField(
            model_name='student',
            name='Branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Department'),
        ),
    ]
