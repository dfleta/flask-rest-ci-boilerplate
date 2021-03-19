
# Recursos del proyecto

## Enunciado del proyecto

https://github.com/dfleta/ollivanders_shop

## Qué es una API REST

https://youtu.be/HeXQ98sogs8 

## Recursos

Flask restful:

https://flask-restful.readthedocs.io/en/latest/index.html

Flask:

https://flask.palletsprojects.com/en/1.1.x/

Testing flask:

https://flask.palletsprojects.com/en/1.1.x/testing/

Cómo usar los `markers` y montar CI en Python:

https://github.com/dfleta/kata_tdd_pytest

`pytest.fixture`

https://pingpong-espacio.slack.com/archives/C01C5693KSN/p1615997416000100

Libro guay de Flask:

https://drive.google.com/file/d/1ZQBZv3qlfcPYW6Okk9lEZiDm_78Msrzh/view?usp=sharing

Lista de códigos http: 

https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

APIs con JSON:

https://flask.palletsprojects.com/en/1.1.x/quickstart/#apis-with-json

jsonify de Flask

https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify

`property` , `classmethod` , `staticmethod` de Python:

https://pythonguide.readthedocs.io/en/latest/python/property.html

Comparar dos objetos Python sobreescribiendo el método `__eq__`

https://medium.com/@chaoren/comparing-class-instances-in-python-is-easy-80f487223228


## Solución en mi repo utilizando Flask-restful

https://github.com/dfleta/ollivanders


### Arrancando

```bash
$ python3.6 -m venv venv

$ source ./venv/bin/activate

https://flask-restful.readthedocs.io/en/latest/installation.html

$ pip3 install flask-restful
```

### Minimal api

```bash
$ python3.6 api.py 

$ curl http://127.0.0.1:5000{
    "hello": "Ollivanders"
}

$ curl localhost:5000

$ pip3 install pytest
```

