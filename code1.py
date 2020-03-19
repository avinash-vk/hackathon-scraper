from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

f=open(r"C:\Users\Srujan Deshpande\Desktop\Klashning\sem1_2019.csv","a")
f2=open(r"C:\Users\Srujan Deshpande\Desktop\Klashning\psem1_2019.csv","a")

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path=r'C:\Users\Srujan Deshpande\chromedriver.exe', chrome_options=option)
browser.get("https://pesuacademy.com/Academy/")
sec = browser.find_element_by_id('knowClsSection')
sec.send_keys('\n')
time.sleep(1)
srn = browser.find_element_by_id('knowClsSectionModalLoginId')

oldprn = ""
for i in range(newnum,newnum+250):
    srno="PES2201"+str(i)       
    srn.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b')
    srn.send_keys(str(srno)+"\n")
    
    try:
        time.sleep(0.8)
        j = 1
        newprn1 = WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(j)+"]/td[1]")))
        newsrn1 = WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(j)+"]/td[2]")))
        name1 = WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(j)+"]/td[3]")))
        sec1 = WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(j)+"]/td[5]")))
        branch1 = WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr["+str(j)+"]/td[8]")))        
        newprn = newprn1.text
        newsrn = newsrn1.text
        name=name1.text
        sec=sec1.text
        branch=branch1.text
        if(srno!=newprn):
            f2.write(srno+'\n')
            continue
#        print(newprn+','+newsrn+','+srno+','+name+','+sec+','+branch+'\n')
        f.write(newprn+','+newsrn+','+name+','+sec+','+branch+'\n')
#        print("pfile")
    except:
        continue
browser.close()
f.close()
f2.close()