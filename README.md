# FakeStoreAPI

[FakeStoreAPI](https://fakestoreapi.com) is a free online REST API that you can use whenever you need Pseudo-real data for
your e-commerce or shopping website without running any server-side code.
It's awesome for teaching purposes, sample codes, tests and etc.

You can visit in detail docs in [FakeStoreAPI](https://fakestoreapi.com) for more information.

## Why?

When I wanted to design a shopping website prototype and needed fake data, I had to
use lorem ipsum data or create a JSON file from the base. I didn't find any online free web service
to return semi-real shop data instead of lorem ipsum data.
so I decided to create this simple web service with NodeJs(express) and MongoDB as a database.

## Resources

There are 4 main resources need in shopping prototypes:

- Products https://fakestoreapi.com/products
- Carts https://fakestoreapi.com/carts
- Users https://fakestoreapi.com/users
- Login Token https://fakestoreapi.com/auth/login

### New! "Rating" (includes rate and count) has been added to each product object!

## How to

you can fetch data with any kind of methods you know(fetch API, Axios, jquery ajax,...)

### Get all products

```js
fetch("https://fakestoreapi.com/products")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Get a single product

```js
fetch("https://fakestoreapi.com/products/1")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Add new product

```js
fetch("https://fakestoreapi.com/products", {
  method: "POST",
  body: JSON.stringify({
    title: "test product",
    price: 13.5,
    description: "lorem ipsum set",
    image: "https://i.pravatar.cc",
    category: "electronic",
  }),
})
  .then((res) => res.json())
  .then((json) => console.log(json));

/* will return
{
 id:31,
 title:'...',
 price:'...',
 category:'...',
 description:'...',
 image:'...'
}
*/
```

Note: Posted data will not really insert into the database and just return a fake id.

### Updating a product

```js
fetch("https://fakestoreapi.com/products/7", {
  method: "PUT",
  body: JSON.stringify({
    title: "test product",
    price: 13.5,
    description: "lorem ipsum set",
    image: "https://i.pravatar.cc",
    category: "electronic",
  }),
})
  .then((res) => res.json())
  .then((json) => console.log(json));

/* will return
{
    id:7,
    title: 'test product',
    price: 13.5,
    description: 'lorem ipsum set',
    image: 'https://i.pravatar.cc',
    category: 'electronic'
}
*/
```

```js
fetch("https://fakestoreapi.com/products/8", {
  method: "PATCH",
  body: JSON.stringify({
    title: "test product",
    price: 13.5,
    description: "lorem ipsum set",
    image: "https://i.pravatar.cc",
    category: "electronic",
  }),
})
  .then((res) => res.json())
  .then((json) => console.log(json));

/* will return
{
    id:8,
    title: 'test product',
    price: 13.5,
    description: 'lorem ipsum set',
    image: 'https://i.pravatar.cc',
    category: 'electronic'
}
*/
```

Note: Edited data will not really be updated into the database.

### Deleting a product

```js
fetch("https://fakestoreapi.com/products/8", {
  method: "DELETE",
});
```

Nothing will delete on the database.

### Sort and Limit

You can use query string to limit results or sort by asc|desc

```js
// Will return all the posts that belong to the first user
fetch("https://fakestoreapi.com/products?limit=3&sort=desc")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

## All available routes

### Products

```js
fields:
{
    id:Number,
    title:String,
    price:Number,
    category:String,
    description:String,
    image:String
}
```

GET:

- /products (get all products)
- /products/1 (get specific product based on id)
- /products?limit=5 (limit return results )
- /products?sort=desc (asc|desc get products in ascending or descending orders (default to asc))
- /products/products/categories (get all categories)
- /products/category/jewelery (get all products in specific category)
- /products/category/jewelery?sort=desc (asc|desc get products in ascending or descending orders (default to asc))

POST:

- /products

-PUT,PATCH

- /products/1

-DELETE

- /products/1

### Carts

```js
fields:
{
    id:Number,
    userId:Number,
    date:Date,
    products:[{productId:Number,quantity:Number}]
}
```

GET:

- /carts (get all carts)
- /carts/1 (get specific cart based on id)
- /carts?startdate=2020-10-03&enddate=2020-12-12 (get carts in date range)
- /carts/user/1 (get a user cart)
- /carts/user/1?startdate=2020-10-03&enddate=2020-12-12 (get user carts in date range)
- /carts?limit=5 (limit return results )
- /carts?sort=desc (asc|desc get carts in ascending or descending orders (default to asc))

POST:

- /carts

PUT,PATCH:

- /carts/1

DELETE:

- /carts/1

### Users

```js
fields:
{
    id:20,
    email:String,
    username:String,
    password:String,
    name:{
        firstname:String,
        lastname:String
        },
    address:{
    city:String,
    street:String,
    number:Number,
    zipcode:String,
    geolocation:{
        lat:String,
        long:String
        }
    },
    phone:String
}
```

GET:

- /users (get all users)
- /users/1 (get specific user based on id)
- /users?limit=5 (limit return results )
- /users?sort=desc (asc|desc get users in ascending or descending orders (default to asc))

POST:

- /users

PUT,PATCH:

- /users/1

DELETE:

- /users/1

### Auth

```js
fields:
{
    username:String,
    password:String
}
```

POST:

- /auth/login

## ToDo

- Add graphql support
- Add pagination
- Add another language support

# Fake Store API - Pruebas Automatizadas

Este proyecto contiene una suite de pruebas automatizadas para validar el funcionamiento de la API pública de Fake Store (https://fakestoreapi.com), cubriendo los principales endpoints de productos, usuarios, autenticación y carritos.

## Estructura del proyecto

- `tests/`: Pruebas automatizadas en Python usando Pytest y Requests.
- `data/`: Datos externos para pruebas.
- `requirements.txt`: Dependencias del proyecto.

## Instalación y ejecución

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta las pruebas:

```bash
pytest tests/
```

## Endpoints cubiertos
- GET /products
- GET /products/{id}
- POST /users
- POST /auth/login
- GET /carts/user/2
- DELETE /carts/{id}
- PUT /products/{id}

## Buenas prácticas aplicadas
- Casos positivos y negativos.
- Validación de status code y estructura de respuesta.
- Uso de datos externos y aleatorios para evitar hardcodeo.
- Código modular y legible.

## (Opcional) Integración CI/CD
Puedes agregar un flujo de integración continua usando GitHub Actions, GitLab CI, etc., para ejecutar las pruebas automáticamente en cada push.

## Decisiones técnicas

- Se implementaron pruebas negativas esperando los códigos de error estándar (404, 400, 500) para evidenciar el conocimiento de buenas prácticas REST, aunque la API pública no responde correctamente en estos casos.
- Se usaron datos aleatorios para evitar hardcodeo y asegurar independencia entre pruebas.
- La estructura del proyecto permite fácil mantenimiento y escalabilidad.

---

**Autor:** Brayan Camilo Herrera Misse

> **Nota importante:**
> 
> La API pública de Fake Store responde con código 200 incluso en casos donde lo correcto sería un error HTTP (por ejemplo, producto no encontrado o registro de usuario con datos incompletos). Las pruebas automatizadas contemplan el comportamiento esperado según buenas prácticas REST (por ejemplo, esperar 404 para recursos no encontrados o 400/500 para datos inválidos), pero algunas fallan debido a esta limitación de la API. Esto se deja así intencionalmente para evidenciar el conocimiento de los estándares y las buenas prácticas en automatización de pruebas de servicios.

## Integración Continua (CI/CD)

Este repositorio incluye un flujo de integración continua con GitHub Actions.  
Cada vez que se realiza un push o un Pull Request a la rama `master`, se ejecutan automáticamente todas las pruebas de la suite usando Pytest.

Puedes ver la configuración en `.github/workflows/python-app.yml`.
