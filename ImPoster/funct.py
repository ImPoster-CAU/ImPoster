import numpy as np
import cv2

def image2gray(src):
    # 이미지를 grayscale로 바꾸는 함수
    height, width, color = src.shape
    dst = src.copy()

    for y in range(0, height):
        for x in range(0, width):
            grayColor = (src.item(y, x,0)+src.item(y, x,1)+src.item(y, x,2))/3
            dst[y, x] = round(grayColor)

    return dst

def setBoundaryByHistogram(src):
    # 각 Region 의 경계값을 히스토그램의 누적을 이용하여, 각 영역의 픽셀 개수가 총 개수의 1/6이 되도록 정함 
    height, width, color = src.shape

    pixelNumOfEachBoundary = height * width / 6

    stack = [0 for i in range(256)]
    maxValueOfEachBoundary = []

    for y in range(0, height):
        for x in range(0, width):
            stack[src.item(y, x, 0)] += 1

    countNumb = 0
    for i in range(0, 255):
        countNumb += stack[i]
        if countNumb >= pixelNumOfEachBoundary :
            countNumb -= pixelNumOfEachBoundary
            maxValueOfEachBoundary.append(i)
            print(i)

    return maxValueOfEachBoundary



def devideLevel(src):
    # setBoundaryByHistogram 함수를 이용하여 나눈 영역값을 기준으로 6단계(0~5)로 나누어주기
    height, width, color = src.shape
    
    maxValueOfEachBoundary = setBoundaryByHistogram(src)

    dst = src.copy();

    for y in range(0, height):
        for x in range(0, width):
            if src.item(y, x, 0) < maxValueOfEachBoundary[0]:
                dst[y, x] = 0

            elif src.item(y, x, 0) < maxValueOfEachBoundary[1]:
                dst[y, x] = 1

            elif src.item(y, x,0) < maxValueOfEachBoundary[2]:
                dst[y, x] = 2

            elif src.item(y, x, 0) < maxValueOfEachBoundary[3]:
                dst[y, x] = 3

            elif src.item(y, x, 0) < maxValueOfEachBoundary[4]:
                dst[y, x] = 4

            else :
                dst[y, x] = 5
   
    return dst

def softenImage(src):
    # 0~5로 나눠진 그림에서 5x5 평균값 필터로 이미지 노이즈를 제거 + 영역의 경계선 부드럽게 만들어주기
    height, width, color = src.shape
    dst = src.copy()

    mask55 = np.ones((5,5), np.float64) / 25
    cv2.filter2D(src, -1, mask55, dst)

    return dst
    
def visualizeImage(src):
    # 위 devide level 함수 결과 디버그 용도
    # 0~5단계로 나뉜 영역을 가시화하여 grayscale img로 보여준다.

    height, width, color = src.shape
    dst = src.copy()

    for y in range(0, height):
        for x in range(0, width):
            dst[y, x] = src[y, x] * (255 / 6) 

    return dst

# 테두리를 출력 시도해보다가 포기함!
# 추후에 안쓰면 지우면 됨!
# def drawEdge(src):
#     #input : 0~7로 labeling 된 이미지
    
#     height, width, color = src.shape

#     dst = src.copy()
#     distance = 3;

#     maskY = [distance, distance, distance, 0]
#     maskX = [-distance, 0, distance, distance]
    
#     for y in range(0, height):
#         for x in range(0, width):
#             for i in range(0, 4):
#                 y_ = y + maskY[i]
#                 x_ = x + maskX[i]

#                 if (y_ < height) and ( x_ >= 0 and x_ < width) :
#                     if src.item(y, x, 0) - src.item(y_, x_, 0) >= 3:
#                         for j in range(0, round(distance / 1)) :
#                             dst[round(y + maskY[i]/distance * j), round(x + maskX[i]/distance * j)] = 0

#                     if src.item(y, x, 0) - src.item(y_, x_, 0) <= -2:
#                         for j in range(0, round(distance / 1)) :
#                             dst[round(y + maskY[i]/distance * j), round(x + maskX[i]/distance * j)] = 0
                    
#                 else :
#                     continue
    
#     return dst


def colorImage(src):
    #팔레트를 이용해 영역에 색칠하기
    #파격적인 색상조합을 추가해주기 바랍니당
    height, width, color = src.shape

    palette2 = [
        (0, 0, 0), #검은색
        (164, 46, 105), #보라색
        (13, 100, 210), #귤색
        (50, 170, 240), #덜연한귤색
        (164,  227, 255),#연한귤색
        (242, 250, 253) #흰색
    ]

    palette3 = [
        (0, 0, 0), #블랙
        (40, 41, 38), #검은색
        (125, 99, 22), #심해색
        (44, 189, 250), #하늘색
        (251, 194, 156), #살구색
        (255,  248, 178) #연노랑
    ]

    palette4 = [
        (148, 58, 108), #보라
        (58, 19, 189), #목젖색
        (233,  151, 35), #뽕따꼭따리
        (60, 200, 255), #레몬껍질색
        (141, 243, 197), #메로나
        (208, 246, 250) #귤피색
        #여기에 팔레트 색상 추가
    ]

    dst = src.copy()
    for y in range(0, height):
        for x in range(0, width):
            dst[y, x] = palette2[src.item(y, x, 0)]
    cv2.imshow("2", dst)

    dst = src.copy()
    for y in range(0, height):
        for x in range(0, width):
            dst[y, x] = palette3[src.item(y, x, 0)]
    cv2.imshow("3", dst)

    dst = src.copy()
    for y in range(0, height):
        for x in range(0, width):
            dst[y, x] = palette4[src.item(y, x, 0)]
    cv2.imshow("4", dst)

    return dst
