import pandas as pd
import matplotlib.pyplot as plt


def gold_prices():    # график цены золота коорд. цена/кг-год
    pd_data = pd.read_csv('annual.csv')
    plt.bar(pd_data['Date'], pd_data['Price'], color=['blue', 'red', 'green'], width=0.8)
    plt.title('Gold price throughout time')
    plt.xlabel('x - year')
    plt.ylabel('y - price per kilo (dollars)')
    plt.show()


def death_from_guns():   # график (диограмма) смертей от огнестрельного оружия в америке (хз какой год и штат)
    pd_data = pd.read_csv('gun_deaths.csv')
    data = {}
    for intent in pd_data['intent']:
        if intent in data:
            data[intent] += 1
        else:
            data[intent] = 1
    plt_data = pd.Series(data)
    plt.pie(plt_data, labels=plt_data.index)
    plt.show()