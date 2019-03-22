## story_saludo
* saludo <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_nombre <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_adios
* adios
 - utter_adios

## story_gracias
* gracias
 - utter_gracias
 
## story_nombre
* nombre{"name":"Sam"}
 - utter_saludo

## story_action_answerbd
* action_answerbd{"action_answerbd": "primera respuesta"}
 - action_answerbd
 - slot{"action_answerbd": "primera respuesta"}

## story_action_hncbd
* action_hncbd{"action_hncbd": "Esta es la incidencia ES-123456"}
 - action_hncbd
 - slot{"action_hncbd": "Esta es la incidencia ES-123456"}

## story_afirmar
* afirmar
 - utter_afirmar

## story_adiosbro
* adiosbro
 - utter_adiosbro

## story_graciasbro
* graciasbro
 - utter_graciasbro
 
## story_saludobro
* saludobro
 - utter_nombre

## story_afirmarbro
* afirmarbro
 - utter_afirmarbro

## story_siguiente_operacion
* siguiente_operacion
 - utter_siguiente_operacion
