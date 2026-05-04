# Django + Railway — Formulario de Contacto

## Estructura del proyecto

```
django_railway/
├── manage.py
├── requirements.txt
├── Procfile
├── railway.toml          ← configuración de Railway
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── contacto/
    ├── models.py         ← modelo de base de datos
    ├── forms.py          ← formulario Django
    ├── views.py          ← lógica
    ├── urls.py           ← rutas
    └── templates/
        └── contacto/
            └── formulario.html
```

## Correr localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrí http://127.0.0.1:8000

## Deploy en Railway

### 1. Subir a GitHub
```bash
git init
git add .
git commit -m "primer commit"
git remote add origin https://github.com/tuusuario/tu-repo.git
git push -u origin main
```

### 2. Crear proyecto en Railway
- Entrá a https://railway.app
- New Project → Deploy from GitHub repo
- Seleccioná tu repositorio

### 3. Variables de entorno en Railway
En el panel de Railway, ir a Variables y agregar:

| Variable | Valor |
|----------|-------|
| `SECRET_KEY` | una clave larga y aleatoria |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `tuapp.railway.app` |

Para generar una SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Railway hace el deploy automáticamente
El `railway.toml` ya configura que corra `migrate` antes de iniciar el servidor.

## Panel de administración

Para acceder al admin de Django en producción:
```bash
# Correr esto una vez (Railway tiene consola en el panel)
python manage.py createsuperuser
```

Luego entrar a: `https://tuapp.railway.app/admin`
