import requests


target_url="https://ok.ru/dk?st.cmd=anonymMain" #/dk?cmd=AnonymLogin&st.cmd=anonymMain
data={"st.email":"","st.password":"","Войти в Одноклассники":"submit"}

response=requests.post(target_url,data=data)
if "Неправильно указан логин и/или пароль"  not in str(response.content):
    print("topildi")w