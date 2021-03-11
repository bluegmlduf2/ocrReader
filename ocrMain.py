from PIL import Image     #pip install pillow
from pytesseract import * #pip install pytesseract
import configparser
import os
 
#pytesseract.tesseract_cmd = r'C:\Users\33871\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#環境変数登録済みなら不要

#Config Parser 초기화
config = configparser.ConfigParser()
#Config File 읽기
iniPath=os.path.dirname(os.path.realpath(__file__)) + os.sep + 'ocrEnv' + os.sep + 'property.ini'
config.read(iniPath)
 
#이미지 -> 문자열 추출
def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'): #디폴트는 영어로 추출
    #이미지 경로
 
    img = Image.open(fullPath)
    txtName = os.path.join(outTxtPath,fileName.split('.')[0])
    #추출(이미지파일, 추출언어, 옵션)
    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다.
    #psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)
    #psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage
    # outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1')
    outText = image_to_string(img, lang=lang)
 
    print('+++ OCT Extract Result +++')
    print('Extract FileName ->>> : ', fileName, ' : <<<-')
    print('\n\n')
    #출력
    print(outText)
    #추출 문자 텍스트 파일 쓰기
    strToTxt(txtName, outText)
 
#문자열 -> 텍스트파일 개별 저장
def strToTxt(txtName, outText):
    with open(txtName + '.txt', 'w', encoding='utf-8') as f:
        f.write(outText)
 
#메인 시작
if __name__ == "__main__":
 
    #텍스트 파일 저장 경로
    outTxtPath = os.path.dirname(os.path.realpath(__file__))+ config['Path']['OcrTxtPath']
 
    #OCR 추출 작업 메인
    rPath=os.path.dirname(os.path.realpath(__file__))
    fPath=config['Path']['OriImgPath']
    path11=os.path.dirname(os.path.realpath(__file__)) + "\\resource"
    for root, dirs, files in os.walk(path11):
        for fname in files:
            fullName = os.path.join(root, fname)
            #한글+영어 추출(kor, eng , kor+eng)
            ocrToStr(fullName, outTxtPath, fname,'jpn+eng')
