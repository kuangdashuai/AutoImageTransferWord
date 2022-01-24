from PIL import Image
import pytesseract
if __name__ == '__main__':
    image_path = 'E:\\code\\workspace\\ygo_1.0\\wanted\\FIpZHrWWYAEB3k2 - 副本.png'

    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    # 文字识别是ORC的一部分内容，ORC的意思是光学字符识别，通俗讲就是文字识别。Tesseract是一个用于文字识别的工具，我们结合Python使用可以很快的实现文字识别
    dir_config = '--tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'
    # chi_sim是简体中文
    # text = pytesseract.image_to_string(Image.open(image_path),
    #                                    config=dir_config, lang='chi_sim')
    #设置为英文或阿拉伯字母的识别
    text = pytesseract.image_to_string(Image.open(image_path), lang='eng')

    print(text)
    f = open('C:\\Users\\kuangdashuai\\Desktop\\output001.txt', 'w')
    f.write(text)
    f.close()
