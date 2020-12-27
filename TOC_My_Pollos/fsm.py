from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url

import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_show_fsm(self, event):
        text = event.message.text

        return text.lower() == 'fsm'

    def on_enter_show_fsm(self, event):
        print("I'm entering fsm")

        reply_token = event.reply_token
        send_image_url(reply_token, 'https://img.onl/UtUh70')  

    def is_going_to_eat(self, event):
        text = event.message.text

        if text.find("餓") != -1:
            return True
        return False

    def on_enter_eat(self, event):
        print("I'm entering eat")

        reply_token = event.reply_token
        send_text_message(reply_token, "想吃一般的還是來一點高檔的呢?\n請輸入「銅板美食」或「高檔餐廳」")
        # self.go_back()

    def is_going_to_drink(self, event):
        text = event.message.text

        if text.find("渴") != -1:
            return True
        return False

    def on_enter_drink(self, event):
        print("I'm entering drink")

        drink = ['御私藏-小野狼', '御私藏-芒果青茶', '迷客夏-青檸香茶', '迷客夏-大正紅茶拿鐵', '白巷子-紅茶奶蓋', '50嵐-八冰綠', '茶湯會-鐵觀音拿鐵']
        reply_token = event.reply_token
        send_text_message(reply_token, '幫您選擇\n\n' + drink[random.randint(0,6)]  + '\n\n祝您用餐愉快，歡迎再次使用!')      

    def is_going_to_big(self, event):
        text = event.message.text
        if text == '高檔餐廳':
            return True
        return False

    def on_enter_big(self, event):
        print("I'm entering big")

        food = ['一番地', '花葵壽喜燒', '築間', 'SHOJO', '七輪', '老四川', 'WOOSA', '陶板屋']
        reply_token = event.reply_token
        send_text_message(reply_token, '幫您選擇\n\n' + food[random.randint(0,7)]  + '\n\n祝您用餐愉快，歡迎再次使用!')   

    def is_going_to_small(self, event):
        text = event.message.text
        if text == '銅板美食':
            return True
        return False

    def on_enter_small(self, event):
        print("I'm entering small")

        food = ['昌鱔魚意麵', '飽之林', '轉餃', '唐家泡菜館', '阿香臭豆腐', '楊記炒飯', '七海魚皮湯', 'GOSU', '職人雙響丼', '子龍點鴨']
        reply_token = event.reply_token
        send_text_message(reply_token, '幫您選擇\n\n' + food[random.randint(0,9)]  + '\n\n祝您用餐愉快，歡迎再次使用!')   

    def is_going_to_thank(self, event):
        text = event.message.text
        if text.find("謝謝") != -1:
            return True
        return False

    def on_enter_thank(self, event):
        print("I'm entering thank")

        reply_token = event.reply_token
        send_image_url(reply_token, 'https://img.onl/w7Nr9')               
        

    def is_going_to_user(self, event):
        return False