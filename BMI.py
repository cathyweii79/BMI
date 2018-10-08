hight = input('請輸入身高(公分):')
weight = input('請輸入體重(公斤):')
hight = int(hight)
weight = int(weight)
hight = hight / 100
BMI = weight / hight / hight

if BMI < 18.5:
	print('你的BMI值為:', BMI,'體重過輕')
elif 18.5 <= BMI < 24:
	print('你的BMI值為:', BMI,'正常範圍, 請繼續保持')
elif 24 <= BMI < 27:
	print('你的BMI值為:', BMI,'請注意!過重囉')
elif 27 <= BMI < 30:
	print('你的BMI值為:', BMI,'輕度肥胖')
elif 30 <= BMI < 35:
	print('你的BMI值為:', BMI,'中度肥胖')
elif 35 <= BMI:
	print('你的BMI值為:', BMI,'重度肥胖')