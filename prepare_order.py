
from orders.order import Order
from products import*
from users import *
from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter

    
class PrepareOrder:
 def __init__(self):
  #We initialize data lists 
  self.file_manager = CSVFileManager()
  self.converter = Converter()
  self.cashiers = []
  self.customers = []
  self.products = []

 def load_data(self):
  #We update Cashiers
  df_cashiers = self.file_manager.read('data/cashiers.csv')
  self.cashiers = self.converter.convert(df_cashiers, 'Cashier')

  #We update Customers
  df_customers = self.file_manager.read('data/customers.csv')
  self.customers = self.converter.convert(df_customers, 'Customer')

  #We update Products
  df_products = self.file_manager.read('data/products.csv')
  self.products = self.converter.convert(df_products, 'Products')

  print('The system has been succesfully updated')

  def search_cashier(self, dni):
   for cashier in self.cashiers:
    if cashier.dni == dni:
     return cashier
   return None
  
  def search_customer(self, dni):
   for customer in self.customers:
    if customer.dni == dni:
     return customer
   return None
  
  def create_order(self):
   dni_cashier = input('Introduce the cashiers DNI')
   cashier = self.search_cashier(dni_cashier)
   
   dni_customer = input('Introduce customers DNI')
   customer = self.search_customer(dni_customer)

   if cashier and customer:
    order = Order(cashier, customer)

    print("\nList of available products:")
    for product in self.products:
     print(f'ID: {product.id} - {product.name} ({product.price}€)')

     adding = True
     while adding:
      product_id = input('Introduce the identification of the product')
      product_obj = next((product for product in self.products if product.id == product_id), None)

      if product_obj:
       order.add(product_obj)
       print(f'Added: {product_obj.name}')
      else:
       print('Product not found')

      resp = input('Do you want to add any other product? (Yes/No): ').lower()
      if resp != 'yes':
          adding = False 
     print ('\n--- ORDERS RESUMEE ---')
     order.show()
   else:
     print('Error: Cashier or Client not found.')
 pass

