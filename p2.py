Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myfilename="california girls.mp3"
>>> myfilename.partition('.')
('california girls', '.', 'mp3')
>>> filename ,separotar ,extension =myfilename.partition('.')
>>> filename
'california girls'
>>> extension
'mp3'
>>> 
