##### Notes 2018-05-02 Event Listener**
##### Notes 2018-05-01 In Progress...
#### PhantomJS: http://phantomjs.org/
#### Chrome: https://chromedriver.storage.googleapis.com/index.html?path=2.27/


#### Notes 2018-05-01 In Progress...
### @MichelleFairow.
### Desc: Testing "https://www.zmodo.com/" Login.
class ZmodoLogin(unittest.TestCase):
    @classmethod
    def setUp(inst):
		inst.drvr = driver_setup(drvr_opt="phantom", drvr_url="https://www.zmodo.com/customer/account/login")
		try:
			closepw = inst.drvr.find_element_by_class_name("closes")
			closepw.click()
			time.sleep(1)
		except:
			pass

	#### Zmodo Website >  Login: No Email or Password. 
   	def testing00(self):
		self.assertIn("Login", str(self.drvr.title))
		lgnbtn = self.drvr.find_element_by_id("send2")
		lgnbtn.click()
		time.sleep(0.25)
		### self.drvr.save_screenshot("phantom00.png")
		self.assertEqual(2, len(self.drvr.find_elements_by_class_name("validation-advice")))

	#### Zmodo Website >  Login: Send Email. 
    def testing01(self):
		self.assertIn("Login", str(self.drvr.title))
		try:
			userfld = self.drvr.find_element_by_id("email")
			userfld.click()
			userfld.send_keys("blah@meshare.com")
		except:
			pass
		lgnbtn = self.drvr.find_element_by_id("send2")
		lgnbtn.click()
		time.sleep(0.25)
		### self.drvr.save_screenshot("phantom01.png")
		self.assertEqual(2, len(self.drvr.find_elements_by_class_name("validation-advice")))

	#### Zmodo Website >  Login: Send Password. 
    def testing02(self):
		self.assertIn("Login", str(self.drvr.title))
		try:
			passfld = self.drvr.find_element_by_id("pass")
			passfld.click()
			passfld.send_keys("blahblahblah")
		except:
			pass
		lgnbtn = self.drvr.find_element_by_id("send2")
		lgnbtn.click()
		time.sleep(0.25)
		### self.drvr.save_screenshot("phantom02.png")
		self.assertEqual(2, len(self.drvr.find_elements_by_class_name("validation-advice")))

	#### Zmodo Website >  Login: Send Email & Password. 
    def testing03(self):
		self.assertIn("Login", str(self.drvr.title))
		try:
			userfld = self.drvr.find_element_by_id("email")
			userfld.click()
			userfld.send_keys("blah@meshare.com")
			passfld = self.drvr.find_element_by_id("pass")
			passfld.click()
			passfld.send_keys("blahblahblah")
		except:
			pass
		lgnbtn = self.drvr.find_element_by_id("send2")
		lgnbtn.click()
		time.sleep(0.25)
		### self.drvr.save_screenshot("phantom03.png")
		self.assertEqual(2, len(self.drvr.find_elements_by_class_name("validation-advice")))

    @classmethod
    def tearDown(inst):
		inst.drvr.quit()