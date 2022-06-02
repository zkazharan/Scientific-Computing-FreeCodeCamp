class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    title = self.name.center(30, '*') + '\n'
    detail = ''
    total = 0
    for each in self.ledger:
      crop_desc = each['description'][0:23]
      detail += crop_desc
      
      len_rest = 30 - len(crop_desc)
      if not '.' in str(each['amount']):
        crop_amount = (str(each['amount']) + '.00').rjust(len_rest)
      else:
        crop_amount = (str(each['amount'])).rjust(len_rest)
        
      detail += crop_amount + '\n'

      total += each['amount']

    total = 'Total: ' + str(total)
      
    output = title + detail + total

    return output

  def deposit(self, amount, description = ''):
    self.ledger.append({'amount' : amount, 'description' : description})

  def withdraw(self, amount, description = ''):
    if(self.check_funds(amount)):
      self.ledger.append({'amount' : -amount, 'description' : description})
      return True
    return False

  def get_balance(self):
    total = 0
    for each in self.ledger:
      total += each['amount']

    return total

  def transfer(self, amount, category):
    if(self.check_funds(amount)):
      self.withdraw(amount, 'Transfer to ' + category.name)
      category.deposit(amount, 'Transfer from ' + self.name)
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def total_ctg_withdraw(self):
    total = 0
    for each in self.ledger:
      if each['amount'] < 0:
        total += -each['amount']
    return total

  def get_rounded_percentage(self, categories):
    percentage = self.total_ctg_withdraw() / total_withdraw(categories) * 100
    self.rounded = (percentage // 10) * 10
    return self.rounded

  def get_o(self, categories):
    self.o_list = list()
    slot = int(self.get_rounded_percentage(categories) / 10)

    for each in range(slot + 1):
      self.o_list.append('o')
      
    for each in range(11 - slot):
      self.o_list.append(' ')

    return self.o_list

def total_withdraw(categories):
    total = 0
    for ctg in categories:
      total += ctg.total_ctg_withdraw()
    return total

def run_all(categories):
  total_withdraw(categories)
  for ctg in categories:
    ctg.get_rounded_percentage(categories)
    ctg.get_o(categories)
  
def create_spend_chart(categories):
  run_all(categories)
  
  output = 'Percentage spent by category\n'
  i = 100

  while i >= 0:
    output += str(i).rjust(3) + '| '
    for ctg in categories:
      output += ctg.o_list[int((i/10))] + '  '
    output += '\n'

    i -= 10

  output += '    -'
  for i in range(len(categories)):
    output += '---'
  output += '\n'

  maxlen = -1
  for ctg in categories:
    if len(ctg.name) > maxlen:
      maxlen = len(ctg.name)

  index = 0
  for line in range(maxlen):
    output += '     '
    for ctg in categories:
      try:
        output += ctg.name[index] + '  '
      except:
        output += '   '
    index += 1

    if not index == maxlen:
      output += '\n'
  
  return output