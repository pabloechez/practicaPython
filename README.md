# Práctica Python
Práctica de KeepCoding para el módulo de python

## Web

## API

### API Usuarios
Listado de usuarios: GET
```
http://127.0.0.1:8000/api/v1/users
```
\
Detalle de usuario: GET
```
http://127.0.0.1:8000/api/v1/users
```
\
Eliminar usuario: DELETE
```
http://127.0.0.1:8000/api/v1/<pk>
```
\
Actualizar usuario: PUT
```
http://127.0.0.1:8000/api/v1/<pk>
```

```
"username": "example",
"first_name": "example",
"last_name": "example",
"email": "example@example",
"password": "example"
```

\
Crear usuario: POST
```
http://127.0.0.1:8000/api/v1/users
```

```
"username": "example",
"first_name": "example",
"last_name": "example",
"email": "example@example"
"password": "example"
```


### API Blog
Listado de blogs: GET
```
http://127.0.0.1:8000/api/v1/blogs/
```

Busqueda: GET
```
http://127.0.0.1:8000/api/v1/blogs/?search=palabra
```

Ordenar: GET
```
http://127.0.0.1:8000/api/v1/blogs/?ordering=first_name
```

### API Posts
Listado de posts: GET
```
http://127.0.0.1:8000/api/v1/posts
```
\
Busquedas: GET
```
http://127.0.0.1:8000/api/v1/posts/?search=palabra
```
\
Ordenación:
```
http://127.0.0.1:8000/api/v1/posts/?ordering=-created_on
```