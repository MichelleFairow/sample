import time
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


##### Notes 2018-05-02 Event Listener**
##### Notes 2018-05-01 In Progress...
#### PhantomJS: http://phantomjs.org/
#### Chrome: https://chromedriver.storage.googleapis.com/index.html?path=2.27/


#### Notes 2018-05-01 In Progress...
### @MichelleFairow.
### Desc: All Driver Setups
### Args: drvr_opt, drvr_url
def driver_setup(drvr_opt=None, drvr_url=None):
	# import time
	# from selenium import webdriver

	if drvr_opt is "phantom":
		pth = "C:\Python27\selenium\phantomjs.exe"
		drvr = webdriver.PhantomJS(executable_path=pth)
	elif drvr_opt is "chrome":
		pth = "C:\Python27\selenium\chromedriver.exe"
		drvr = webdriver.Chrome(executable_path=pth)
	else:
		return 1
	if drvr_url is not None:
		drvr.get(drvr_url)
		time.sleep(1.25)
		try:
			closepw = inst.drvr.find_element_by_class_name("closes")
			closepw.click()
			time.sleep(0.75)
		except:
			pass
	try:
		drvr.set_window_size(1500, 2000)
	except:
		pass
	return drvr




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




#### Notes 2018-05-01 In Progress...
### ### @MichelleFairow.
### ### Desc: Testing "https://www.zmodo.com/" Login > Forgot Login.
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
### Notes 2018-04-30 Switch to open for all?
### Notes 2018-04-30 Further Page Testing After Navigation & Check Navigation Occurred*
## @MichelleFairow.
## Desc: Testing "https://www.zmodo.com/" Home Page.
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
### ### @MichelleFairow.
### ### Desc: Testing "https://www.zmodo.com/" > "Support" Page.
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

	### Notes 2018-05-01 Use Not CSS
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




#### Notes 2018-05-01 In Progress...
### @MichelleFairow.
### Desc: Testing "https://www.zmodo.com/" > "Contact" Page.
class ZmodoContact(unittest.TestCase):
	@classmethod
	def setUp(inst):
		#### inst.drvr = driver_setup(drvr_opt="phantom", drvr_url=None)
		#### inst.drvr.get("https://www.zmodo.com")
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
			mns[38].click()
		except:
			try:
				mns = inst.navm.find_element_by_link_text("Contact")
				mns.click()
			except:
				print "fail @560"
		time.sleep(0.25)
		if len(inst.drvr.window_handles) > 1:
			inst.drvr.switch_to_window(inst.drvr.window_handles[-1])

    #### Zmodo Website >  "Contact" > ...
	def testing00(self):
		pass

    #### Zmodo Website >  "Contact" > ...
	def testing01(self):
		pass

    #### Zmodo Website >  "Contact" > ...
	def testing02(self):
		pass

	@classmethod
	def tearDown(inst):
		inst.drvr.quit()




### #### Notes 2018-05-01 In Progress...
### ### @MichelleFairow.
### ### Desc: Testing "https://www.zmodo.com/" > "Products" Page.
### class ZmodoProducts(unittest.TestCase):
### 	@classmethod
### 	def setUp(inst):
### 		inst.drvr = driver_setup(drvr_opt="chrome", drvr_url=None)
### 		inst.drvr.get("https://www.zmodo.com/")
### 		time.sleep(2)
###			try:
###				closepw = inst.drvr.find_element_by_class_name("closes")
###				closepw.click()
###				time.sleep(1)
###			except:
###				pass
### 		inst.navm = inst.drvr.find_element_by_css_selector("#zmodo-nav > div > ul.nav-list.nav-tit")
### 		try:
### 			mns = inst.navm.find_elements_by_tag_name("a")
### 			mns[1].click()
### 		except:
### 			try:
### 				mns = inst.navm.find_element_by_link_text("Products")
### 				mns.click()
### 			except:
### 				mns = inst.drvr.find_element_by_css_selector("#zmodo-nav > div > ul.nav-list.nav-tit > li.nav-item.nav-item-menu.nav-item-product > a > span.nav-link-text")
### 				mns.click()
### 		inst.drvr.save_screenshot("TEST050118.png")
### 		try:
### 			elem = inst.drvr.find_element_by_link_text("VIEW ALL PRODUCTS")
### 			elem.click()
### 		except:
### 			pass
### 		time.sleep(0.50)
### 		if len(inst.drvr.window_handles) > 1:
### 			inst.drvr.switch_to_window(inst.drvr.window_handles[-1])
### 		inst.elems = inst.drvr.find_elements_by_class_name("store-part03-list")
###
###     #### Zmodo Website >  "Products" > Monitoring Solutions.
### 	def testing00(self):
###  		self.assertTrue(len(self.elems) > 0)
###  		subprods = self.elems[0].find_elements_by_tag_name("li")
###  		self.assertTrue(len(subprods) > 2)
###
### 	#### Zmodo Website >  "Products" > Outdoor Monitoring.
### 	def testing01(self):
### 		self.assertTrue(len(self.elems) > 1)
### 		subprods = self.elems[1].find_elements_by_tag_name("li")
###  		self.assertTrue(len(subprods) > 2)
###
### 	#### Zmodo Website >  "Products" > Smart Accesseries.
### 	def testing02(self):
###  		self.assertTrue(len(self.elems) > 2)
###  		subprods = self.elems[2].find_elements_by_tag_name("li")
###  		self.assertTrue(len(subprods) >1)
###
###  	#### Zmodo Website >  "Products" > Security Kits.
### 	def testing03(self):
###  		self.assertTrue(len(self.elems) > 2)
###  		subprods = self.elems[3].find_elements_by_tag_name("li")
###  		self.assertTrue(len(subprods) > 2)
###
### 	@classmethod
### 	def tearDown(inst):
### 		time.sleep(1)
### 		inst.drvr.quit()




