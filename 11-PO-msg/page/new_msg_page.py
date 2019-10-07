from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class New_msg_page(BaseAction):
    #点击接收者发送18888888888
    #点击键入信息 hello123
    #点击发送
    receiver_text = By.ID,"com.android.mms:id/recipients_editor"
    send_text = By.ID,"com.android.mms:id/embedded_text_editor"
    send_btn = By.ID,"com.android.mms:id/send_button_sms"

    def input_receiver(self,text):
        self.input(self.receiver_text,text)
    def input_msg(self,text):
        self.input(self.send_text,text)
    def click_send(self):
        self.click(self.send_btn)


