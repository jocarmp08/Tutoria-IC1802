### Buenas prácticas de estilo
Un buen Ingeniero en Computación es capaz de escribir código legible y fácil de mantener. Un código bien escrito permite depurar más rápidamente, escribir menos comentarios y que otros programadores entiendan su producto con sencillez. 

El siguiente es un código escrito con malas prácticas de programación:

    def foo():
	    bar = "hola mundo"
	    print(bar)

¿Qué hace la función? ¿Qué significa *foo*? ¿Qué es *bar*? El código anterior puede reescribirse de la siguiente manera:

    def mostrar_texto_hola_mundo():
	    texto_hola_mundo = "hola mundo"
	    print(texto_hola_mundo)

¿Se entiende ahora? Para algunos programadores puede ser aburrido formular y escribir nombres tan largos para sus variables y funciones. Sin embargo, este hábito ayuda a ahorrarse un mal rato al tratar de entender su propio código después de no haber trabajado en él durante una semana o cuando intente explicárselo a un amigo. Además, el código anterior casi no necesita comentarios, lo cual, la mayoría del tiempo es una buena noticia.

 - Las **variables** son “elementos” que viven en su código. Por lo general, sus nombres son **sustantivos**. Por ejemplo: *baraja*, *carta*, *mensaje*, *jugador*, etc.
 - Las **funciones** realizan acciones con las variables. Por lo general, sus nombres incluyen **verbos infinitivos**. Por ejemplo: *construir_baraja*, *tomar_carta*, *mostrar_mensaje*, *cambiar_jugador*, etc.
 - Si su código está bien escrito y se logra entender sin comentarlo, no lo comente. Muchas líneas pueden representar una carga visual innecesaria que pueden hacer su código aburrido de leer.
 - Siempre ubique las variables necesarias al inicio de la función. Esparcir variables a través del código dificulta la tarea de depuración
 - No mezcle *tabs* con *espacios* cuando indenta su código. 
 - Tenga cuidado con las comillas: utilice ‘ ‘ cuando se trate de un único carácter, “ “ en cualquier otro caso.

**Python** posee un manual de estilo llamado **PEP-8**. Es un estándar diseñado para que los programas escritos en este lenguaje sean entendibles para todos los programadores.
Se puede consultar en la [página oficial de PEP 8](https://www.python.org/dev/peps/pep-0008/) (en inglés) o leer un resumen en español [aquí](https://alexanderae.com/pep8-guia-de-estilo-para-python.html#fnref-3).


