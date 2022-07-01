from django.db import models

# Create your models here.

candidato1, candidato2, candidato3, candidato4, candidato5 = [
    'TESTEA',
    'TESTEB',
    'TESTEC',
    'TESTED',
    'TESTEE',
]
candidato6, candidato7, candidato8, candidato9, candidato10 = [
    'TESTEF',
    'TESTEG',
    'TESTEH',
    'TESTEI',
    'TESTEJ',
]

voto_rei = [
    ('1', candidato1),
    ('2', candidato2),
    ('3', candidato3),
    ('4', candidato4),
    ('5', candidato5),
]

voto_rainha = [
    ('6', candidato6),
    ('7', candidato7),
    ('8', candidato8),
    ('9', candidato9),
    ('10', candidato10),
]

class Alunos(models.Model):
    matricula = models.IntegerField(db_column='matricula', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=255, blank=True, null=True)
    voto_rei = models.CharField(db_column='voto_rei', choices=voto_rei, max_length=10, blank=True, null=True)
    voto_rainha = models.CharField(db_column='voto_rainha', choices=voto_rainha, max_length=10, blank=True, null=True)
    statusvoto = models.CharField(db_column='statusVoto', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alunos'
    def __str__(self):
        return self.nome