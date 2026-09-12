# Proyecto grupal: diseño e implementación de una API backend 

## Curso y grupo 

|Desarrollo_de_Backend (ICINF1108) 2026 | grupo 01 |

## Integrantes y Responsabilidades

| Estudiante | Responsabilidad |
| --- | --- |
| Beatriz Martin| coordinación + documentación e integración, uvicorn| 
| Josefa Sotomayor | Dominio y Datos |
| Ariel Covarrubia | API y lógica de negocio |
| Patricio Salazar | Calidad y Pruebas |

## Requerimientos
- [UV](https://docs.astral.sh/uv/) (probado con UV 0.12.13)

## Descripción breve del proyecto
> descripcion breve a definir 

## Tecnologias utilizadas
- Python
- FastAPI
- Pydantic
- Uvicorn

## Almacenamiento
En memoria mediante diccionarios

## Estructura del proyecto
El proyecto sigue una arquitectura separada por responsabilidades para evitar que las rutas contengan la lógica principal

``` text
app/
  domain/           # Entidades y reglas del dominio  
  repositories/     # Almacenamiento en memoria (listas/diccionarios)
  routers/          # Definición de rutas/endpoints
  schemas/          # Definición de DTOs y validaciones de entrada/salida
  services/         # Casos de uso y lógica de negocio
  main.py           # Crea y configura la aplicación; recibe solicitudes HTTP
tests manual/       # Colecciones exportadas (Postman, Thunder Client o .http)
pyproject.toml      # Listado de dependencias
README.md           # Documentación principal
uv.lock             # Archivo de bloqueo de versiones de dependencias

```

## Ejecucion del proyecto
Para ejecutar este proyecto localmente desde una copia limpia utilizando `uv`, sigue estos pasos en tu terminal:

### Clonar el repositorio y entrar a la carpeta:
```bash
git clone https://github.com/beatmartin/icinf1108-taller-1-grupo-1.git
cd backend-2026-grupo-01
```

### Sincronizar e intalar las dependencias automáticamente con `uv`:
```bash
uv sync
```

### Activar entorno virtual del proyecto:

* #### sistemas linux
```bash
source  .venv/bin/activate
```
* #### sistemas Windows
```bash
.venv\Scripts\Activate.ps1
```

### Ejecutar el servidor de desarrollo:
```bash
uv run uvicorn app.main:app --reload
```

## Acceso a Swagger/OpenAPPI
la aplicación queda disponible en 
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs


### Desactivar entorno vitual del proyecto:
```bash
deactivate
```

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