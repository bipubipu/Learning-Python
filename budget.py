class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        return self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        entries = ''
        for entry in self.ledger:
            entries += f"{entry['description'][0:23]:23}{entry['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance() :.2f}"
        return title + entries + total


def get_expense(category):
    expense = 0
    for entry in category.ledger:
        if entry['amount'] < 0:
            expense -= entry['amount']
    return expense


def create_spend_chart(categories):

    chart = 'Percentage spent by category\n'
    expenses = sum(get_expense(category) for category in categories)
    percentages = list(
        map(lambda i: int(get_expense(i)/expenses // 0.01), categories))

    # print out numbers
    for n in range(100, -1, -10):
        chart += f"{n:>3}| "
        for percentage in percentages:
            if percentage >= n:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # print out labels
    max_length = max(map(lambda x: len(x.name), categories))
    for i in range(max_length):
        chart += '     '
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  '
            else:
                chart += '   '
        chart += '\n'
    return chart.rstrip() + '  '
