from selenium import webdriver
import time
import os


def ChromeBrowser():
  # without image
  def RunDriver():
    print("driver starting..")
    global driver
    options = webdriver.ChromeOptions ()
    options.add_argument(f"user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Chrome\\Whatsapp Mk\\Wordpress")
    driver = webdriver.Chrome(executable_path=f"{os.path.abspath(os.getcwd())}\\chromedriver.exe", options=options)

  def login(username="Abderrazzak.2", password="5SImJS^gL2ZG2!dEiIJ3@Edx"):
    RunDriver()
    
    print("login by")
    print(f" -username: {username}")
    print(f" -password: {password}")
    url = 'https://welightbox.com/mk/login/'
    driver.get(url)
    time.sleep(5)

    try:
      driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(username)
      driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys(password)
      driver.find_element_by_xpath('//*[@id="rememberme"]').click()
      driver.find_element_by_xpath('//*[@id="post-0"]/div/div/form/div[4]/button').click()
      time.sleep(10)
      print("Logged in")
      driver.quit()
    except:
      print("Error !!")
      print("Check your username and password before trying again")

  def changeText():
    RunDriver()
    try:
      print("Page loading")
      url = 'https://welightbox.com/mk/wp-admin/post.php?post=2&action=edit'
      driver.get(url)

      time.sleep(60)
      words = ['home', 'home ']
      driver.find_element_by_xpath('//*[@id="editor"]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/h1').click()
      while True:
        for word in words:
          time.sleep(6)
          driver.find_element_by_xpath('//*[@id="editor"]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/h1').clear()
          time.sleep(1)
          driver.find_element_by_xpath('//*[@id="editor"]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/h1').send_keys(word)
          time.sleep(1)
          driver.find_element_by_xpath('//*[@id="editor"]/div/div[1]/div[1]/div[1]/div/div[3]/button[2]').click()
          print("Data has been updated")
      driver.quit()
    except:
      print("Error !!")
  try:
    login()
  except:
    print("Error in login fonction !!")
  
  while True:
    try:
      changeText()
    except:
      time.sleep(10)  
      changeText()




while True:
  try:
    ChromeBrowser()
  except:
    ChromeBrowser()