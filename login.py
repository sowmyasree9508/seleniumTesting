from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("file:///C:/Users/sowmya/AppData/Local/Temp/Temp1_attachments.zip/login1.html")

driver.find_element_by_name("txt1").send_keys("abhishek@gmail.com")
driver.find_element_by_name("txt2").send_keys("@Bcdefghijk1")
driver.find_element_by_xpath("//button[text()='Login']").click