from django.contrib import admin
from django.urls import path, include

import APP_EncuentraGasolinera

urlpatterns = [
    path('', cargar_pagina_inicio),
    path('APP_EncuentraGasolinera/', include(APP_EncuentraGasolinera.urls)),
]
