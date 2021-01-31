import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

###################################################################################
# I have conceived the code of the test case for clarity as well as for reusability. 
# I am aware that for such a simple test case it might be kind of unnecessary but I 
# tried to design it in the most readable way possible. Chrome was selected here as 
# it's usually easily accessible but it could be quicly replaced by another browser. 
###################################################################################

class HipoApplyNow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.SearchEngine = 'https://www.google.com.tr/'
        self.SearchEngineCheck = 'google.com.tr'
        self.SearchPhrase = 'Hipo Labs'
        self.TargetWebsiteCheck = 'hipolabs.com'
        self.PageToOpen = 'TEAM'
        self.ButtonToClick_id = 'pageTeamApplynowButton'
        self.TextToFind = 'APPLY NOW'

    def test_case(self):
        driver = self.driver
        driver.get(self.SearchEngine)
        self.assertIn(self.SearchEngineCheck, driver.current_url, msg = 'could not access selected search engine')

        element = driver.find_element_by_name("q")
        element.clear()
        element.send_keys(self.SearchPhrase)
        element.send_keys(Keys.RETURN)

        try:
            driver.find_element_by_xpath("//a[contains(@href,'{}')]".format(self.TargetWebsiteCheck)).click()
        except:
            self.fail('Could not find {} in the search results'.format(self.TargetWebsiteCheck))   
        self.assertIn(self.TargetWebsiteCheck, driver.current_url, msg = 'could not access selected website')
        
        driver.find_element_by_link_text(self.PageToOpen).click()

        driver.find_element_by_id('{}'.format(self.ButtonToClick_id)).click()
        # since this button is one of the last elements to be loaded in the 'TEAM' page I have considered
        # using an implicit wait to avoid raising an error by making sure that the button is present and 
        # clickable. However, when running the automated test this did not seem necessary.
        
        driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(self.TextToFind)).screenshot('{}_screenshot.png'.format(self.TextToFind))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
