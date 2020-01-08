from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users/Nikita/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.facebook.com/')

name=input("Enter the name of the username : ")
passwrd=input("Enter the password : ")

user=driver.find_element_by_id('email')
user.send_keys(name)

password=driver.find_element_by_id('pass')
password.send_keys(passwrd)

login=driver.find_element_by_id('u_0_2')
login.submit()



