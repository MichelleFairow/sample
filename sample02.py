#### Notes 2018-05-01 In Progress...
#### @MichelleFairow.
#### Desc: Testing "https://www.zmodo.com/" Login > Forgot Login.
class ZmodoLoginForgot(unittest.TestCase):
	@classmethod
	def setUp(inst):
		inst.drvr = driver_setup(drvr_opt="phantom", drvr_url="https://www.zmodo.com/customer/account/login")
		try:
			closepw = inst.drvr.find_element_by_class_name("closes")
			closepw.click()
			time.sleep(1)
		except:
			pass
		frgtall = inst.drvr.find_element_by_partial_link_text("Forgot")
		frgtall.click()
		time.sleep(0.75)
    
	#### Zmodo Website >  Forogt Username/Password > Submit.
	def testing00(self):
		self.assertIn("Zmodo", str(self.drvr.title))
		sbtn = self.drvr.find_elements_by_tag_name("button")
		if len(sbtn) > 0:
			sbtn[0].click()
			time.sleep(0.25)
			self.assertEqual(1, len(self.drvr.find_elements_by_class_name("validation-advice")))

	#### Zmodo Website >  Forogt Username/Password > Invalid Email > Submit.
	def testing01(self):
		self.assertIn("Zmodo", str(self.drvr.title))
		sbtn = self.drvr.find_elements_by_tag_name("button")
		if len(sbtn) > 0:
			usereml = self.drvr.find_element_by_id("email_address")
			usereml.send_keys("michellefairow")
			sbtn[0].click()
			time.sleep(0.25)
			self.assertEqual(1, len(self.drvr.find_elements_by_class_name("validation-advice")))

	#### Zmodo Website >  Forogt Username/Password > Invalid Email > Submit.
	def testing02(self):
		self.assertIn("Zmodo", str(self.drvr.title))
		sbtn = self.drvr.find_elements_by_tag_name("button")
		if len(sbtn) > 0:
			usereml = self.drvr.find_element_by_id("email_address")
			usereml.send_keys("@meshare.com")
			sbtn[0].click()
			time.sleep(0.25)
			self.assertEqual(1, len(self.drvr.find_elements_by_class_name("validation-advice")))

	@classmethod
	def tearDown(inst):
		inst.drvr.quit()


#### Notes 2018-05-01 In Progress...
#### Notes 2018-04-30 Switch to open for all?
#### Notes 2018-04-30 Further Page Testing After Navigation & Check Navigation Occurred*
#### @MichelleFairow.
#### Desc: Testing "https://www.zmodo.com/" Home Page.
class ZmodoHome(unittest.TestCase):
	@classmethod
	def setUp(inst):
		inst.drvr = driver_setup(drvr_opt="phantom", drvr_url="https://www.zmodo.com")
		try:
			closepw = inst.drvr.find_element_by_class_name("closes")
			closepw.click()
			time.sleep(1)
		except:
			pass
		inst.lowmenu = inst.drvr.find_element_by_css_selector("#zmodo-footer > div > ul.footer-zmodo")
		try:
			inst.drvr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		except:
			pass
		time.sleep(0.25)
       
	#### Zmodo Website >  Scroll Down. Check Driver Title & URL.
	def testing00(self):
		self.assertIn("Zmodo", str(self.drvr.title))
		self.drvr.execute_script("window.scrollTo(0, 0);")

	#### Zmodo Website > Check "2018 Zmodo"
	def testing01(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 0)
		self.assertIn("2018", lmitems[0].text)
		#### self.assertIn("", lmitems[0].get_attribute("href"))
		#### lmitems[0].click()

	#### Zmodo Website > Check & Click "About Us"
	def testing02(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 1)
		self.assertIn("About", lmitems[1].text)
		self.assertIn("about", lmitems[1].get_attribute("href"))
		lmitems[1].click()

	#### Zmodo Website > Check & Click "Legal"
	def testing03(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 2)
		self.assertIn("Legal", lmitems[2].text)
		self.assertIn("legal", lmitems[2].get_attribute("href"))
		lmitems[2].click()

	#### Zmodo Website > Check & Click "Privacy Policy"
	def testing04(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 3)
		self.assertIn("Privacy", lmitems[3].text)
		self.assertIn("privacy", lmitems[3].get_attribute("href"))
		lmitems[3].click()

	#### Zmodo Website > Check & Click "Press"
	def testing05(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 4)
		self.assertIn("Press", lmitems[4].text)
		self.assertIn("press", lmitems[4].get_attribute("href"))
		lmitems[4].click()

	#### Zmodo Website > Check & Click "Contact"
	def testing06(self):
		lmitems = self.lowmenu.find_elements_by_tag_name("a")
		self.assertTrue(len(lmitems) > 5)
		self.assertIn("Contact", lmitems[5].text)
		self.assertIn("contact", lmitems[5].get_attribute("href"))
		lmitems[5].click()

	@classmethod
	def tearDown(inst):
		inst.drvr.quit()