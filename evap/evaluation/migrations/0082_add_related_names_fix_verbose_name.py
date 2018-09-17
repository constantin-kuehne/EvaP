# Generated by Django 2.0.7 on 2018-09-03 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0081_create_direct_delegation_email_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='evaluation.Semester', verbose_name='semester'),
        ),
        migrations.AlterField(
            model_name='faqquestion',
            name='answer_en',
            field=models.TextField(verbose_name='answer (english)'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='evaluation.Questionnaire'),
        ),
    ]
