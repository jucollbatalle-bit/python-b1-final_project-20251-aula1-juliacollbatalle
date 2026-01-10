from util.file_manager import CSVFileManager
from orders.order import Order
from util.converter import CashierConverter, CustomerConverter, ProductConverter

    
class PrepareOrder:
    def __init__(self):
      self.file_manager = CSVFileManager()          # We initiate the code
      self.cashier_converter = CashierConverter()
      self.customer_converter = CustomerConverter()
      self.product_converter = ProductConverter()
      
      self.cashiers = []
      self.customers = []
      self.products = []
    
    def load_data(self):                            #We upload Cashiers, Customers and Products
      df_cashiers = self.file_manager.read('data/cashiers.csv')
      self.cashiers = self.cashier_converter.convert(df_cashiers, 'Cashier')
      print(f'Cashiers data has been succesfully uploaded: {len(self.cashiers)}')
      
      df_customers = self.file_manager.read('data/customers.csv')
      self.customers = self.customer_converter.convert(df_customers, 'Customer')
      print(f'Customers data has been succesfully uploaded: {len(self.customers)}')
      
      product_files = ['hamburgers', 'sodas', 'drinks', 'happyMeal']
      for product_type in product_files:
            path = f'data/{product_type}.csv'
            
            df_temp = self.file_manager.read(path)
            
            if not df_temp.empty:
                new_prods = self.product_converter.convert(df_temp, product_type)
                self.products.extend(new_prods)

      print('The system has been succesfully updated')
      
    def search_cashier(self, dni):
      for cashier in self.cashiers:
        if str(cashier.dni).strip() == str(dni).strip():
          return cashier
      return None
  
    def search_customer(self, dni):
      for customer in self.customers:
        if str(customer.dni).strip() == str(dni).strip():
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
          product_obj = next((product for product in self.products if str(product.id).strip() == str(product_id).strip()), None)

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

if __name__ == "__main__":
    app = PrepareOrder()
    app.load_data()      
    app.create_order()   


