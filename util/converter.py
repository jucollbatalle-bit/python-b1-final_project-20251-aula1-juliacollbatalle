from abc import ABC, abstractmethod

import pandas as pd

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    list_cashiers = []
    for _, row in dataFrame.iterrows():
      list_cashiers.append(row.to_dict())
      return list_cashiers
    pass

class CustomerConverter(Converter):
  def convert(self,dataFrame,*args) -> list:
    list_users = []
    for _, row in dataFrame.iterrows():
      list_users.append(row.to_dict())
    return list_users
  pass

class ProductConverter(Converter):
  def convert(self, dataFrame: pd.DataFrame, *args) -> list:
    list_products = []
    for _, row in dataFrame.iterrows():
      list_products.append(row.to_dict())
    return list_products
  pass