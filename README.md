# [[PYTHON]: Missing Value Treatment with continuos Target (MTC)]() 

- #### Creado, por: Franco A. Mansilla Ibañez, Chile.
- website: https://www.francomansilla.com


`versión 1.0- 09/2022`

## Descripción: 

1. Este código permite hacer missing value en función a la variable target, si es que tu proposito es realizar un modelo con forma supervisada. 
2. Utiliza una regresión simple entre la variable target (y) y variable a imputar (x). 
3. Para mayor detalles e información visitar el blog medium: ["Regresión: Método para tratamiento de Missing Value"](https://medium.com/@fmansillaib/regresi%C3%B3n-m%C3%A9todo-para-tratamiento-de-missing-value-5ec7de4f5878)



## Instalación:
- Paso 1: Es código que se puede utilizar en la misma interfaz usuario. 
- Paso 2: 

## Syntax 

En stata llamar, código:

```stata
  psmote var_x's, var_y(variable) class_min(#) balance(#) sample(var_muestra) seed(#)
```

- [ ] **var_x:** Señalar la(s) variable(s) en que el código analizara. 
- [ ] **var_y:** Señalar una única variable (grupo).
- [ ] **sample:** Señalar variable muestra que contenga una marca con 1 las observaciones a introducir al proceso, si es para toda la muestra, señalar all_sample
-	[ ] **class_min:** Señalar la cantidad de observaciones que tiene clase minoritaria. 
-	[ ] **balance:** Señalar el porcentaje a completar la clase desequilibra con respecto a la clase completa (señalar entre 0 a 100 que equivale a 0% a 100%).
-	[ ] **seed:** Señalar la semilla de iniciación del código. 


## Alcance:

1. La variable clase tiene que estar codificada como 0 o 1, donde la clase 1 es el minoritario. En otra caso, deberá crear una variable con la nomenclatura señalada recién.
2. La variables **var_x** y **var_y** deben estar ausentes de valores missing. Al dejar valores missing, la técnica rellenara esos valores missing. 
3. Solo funciona para variable clase (**var_y**) dicotómica, no así categórica o continua; a no ser que haga la transformación respectiva a dicotómica. 

## OUTPUT Ejemplo:
- [ ] Sin aplicar el código pSMOTE:
![sin pSMOTE](https://github.com/fmansillaib/stata_pSMOTE/blob/main/4.%20Imagenes/1.sin_psmote.png)

- [ ] Con aplicar el código pSMOTE (balance 100):
![con pSMOTE](https://github.com/fmansillaib/stata_pSMOTE/blob/main/4.%20Imagenes/2.con_psmote.png)

