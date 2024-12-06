from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
import time
# Khởi tạo trình điều khiển Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mở trang web
driver.get("http://127.0.0.1:8000/")
driver.save_screenshot("screenshot0.png")

sign_up_button = driver.find_element("link text", "Sign up")
sign_up_button.click()
driver.save_screenshot("screenshot1.png")
print("MO trang web thanh cong")

#form dang ki================================================================================
username_signup = driver.find_element(By.NAME, "username" )
ranUsername = Faker().user_name()
username_signup.send_keys(ranUsername)

password_signup = driver.find_element(By.NAME, "password" )
ranPassword = passwordValid = Faker().password(length=8, digits=True, special_chars=True, lower_case=True, upper_case=True)
password_signup.send_keys(ranPassword)

confirm_password = driver.find_element(By.NAME, "confirm_password" )
confirm_password.send_keys(ranPassword)

email = driver.find_element(By.NAME, "email" )
ranEmail = Faker().email()
email.send_keys(ranEmail)

time.sleep(5)
sign_up_button1 = driver.find_element(By.NAME, "signup")
sign_up_button1.click()

driver.save_screenshot("screenshot2.png")
print("DKi thanh cong")
time.sleep((10))


#form dang nhap====================================================================================
username_signin = driver.find_element(By.NAME, "username" )
username_signin.send_keys(ranUsername)

password_signin = driver.find_element(By.NAME, "password" )
password_signin.send_keys(ranPassword)
time.sleep(3)

driver.save_screenshot("screenshot3.png")

sign_in_button = driver.find_element(By.NAME, "signin")
sign_in_button.click()
print("Dnhap thanh cong")
time.sleep(3)
driver.save_screenshot("screenshot4.png")


#xem thong bao====================================================================
notices = driver.find_element(By.LINK_TEXT, "Notice")
notices.click()
driver.save_screenshot("screenshot5.png")
print("xem thong bao thanh cong")
time.sleep(5)

home = driver.find_element(By.LINK_TEXT, "Home")
home.click()
time.sleep(2)

#cai dat tai khoan==============================================================================
dropdown = driver.find_element(By.ID, 'name')
dropdown.click()
print("click ok!")
time.sleep(3)

setting = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "setting"))
)
setting.click()
time.sleep(2)

ten = driver.find_element(By.NAME, "first_name" )
ten.send_keys('Hoang')
ho = driver.find_element(By.NAME, "last_name" )
ho.send_keys('Le')
ngay = driver.find_element(By.NAME, "date_of_birth" )
ngay.send_keys('22-10-2004')
print("sinhnhat thanh cong")
time.sleep(1)

gioitinh = driver.find_element(By.NAME, "gender" )  # Thay bằng ID của <select>
gioitinh.click()
time.sleep(2)
# Dùng Select để thao tác dropdown
select = Select(gioitinh)
select.select_by_value("Male")
print("gioi tinh ok")

phong = driver.find_element(By.NAME, "department" )
phong.send_keys('phong513')
time.sleep(3)

driver.find_element(By.ID, 'update').click()
print("cai dat tai khoan thanh cong")

time.sleep(2)
driver.save_screenshot("screenshot6.png")

#dang ki du kien=========================================================================================================
expected_Registration = driver.find_element("link text", "Expected Registration")
expected_Registration.click()


sub = driver.find_element(By.CLASS_NAME, "btn-register")
sub.click()
time.sleep(2)

delete = driver.find_element(By.CLASS_NAME, "btn-delete")
delete.click()
time.sleep(2)
print("dang ki du kien thanh cong")


#dang xuat==================================================================================================================
driver.find_element(By.ID, 'name').click()
time.sleep(2)

log_out = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "log_out"))
)
log_out.click()
print("log out ok")
time.sleep(2)

driver.find_element(By.ID, "sign_in").click()
time.sleep(2)

#quen mk=================================================================================================================
driver.find_element(By.ID, "quen_mk").click()
email_forget = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email_forget.send_keys(ranEmail)

driver.find_element(By.ID, "submit_quen_mk").click()

time.sleep(10)

new_passWord = driver.find_element(By.NAME, "new_password" )
new_passWord.send_keys('Hoangle12345@')
confirm_password_new = driver.find_element(By.NAME, "Hoangle12345@" )
confirm_password_new.send_keys('Hoangle12345@')
reset = driver.find_element("link text", "Reset password")
driver.save_screenshot("screenshot8.png")
time.sleep(2)
reset.click()
print("quen mk thanh cong")

#dang nhap sau khi reset mk=================================================================================================
username_signin3 = driver.find_element(By.NAME, "username" )
username_signin3.send_keys(ranUsername)

password_signin3 = driver.find_element(By.NAME, "password" )
password_signin3.send_keys('Hoangle12345@')

driver.save_screenshot("screenshot9.png")
time.sleep(2)
print("dang nhap lai thanh cong")

time.sleep(30)
# Đóng trình duyệt
driver.quit()