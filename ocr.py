from cnocr import CnOcr
#更精确识别，但是不能太长了
if __name__ == '__main__':

    ocr = CnOcr()
    res = ocr.ocr('E:\\code\\workspace\\ygo_1.0\\wanted\\FIpZHrWWYAEB3k2.png')
    print("Predicted Chars:", res)
