# Bugs Found — Pruebas manuales Backend Grupo 01

Documento de seguimiento de bugs encontrados durante las pruebas con Postman/Swagger.
Responsable de pruebas: Patricio Salazar (QA)

---

## Bug 1: Rutas de Hábitos, Categorías y Registros no responden (404)

- **Estado:** Pendiente de confirmar / posiblemente resuelto
- **Endpoint(s) afectado(s):** `GET/POST /habitos/`, `GET/POST /categorias/`, `GET/POST /registros/`
- **Resultado obtenido:** `404 Not Found`
- **Causa raíz:** `main.py` inicialmente solo incluía el router de Usuarios (`app.include_router(usuarios.router)`). Faltaba conectar los routers de Categorías, Hábitos y Registros.
- **Cómo confirmarlo:** revisar `/docs` — si la sección correspondiente no aparece en Swagger, el router no está incluido en `main.py`.
- **Responsable sugerido:** Beatriz (main.py / integración)

---

## Bug 2: `usuarios.py` sin tipos en los parámetros del body

- **Estado:** Resuelto
- **Endpoint(s) afectado(s):** `POST /usuarios/`, `PUT /usuarios/{id}`
- **Resultado obtenido (antes del fix):** `422 Unprocessable Entity` — "Add missing query parameter", incluso con un body JSON válido.
- **Causa raíz:** las funciones `crear_usuario(datos)` y `actualizar_usuario(usuario_id, datos)` no tenían tipo declarado (`datos: UsuarioCreate`), por lo que FastAPI interpretaba `datos` como query parameter en vez de body.
- **Solución aplicada:** se agregó `usuario_schema.py` (con `UsuarioCreate`, `UsuarioUpdate`, `UsuarioResponse`) y se tipó el parámetro en el router.
- **Responsable:** Ariel (routers) + Josefa (schemas)

---

## Bug 3: Falta dependencia `email-validator`

- **Estado:** Resuelto
- **Síntoma:** el servidor no levantaba. Error: `ImportError: email-validator is not installed, run 'pip install pydantic[email]'`
- **Causa raíz:** `usuario_schema.py` usa el tipo `EmailStr` de Pydantic, que requiere la librería opcional `email-validator`.
- **Solución aplicada:** `uv add pydantic[email]` (o `pip install email-validator`), actualizando `pyproject.toml` / `uv.lock`.

---

## Bug 4: Desajuste de nombres entre `usuario_repository.py` y `usuario_service.py`

- **Estado:** ✅ RESUELTO (confirmado 12/09/2026, tras merge de main a la rama psalazar)
- **Endpoint(s) afectado(s):** Todos los de Usuarios — ya verificados manualmente los 5:
  - `POST /usuarios/` → `201 Created`. Body enviado: `{"name": "Patricio", "email": "psalazar2026@alu.uct.cl"}`. Response incluye `id`, `name`, `email` y `fecha_registro` autogenerada.
  - `GET /usuarios/` → `200 OK`, devuelve el arreglo con el usuario creado.
  - `GET /usuarios/{id}` (ej. `/usuarios/1`) → `200 OK`, devuelve el usuario correcto.
  - `PUT /usuarios/{id}` → `200 OK`. Se probó actualizando `email` de `psalazar2026@alu.uct.cl` a `psalazar2026@alu.com`; el response refleja el cambio y mantiene `id` y `fecha_registro` originales.
  - `DELETE /usuarios/{id}` → `204 No Content`.
- **Causa raíz (histórica):** `usuario_service.py` importaba `usuario_repository` y llamaba a métodos `crear()`, `generar_id()`, `obtener_por_email()`, `obtener_por_id()`, pero `usuario_repository.py` solo definía funciones sueltas con nombres distintos (`guardar()`, `listar()`, `obtener()`, `actualizar()`, `eliminar()`, `existe()`), sin exponer ningún objeto `usuario_repository`. El import fallaba silenciosamente y el servicio asumía que el repositorio no existía.
- **Solución aplicada:** se alinearon los nombres entre repositorio y servicio (confirmado funcionando end-to-end).

---

## Bug 5: Import con typo en `registros.py`

- **Estado:** Pendiente de confirmar si sigue vigente tras el cambio de estructura de carpetas
- **Archivo:** `routers/registros.py`
- **Detalle:** se importa `RegistroHabitoUpate` (falta la "d") desde `registro_schema.py`, además de `RegistroHabitoUpdate` (correcto). El import con typo no se usa en ningún lado — es código muerto que puede romper el arranque si esa clase no existe con ese nombre exacto en el schema.
- **Responsable sugerido:** Josefa (schemas) / Ariel (routers)

---

## Notas generales

- El proyecto cambió su estructura de carpetas de `App/`, `Domain/`, `Repositories/` (mayúscula) a `app/`, `domain/`, `repositories/` (minúscula) durante el desarrollo. Verificar que todos los imports en el proyecto sean consistentes con la nueva convención en minúscula.
- Comando actualizado para levantar el servidor: `uvicorn app.main:app --reload` (ejecutado desde la raíz del proyecto).