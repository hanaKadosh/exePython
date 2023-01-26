import requests


x = requests.get('https://48435647-0773-423e-8b57-8c541f763dd2.mock.pstmn.io/users')

print(x.text)
