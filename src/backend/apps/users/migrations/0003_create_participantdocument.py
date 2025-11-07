"""
Create ParticipantDocument model.
"""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_add_school_grade_is_eligible'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='participant_documents/')),
                ('doc_type', models.CharField(choices=[('id', 'Documento de Identidade'), ('school_proof', 'Comprovante Escolar'), ('other', 'Outro')], default='other', max_length=30)),
                ('status', models.CharField(choices=[('pending', 'Pendente'), ('approved', 'Aprovado'), ('rejected', 'Rejeitado')], default='pending', max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('review_notes', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='users.user', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Documento do Participante',
                'verbose_name_plural': 'Documentos dos Participantes',
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
