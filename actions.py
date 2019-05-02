# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import psycopg2
import re
import time

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionHour(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_hora"

    def run(self, dispatcher, tracker, domain):
        hour = time.strftime("%H:%M:%S") + " "
        dispatcher.utter_message(hour)
        return []

class ActionDay(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_dia"

    def run(self, dispatcher, tracker, domain):
        fecha = time.strftime("%A/%d/%B/%Y") + " "
        fecha2 = fecha.split("/")
        dia = fecha2[0]
        dian = fecha2[1]
        mes = fecha2[2]
        anyo = fecha2[3]
        dia = dia.upper()
        if dia == "MONDAY":
            dia = "Lunes"
        elif dia == "TUESDAY":
            dia = "Martes"
        elif dia == "WEDNESDAY":
            dia = "Miercoles"
        elif dia == "THURSDAY":
            dia = "Jueves"
        elif dia == "FRIDAY":
            dia = "Viernes"
        elif dia == "SATURDAY":
            dia = "Sabado"
        elif dia == "SUNDAY":
            dia = "Domingo"

        mes = mes.upper()
        if mes == "JANUARY":
            mes = "Enero"
        elif mes == "FEBRUARY":
            mes = "Febrero"
        elif mes == "MARCH":
            mes = "Marzo"
        elif mes == "APRIL":
            mes = "Abril"
        elif mes == "MAY":
            mes = "Mayo"
        elif mes == "JUNE":
            mes = "Junio"
        elif mes == "JULY":
            mes = "Julio"
        elif mes == "AUGUST":
            mes = "Agosto"
        elif mes == "SEPTEMBER":
            mes = "Septiembre"
        elif mes == "OCTOBER":
            mes = "Octubre"
        elif mes == "NOVEMBER":
            mes = "Noviembre"
        elif mes == "DICEMBER":
            mes = "Diciembre"

        fecha = "Hoy es " + dia + " " + dian + " de " + mes + " del " + anyo

        dispatcher.utter_message(fecha)
        return []

class ActionAnswer(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_answerbd"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.get_slot('action_answerbd')
        name = tracker.get_slot('name')
        conn = psycopg2.connect("dbname='rasa_prueba' user='postgres' host='localhost' password='root'")
        cur = conn.cursor()

        if answer != "":
            cur.execute("SELECT contenido from answers where id =" + answer + ";")
            rows = cur.fetchall()
            for x in rows:
                answer = x[0]
        else:
            return []

        ''' 
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="prueba_rasa")
        answer = tracker.get_slot('action_answerbd')

        mycursor = mydb.cursor()
        mycursor.execute("SELECT contenido FROM answers WHERE id_answer = 1")

        myresult = mycursor.fetchall()

        for x in myresult:
            answer = x[0]
        '''
        dispatcher.utter_message(answer)

        return []

class ActionHNC(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_hncbd"

    def run(self, dispatcher, tracker, domain):
        hnc = tracker.get_slot('action_hncbd')
        conn = psycopg2.connect("dbname='rasa_prueba' user='postgres' host='localhost' password='root'")
        cur = conn.cursor()

        if hnc != "":
            hnc = str(hnc)
            hnc = hnc.upper()
            if 'ES' in hnc:
                hncreg = re.findall(r'[E]{1}[S]{1}[-]{1}\d{6}', hnc)
                try:
                    hncreg = hncreg[0]
                    hncreg3 = hncreg[3:]
                    if hncreg == hnc and int(hncreg3) >= 100000 and int(hncreg3) <= 999999:
                        cur.execute("SELECT contenido from incidencias where hnc ='" + hncreg + "';")
                        rows = cur.fetchall()
                        if rows != []:
                            for x in rows:
                                hnc = x[0]
                        else:
                            hnc = "Incidencia valida pero no encontrada en la base de datos"
                    else:
                        hnc = "Eso no es una incidencia valida machote"
                except Exception as e:
                    hnc = "Eso no es una incidencia valida machote"
            elif 'FR' in hnc:
                hncreg2 = re.findall(r'[F]{1}[R]{1}[-]{1}\d{6}', hnc)
                try:
                    hncreg2 = hncreg2[0]
                    hncreg4 = hncreg2[3:]
                    if hncreg2 == hnc and int(hncreg4) >= 100000 and int(hncreg4) <= 999999:
                        cur.execute("SELECT contenido from incidencias where hnc ='" + hncreg2 + "';")
                        rows = cur.fetchall()
                        if rows != []:
                            for x in rows:
                                hnc = x[0]
                        else:
                            hnc = "Incidencia valida pero no encontrada en la base de datos"
                    else:
                        hnc = "Eso no es una incidencia valida machote"
                except Exception as e:
                    hnc = "Eso no es una incidencia valida machote"
        else:
            hnc = "Eso no es una incidencia valida machote"
            return []

        dispatcher.utter_message(hnc)

        return []

class ActionHNCERCOBS(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_incidencia"

    def run(self, dispatcher, tracker, domain):
        inci = tracker.get_slot('action_incidencia')
        cod = tracker.get_slot('cod_action')
        conn = psycopg2.connect("dbname='rasa_prueba' user='postgres' host='localhost' password='root'")
        cur = conn.cursor()

        if "hnc" in inci:
            hnc = inci
            hnc = str(hnc)
            hnc = hnc.upper()
            if 'HNC' in hnc:
                try:
                    if int(cod) >= 2000000000 and int(cod) <= 3999999999:
                        cur.execute("SELECT contenido from hnc where hnc ='" + cod + "';")
                        rows = cur.fetchall()
                        if rows != []:
                            for x in rows:
                                inci = x[0]
                        else:
                            inci = "Incidencia hnc valida pero no encontrada en la base de datos"
                            return []
                    else:
                        inci = "Eso no es una incidencia valida machote1"
                        return []
                except Exception as e:
                    inci = "Eso no es una incidencia valida machote2"
                    return []
        elif "obs" in inci:
            obs = inci
            obs = str(obs)
            obs = obs.upper()
            if 'OBS' in obs:
                try:
                    if int(cod) >= 4000000000 and int(cod) <= 5999999999:
                        cur.execute("SELECT contenido from obs where obs ='" + cod + "';")
                        rows = cur.fetchall()
                        if rows != []:
                            for x in rows:
                                inci = x[0]
                        else:
                            inci = "Incidencia obs valida pero no encontrada en la base de datos"
                            return []
                    else:
                        inci = "Eso no es una incidencia valida machote1"
                        return []
                except Exception as e:
                    inci = "Eso no es una incidencia valida machote2"
                    return []
        elif "erc" in inci:
            erc = inci
            erc = str(erc)
            erc = erc.upper()
            if 'ERC' in erc:
                try:
                    cod = cod.upper()
                    cod = cod.replace(" ", "")
                    cur.execute("SELECT contenido from erc where erc ='" + cod + "';")
                    rows = cur.fetchall()
                    if rows != []:
                        for x in rows:
                            inci = x[0]
                    else:
                        inci = "Incidencia erc valida pero no encontrada en la base de datos"
                        return []
                except Exception as e:
                    inci = "Eso no es una incidencia valida machote2"
                    return []
        else:
            inci = "Eso no es una incidencia valida machote3"
            return []

        dispatcher.utter_message(inci)

        return []