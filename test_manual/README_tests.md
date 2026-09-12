# tests_manual/

Colecciones exportadas (Postman, Thunder Client o .http) con los casos de prueba manuales de la API — casos exitosos y de error para cada endpoint.

## Contenido de esta carpeta

- `coleccion_postman.json` — colección exportada desde Postman (formato Collection v2.1), organizada en carpetas por entidad: Usuarios, Categorías, Hábitos, Registros.
- `bugs_encontrados.md` — registro de bugs detectados durante las pruebas, con endpoint afectado, resultado obtenido, causa raíz y responsable sugerido.

## Cómo levantar el servidor antes de correr las pruebas

Desde la raíz del proyecto:

```bash
source .venv/bin/activate      # o .venv/bin/activate.fish si usas fish shell
uvicorn app.main:app --reload
```

El servidor queda disponible en `http://127.0.0.1:8000`. La documentación interactiva (Swagger) está en `http://127.0.0.1:8000/docs`.

## Cómo importar la colección en Postman

1. Abrir Postman
2. Botón "Import" (arriba a la izquierda, o `Ctrl+O`)
3. Seleccionar el archivo `coleccion_postman.json` de esta carpeta
4. La colección aparecerá en el panel izquierdo con las 4 carpetas por entidad, cada request lista para ejecutar con "Send"

## Variables usadas

- `base_url`: `http://127.0.0.1:8000` (host local del servidor)

## Casos cubiertos por entidad

Cada entidad (Usuarios, Categorías, Hábitos, Registros) incluye, cuando el endpoint correspondiente ya está disponible:

- Caso exitoso (happy path) para crear, listar, obtener, actualizar y eliminar
- Casos de error: datos inválidos, recurso no encontrado, duplicados, y otras reglas de negocio (fecha futura, archivado) según lo implementado en cada `service.py`

## Bugs detectados

Ver `bugs_encontrados.md` para el detalle de problemas encontrados durante las pruebas, incluyendo diagnóstico técnico y responsable sugerido para cada uno.
