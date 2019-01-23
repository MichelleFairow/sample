#### Notes 2018-05-01 In Progress...
#### @MichelleFairow.
#### Desc: Testing "https://www.zmodo.com/" Login.
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
		#### self.drvr.save_screenshot("phantom00.png")
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
		#### self.drvr.save_screenshot("phantom01.png")
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
		#### self.drvr.save_screenshot("phantom03.png")
		self.assertEqual(2, len(self.drvr.find_elements_by_class_name("validation-advice")))

	@classmethod
	def tearDown(inst):
		inst.drvr.quit()


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


#### Notes 2018-05-01 In Progress... 
#### @MichelleFairow.
#### Desc: Testing "https://www.zmodo.com/" > "Support" Page.
class ZmodoSupport(unittest.TestCase):
	@classmethod
	def setUp(inst):
		inst.drvr = driver_setup(drvr_opt="phantom", drvr_url="https://www.zmodo.com")
		try:
			closepw = inst.drvr.find_element_by_class_name("closes")
			closepw.click()
			time.sleep(1)
		except:
			pass
		inst.navm = inst.drvr.find_element_by_css_selector("#zmodo-nav > div > ul.nav-list.nav-tit")
		try:
			mns = inst.navm.find_elements_by_tag_name("a")
			mns[37].click()
		except:
			try:
				mns = inst.navm.find_element_by_link_text("Support")
				mns.click()
			except:
				print "fail @451"
		time.sleep(0.50)
		if len(inst.drvr.window_handles) > 1:
			inst.drvr.switch_to_window(inst.drvr.window_handles[-1])

	#### Notes 2018-05-01 Use Not CSS
	#### Zmodo Website >  "Support" > "Zmodo Store Support" Icon.
	def testing00(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part04 > div > ul > li.supports-part04-item.supports-part04-item01")
		self.assertIn("Support", str(elem.text))
	
	#### Zmodo Website >  "Support" > "Cloud Service" Icon.
	def testing01(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part04 > div > ul > li.supports-part04-item.supports-part04-item02")
		self.assertIn("Cloud", str(elem.text))

	#### Zmodo Website >  "Support" > "Zmodo App" Icon.
	def testing02(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part04 > div > ul > li.supports-part04-item.supports-part04-item04")
		self.assertIn("Zmodo App", str(elem.text))

	#### Zmodo Website >  "Support" > "Zmodo Network Tester" Icon.
	def testing03(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part04 > div > ul > li.supports-part04-item.supports-part04-item05")
		self.assertIn("Network", str(elem.text))

	#### Zmodo Website >  "Support" > "Warranty & RMA" Icon.
	def testing04(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part04 > div > ul > li.supports-part04-item.supports-part04-item06")
		self.assertIn("Warranty", str(elem.text))

	#### Zmodo Website >  "Support" > "For Smart Home Devices" > "For Smart Home Devices" Icon
	def testing05(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part05 > div > ul > li.contact-part02-con-item.contact-part02-con-item04")
		self.assertIn("217-693-5706", str(elem.text))

	#### Zmodo Website >  "Support" > "Live Chat" 
	def testing06(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part05 > div > ul > li.supports-part05-item.supports-part05-item02")
		self.assertIn("Live chat", str(elem.text))

	#### Zmodo Website >  "Support" > "Write us an E-mail"
	def testing07(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part05 > div > ul > li.supports-part05-item.supports-part05-item03")
		self.assertIn("sales@zmodo.com", str(elem.text))

	#### Zmodo Website >  "Support" > "Call us"
	def testing08(self):
		elem = self.drvr.find_element_by_css_selector("body > div.main > section.supports-part05 > div > ul > li.supports-part05-item.supports-part05-item04")
		self.assertIn("217-903-5037", str(elem.text))

	@classmethod
	def tearDown(inst):
		inst.drvr.quit()