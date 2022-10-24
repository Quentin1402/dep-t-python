import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot

attackers = pd.read_csv('men_best_attackers.csv')
attackers.rename(columns={"Faults": "FaultsSpike"}, inplace=True)
attackers.rename(columns={"Total attempts": "Total_attempts_spike"}, inplace=True)
attackers.drop(["Rank", "ShirtNumber"], axis = 1, inplace=True)
attackers["Success"] = attackers["Spikes"] / attackers["Total_attempts_spike"]

attackers

fig = sb.catplot(x='Success', data=attackers, kind='box', height=8)
st.pyplot(fig)

fig = sb.catplot(x='Success', data=attackers.query("Success < 0.6 & Success > 0.2"), kind='box', height=8)
st.pyplot(fig)

fig = sb.catplot(x="Team", y="Success", data= attackers.query("Success < 0.6 & Success > 0.2"), kind="bar", height=10)
st.pyplot(fig)

attackers["Fail"] = attackers["FaultsSpike"] / attackers["Total_attempts_spike"]
fig = sb.catplot(x="Team", y="Fail", data= attackers.query("Fail < 0.35"), kind="bar", height=10)
st.pyplot(fig)

servers = pd.read_csv('men_best_servers.csv')
servers.rename(columns={"Faults": "FaultsServe"}, inplace=True)
servers.rename(columns={"Total attempts": "Total_attempts_serve"}, inplace=True)
servers.drop(["Rank", "ShirtNumber"], axis = 1, inplace=True)

servers

servers["Success"] = servers["Aces"] / servers["Total_attempts_serve"]
servers["Fail"] = servers["FaultsServe"] / servers["Total_attempts_serve"]

fig = sb.relplot(x="FaultsServe", y="Total_attempts_serve", data=servers.query("Total_attempts_serve > 25"), height=10)
st.pyplot(fig)

scores = pd.read_csv('men_best_scores.csv')
scores.drop(["Rank", "ShirtNumber"], axis = 1, inplace=True)
scores["Point_all"] = attackers["Success"] + servers["Success"]
scores["Fault_all"] = attackers["Fail"] + servers["Fail"]
scores["Result"] = scores["Point_all"] - scores["Fault_all"]
fig = sb.catplot(x="Team", y="Result", data= scores, kind="bar", height=10)
st.pyplot(fig)