# Proyecto grupal: diseño e implementación de una API backend 

## Curso y grupo 

|Desarrollo_de_Backend (ICINF1108) 2026 | grupo 01 |

## Integrantes y Responsabilidades

| Estudiante | Responsabilidad |
| --- | --- |
| Beatriz Martin| coordinación + documentación e integración | 
| Josefa Sotomayor | Dominio y Datos |
| Ariel Covarrubia | API y lógica de negocio |
| Patricio Salazar | Calidad y Pruebas |

## Descripción breve del proyecto
> descripcion breve a definir 

## Tecnologias utilizadas
- Python
- FastAPI
- Pydantic
- Uvicorn

## Almacenamiento
En memoria mediante listas o diccionarios. 

## Estructura del proyecto
El proyecto sigue una arquitectura separada por responsabilidades para evitar que las rutas contengan la lógica principal

``` text
app/
  main.py           # Crea y configura la aplicación; recibe solicitudes HTTP
  routers/          # Definición de rutas/endpoints
  schemas/          # Definición de DTOs y validaciones de entrada/salida
  domain/           # Entidades y reglas del dominio
  services/         # Casos de uso y lógica de negocio
  repositories/     # Almacenamiento en memoria (listas/diccionarios)
tests manual/       # Colecciones exportadas (Postman, Thunder Client o .http)
README.md           # Documentación principal
requirements.txt    # Listado de dependencias

```

## Ejecucion del proyecto
> Espacio a definir 

## Contrato de endpoints
| Entidad | Método | URI | Descripción | Parámetros | Respuesta |
| --- | --- | --- | --- | --- | --- |
| | | | | | 
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

> Espacio a definir, se esperan 12 mínimo

## Acceso a Swagger/OpenAPPI
> Espacio a definir 