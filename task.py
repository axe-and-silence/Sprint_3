import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


    @property
    def name_items(self):
        return self.__name_items
    

    @property
    def number_items(self):
        return self.__number_items


    def add_item_to_cheque (self,name):
        self.name = name
        if len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1


    def delete_item_from_check (self,name):
        self.name = name
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__number_items -= 1
            self.__name_items.remove(name)


    def check_amount (self):
        total=[]
        for item in self.__name_items:
            if item in self.__item_price:
                total.append(self.__item_price[item])
        
        sum_total = sum(total)
        if len(self.__name_items) > 10:
            return sum_total * 0.9
        else:
            return sum_total
 
       
    def twenty_percent_tax_calculation (self):
        total = []
        twenty_percent_tax = [
            item for item in self.__name_items if self.__tax_rate.get(item, 0) == 20
        ]
        
        for item2 in twenty_percent_tax:
            if item2 in twenty_percent_tax:
                total.append(self.__item_price[item2])

        sum_total = sum(total)
        if len(self.__name_items) > 10:
            return (sum_total * 0.9) * 0.2
        else:
            return sum_total * 0.2
        

    def ten_percent_tax_calculation (self):
        total = []
        ten_percent_tax = [
            item for item in self.__name_items if self.__tax_rate.get(item, 0) == 10
        ]
        
        for item2 in ten_percent_tax:
            if item2 in ten_percent_tax:
                total.append(self.__item_price[item2])

        sum_total = sum(total)
        if len(self.__name_items) > 10:
            return (sum_total * 0.9) * 0.1
        else:
            return sum_total * 0.1


    def total_tax(self):
        twenty_percent_tax_calculation = self.twenty_percent_tax_calculation()
        ten_percent_tax_calculation = self.ten_percent_tax_calculation() 
        if twenty_percent_tax_calculation is not None and ten_percent_tax_calculation is not None:
            total = ten_percent_tax_calculation + twenty_percent_tax_calculation
            return total
        else:
            return None


    @staticmethod    
    def get_telephone_number(telephone_number):
        try:
            num = int(telephone_number)
        except ValueError:
            raise ValueError('Необходимо ввести цифры')
    
        if len(str(num)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f'+7{num}'
