
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time
import datetime
import NBAI_dev_base_ui


class OrionDevUploadUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/guoec/Downloads/chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.valid_username = "fengyuan3699+1@gmail.com"
        self.valid_password = "nbai123"

        # self.task_file_path = '/home/mikeli/Downloads/tasks/'
        self.task_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './FilesOfUI'))
        print(self.task_file_path)
        self.task_file_name = '/word2vec_orion.zip'
        self.taskname = "NBAI-" + str(datetime.date.today()) + str("-UI-5")
        self.message = "4"

    def test_gs2_ui(self):
        driver = self.driver
        driver.get("http://192.168.88.216:8080/orion-dashboard-boot")
        driver.maximize_window()
        time.sleep(2)

        # login
        login_page = NBAI_dev_base_ui.login_base(self.driver)  # 引入登录文件，文件名+class名
        login_page.login(self.driver, self.valid_username, self.valid_password)
        time.sleep(5)

        self.driver.execute_script("scroll(0, 0);")  # To page top
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="m_ver_menu"]/ul/li[3]/a/span/span/span').click()
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-cygnus/div[2]/div[5]/button')


    # path = os.path.dirname(__file__)
    # outfile = os.path.join(path, 'NBAI_dev_upload_ui.py')
    # run(argv=['nosetests', '-v', '--with-html-output', '--html-out-file=20190522-dev-upload(UI-test) Report.html',
    #           outfile], plugins=[HtmlOutput()])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
