import cv2
import numpy as np
import funct

# 여기에서 파일명을 바꾸며 출력해주고 있음!
img = cv2.imread("./image/shirtman.png")
img = funct.image2gray(img)
img = cv2.resize(img,(int(((800*img.shape[1])/img.shape[0])),800), interpolation = cv2.INTER_CUBIC)
img = funct.devideLevel(img)
img = funct.softenImage(img)

# 어떤 color palette의 이미지를 출력할지 선택하는 기능 추가 필요
funct.colorImage(img)

# 현재 컬러 디버깅을 위해 여러 팔레트를 한 번에 출력하고자 함수에 imshow를 넣어뒀는데, 
# 기능 추가시 / 프로그램 제출 전에 imshow 함수를 밖으로 빼내는게 좋을 것 같네요
# img = funct.colorImage(img)
# cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
