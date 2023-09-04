import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

rng = np.random.default_rng()

st.sidebar.subheader("Distribuição de probabilidades")
dist = st.sidebar.selectbox("Distribuição", ["Gaussiana (Normal)", 
                                      "Log-Normal",
                                      "Gamma",
                                      "Binomial",
                                      "Exponencial",
                                      "Binomial negativa",
                                      "Poisson"])

n = st.sidebar.number_input("Tamanho da amostra", min_value=int(1), max_value=int(100000), value=int(1000), step=int(100))

st.sidebar.subheader("Parâmetros")
if dist == "Gaussiana (Normal)":
    m = st.sidebar.number_input("Média", value=float(0), step = float(1))
    sd = st.sidebar.number_input("Desvio padrão", min_value=float(0), value=float(1), step = float(1))
    sample = rng.normal(loc = m, scale = sd, size = n)
elif dist == "Log-Normal":
    m = st.sidebar.number_input("Média (log)", min_value=float(0) , value=float(1), step=float(0.5))
    sd = st.sidebar.number_input("Desvio padrão (log)", min_value=float(0), max_value=float(100), value=float(1), step = float(0.5))
    sample = rng.lognormal(mean = m, sigma = sd, size = n)
elif dist == "Gamma":
    sha = st.sidebar.number_input("Forma (k)", min_value=float(0) , value=float(1), step=float(0.5))
    sca = st.sidebar.number_input("Escala (theta)", min_value=float(0), max_value=float(100), value=float(1), step = float(0.5))
    sample = rng.gamma(shape = sha, scale=sca, size = n)
elif dist == "Binomial":
    nn = st.sidebar.number_input("Tentativas (n)", min_value=float(0) , value=float(1), step=float(1))
    pro = st.sidebar.number_input("Probabilidade (p)", min_value=float(0), max_value=float(1), value=float(0.5), step = float(0.01))
    sample = rng.binomial(n=nn, p = pro, size = n)
elif dist == "Exponencial":
    sca = st.sidebar.number_input("Escala", min_value=float(0), max_value=float(100), value=float(1), step = float(0.5))
    sample = rng.exponential(scale=sca, size = n)
elif dist == "Binomial negativa":
    nn = st.sidebar.number_input("Tentativas (n)", min_value=float(0) , value=float(1), step=float(1))
    pro = st.sidebar.number_input("Probabilidade (p)", min_value=float(0), max_value=float(1), value=float(0.5), step = float(0.01))
    sample = rng.negative_binomial(n = nn, p = pro, size = n)
else: # dist == "Poisson"
    lam = st.sidebar.number_input("Lambda", min_value=float(0), value=float(5), step=float(0.5))
    sample = rng.poisson(lam=lam, size = n)

run = st.sidebar.button("Amostrar")

if run:
    fig=plt.figure(1)
    plt.hist(sample, ec="silver", fc="teal")
    plt.title("Distribuição " + dist, weight = "bold", loc="left")
    plt.xlabel("Valores amostrados")
    plt.ylabel("Frequência")
    st.pyplot(plt)
