from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Message_list_page(BaseAction):
    #点击新建短信
    new_msg_btn = By.ID, "com.android.mms:id/action_compose_new"
    def click_new_msg(self):
        self.click(self.new_msg_btn)
