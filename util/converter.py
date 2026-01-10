from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter:
    def convert(self, dataFrame, entity_type) -> list:
        objects = []
        for _, row in dataFrame.iterrows():
            if entity_type == 'Cashier':
                objects.append(Cashier(str(row['dni']), row['name'], row['age'], row['timetable'], row['salary']))
            elif entity_type == 'Customer':
                objects.append(Customer(str(row['dni']), row['name'], row['age'], row['email'], row['postal_code']))
            elif entity_type == 'Hamburger':
                objects.append(Hamburger(row['id'], row['name'], row['price']))
            elif entity_type == 'Soda':
                objects.append(Soda(row['id'], row['name'], row['price']))
            # ... añadir Drink y HappyMeal igual
        return objects

    def print(self, object_list):
        for obj in object_list:
            if hasattr(obj, 'describe'): print(obj.describe())
            else: print(f"Producte - Tipus: {obj.type()}, Nom: {obj.name}, Id: {obj.id}, Preu: {obj.price}")