__author__ = 'mike'
import os
import unittest
import TestOrionUI
from login_20_ui import TestLoginOrion
from NBAI_dev_upload_ui import OrionDevUploadUI
from NBAI_Pro_upload_ui import OrionProUploadUI

from HTML import HTMLStyle

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestOrionUI.login_20_ui.TestLoginOrion),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestOrionUI.NBAI_dev_upload_ui.OrionDevUploadUI),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     TestOrionPlatform.TestOrionUI.NBAI_Pro_upload_ui.OrionProUploadUI),
        ])

        outfile = open("TestReport_UI/TestReport_OrionUI.html", "w")

        runner1 = HTMLStyle(
            stream=outfile,
            title='UI Test Report',
            description='Orion UI Tests'
        )

        runner1.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
