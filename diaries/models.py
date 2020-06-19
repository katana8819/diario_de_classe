from django.db import models

# Create your models here.

STATE_CHOICES = (
	(('AC', 'Acre'),
	 ('AL', 'Alagoas'),
	 ('AP', 'Amapá'),
	 ('AM', 'Amazonas'),
	 ('BA', 'Bahia'),
	 ('CE', 'Ceará'),
	 ('DF', 'Distrito Federal'),
	 ('ES', 'Espírito Santo'),
	 ('GO', 'Goiás'),
	 ('MA', 'Maranhão'),
	 ('MT', 'Mato Grosso'),
	 ('MS', 'Mato Grosso do Sul'),
	 ('MG', 'Minas Gerais'),
	 ('PA', 'Pará'), ('PB', 'Paraíba'),
	 ('PR', 'Paraná'),
	 ('PE', 'Pernambuco'),
	 ('PI', 'Piauí'),
	 ('RJ', 'Rio de Janeiro'),
	 ('RN', 'Rio Grande do Norte'),
	 ('RS', 'Rio Grande do Sul'),
	 ('RO', 'Rondônia'),
	 ('RR', 'Roraima'),
	 ('SC', 'Santa Catarina'),
	 ('SP', 'São Paulo'),
	 ('SE', 'Sergipe'),
	 ('TO', 'Tocantins'))
)

class Student(models.Model):
    """Os campos para cadastro do aluno"""
    name = models.CharField(max_length=18)
    lname = models.CharField(max_length=18)
    ncpf = models.CharField(max_length=11, unique=True)
    nrg = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField()
    nphone01 = models.CharField(max_length=15, blank=True)
    nphone02 = models.CharField(max_length=15, blank=True)
    addr01 = models.CharField(max_length=50, blank=True)
    addr02 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=25, blank=True)
    ncep = models.CharField(max_length=8, blank=True)
    local = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, blank=True, choices=STATE_CHOICES)
    email = models.EmailField(blank=True)
    course = models.CharField(max_length=50, blank=True)
    team = models.PositiveSmallIntegerField(blank=True, null=True)
    college = models.CharField(max_length=30, blank=True)
    finish = models.PositiveSmallIntegerField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    novalid = models.BooleanField(default=False)
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name
        
class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:90] + "..."
