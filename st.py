from floUer import *
import streamlit as st

#1.3:
# Pandas support
# floUer_multi support


pg_nums = count_pages_opt_fp_ru()
st.title('FloUer Калькулятор v1.3 (Experimental)')
page_selected = st.slider('Страница сайта', 1, pg_nums[-1], 1)

names = []
data = get_flower_opt_fp_ru(page_selected)
for key, value in data.items():
    names.append(key)
option = st.selectbox(options=names, label='Выберите цветы : ')
value = data.get(option)
st.write("**ВНИМАНИЕ!** Выбор количества цветов на добработке из-за разной кратности закупочного количества цветов.")
if float(value) == 0.0:
    st.write("**Цена недоступна для данных цветов.**")
else:
    amount = st.number_input(min_value=1, step=1, label="Количество цветов (в шт.) : ")  #Добавить проверку кратности цветов. (Т.к по умолчанию - 10)
    nacenka = st.number_input(min_value=0, max_value=100, step=1, label="Введите наценку (в %): ")
    izn = float(value) * float(float(amount))
    itog = (float(value) + (float(value) / 100 * nacenka)) * float(amount)
    pribil = itog - izn
    rentabel = float(pribil / izn * 100)

    st.write("Цена одного цветка : ", round(float(value), 2), " руб.")
    st.write("Закупочная цена : ", round(izn, 2), " руб.")
    st.write("**Цена продажи :**", round(itog, 2), "**руб.**")
    st.write("**Прибыль :**", round(pribil, 2), "**руб.**")

