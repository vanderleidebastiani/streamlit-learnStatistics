import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

rng = np.random.default_rng()

st.sidebar.subheader("Estatísticas descritivas")

dist = st.sidebar.selectbox("Números", ["Inteiros", "Contínuos"])

n = st.sidebar.number_input(
    "Tamanho da amostra",
    min_value=int(1),
    max_value=int(1000),
    value=int(10),
    step=int(1),
)

st.sidebar.subheader("Parâmetros")
if dist == "Contínuos":
    loc = rng.uniform() * 100
    sca = rng.uniform() * 10
    sample = rng.normal(loc=loc, scale=sca, size=n)
    sample = sample.round(2)
else:  # dist == "Inteiros"
    lam = rng.uniform() * 10
    sample = rng.poisson(lam=lam, size=n)

run = st.sidebar.button("Amostrar")

if run:
    st.subheader("Números amostrados")
    fig = plt.figure(1)
    plt.hist(sample, ec="silver", fc="teal")
    plt.xlabel("Valores amostrados")
    plt.ylabel("Frequência")
    col1, col2 = st.columns([0.3, 0.7])
    col1.text(sample)
    col2.pyplot(plt)
    st.subheader("Estatísticas descritivas")
    v1 = np.mean(sample)
    v2 = np.std(sample)
    v3 = np.median(sample)
    st.caption("Média = " + str(v1.round(2)))
    st.caption("Desvio padrão = " + str(v2.round(2)))
    st.caption("Mediana = " + str(v3.round(2)))
