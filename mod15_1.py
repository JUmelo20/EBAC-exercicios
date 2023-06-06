import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import datetime
import base64

# 1. Título da aplicação
st.title("Minha Aplicação Streamlit")

# 2. Texto explicativo
st.write("Bem-vindo à minha aplicação!")

# 3. Entrada de texto
name = st.text_input("Digite seu nome")

# 4. Botão
if st.button("Enviar"):
    st.write(f"Olá, {name}!")

# 5. Checkbox
option = st.checkbox("Mostrar imagem")
if option:
    st.image("imagem.png", caption="Imagem de exemplo")

# 6. Selectbox
animal = st.selectbox("Selecione um animal", ["Cachorro", "Gato", "Pássaro"])
st.write("Você selecionou:", animal)

# 7. Slider
age = st.slider("Selecione sua idade", 0, 100, 25)
st.write("Sua idade é:", age)

# 8. Gráfico de linha
chart_data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
st.line_chart(chart_data)

# 9. Gráfico de barras
bar_data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
st.bar_chart(bar_data)

# 10. Mapa
map_data = pd.DataFrame({"lat": [37.7749, 34.0522], "lon": [-122.4194, -118.2437]})
st.map(map_data)

# 11. Tabela de dados
table_data = pd.DataFrame({"Nome": ["João", "Maria", "José"], "Idade": [20, 25, 30]})
st.table(table_data)

# 12. Texto formatado
st.markdown("Este é um texto em **negrito**.")

# 13. Data e hora
current_time = st.text("Aguardando data e hora...")
st.write("A data e hora atual é:", datetime.datetime.now())
current_time.empty()

# 14. Sidebar
st.sidebar.title("Opções")
option = st.sidebar.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])
st.sidebar.write("Você selecionou:", option)

# 15. Expander
with st.expander("Veja mais"):
    st.write("Conteúdo expandido")

# 16. Cache
@st.cache_data()
def expensive_computation(a, b):
    result = a ** b
    return result

result = expensive_computation(2, 3)
st.write("Resultado:", result)

# 17. Arquivo para download
data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
csv = data.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Baixar CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# 18. Inserção de código
code = '''def hello():
    print("Olá, mundo!")'''
st.code(code, language="python")

# 19. Inserção de vídeo
gif_file = 'AccurateDependentAmmonite-max-1mb.gif'
gif = open(gif_file, "rb").read()

# 20. Exibe o GIF na aplicação
st.image(gif)
