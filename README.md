# ImPoster

### 1. Project Goal
![image](https://user-images.githubusercontent.com/29995264/140717986-34626cfa-64db-4c90-9236-3d60ba2b5622.png)  
What we are going to do is to transform images taken from cameras into fancy posters such as modern art images.  
Our program considers the direction and brightness of the light. After that, depending on the analysis it colors the optimal position at the image.   
Like the example below, Our program will detect the same regions and color it by shadow.  
Also we get to select colors as user input, with the selected colors users can customize their own poster image.

### 2. Implementation Plan
## Step1. Convert image into grayscale
    - Distract all the color images to make it easy to detect edges and  separate 
    - regions into several parts. 
	
## Step2. Split areas into 7-8 by brightness level 
    - Classify the regions according to the brightness level,  
    - these separated areas will be colored as the same region.
    - We are going to use some edge, vertex detection methods and so on.

## Step3. Label splitted areas
    - With the categorized brightness level we can make distinct labeled areas in the image.
    - Each of the Different labeled areas will be colored with variable tone

## Step4. Color splitted areas of image with preset palette due to informations
    - Coloring each labeled area with presetted palette color. 
    - We can make a preset with User’s personal taste within a variable pool.
	
	
### 3. Roll distribution
- step 1 & step 2: 윤석원, 박성민
- step 3 & step 4: 유승훈, 조중현


### 4. Timeline (Schedule)
- 11/13 : Implementing each algorithm.
- 11/20 : Combining algorithm together, and debug
- 11/24 : Completing project and adding process examples, Making announcement.

