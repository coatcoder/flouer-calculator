from floUer import *
import streamlit as st

st.title('FloUer Калькулятор v1.1a')
get_flower()
names = []

# Ради всего святого оптимизируй, это занимает слишком много ресурсов и времени, может привести к ошибкам.

for key,value in data.items():
   names.append(key)

option = st.selectbox(options=names, label='Выберите цветы : ')

value = data.get(option)
st.write("Название : ", option)
if float(value) == 0.0:
   st.write("**Цена недоступна для данных цветов.**")
else:
   amount = st.number_input(min_value=10, step=10, label="Количество цветов : ")
   nacenka = st.number_input(min_value=0, max_value=100, step=1, label="Введите наценку : ")
   izn = float(value) * float(float(amount) / 10)
   itog = (float(value) + (float(value) / 100) * nacenka) * float(float(amount) / 10)
   st.write("Цена за 10 шт. : ", round(float(value),2), " руб.")
   st.write("Цена без наценки : ", round(izn,2), " руб.")
   st.write("**Цена с наценкой:**", round(itog,2), "**руб.**")


#data[option]