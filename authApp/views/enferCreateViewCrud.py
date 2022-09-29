from optparse import Values
from django.views import View
from authApp.models import Enfermero, enfermero
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class EnferView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,pk=0):
        if(pk>0):
            enfermeros=list(Enfermero.objects.filter(pk=pk).values())
            if len(enfermeros)>0:
                enfer=enfermeros[0]
                datos={'message':"Success",'enfermeros':enfermeros}
            else:
                datos={'message':"No se encontro registro"}
            return JsonResponse(datos)     
        else:    
            enfermeros = list(Enfermero.objects.values())
            if len(enfermeros)>0:
                datos={'message':"Success",'enfermeros':enfermeros}
            else:    
                datos={'message':"No se encontro registro"}
            return JsonResponse(datos) 

    def post(self, request):
        jd=json.loads(request.body)
        Enfermero.objects.create(idenfermero=jd['idenfermero'],nombre=jd['nombre'],apellidos=jd['apellidos'],telefono=jd['telefono'],
        email=jd['email'],genero=jd['genero'],user_id=jd['user_id'])
        datos={'message':"Success"}
        return JsonResponse(datos) 


    def put(self, request,pk):
         jd=json.loads(request.body)
         enfermeros=list(Enfermero.objects.filter(pk=pk).values())
         if len(enfermeros) > 0:
            enfer=Enfermero.objects.get(pk=pk)
            enfer.idenfermero=jd['idenfermero']
            enfer.nombre=jd['nombre']
            enfer.apellidos=jd['apellidos']
            enfer.telefono=jd['telefono']
            enfer.email=jd['email']
            enfer.genero=jd['genero']
            enfer.genero=jd['genero']
            enfer.user_id=jd['user_id']
            enfer.save()
            datos={'message':"Success"}
         else:
            datos={'message':"No se encontro registro"}
         return JsonResponse(datos)   

    def delete(self, request,pk):
         enfermeros=list(Enfermero.objects.filter(pk=pk).values())
         if len(enfermeros) > 0:
            Enfermero.objects.filter(pk=pk).delete()
            datos={'message':"Success"}
         else:
            datos={'message':"No se encontro registro"}
         return JsonResponse(datos)       
