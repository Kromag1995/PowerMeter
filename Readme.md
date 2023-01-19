Para correr el ejercicio se puede correr con el ambiente local o levanter un docker

## Local
```
pip install -r requierment.txt
python manage.py runserver
```

## Docker

```
docker build . -t powermeter
docker run -it -p 8000:8000 powermeter
```

En ambas formas queda levantado el server en localhost:8000

## Endpoints

### wattmeter/

GET Trae todos los medidores

POST Crea nuevo medidor

Ejemplo del body
```
{
    "name": "test",
    "unkey": "test" 
}
```

##### wattmeter/< pk>

GET Trae la info de un medidor con esa pk en caso de que exista

##### wattmeter/< pk>/max_consume

GET Trae el consumo maximo de ese medidor

##### wattmeter/< pk>/min_consume

GET Trae el consumo minimo de ese medidor

##### wattmeter/< pk>/mean_consume

GET Trae el consumo promedio de ese medidor

##### wattmeter/< pk>/total_consume

GET Trae el consumo total de ese medidor

### measure/

GET Trae todas las mediciones

POST Crea nueva medicion

Ejemplo del body

```
{
    "value": 100,
    "wattmeter": 1
}
```



##### measure/< pk>

GET Trae la medicion con ese pk si existe
