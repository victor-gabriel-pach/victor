"""
Migration to add school_grade and is_eligible to User model.
"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school_grade',
            field=models.CharField(blank=True, choices=[('9ef', '9º ano do Ensino Fundamental'), ('1em', '1º ano do Ensino Médio'), ('2em', '2º ano do Ensino Médio'), ('3em', '3º ano do Ensino Médio'), ('other', 'Outro')], max_length=10, null=True, verbose_name='Série/Ano Escolar'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_eligible',
            field=models.BooleanField(default=False, verbose_name='Elegível'),
        ),
    ]
