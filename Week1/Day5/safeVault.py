user = {'id': 1}
#print(user['email'])
email = user.get('email', 'not found')

print(email)