# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
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
臺灣閩南語羅馬字拼音對照吳守禮方音聲母表 = {'p':'ㄅ', 'ph':'ㄆ', 'm':'ㄇ', 'b':'ㆠ', 't':'ㄉ', 'th':'ㄊ', 'n':'ㄋ', 'l':'ㄌ',
		'k':'ㄍ', 'kh':'ㄎ', 'ng':'ㄫ', 'g':'ㆣ', 'h':'ㄏ', 'ts':'ㄗ', 'tsh':'ㄘ', 's':'ㄙ', 'j':'ㆡ',
		'tsi':'ㄐ', 'tshi':'ㄑ', 'si':'ㄒ', 'ji':'ㆢ', '':'', }
臺灣閩南語羅馬字拼音對照吳守禮方音韻母表 = {'a':'ㄚ', 'e':'ㆤ', 'i':'ㄧ', 'oo':'ㆦ', 'o':'ㄜ', 'u':'ㄨ',
		'ai':'ㄞ', 'au':'ㄠ', 'ia':'ㄧㄚ', 'io':'ㄧㄜ', 'iu':'ㄧㄨ', 'ua':'ㄨㄚ', 'ue':'ㄨㆤ', 'ui':'ㄨㄧ', 'iau':'ㄧㄠ', 'uai':'ㄨㄞ',
		'ann':'ㆩ', 'enn':'ㆥ', 'inn':'ㆪ', 'onn':'ㆲ', 'm':'ㆬ', 'ng':'ㆭ', 'ainn':'ㆮ', 'iann':'ㄧㆩ', 'iaunn':'ㄧㆯ', 'iunn':'ㄧㆫ', 'uann':'ㄨㆩ', 'uannh':'ㄨㆩㆷ', 'uainn':'ㄨㆮ',
		'am':'ㆰ', 'an':'ㄢ', 'ang':'ㄤ', 'im':'ㄧㆬ', 'in':'ㄧㄣ', 'ing':'ㄧㄥ', 'om':'ㆱ', 'ong':'ㆲ', 'iam':'ㄧㆰ', 'ian':'ㄧㄢ', 'iang':'ㄧㄤ', 'iong':'ㄧㆲ', 'un':'ㄨㄣ', 'uan':'ㄨㄢ',
		'ah':'ㄚㆷ', 'eh':'ㆤㆷ', 'ih':'ㄧㆷ', 'oh':'ㄜㆷ', 'uh':'ㄨ', 'auh':'ㄠㆷ', 'iah':'ㄧㄚㆷ', 'ioh':'ㄧㄜㆷ', 'iuh':'ㄧㄨㆷ', 'iauh':'ㄧㄠㆷ', 'uah':'ㄨㄚㆷ', 'ueh':'ㄨㆤㆷ', 'ooh':'ㆦㆷ',
		'annh':'ㆩㆷ', 'ennh':'ㆥㆷ', 'innh':'ㆪㆷ', 'mh':'ㆬㆷ', 'iannh':'ㄧㆩㆷ', 'ngh':'ㆭㆷ', 'ap':'ㄚㆴ', 'at':'ㄚㆵ', 'ak':'ㄚㆶ', 'op':'ㆦㆴ', 'ok':'ㆦㆶ', 'iok':'ㄧㆦㆶ',
		'ip':'ㄧㆴ', 'it':'ㄧㆵ', 'ik':'ㄧㆶ', 'iap':'ㄧㄚㆴ', 'iat':'ㄧㄚㆵ', 'iak':'ㄧㄚㆶ', 'ut':'ㄨㆵ', 'uat':'ㄨㄚㆵ',
		'ioo':'ㄧㆦ', 'iooh':'ㄧㆦㆷ',
		'ir':'ㆨ', 'irh':'ㆨㆷ', 'irp':'ㆨㆴ', 'irt':'ㆨㆵ', 'irk':'ㆨㆶ', 'irinn':'ㆨㆪ', 'irm':'ㆨㆬ', 'irn':'ㆨㄣ', 'irng':'ㆨㄥ',  # 泉 豬仔
		'er':'ㄮ', 'ere':'ㄮㆤ', 'erh':'ㄮㆷ', 'ereh':'ㄮㆤㆷ', 'erm':'ㄮㆬ',
		'ee':'ㄝ', 'uee':'ㄨㄝ', 'eeh':'ㄝㆷ', 'eng':'ㄝㄥ',
		'or':'ㄛ', 'orh':'ㄛㆷ', 'ior':'ㄧㄛ', 'iorh':'ㄧㄛㆷ',  # 蚵仔
		'ie':'ㄧㄝ',  # 教育部辭典鹿港腔
		'uinn':'ㄨㆪ', 'ionn':'ㄧㆧ', 'uang':'ㄨㄤ',
		'aih':'ㄞㆷ', 'ainnh':'ㆮㆷ', 'aunnh':'ㆯㆷ', 'uih':'ㄨㄧㆷ',
		'aunn':'ㆯ', 'uenn':'ㄨㆥ', 'uaih':'ㄨㄞㆷ', 'iunnh':'ㄧㆫㆷ', 'iaunnh':'ㄧㆯㆷ', 'uennh':'ㄨㆥㆷ', 'uinnh':'ㄨㆪㆷ', 'uainnh':'ㄨㆮㆷ',
		'iut':'ㄧㄨㆵ', 'uak':'ㄨㄚㆶ', 'onnh':'ㆧㆷ',
		'oi':'ㆦㄧ', 'oih':'ㆦㄧㆷ',
		}
臺灣閩南語羅馬字拼音對照吳守禮方音聲調表 = {'0':'˙', '1':'', '2':'ˋ', '3':'˪',
'4':'', '5':'ˊ', '6':'˫', '7':'˫',
'8':'㆐', '9':'^', '10':'㆐'}

class 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組():
	聲母表 = 臺灣閩南語羅馬字拼音對照吳守禮方音聲母表
	韻母表 = 臺灣閩南語羅馬字拼音對照吳守禮方音韻母表
	聲調符號表 = 臺灣閩南語羅馬字拼音對照吳守禮方音聲調表
	聲 = None
	韻 = None
	調 = None
	音標 = None
	def __init__(self, 聲, 韻, 調, 輕):
		if 聲 == None or 韻 == None or 調 == None or 輕 == None :
			return
		if 韻.startswith('i') and (聲 == 'ts' or 聲 == 'tsh' or 聲 == 's' or 聲 == 'j'):
			聲 += 'i'
		if 輕 == '0':
			調 = '0'
		self.聲 = self.聲母表[聲]
		self.韻 = self.韻母表[韻]
		self.調 = self.聲調符號表[調]
		if 調 == '0':
			self.音標 = self.調 + self.聲 + self.韻
		elif 調 == '8':
			self.音標 = self.聲 + self.韻[:-1] + self.調 + self.韻[-1:]
		else:
			self.音標 = self.聲 + self.韻 + self.調
	def 產生音標組字式(self):
		if self.音標 == None:
			return None
		elif len(self.音標) == 1:
			return '⿿' + self.音標 + '　'
		else:
			return '⿿' * (len(self.音標) - 1) + self.音標
