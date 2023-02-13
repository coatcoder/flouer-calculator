from floUer import *
import streamlit as st


st.title('FloUer Калькулятор v1.1a')


get_flower()
names = []

# Ради всего святого оптимизируй, это занимает слишком много ресурсов и времени, может привести к ошибкам.
# Еще раз напоминаю себе о переработке алгоритма в более удобную структуру.

for key,value in data.items():
   names.append(key)

option = st.selectbox(options=names, label='Выберите цветы : ')

value = data.get(option)
st.write("Название : ", option)
if float(value) == 0.0:
   st.write("**Цена недоступна для данных цветов.**")
else:
   amount = st.number_input(min_value=1, step=1, label="Количество цветов (в 10 шт.) : ")
   nacenka = st.number_input(min_value=0, max_value=100, step=1, label="Введите наценку (в %): ")
   izn = float(value) * float(float(amount))
   itog = (float(value) + (float(value) / 100) * nacenka) * float(float(amount))
   pribil = itog - izn
   rentabel = float(pribil / izn * 100)

   st.write("Цена за 10 шт. : ", round(float(value),2), " руб.")
   st.write("Цена без наценки : ", round(izn,2), " руб.")
   st.write("**Цена с наценкой :**", round(itog,2), "**руб.**")
   st.write("**Прибыль :**", round(pribil, 2), "**руб.**")
   st.write("**Рентабельность :**", round(rentabel), "**%**")

#data[option]