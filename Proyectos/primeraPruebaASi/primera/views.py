from django.http import HttpResponse
from django.http import JsonResponse
#api rest imports

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from primera.serializers import UserSerializer, GroupSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView

import json

#api rest

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class dietas_alimentacion(viewsets.ModelViewSet):
    @csrf_exempt
    def dieta(request):
        data=JSONParser().parse(request)

        posIndice = data["RutinaNumero"]

        #variables
        cal_quemadas=0
        km_recorridos=0
        M_recorridos=0
        lipidos=0
        proteina=0
        glucidos=0
        

        Alimentos={
            "alimentos":[
            {
                "desayunos":[
                    {
                        'desayuno':1,
                        'lipidos':18,
                        'proteina':30,
                        'glucidos':295,
                        'total':343  
                    },
                    {   
                        'desayuno':2,
                        'lipidos':39,
                        'proteina':39,
                        'glucidos':285,
                        'total':363  
                    },
                    {   
                        'desayuno':3,
                        'lipidos':453,
                        'proteina':160,
                        'glucidos':436,
                        'total':1049
                    },
                    {   
                        'desayuno':4,
                        'lipidos':380,
                        'proteina':111,
                        'glucidos':99,
                        'total':590
                    },
                    {   
                        'desayuno':5,
                        'lipidos':80,
                        'proteina':166,
                        'glucidos':141,
                        'total':387
                    },
                   ]},{"almuerzos":[
                    {
                        'almuerzo':1,
                        'lipidos':18,
                        'proteina':30,
                        'glucidos':295,
                        'total':343  
                    },
                    {   
                        'almuerzo':2,
                        'lipidos':39,
                        'proteina':39,
                        'glucidos':285,
                        'total':363  
                    },
                    {   
                        'almuerzo':3,
                        'lipidos':453,
                        'proteina':160,
                        'glucidos':436,
                        'total':1049
                    },
                    {   
                        'almuerzo':4,
                        'lipidos':380,
                        'proteina':111,
                        'glucidos':99,
                        'total':590
                    },
                    {   
                        'almuerzo':5,
                        'lipidos':80,
                        'proteina':166,
                        'glucidos':141,
                        'total':387
                    },
                ]},{"cenas":[
                    {
                        'cena':1,
                        'lipidos':18,
                        'proteina':30,
                        'glucidos':295,
                        'total':343  
                    },
                    {   
                        'cena':2,
                        'lipidos':39,
                        'proteina':39,
                        'glucidos':285,
                        'total':363  
                    },
                    {   
                        'cena':3,
                        'lipidos':453,
                        'proteina':160,
                        'glucidos':436,
                        'total':1049
                    },
                    {   
                        'cena':4,
                        'lipidos':380,
                        'proteina':111,
                        'glucidos':99,
                        'total':590
                    },
                    {   
                        'cena':5,
                        'lipidos':80,
                        'proteina':166,
                        'glucidos':141,
                        'total':387
                    },
                ]},
            ]
        }

        rutinas={
           "rutinas":[
               {
                    'rutina':1,
                    'cal_quemadas':80,
                    'tipo_distancia':'km'
                },
                {
                    'rutina':2,
                    'cal_quemadas':80,
                    'tipo_distancia':'km'
                },
                {
                    'rutina':3,
                    'cal_quemadas':80,
                    'tipo_distancia':'m'
                },
                {
                    'rutina':4,
                    'cal_quemadas':80,
                    'tipo_distancia':'km'
                }
           ]
       }
        #print(Alimentos)
        #print(rutinas)
        print("========================")
        
        total=0;
        lipidos1=0;
        proteina1=0;
        glucidos1=0;

        lipidos2=0;
        proteina2=0;
        glucidos2=0;

        lipidos3=0;
        proteina3=0;
        glucidos3=0;
        
        for k in Alimentos["alimentos"]:
        # print(k)
            for key, value in k.items():
                for json in value:
                    #print(json)#si lo descomento se repiten datos en consola
                    try:   
                        if key=="desayunos" and data["desayuno"]==json["desayuno"]:
                                lipidos1=lipidos1+json["lipidos"]
                                proteina1=proteina1+json["proteina"]
                                glucidos1=glucidos1+json["glucidos"]
                                print(json)
                                tipo = json[key]


                        if key == "almuerzos"and data["almuerzo"]==json["almuerzo"]:
                                lipidos2=lipidos2+json["lipidos"]
                                proteina2=proteina2+json["proteina"]
                                glucidos2=glucidos2+json["glucidos"]
                                print(json)
                                tipo = json[key]

                        if key=="cenas"and data["cena"]==json["cena"]:
                                lipidos3=lipidos3+json["lipidos"]
                                proteina3=proteina3+json["proteina"]
                                glucidos3=glucidos3+json["glucidos"]
                                print(json)
                                tipo = json[key]


                    except KeyError:
                        pass

        totallip=(lipidos1+lipidos2+lipidos3)
        totalpro=(proteina1+proteina2+proteina3)
        totalglu=(glucidos1+glucidos2+glucidos3)
        total=(totallip+totalpro+totalglu)
        print("La suma de los totales es:")
        print(total)

        Rutinas = {
            "rutinas":{
                1: {   
                    'cal_quemadas':80,
                    'tipo_distanciakm':200
                },
                2: {
                    'cal_quemadas':80,
                    'tipo_distanciam':100
                },
                3: {
                    'cal_quemadas':80,
                    'tipo_distanciam':90
                },
                4: {
                    'cal_quemadas':80,
                    'tipo_distanciakm':45
                }
            }
        }


        json = Rutinas["rutinas"][posIndice]
        caloria = json["cal_quemadas"]

        if "tipo_distanciakm" in json.keys():
            distancia = json["tipo_distanciakm"] * 1000
        else:
            distancia = json["tipo_distanciam"]

        TotalCalorias = caloria * distancia


        jsonResultado = {
            'Total': total,
            'TotalRutina': TotalCalorias,
        }

        #multiplicas los km*1000 para pasarlo a m y los que estan en metros se dejan quieto

        #Aqui tienes 80 calorias * 45000 metros entonces eso da aca el resultado de
        #Y asi de sencillo en un folor for hicimos todo eso, ahi se hara automatico para todos 

        #obtienes la rutina y  a la final imprimes la rutina agrega dentro de lo que has obetinedo 

        return JsonResponse(jsonResultado)

def index(request):
    return JsonResponse({'':''})
    
    

