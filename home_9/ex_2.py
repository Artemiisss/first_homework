def hiding_mail(mail) -> str:
    name, domain = mail.split('@')
    return f'Your hidden mail is: {name[0:-7]}***@**{domain[3:]}'


print(hiding_mail('python.developer@gmail.com'))
