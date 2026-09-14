# Proyecto grupal: diseño e implementación de una API backend 

## Curso y grupo 

Desarrollo_de_Backend (ICINF1108) 2026 - grupo 01

## Integrantes y Responsabilidades

| Estudiante | Responsabilidad |
| --- | --- |
| Beatriz Martin| coordinación + documentación e integración| 
| Josefa Sotomayor | Dominio y Datos |
| Ariel Covarrubia | API y lógica de negocio |
| Patricio Salazar | Calidad y Pruebas |

## Requerimientos
>asegurese de cumplir con los requerimientos establecidos para poder llevar a cabo de forma exitosa la Ejecución del proyecto
- [uv](https://docs.astral.sh/uv/) (probado con UV 0.12.13)

## Descripción breve del proyecto
Este proyecto está centralizado en solucionar la dificultad de medir el progreso del bienestar diario (ejercicio, sueño, alimentación) a causa de registros desorganizados en notas sueltas, llevándose a cabo con la ayuda de una API REST en Python y FastAPI que permite gestionar usuarios, registrar el cumplimiento diario y consultar el historial mediante filtros y paginación.

## Tecnologias utilizadas
- Python (3.14.7)
- FastAPI
- Pydantic
- Uvicorn

## Almacenamiento
En memoria mediante diccionarios

## Estructura del proyecto
El proyecto sigue una arquitectura separada por responsabilidades para evitar que las rutas contengan la lógica principal

```text
app/
  domain/           # Entidades y reglas del dominio  
  repositories/     # Almacenamiento en memoria (listas/diccionarios)
  routers/          # Definición de rutas/endpoints
  schemas/          # Definición de DTOs y validaciones de entrada/salida
  services/         # Casos de uso y lógica de negocio
  main.py           # Crea y configura la aplicación; recibe solicitudes HTTP
tests manual/       # Colecciones exportadas (Postman)
pyproject.toml      # Listado de dependencias
README.md           # Documentación principal
uv.lock             # Archivo de bloqueo de versiones de dependencias

```

## Ejecución del proyecto
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

### Activar entorno virtual del proyecto
la activación de entornos vituales depende del Shell activo de su sistema operativo, se indicaron los dos casos más comunes para sistemas linux, macOS y Windows

- #### Sistemas Linux/macOS `(Bash / Zsh / Dash / Ksh)`
```bash
source  .venv/bin/activate
```

+ si es que utiliza `fish` utilice `source venv/bin/activate.fish`
+ si es que utiliza `Csh / Tcsh` utilice `source venv/bin/activate.csh`

- #### Sistemas Windows `PowerShell (POSIX)`
```bash
.venv\Scripts\Activate.ps1
```

### Ejecutar el servidor de desarrollo:
```bash
uv run uvicorn app.main:app --reload
```

## Acceso a Swagger/OpenAPPI
la aplicación queda disponible en 
- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`


### Desactivar entorno vitual del proyecto:
```bash
deactivate
```

## Contrato de endpoints
| Entidad | Método | URI | Descripción | Parámetros | Respuesta |
| --- | --- | --- | --- | --- | --- |
| Usuario | POST | `/usuarios/` | Crear un nuevo usuario en la plataforma | **Body**: `UsuarioCreate` | 201 Created<br>`UsuarioResponse` |
| Usuario | GET | `/usuarios/` | Obtener el listado completo de usuarios | *Ninguno* | 200 OK<br>`list[UsuarioResponse]` |
| Usuario | GET | `/usuarios/{usuario_id}` | Obtener la información de un usuario por su ID | **Path**: `usuario_id` (int) | 200 OK<br>`UsuarioResponse` |
| Usuario | PUT | `/usuarios/{usuario_id}` | Actualizar los datos de un usuario existente | **Path**: `usuario_id` (int)<br>**Body**: `UsuarioUpdate` | 200 OK<br>`UsuarioResponse` |
| Usuario | DELETE | `/usuarios/{usuario_id}` | Eliminar un usuario del sistema | **Path**: `usuario_id` (int) | 204 No Content |
| Hábitos | POST | `/habitos/` | Registrar un nuevo hábito saludable | **Body**: `HabitoCreate` | 201 Created<br>`HabitoResponse` |
| Hábitos | GET | `/habitos/` | Consultar hábitos con opción de filtros y paginación | **Query**:<br>- `usuario_id` (int, opcional)<br>- `categoria_id` (int, opcional)<br>- `estado` (str, opcional)<br>- `orden` (str, default: "nombre")<br>- `pagina` (int, default: 1)<br>- `tamano_pagina` (int, default: 10) | 200 OK<br>`list[HabitoResponse]` |
| Hábitos | GET | `/habitos/{habito_id}` | Obtener los detalles de un hábito específico | **Path**: `habito_id` (int) | 200 OK<br>`HabitoResponse` |
| Hábitos | PUT | `/habitos/{habito_id}` | Modificar los datos de un hábito existente | **Path**: `habito_id` (int)<br>Body: `HabitoUpdate` | 200 OK<br>`HabitoResponse` |
| Hábitos | DELETE | `/habitos/{habito_id}` | Eliminar un hábito | **Path**: `habito_id` (int) | 204 No Content |
| Registros de Hábito | POST | `/registros-habito/` | Crear un nuevo registro de cumplimiento para un hábito | **Body**: `RegistroHabitoCreate` | 201 Created<br>`RegistroHabitoResponse` |
| Registros de Hábito | GET | `/registros-habito/` | Listar todos los registros de hábitos guardados | *Ninguno* | 200 OK<br>`list[RegistroHabitoResponse]` |
| Registros de Hábito | GET | `/registros-habito/{registro_id}` | Obtener la información de un registro por su ID | **Path**: `registro_id` (int) | 200 OK<br>`RegistroHabitoResponse` |
| Registros de Hábito | PUT | `/registros-habito/{registro_id}` | Actualizar los datos de un registro existente | **Path**: `registro_id` (int)<br>Body: `RegistroHabitoUpdate` | 200 OK<br>`RegistroHabitoResponse` |
| Registros de Hábito | DELETE | `/registros-habito/{registro_id}` | Eliminar un registro de hábito | **Path**: `registro_id` (int) | 204 No Content |
| Categorías | GET | `/categorias/` | Listar todas las categorías disponibles | *Ninguno* | 200 OK<br>`list[CategoriaResponse]` |
| Categorías | POST | `/categorias/` | Crear una nueva categoría de hábitos | **Body**: `CategoriaCreate` | 201 Created<br>`CategoriaResponse` |