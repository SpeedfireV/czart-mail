import smtplib

sender_email = "czartorymail@gmail.com"
rec_email = "grzegorz.niespodzianek@gmail.com"
password = input()
message = "Witamy w aplikacji CzartVote!!!"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Logowanie zakończone sukcesem")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)