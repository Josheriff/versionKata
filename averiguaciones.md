# Texto en español para mayor fluidez

Este texto solo vale par aclararme las ideas, no tiene una utilidad final dentro del proyecto

## Lo estaba haciendo mal:

La idea es hacer TDD y me pongo a investigar lo que me depara el futuro.

vuelta a empezar, comenzando con los test y luego ya veremos.


## Pasos que voy siguiendo para luego recuperar la idea

[x] El caso mas sencillo: no hay nada en el requirements.txt

[x] Caso que todo esté actualizado (requiero llamar a espias para saber si se llama al metodo que lo chequea)

[ ] Caso que haya una librería desactualizada (requiero llamar a espia para metodo, y saber que devuelve que algo no esta actualizado (doubles?))
[ ] Caso mas de una librería está desactualizada.

[ ] Caso no se encuentra el fichero de dependencias, debería devolver otro error diferente

### Refactors derivados de los pasos anteriores

Aunque parezca increible el gestor de actualizaciones de paquetes, ¡¡¡ha tenido un problema de paquetes!!! (Bendita ironía)

En mi infinita alegría, he dicho ¿Para que usar POO si esto son 4 funciones?

- He tenido que usar POO porque los Spy() solo sé ponerlos sobre clases, que se instancias como espias.
- Ademas estas clases espía las he tenido que sacar fuera de la clase principal como colaboradores.
    - Lo cual me demuestra que el TDD ayuda a tomar decisiones de arquitectura y estructuración de código.
- Al ir a empezar el caso de una sola librería desactualizada me doy cuenta que no estoy tratando bien la constante vacía que representa a un archivo vacío.
    - si quiero chequear todos los paquetes tengo que ir uno por uno, esto es linea a linea... por lo tanto la constante es una linea vacia que no significa que sea None...
    significa mas bien que la
    ```
    if line == '\n':
        print "NO VALE ESTA LINEA"

    ```
- También he averiguado que en el caso de que el archivo no existiera el propio python devolvería el error... mas adelante debería capturarse y hacer algo con el para no interrumpir la ejecución
y permitir la recursividad

## Averiguacion sobre pypi

-> url que devuelve un json con info sobre paquete:
- https://pypi.python.org/pypi/<name-of-the-package>/json

example: -> https://pypi.python.org/pypi/ooquery/json

response example:

```javascript

{
    "info": {
        "maintainer": "",
        "docs_url": null,
        "requires_python": "",
        "maintainer_email": "",
        "cheesecake_code_kwalitee_id": null,
        "keywords": "",
        "package_url": "http://pypi.python.org/pypi/ooquery",
        "author": "GISCE-TI, S.L.",
        "author_email": "devel@gisce.net",
        "download_url": "",
        "platform": "",
        "version": "0.11.0",
        "cheesecake_documentation_id": null,
        "_pypi_hidden": false,
        "description": "",
        "release_url": "http://pypi.python.org/pypi/ooquery/0.11.0",
        "downloads": {
            "last_month": 0,
            "last_week": 0,
            "last_day": 0
        },
        "_pypi_ordering": 12,
        "classifiers": [],
        "bugtrack_url": null,
        "name": "ooquery",
        "license": "MIT",
        "summary": "OpenObject Query Parser",
        "home_page": "https://github.com/gisce/ooquery",
        "cheesecake_installability_id": null
    },
    "releases": {
        "0.9.0": [
            {
                "has_sig": false,
                "upload_time": "2017-10-31T07:55:57",
                "comment_text": "",
                "python_version": "source",
                "url": "https://pypi.python.org/packages/31/ad/14b6d01004ad47ec6e217a4d9fd685c47d0241d7098ad6326689909a3cc3/ooquery-0.9.0.tar.gz",
                "md5_digest": "1aa1ad2afafb4da314b1388cd3aa2d00",
                "downloads": 0,
                "filename": "ooquery-0.9.0.tar.gz",
                "packagetype": "sdist",
                "path": "31/ad/14b6d01004ad47ec6e217a4d9fd685c47d0241d7098ad6326689909a3cc3/ooquery-0.9.0.tar.gz",
                "size": 3114
            }
        ],
        "0.10.0": [
            {
                "has_sig": false,
                "upload_time": "2017-10-31T08:09:22",
                "comment_text": "",
                "python_version": "source",
                "url": "https://pypi.python.org/packages/97/f2/ba211b58162a29128deaa94e7cbde035ab82e8b00399a33239f1b8f4beee/ooquery-0.10.0.tar.gz",
                "md5_digest": "aa751180f6321d0d63a327539cd1c849",
                "downloads": 0,
                "filename": "ooquery-0.10.0.tar.gz",
                "packagetype": "sdist",
                "path": "97/f2/ba211b58162a29128deaa94e7cbde035ab82e8b00399a33239f1b8f4beee/ooquery-0.10.0.tar.gz",
                "size": 3128
            }
        ],
        "0.8.1": [
            {
                "has_sig": false,
                "upload_time": "2017-06-13T16:46:34",
                "comment_text": "",
                "python_version": "source",
                "url": "https://pypi.python.org/packages/c4/a0/956147d00ec5d001c061b3027895ed1dbde64698fcce8f575b3c0e000c23/ooquery-0.8.1.tar.gz",
                "md5_digest": "b4727b42582d19f53308770e90acb1c7",
                "downloads": 0,
                "filename": "ooquery-0.8.1.tar.gz",
                "packagetype": "sdist",
                "path": "c4/a0/956147d00ec5d001c061b3027895ed1dbde64698fcce8f575b3c0e000c23/ooquery-0.8.1.tar.gz",
                "size": 3025
            }
        ]
}

```
