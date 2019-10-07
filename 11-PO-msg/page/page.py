from page.msg_list_page import Message_list_page
from page.new_msg_page import New_msg_page


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def msg_list(self):
        return Message_list_page(self.driver)

    @property
    def new_msg(self):
        return New_msg_page(self.driver)