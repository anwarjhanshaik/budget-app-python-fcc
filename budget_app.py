class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    #str method 
    def __str__(self):
        title = str(self.name).center(30, "*")
        output_string = ""
        for individual_dict in self.ledger:
            output_string += f"{individual_dict['description'][:23]}".ljust(23)+f"{individual_dict['amount']:.2f}".rjust(7)+"\n"
        total_balance = sum([individual_dict["amount"] for individual_dict in self.ledger])
        return f"{title}\n{output_string}Total: {total_balance}"
        
    #deposit method 
    def deposit(self, amount, description = ""):
        transition = {'amount' : amount, 'description' : description}
        self.ledger.append(transition)

    #check_funds method 
    def check_funds(self, amount):
        current_balance = sum([individual_dict["amount"] for individual_dict in self.ledger])
        if amount > current_balance:
            return False
        else:
            return True
    
    #withdraw method 
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            debitation = {'amount' : amount * -1, 'description' : description}
            self.ledger.append(debitation)
            return True
        else:
            return False
    
    #get_balance
    def get_balance(self):
        current_balance = sum([individual_dict["amount"] for individual_dict in self.ledger])
        return current_balance
    
    #transfer method 
    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

def create_spend_chart(categories):
  title = "Percentage spent by category"
  category_totals = []
  for obj in categories: #looping through each object
    current_category_spent = 0
    for individual_dict in obj.ledger: #looping through each objects ledger
      if individual_dict['amount'] < 0:
        current_category_spent += abs(individual_dict['amount'])
    category_totals.append(current_category_spent)
  
  grand_total = sum(category_totals)
  percentages = [int(amount / grand_total * 100) // 10 * 10 for amount in category_totals]
  
  chart_string = ""
  for i in range(100, -1, -10):
    chart_string += str(i).rjust(3) + "| "
    for amount in percentages:
        if i <= amount:
          chart_string += "o  "
        else:
          chart_string += "   "
    chart_string += "\n"
  
  bars = "    "
  for obj in category_totals:
      bars += "---"
  bars += "-"

  max_length = max(len(obj.name) for obj in categories)
  output_name = ""
  for i in range(max_length):
      output_name += "     "
      for obj in categories:
          if i < len(obj.name):
              output_name += obj.name[i] + "  "
          else:
              output_name += "   "
      if i < max_length - 1:
        output_name += "\n"
  return f"{title}\n{chart_string}{bars}\n{output_name}"

print(create_spend_chart([food, clothing]))
