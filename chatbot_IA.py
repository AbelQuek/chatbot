#Importamos la librería nltk 
from nltk.chat.util import Chat, reflections

mis_reflexions = {
	"" : "",
	"" : ""
}

# base de conocimientos del chatbot
pares = [
	
		#bajo rendimiento
	[
		r"Bajo Rendimiento",
		[ "¿A que se deve este Problema? Escribe una de las opciones: \n Problemas de Aprenizaje \n Problemas Familiares ",]
	],
	[
		r"Problemas de Aprendizaje",
		[ " Segun el Artículo 31º 'Medidas correctivas por bajo rendimiento' El estudiante que muestra bajo rendimiento académico será objeto de las siguientes medidas dependiendo a cuantas veces desaprobo un curso: \n 👇 \n  ¿Cuántas veces desaprobaste un curso?   \n 1 \n 2 \n 3 ",]
    ],
    [
		r"1",
		[ " a. El estudiante que es desaprobado en una asignatura por primera vez es sujeto a observación académica. Lo que se le hace saber al momento derealizar su matrícula en el periodo lectivo siguiente. el cual tendra que levantar una amonestacion \n\n te recomiendo esta pagina donde  aprenderás  ciertas estrategias de estudio para que así puedas aprobar tus cursos y mejorar en tus estudios.👇\n https://aliatuniversidades.com.mx/blog/index.php/7-metodos-de-estudio-que-puedes-aplicar-en-la-universidad/ \n\n ¿Quieres hacer otra consulta?",]
	],
	[
		r"2",
		[ " b. Sí el estudiante es desaprobado por segunda vez en la misma asignatura, sele hace saber que mantiene la condición de observado académicamente y sele asigna un docente tutor conforme al reglamento de actividad tutorial del estudiante..\n\n te recomiendo esta pagina donde  aprenderás  ciertas estrategias de estudio para que así puedas aprobar tus cursos y mejorar en tus estudios.👇\n https://aliatuniversidades.com.mx/blog/index.php/7-metodos-de-estudio-que-puedes-aplicar-en-la-universidad/ \n\n ¿Quieres hacer otra consulta?",]
	],
	[
		r"3",
		[ " c. Sí el estudiante es desaprobado por tercera vez en la misma asignatura, es suspendido un año académico. Es matriculado luego solo en la asignatura desaprobada,de ser desaprobado es separado automáticamente como estudiante de laEscuela Profesional respectiva. Esta separación no tiene carácterdisciplinario.\n\n te recomiendo esta pagina donde  aprenderás  ciertas estrategias de estudio para que así puedas aprobar tus cursos y mejorar en tus estudios.👇\n https://aliatuniversidades.com.mx/blog/index.php/7-metodos-de-estudio-que-puedes-aplicar-en-la-universidad/ \n\n ¿Quieres hacer otra consulta?",]
	],
	
	[
		r"Si",
		[ " ¿Qué tipo de consulta deseas realizar?\n Bajo Rendimiento \n Cursos \n Opcines Academicas",]
	],
	[
		r"No",
		[ " gracias!! Espero que toda la información que te brinde haya sido de mucha ayuda ,Suerte en tu vida academica 😉 \n\n Si tienes cualquier duda acerca de las tutorias , no dudes en hablarme \n\n estare esperando tu menasaje.... ",]
	],
    [
		r"Problemas Familiares",
		[ " te recomiendo asistir a nuestro taller de psicología; donde encontraras a los mejores especialistas 👨 que te podrán ayudar a resolver tus problemas.\n aqui podras sacar una cita👇 \n https://clinica-unsaac.innovarperu.com/ \n\n ¿Quieres hacer otra consulta?",]
	],
    # Cursos
	[
		r"Cursos",
		[ " aqui podras ver todos los cursos que te ofrece la carrera y los cursos que podras llevar dependiendo al semestre que estas cursando.\n 1.-Catalogo de cursos:http://ccomputo.unsaac.edu.pe/index.php?op=catalog&dt=vCvqh09qWpsFWhbF \n 2.-Malla curricular:http://www.unsaac.edu.pe/index.php/academico/pre-grado/academico-mallas-php \n\n ¿Quieres hacer otra consulta?",]
	],
	

    #opciones academicas
	[
		r"Opciones Academicas",
		[ "aqui te mostramos las sisguiente opcion: \n Perfil Profesional \n" ,]
	],
	[
		r"Perfil Profesional",
		[ " Aquí te muestro las siguientes opcines  en las que puedes ezpecializarte 👇 \n -> Ingenieria de software \n ->Inteligencia Artificial \n ->Ing. en computacion \n -> Area de ciencias de la computacion " ,]
	],
	[
		r"Ingenieria de software",
		[ " dentro del area de ing de software, \n se considera que el egresado Anliza, diseña, desarrolla y gestiona software en base a especificaciones del usuario.\n para mas informacion: 👇\n\n http://in.unsaac.edu.pe/home/  \n\n ¿Quieres hacer otra consulta?",]
	],
	[
		r"Inteligencia Artificial",
		[ " dentro del area de Inteligencia Artificial. \n se considera que el egresado  se desempeñe en areas de resolucion de problemas de IA, extraccion de conocimientos de informacion de datos, diseño de sistemas robotizados, implementar un sistema inteligente de vision artificial.\n para mas informacion: 👇\n\n http://in.unsaac.edu.pe/home/  \n\n ¿Quieres hacer otra consulta?",]
	],
	[
		r"Ingenieria en computacion",
		[ " dentro del area de ing computacion, \n se considera que el egresado implemente plataformas de hardware y software de sistema para dar soporte a soluciones de sistemas de informacion y TIC \n para mas informacion: 👇\n\n http://in.unsaac.edu.pe/home/  \n\n ¿Quieres hacer otra consulta?",]
	],
	[
		r"Area de ciencias de la computacion",
		[ " dentro del Area de ciencias de la computacion, \n se considera que el egresado implementa algoritmos para automatizar y optimizar procesos en las organizaciones \n utilizando conceptos y tecnologias  de ciencias computacion. \n para mas informacion: 👇\n\n http://in.unsaac.edu.pe/home/  \n\n ¿Quieres hacer otra consulta?",]
	],
	
	
]

#Función principal para iniciar con el chat bot
def chatear():
	print("¡Hola! Bienvenid@ soy tu asistente tutor! Yarvis 🤖.\n ¿Qué tipo de consulta deseas hacer ?\n Bajo Rendimiento \n Cursos \n Opciones Academicas ")
	chat = Chat(pares, mis_reflexions)
	chat.converse()
if __name__=="__main__":
	chatear()

chatear()
