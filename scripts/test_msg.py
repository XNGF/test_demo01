import time
import pytest

from base.base_driver import init_driver
from page.page import Page


class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize(("phone","content"),[("18888888888","hello"),("13333333333","abc")])
    def test_send_msg(self,phone,content):
        self.page.msg_list.click_new_msg()

        self.page.new_msg.input_receiver(phone)
        self.page.new_msg.input_msg(content)
<<<<<<< HEAD:scripts/test_msg.py
        self.page.new_msg.click_send()
=======
        self.page.new_msg.click_send()
>>>>>>> 21db7bcc05765e37e3f62d7b2bf0f5ecf4c32cff:11-PO-msg/scripts/test_msg.py
