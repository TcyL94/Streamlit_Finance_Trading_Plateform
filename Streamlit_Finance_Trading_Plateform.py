import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import datetime


page = st.sidebar.radio("Choose your page", ["Users", "Infos", "Historique"]) 

if page == "Users":
	st.title("Information utilisateur")
	nom = st.text_input('Nom')
	prenom = st.text_input('Prénom')
	capital = st.text_input('Capital')
	date = st.date_input('Date de création du compte', datetime.date(2022, 1, 1))

	get_data = []

	if st.button("Sauvegarder"):
		info_user = pd.DataFrame({"Nom": [nom], "Prenom": [prenom], "Capital": [capital], "Date": [date]})

	save_user = info_user.to_csv("/Users/macbookair/Desktop/COURS_M2/Python/Streamlit_Finance_Trading_Plateform/info_users.csv", index=True)


elif page == "Infos":
	st.title("Saisie du Ticker")
	ticker = st.text_input('Ticker', '')
	date_debut = st.date_input('Date de début de cotation', datetime.date(2021, 1, 1))
	date_fin = st.date_input('Date de fin de cotation', datetime.date(2022, 1, 1))
	dataa = web.DataReader(ticker, data_source = "yahoo", start = date_debut, end = date_fin)
	radio = st.radio("Ajouter un ou plusieurs cours", ('Cours unique', 'Multiple cours'))
	st.table(dataa)

	info_ticker = pd.DataFrame({"Ticker": [ticker], "Date debut": [date_debut], "Date fin": [date_fin]})
	save_ticker = info_ticker.to_csv("/Users/macbookair/Desktop/COURS_M2/Python/Streamlit_Finance_Trading_Plateform/info_data.csv", index=True)

else:
	st.title("Liste des utilisateurs et historique des transactions")

	ddd = {"Nom": nom, "Prénom": prenom, "Date de passage à l'ordre": date_fin, "Action choisie": ticker, "Quantité" : "None", "Valeur de la transaction" : ""}
	infos_data = pd.DataFrame(ddd)
	st.write(infos_data)

	user = pd.read_csv("/Users/macbookair/Desktop/COURS_M2/Python/Streamlit_Finance_Trading_Plateform/info_users.csv")
	st.write(user)
