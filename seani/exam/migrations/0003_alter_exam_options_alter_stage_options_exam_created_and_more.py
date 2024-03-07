# Generated by Django 5.0.2 on 2024-03-07 19:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
        ('exam', '0002_alter_stage_application_date_exam_exammodule_and_more'),
        ('library', '0004_alter_question_question_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'examen', 'verbose_name_plural': 'examenes'},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': 'etapa', 'verbose_name_plural': 'estapas'},
        ),
        migrations.AddField(
            model_name='exam',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='application_date',
            field=models.DateField(verbose_name='Fecha de aplicación'),
        ),
        migrations.CreateModel(
            name='Breakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='-', max_length=5, verbose_name='Respuesta')),
                ('correct', models.CharField(default='-', max_length=5, verbose_name='Respuesta Correcta')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam', verbose_name='Examen')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question', verbose_name='Pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='exam.Breakdown', to='library.question', verbose_name='Preguntas'),
        ),
    ]
