# KkamppagE-book
## project_KkamppagE-book_opencv
👀 깜빡E-book :: openCV로 간단한 눈 깜빡임 페이지 조작 시스템 구현 👀
* 2020 프로젝트 종합 설계 '깜빡E-book'
* 프로젝트 기간 : 2020.03 ~ 2020.04 
  
  
## 기획 배경
![image](https://user-images.githubusercontent.com/79209568/111514869-7fdd0480-8795-11eb-8308-da4093e7ca23.png)
  
### 전자책 시장의 현황 분석
* 휴대용 전자기기 사용 증가
* COVID-19로 인한 비대면∙비접촉 서비스 증가
> 작년 대비 전자책 매출 15~20% 증가  

### 독서장애인의 독서접근성
* 기존의 터치∙클릭식으로 동작하는 전자책은 손이 불편한 독서장애인의 낮은 독서접근성의 해결이 어려움
* **눈 깜빡임으로 페이지를 조작**할 수 있는 프로그램을 통해 독서장애인의 독서 편의를 도모  
  
  
## 시스템 동작
![image](https://user-images.githubusercontent.com/79209568/111637653-fc76ee00-883c-11eb-8118-d57b547d74d6.png)
  
  
## Usage
* 프롬프트에서 해당 프로젝트 위치로 이동
* Kkamppag_Ebook.py 실행
  
  ```shell
  python Kkamppag_Ebook.py
  ```  
  
  
```python
#blink & double blink
if (pred_l < 0.1) and (pred_r < 0.1):
  p1 = 1
  d_end_time = time.time() - d_start_time
if (p1 == 1) and ((pred_l >= 0.3) or (pred_r >= 0.3)):
  total = total + 1
  p1 = 0
  d_start_time = time.time()

#long blink
if (pred_l < 0.1) and (pred_r < 0.1):
  l_end_time = time.time() - l_start_time
if (pred_l >= 0.3) or (pred_r >= 0.3):
  l_start_time = time.time()

#start_time과 end_time 차이가 0.9초 이하면 double blink
double_blink = '' if d_end_time >= 0.9 else 'Double Blink'

#감은 상태로 1초 이상이면 long blink
long_blink = '' if l_end_time < 1.0 else 'Long Blink'
```


## Demo
### Blink
* **No page Movement**
![blink](https://user-images.githubusercontent.com/79209568/111640732-d3a42800-883f-11eb-895c-d4851d4f18d6.gif)

### Double Blink
* **Next page**
![double_blink](https://user-images.githubusercontent.com/79209568/111641323-60e77c80-8840-11eb-884b-88606980ee86.gif)

### Long Blink
* **Previous page**
![long_blink](https://user-images.githubusercontent.com/79209568/111641879-ea974a00-8840-11eb-9f58-1f1e6b378899.gif)
  
  
  
## 시스템 설계
![image](https://user-images.githubusercontent.com/79209568/111575966-dd536e80-87f2-11eb-94f7-d78b5eae1802.png)

1. 감은 눈과 뜬 눈으로 구성된 [데이터셋](#Blink-Dataset)을 사용해서 눈이 떠져있는 상태에는 1.0, 눈이 감겨있는 상태에는 0.0을 예측하는 모델을 생성한다.   
(Using a dataset consist of closed eyes and open eyes, build a model that predicts 1.0 for open eyes and 0.0 for closed eyes.)  
[👉모델생성과정👈](https://github.com/chaeyun0122/KkamppagE-book_openCV/blob/main/preprocessing_train.ipynb)
   
2. 웹캠으로부터 사용자의 [얼굴을 인식](#얼굴-인식)한다.  
(Recognize the user's face from the webcam.)  
  
3. 인식한 사용자의 얼굴에서 눈을 크롭하여 눈 깜빡임 감지 모델을 적용한다.  
(Apply blink detection model to cropped eyes)  
  
4. 실시간으로 사용자의 눈 깜빡임에 따라 0~1 사이의 예측값이 깜빡임 상태 변수(pred_l, pred_r)에 업데이트된다. <sub>[참고 코드](#참고-코드)</sub>  
(As users blink in real time, prediction values between 0 and 1 are updated in the blink state variable.)  
  
  
## 필요 모듈
* cv2
* dlib
     > - Install cmake in prompt  
      ```
      pip install cmake
      ```   
     > - Download dlib file in [this web](http://dlib.net/) and unzip.   
     > - Prompt again, Go to the place where 'dlib' is located and write the code in turn.   
      ```
      python setup.py build
      ```   
      ```
      python setup.py install
      ```   
* imutils
* keras
* time  
  
  
## References
### Blink Dataset
* 감은 눈과 뜬 눈 데이터셋
* [👉URL👈](https://github.com/kairess/eye_blink_detector/blob/118b15c7a1444411cc823a540b23ad2db94c7167/dataset/dataset.csv)

### 얼굴 인식
* 학습된 얼굴 인식 모델 사용
* [👉URL👈](https://github.com/davisking/dlib-models/blob/4232818ed889ba60e33d5bf5fc47d28f27a911f9/shape_predictor_68_face_landmarks.dat.bz2)

### 참고 코드
* video capture, 눈 깜빡임 인식 코드 참고
* [👉URL👈](https://github.com/kairess/eye_blink_detector/blob/118b15c7a1444411cc823a540b23ad2db94c7167/test.py)
  
> #### [🔺  Go back to original text](#시스템-설계)  
  
  
## 깜빡E-book의 다른 프로젝트
* [ANDROID](https://github.com/chaeyun0122/KkamppagE-book_Android.git)
