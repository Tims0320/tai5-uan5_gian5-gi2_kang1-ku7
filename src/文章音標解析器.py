from 通用拼音音標 import 通用拼音音標
from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
class 文章音標解析器:
	音標工具 = None
	合法字元 = None
	def __init__(self, 音標工具):
		self.音標工具 = 音標工具

	def 解析語句(self, 語句):
		合法字元的暫時所在 = self.合法字元
		self.合法字元 = None
		解析結果 = self.解析語句佮顯示毋著字元(語句)[0]
		self.合法字元 = 合法字元的暫時所在
		return 解析結果

	def 解析語句佮顯示毋著字元(self, 語句):
		解析結果 = ''
		處理位置 = 0
		語句長度 = len(語句)
		無問題諾 = True
		while 處理位置 < 語句長度:
			for 音標長度 in range(16, 0, -1):
				音標 = self.音標工具(語句[處理位置:處理位置 + 音標長度])
				if 音標.音標 != None:
					臺灣閩南語羅馬字拼音=音標.轉換到臺灣閩南語羅馬字拼音()
					if 臺灣閩南語羅馬字拼音==None:
						print(音標.音標+'轉臺灣閩南語羅馬字拼音有問題！！')				
						print(音標.聲韻對照表[音標.聲韻])
						無問題諾 = False
					else:
						解析結果 += 臺灣閩南語羅馬字拼音
					處理位置 += 音標長度
					break
			else:
#				if not 語句[處理位置].isnumeric():
				if self.合法字元 == None or 語句[處理位置] in self.合法字元:
					解析結果 += 語句[處理位置]
				else:
					print("錯誤=" + 語句[處理位置] + " 佇「" + 語句 + '」的' + str(處理位置))
					解析結果 += 語句[處理位置]
					無問題諾 = False
				處理位置 += 1
		return (解析結果, 無問題諾)

if __name__ == '__main__':
	解析器 = 文章音標解析器(臺灣閩南語羅馬字拼音)
	解析器.合法字元 = {' ', '-'}
	print(解析器.解析語句('tshiǔnn	tshiūnn'))
	print(解析器.解析語句('tsua̋n-ne tsua̋n'))
	print(解析器.解析語句('--tsi̍t-kuá --tsit-kuá'))
	print(解析器.解析語句('--tsi̍t-kuá -@-tsit-kuá'))
	print(臺灣閩南語羅馬字拼音('nau2').音標)
	解析器 = 文章音標解析器(通用拼音音標)
	print(解析器.解析語句('hue2_zit6_e5_sit7_le4'))
	print(解析器.解析語句('17,"一下子","一時仔","zit6-si5-a4","cit8-si5-a2"'))
	print(解析器.解析語句('"一丁不識","[(it7)-(ding1)-(but7)-(sik7)]","文"'))
	print(解析器.解析語句('m33gorh66 ho23 sua12 a44 liam53 mua45mua44 e52 ve45cia11 ziah77 giann53 vor53 qo23hun12zing11 , 	'))
	print(解析器.解析語句('qin21 a24 dor43 i45ging12 ga23 tau55 cun22 cut76ki34 cia12 tang12a41qua22 gong44 '))
	print(解析器.解析語句('mui45  ging12ge34  zit68ging12cu33'))
	print(解析器.解析語句('nau2'))
	
