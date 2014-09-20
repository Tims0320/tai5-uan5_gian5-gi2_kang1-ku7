# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import kenlm
from 臺灣言語工具.表單.語句連詞 import 語句連詞
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分詞符號

class 肯語句連詞(語句連詞):
	_譀鏡 = 物件譀鏡()
	def __init__(self, 語言模型檔案):
		self._語言模型 = kenlm.LanguageModel(語言模型檔案)
	def 上濟詞數(self):
		return self._語言模型.order
	def 評詞陣列分(self, 詞陣列, 開始的所在=0):
		字串 = []
		for 詞物件 in 詞陣列: 
			字串.append(self._譀鏡.看分詞(詞物件))
		for 所在, 結果 in enumerate(
				self._語言模型.full_scores(分詞符號.join(字串))):
			if 所在 >= 開始的所在:
				分數 = 結果[0]
# 				長度 = 結果[1] #這个機率連詞長度
				try:
					分數 += 詞陣列[所在].屬性['機率']
				except:
					pass
				yield 分數
