height = input('請輸入您的身高(cm): ')
weight = input('請輸入您的體重(kg): ')
height = int(height) / 100
weight = int(weight)
BMI = weight / (height * height)
if BMI < 18.5 :
	print('你的BMI值為', BMI, '屬體重過輕')
elif BMI >= 18.5 and BMI < 24 :
	print('你的BMI值為', BMI, '屬正常範圍')
elif BMI >= 24 and BMI < 27 :
	print('你的BMI值為', BMI, '屬過重')
elif BMI >= 27 and BMI < 30 :
	print('你的BMI值為', BMI, '屬輕度肥胖')
elif BMI >= 30 and BMI < 35 :
	print('你的BMI值為', BMI, '屬中度肥胖')
else:
	print('你的BMI值為', BMI, '屬重度肥胖')
