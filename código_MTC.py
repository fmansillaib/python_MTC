from sklearn.linear_model import LinearRegression

# df a imputar
df_new = df.copy()

# df con valores sin na y filtro
df_var = df.filter(regex = 'ing|cost' , axis = 1)
# o
var_nd = ['ventas', 'muestra']
#Variables a imputar
var_x = [x for x in df_new.columns if x not in var_nd]

for i in df_var.columns.tolist():  #ó poner for i in var_x:
    
    umbral_unique = 10 # Scalar
    umbral_nan = 0.1 # Scalar
    target = 'venta' # Columna df.
    muestra = 'muestra' # Columna df.
    ventana = 'Train' # Atributo de la Columna Muestra.
    
    #Criterio 1: Umbral de Missing Value
    porc_i = round(df[i].isnull().sum()/len(df[i]),4)
    
    #Criterio 2: Cantidad de Valores Unicos
    unique_val = df[i].loc[df[muestra]==ventana].nunique()
    
    # Imputación por Regresión variables continuas y categorias de caracter continuas.
    if porc_i <= umbral_nan and unique_val >= umbral_unique:
        
        print('La variable '+i ,'fue imputada con REGRESIÓN LINEAL', 'con',+unique_val,'valores únicos y',porc_i, 'valores perdidos.' )        
        
        # Regresión Lineal 
        y = df[target].loc[(df[i].notnull()) & (df[muestra]==ventana)].values.reshape(-1, 1)
        X = df[i].loc[(df[i].notnull()) & (df[muestra]==ventana)].values.reshape(-1, 1)

        lr = LinearRegression()
        lr.fit(y, X)
        b0 = lr.intercept_
        b1 = lr.coef_
        
        # Calculo de Mediana en Ventas cuando X(i) es Null
        p50 =  df[target].loc[(df[i].isnull()) & (df[muestra]==ventana)].median()
        
        # Valor de X(i) que deberia ir en el NaN de la variable X(i)
        value_p50 = b0 + b1 * p50
        
        # Reemplazo en el dataframe copy los NaN de la variable X(i)
        df_new[i].fillna(value_p50[0,0], inplace = True)
    
    # Elimina variables con MISSING VALUE mayor al Umbral y un único valor en los valores únicos.
    elif porc_i > umbral_nan or unique_val <= 1:
        
        print('La variable '+i ,'fue ELIMINADA por tener',porc_i, 'valores perdidos.' )        
        df_new.drop(i, axis = 1, inplace = True)
        
    # Imputación por Valor Faltantes a varaibles dicotomicas y variables con menos de 15 categorias
    elif unique_val > 1  & unique_val < umbral_unique:
        print('La variable '+i ,'fue imputada por VALOR FALTANTE', 'con',+unique_val,'valores únicos y',porc_i, 'valores perdidos.' )        
        
        #Calculo máximo valor
        value_max = df[i].max()
        #Valor máximo +1
        value_mas1 = value_max + 1
        #Reemplazar NaN por el Valor asignado.
        df_new[i].fillna(value_mas1, inplace = True)
#FIN
