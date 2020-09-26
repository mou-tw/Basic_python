import hashlib

md5 = hashlib.md5()
md5.update(b'JACKKKKKK')   #傳入byte型式的字串
print(md5.hexdigest())   #用hexidigest解碼



