from django.contrib import admin
from .models.user import User
from .models.medico import Medico
from .models.enfermero import Enfermero
from .models.auxiliar import Auxiliar
from .models.familiar import Familiar
from .models.sugerencia import Sugerencia
from .models.paciente import Paciente
from .models.historia import Historiaclinica
from .models.signosvitales import Signosvitales
from .models.detallesignos import Detallesignos





admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(Sugerencia)
admin.site.register(Paciente)
admin.site.register(Historiaclinica)
admin.site.register(Signosvitales)
admin.site.register(Detallesignos)



# Register your models here.
