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

- **Estado:** Solución identificada, pendiente de aplicar
- **Endpoint(s) afectado(s):** TODOS los de usuarios — confirmado en `POST /usuarios/` y `GET /usuarios/` (listar). Por la misma causa raíz, afecta también `GET /usuarios/{id}`, `PUT /usuarios/{id}`, `DELETE /usuarios/{id}`.
- **Resultado obtenido:** `500 Internal Server Error` — `RuntimeError: El repositorio de usuarios todavía no está implementado.`
- **Causa raíz:** `usuario_service.py` importa `usuario_repository` y llama a métodos `crear()`, `generar_id()`, `obtener_por_email()`, `obtener_por_id()`. El archivo `usuario_repository.py` solo define funciones sueltas con nombres distintos: `guardar()`, `listar()`, `obtener()`, `actualizar()`, `eliminar()`, `existe()` — y no expone ningún objeto llamado `usuario_repository`, por lo que el `import` falla silenciosamente (capturado por un `try/except ImportError`) y el servicio siempre asume que el repositorio no existe.
- **Solución propuesta:** agregar a `usuario_repository.py` las funciones faltantes (`obtener_por_email`, `generar_id`) y envolver todo en una clase `UsuarioRepository` con alias (`crear = guardar`, `obtener_por_id = obtener`), instanciada como `usuario_repository = UsuarioRepository()`.
- **Responsable:** Josefa (repositories) — coordinar con Ariel (services) antes de aplicar.

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
