height = input('請輸入您的身高:')
height = float(height)
height = height / 100
weight = input('請輸入您的體重:')
weight = float(weight)
b = weight / height / height
print('BMI值:',b) 
if b < 18.5 :
    print('體重過輕')
elif b >= 18.5 and b < 24 :
    print('正常範圍')
elif b >= 24 and b < 27:
    print('過重')
elif b >= 27 and b < 30 :
    print('輕度肥胖')
elif b >= 30 and b < 35 :
    print('中度肥胖')
else:
	print('重度肥胖')

