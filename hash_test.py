from passlib.hash import pbkdf2_sha256

password='1234'

hash_pw  = pbkdf2_sha256.hash(password)
print(hash_pw)
print(pbkdf2_sha256.verify(password,hash_pw))

# print(hash_pw=='$pbkdf2-sha256$29000$n5NyTgkBYMwZg3BurVUKAQ$CI567w9vElgnarFm9dLVmGQWK.uxbZB63pkbtBhda7k')
