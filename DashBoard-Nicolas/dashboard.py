import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# Sidebar
df = pd.read_csv("DashBoard-Nicolas/ecommerce_sales.csv")

st.sidebar.title("🧭 Navegação")
page = st.sidebar.radio("Ir para:", ["🏠 Home", "🎓 Formação e 
Experiência", "🧑‍💻 Skills", "📊 Análise de Dados"])

# HOME
if page == "🏠 Home":
    st.title("👨‍💻 Nicolas Ferreira")
    st.subheader("Estudante de Engenharia de Software | FIAP | 4º Semestre")
    st.write("Bem-vindo ao meu Dashboard Profissional! 🚀")
    st.info("Objetivo: Atuar como Estagiário em Data Science, Engenharia de software e relacionaods, aplicando análise de dados e oque for necessário para resolver problemas reais do mercado.")

# FORMAÇÃO e EXPERIÊNCIA
elif page == "🎓 Formação & Experiência":
    st.header("🎓 Formação Acadêmica")
    st.write("- Engenharia de Software, FIAP, 4º semestre")

    st.header("📜 Certificações")
    st.write("- Comunicação efetiva e empática (Nestlé)")
    st.write("- Networking Academy Learn-A-Thon 2025 (Cisco)")

    st.header("💼 Experiências")
    st.write("- Projetos acadêmicos em Data Science e Python")
    st.write("- Participação em desafios de análise de dados")

# SKILLS
elif page == "🧑‍💻 Skills":
    st.header("🛠️ Skills Técnicas")
    st.success("- Python (Pandas, Numpy, Matplotlib, Seaborn, Streamlit)")
    st.success("- SQL (MySQL)")
    st.success("- Git, Github")
    st.success("- Análise Estatística")

    st.header("🤝 Soft Skills")
    st.info("- Comunicação, trabalho em equipe, resolução de problemas, adaptabilidade")

# ANÁLISE DE DADOS

elif page == "📊 Análise de Dados":
    st.header("📊 Análise de Dados - Vendas de E-commerce")

    st.subheader("1. Apresentação dos dados e tipos de variáveis")
    st.write(df.head())
    st.write("Tipos de variáveis:")
    st.write(df.dtypes)

    st.subheader("2. Medidas centrais, dispersão e correlação")
    st.write("Resumo estatístico:")
    st.write(df.describe())

    st.write("Matriz de correlação (apenas colunas numéricas):")
    st.write(df.select_dtypes(include=np.number).corr())

    fig, ax = plt.subplots()
    sns.histplot(df['Preço'], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Receita por Categoria")
    revenue_by_cat = df.groupby('Categoria')['Receita'].sum()
    st.bar_chart(revenue_by_cat)

    st.subheader("3. Intervalos de Confiança e Testes de Hipótese")
    mean_revenue = df['Receita'].mean()
    ci = stats.t.interval(0.95, len(df['Receita'])-1, loc=mean_revenue, scale=stats.sem(df['Receita']))
    st.write(f"Intervalo de confiança 95% da receita média: {ci}")

    cat_a = df[df['Categoria']=='A']['Receita']
    cat_b = df[df['Categoria']=='B']['Receita']
    t_stat, p_val = stats.ttest_ind(cat_a, cat_b, equal_var=False)
    st.write(f"T-test entre Categoria A e B: t={t_stat:.2f}, p={p_val:.4f}")
    if p_val < 0.05:
        st.success("Resultado: diferença significativa entre categorias A e B ✅")
    else:
        st.warning("Resultado: não há diferença significativa entre categorias A e B ❌")
