import pandas as pd
from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
    @abstractmethod
    def convert(self, dataFrame: pd.DataFrame, entity_type: str):
        pass

    def print(self, objects_list):
        for obj in objects_list:
            if hasattr(obj, 'describe'):
                print(obj.describe())
            else:
                print(f"Producte - ID: {obj.id}, Nom: {obj.name}, Preu: {obj.price}€")

class CashierConverter(Converter):
    def convert(self, dataFrame, entity_type):
        cashiers = []
        for _, row in dataFrame.iterrows():
            cashiers.append(Cashier(row['dni'], row['name'], row['age'], row['timetable'], row['salary']))
        return cashiers

class CustomerConverter(Converter):
    def convert(self, dataFrame, entity_type):
        customers = []
        for _, row in dataFrame.iterrows():
            customers.append(Customer(row['dni'], row['name'], row['age'], row['email'], row['postalcode']))
        return customers

class ProductConverter(Converter):
    def convert(self, dataFrame, entity_type):
        products = []
        for _, row in dataFrame.iterrows():
            # Depenent de l'entity_type (nom del fitxer), creem un objecte o un altre
            if entity_type == 'hamburgers':
                products.append(Hamburger(row['id'], row['name'], row['price']))
            elif entity_type == 'sodas':
                products.append(Soda(row['id'], row['name'], row['price']))
            elif entity_type == 'drinks':
                products.append(Drink(row['id'], row['name'], row['price']))
            elif entity_type == 'happyMeal':
                products.append(HappyMeal(row['id'], row['name'], row['price']))
        return products