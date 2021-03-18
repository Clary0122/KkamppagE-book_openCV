# KkamppagE-book
## project_KkamppagE-book_opencv
👀 깜빡E-book :: 눈 깜빡임으로 E-book 페이지 조작 👀 
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
  
## 시스템 설계
![image](https://user-images.githubusercontent.com/79209568/111575966-dd536e80-87f2-11eb-94f7-d78b5eae1802.png)

1. 감은 눈과 뜬 눈으로 구성된 데이터셋을 사용해서 눈이 떠져있는 상태에는 1.0, 눈이 감겨있는 상태에는 0.0을 예측하는 모델을 생성한다.  
(Using a dataset consist of closed eyes and open eyes, build a model that predicts 1.0 for open eyes and 0.0 for closed eyes.)
  
2. 웹캠으로부터 사용자의 얼굴을 인식한다.  
(Recognize the user's face from the webcam.)

3. 인식한 사용자의 얼굴에서 눈을 크롭하여 눈 깜빡임 감지 모델을 적용한다.  
(Apply blink detection model to cropped eyes)

4. 실시간으로 사용자의 눈 깜빡임에 따라 0~1 사이의 예측값이 깜빡임 상태 변수(pred_l, pred_r)에 업데이트된다.   
(As users blink in real time, prediction values between 0 and 1 are updated in the blink state variable.)  
  
## 시스템 동작
![image](https://user-images.githubusercontent.com/79209568/111637653-fc76ee00-883c-11eb-8118-d57b547d74d6.png)
  
## Demo
### Blink
* No page Movement
![blink](https://user-images.githubusercontent.com/79209568/111640732-d3a42800-883f-11eb-895c-d4851d4f18d6.gif)

### Double Blink
* Next page
![double_blink](https://user-images.githubusercontent.com/79209568/111641323-60e77c80-8840-11eb-884b-88606980ee86.gif)

### Long Blink
* Previous page
![long_blink](https://user-images.githubusercontent.com/79209568/111641879-ea974a00-8840-11eb-9f58-1f1e6b378899.gif)
  
  
## 실행하기
### 필요 모듈
* Click for download method
  <details>
  <summary>cv2</summary>
  <div markdown="1">       
    ```shell
    pip install opencv-python
    ```
  </div>
  </details>
  <details>
  <summary>dlib</summary>
  <div markdown="1">       
    * Install cmake in console
    ```shell
    pip install cmake
    ```
    * Download dlib file in [this web](http://dlib.net/) and unzip.
    * console again, Go to the place where 'dlib' is located and write the code in turn.
    ```shell
    python setup.py build
    ```
    ```shell
    python setup.py install
    ```
  </div>
  </details>
  <details>
  <summary>numpy</summary>
  <div markdown="1">       
    ```shell
    pip install numpy
    ```
  </div>
  </details>
  <details>
  <summary>imutils</summary>
  <div markdown="1">       
    ```shell
    pip install imutils
    ```
  </div>
  </details>
  <details>
  <summary>keras</summary>
  <div markdown="1">       
    ```shell
    pip install Keras
    ```
  </div>
  </details>

### 실행

