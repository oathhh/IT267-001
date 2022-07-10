class JuiceOrder:

    def __init__(self,customer_name:str,menu:str,num = 1,size = '') -> None:
      self.customer_name = customer_name
      self.menu = menu
      self.num = num
      self.size = size
      self.price = 35

    def check_menu(self):
        menu_od = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,}

        if self.menu in menu_od:
            self.price = menu_od.get(self.menu)
    def compute_price(self):
        if self.size == 'R':
            self.price += 4
        else:
            self.price
        JuiceOrder.total = self.price*self.num
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} => {JuiceOrder.total}'
        
if __name__ == "__main__":
    od1 = JuiceOrder("WJ","(L *35)")
    od2 = JuiceOrder("OJ","(R *25)")
    od3 = JuiceOrder("PJ","(L *35)")
    
    print(od1.display_detail())
    print(od2.display_detail())
    print(od3.display_detail())

        

    