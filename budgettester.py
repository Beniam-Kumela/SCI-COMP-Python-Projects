class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()
    
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output
    

  def deposit(self, amount, description = ""):
    
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
      
  def get_balance(self):
    
    total_cash = 0
    for item in self.ledger:
      total_cash += item["amount"]
    return total_cash

  def transfer(self, amount, category):
    
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    
    if self.get_balance() >= amount:
      return True
    return False
    
def create_spend_chart(categories):
    graph = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    return graph


        


        
      
  
  