# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import mysql.connector
from rasa_core_sdk.events import SlotSet
import psycopg2
import re

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