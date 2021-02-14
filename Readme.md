



Importador de la BD
======================

¿Que hace?
Busca la base de datos \*.pkl disponible en el archivo principal del proyecto. En el caso real lo tengo linkeado como un enlace físico de la base de datos original, la que compilo cada vez que pasa un nuevo mes.
¿Producto?
Importa la base de datos como un objeto python BD del tipo pd.Dataframe() al contexto del ejecutador

Analizador
======================

¿Que hace?
Calcula los datos del REM8 que corresponda a la base de datos suministrada.
¿Producto?
Informe REM8 detallando rango de fechas y sectores.