#### Notes 2018-05-01 In Progress...
### @MichelleFairow.
### Desc: Testing "https://www.zmodo.com/" > "Cloud" Page.
### class ZmodoCloud(unittest.TestCase):
### 	@classmethod
### 	def setUp(inst):
### 		inst.drvr = driver_setup(drvr_opt="chrome", drvr_url=None)
### 		inst.drvr.get("https://www.zmodo.com/")
### 		time.sleep(2)
###
###			try:
###				closepw = inst.drvr.find_element_by_class_name("closes")
###				closepw.click()
###				time.sleep(1)
###			except:
###				pass
###
### 		inst.navm = inst.drvr.find_element_by_css_selector("#zmodo-nav > div > ul.nav-list.nav-tit")
### 		try:
### 			mns = inst.navm.find_elements_by_tag_name("a")
### 			mns[36].click()
### 		except:
### 			mns = inst.navm.find_element_by_link_text("Cloud")
### 			mns.click()
### 
### 		time.sleep(0.25)
### 		if len(inst.drvr.window_handles) > 1:
### 			inst.drvr.switch_to_window(inst.drvr.window_handles[-1])
### 			inst.cldarea = inst.drvr.find_element_by_class_name("cloud-plan")
### 		else:
### 			inst.cldarea = None
### 		if inst.cldarea is not None:
### 			inst.cldplans = inst.cldarea.find_elements_by_class_name("plan-explore")
### 		else:
### 			inst.cldplans = None
###
###	#### Zmodo Website >  "Cloud" > Pricing > "Basic" Plan > Description.
###	def testing00(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 0)
###			#### self.cldplans[0].find_element_by_class_name("plan-explore01")
###
###	#### Zmodo Website >  "Cloud" > Pricing > "Basic" Plan > Cost.
###	def testing01(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 0)
###			self.costdesc = self.cldplans[0].find_element_by_class_name("plan-time")
###			print self.costdesc.text
###
###	#### Zmodo Website >  "Cloud" > Pricing > "7-Day" Plan > Description.
###	def testing02(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 1)
###			#### self.cldplans[1].find_element_by_class_name("plan-explore01")
###
###	#### Zmodo Website >  "Cloud" > Pricing > "7-Day" Plan > Cost.
###	def testing03(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 1)
###			self.costdesc = self.cldplans[1].find_element_by_class_name("plan-time")
###			print self.costdesc.text
###
###	#### Zmodo Website >  "Cloud" > Pricing > "30-Day" Plan > Description.
###	def testing04(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 2)
###			#### self.cldplans[2].find_element_by_class_name("plan-explore01")
###
###	#### Zmodo Website >  "Cloud" > Pricing > "30-Day" Plan > Cost. 
###	def testing05(self):
###		if self.cldplans is not None:
###			self.assertTrue(len(self.cldplans) > 2)
###			self.costdesc = self.cldplans[2].find_element_by_class_name("plan-time")
###			print self.costdesc.text
###
###	@classmethod
###	def tearDown(inst):
###		time.sleep(0.25)
###		inst.drvr.quit()




#### Notes 2018-05-01 In Progress...
### ### @MichelleFairow.
### ### Desc: Testing "https://www.zmodo.com/" > "Store" Page.
### class ZmodoStore(unittest.TestCase):
### 	@classmethod
### 	def setUp(inst):
### 		inst.drvr = driver_setup(drvr_opt="chrome", drvr_url=None)
### 		inst.drvr.get("https://www.zmodo.com/")
### 		time.sleep(2)
###			try:
###				closepw = inst.drvr.find_element_by_class_name("closes")
###				closepw.click()
###				time.sleep(0.25)
###			except:
###				pass
###
### 		inst.navm = inst.drvr.find_element_by_css_selector("#zmodo-nav > div > ul.nav-list.nav-tit")
### 		mns = inst.navm.find_elements_by_tag_name("a")
### 		mns[40].click()
### 		time.sleep(0.25)
### 		if len(inst.drvr.window_handles) > 1:
### 			inst.drvr.switch_to_window(inst.drvr.window_handles[-1])
### 
###     #### Zmodo Website >  "Store" > ...
### 	def testing00(self):
### 		pass
### 
### 	#### Zmodo Website >  "Store" > ...
### 	def testing01(self):
### 		pass
### 
### 	#### Zmodo Website >  "Store" > ...
### 	def testing02(self):
### 		pass
### 
### 	@classmethod
### 	def tearDown(inst):
### 		time.sleep(1)
### 		inst.drvr.quit()




### if __name__ == '__main__':
###    unittest.main()