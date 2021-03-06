# KkamppagE-book
## project_KkamppagE-book_opencv
๐ ๊น๋นกE-book :: openCV๋ก ๊ฐ๋จํ ๋ ๊น๋นก์ ํ์ด์ง ์กฐ์ ์์คํ ๊ตฌํ ๐
* 2020 ํ๋ก์ ํธ ์ขํฉ ์ค๊ณ '๊น๋นกE-book'
* ํ๋ก์ ํธ ๊ธฐ๊ฐ : 2020.03 ~ 2020.04 
  
  
## ๊ธฐํ ๋ฐฐ๊ฒฝ
![image](https://user-images.githubusercontent.com/79209568/111514869-7fdd0480-8795-11eb-8308-da4093e7ca23.png)
  
### ์ ์์ฑ ์์ฅ์ ํํฉ ๋ถ์
* ํด๋์ฉ ์ ์๊ธฐ๊ธฐ ์ฌ์ฉ ์ฆ๊ฐ
* COVID-19๋ก ์ธํ ๋น๋๋ฉดโ๋น์ ์ด ์๋น์ค ์ฆ๊ฐ
> ์๋ ๋๋น ์ ์์ฑ ๋งค์ถ 15~20% ์ฆ๊ฐ  

### ๋์์ฅ์ ์ธ์ ๋์์ ๊ทผ์ฑ
* ๊ธฐ์กด์ ํฐ์นโํด๋ฆญ์์ผ๋ก ๋์ํ๋ ์ ์์ฑ์ ์์ด ๋ถํธํ ๋์์ฅ์ ์ธ์ ๋ฎ์ ๋์์ ๊ทผ์ฑ์ ํด๊ฒฐ์ด ์ด๋ ค์
* **๋ ๊น๋นก์์ผ๋ก ํ์ด์ง๋ฅผ ์กฐ์**ํ  ์ ์๋ ํ๋ก๊ทธ๋จ์ ํตํด ๋์์ฅ์ ์ธ์ ๋์ ํธ์๋ฅผ ๋๋ชจ  
  
  
## ์์คํ ๋์
![image](https://user-images.githubusercontent.com/79209568/111637653-fc76ee00-883c-11eb-8118-d57b547d74d6.png)
  
  
## Usage
* ํ๋กฌํํธ์์ ํด๋น ํ๋ก์ ํธ ์์น๋ก ์ด๋
* Kkamppag_Ebook.py ์คํ
  
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

#start_time๊ณผ end_time ์ฐจ์ด๊ฐ 0.9์ด ์ดํ๋ฉด double blink
double_blink = '' if d_end_time >= 0.9 else 'Double Blink'

#๊ฐ์ ์ํ๋ก 1์ด ์ด์์ด๋ฉด long blink
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
  
  
  
## ์์คํ ์ค๊ณ
![image](https://user-images.githubusercontent.com/79209568/111575966-dd536e80-87f2-11eb-94f7-d78b5eae1802.png)

1. ๊ฐ์ ๋๊ณผ ๋ฌ ๋์ผ๋ก ๊ตฌ์ฑ๋ [๋ฐ์ดํฐ์](#Blink-Dataset)์ ์ฌ์ฉํด์ ๋์ด ๋ ์ ธ์๋ ์ํ์๋ 1.0, ๋์ด ๊ฐ๊ฒจ์๋ ์ํ์๋ 0.0์ ์์ธกํ๋ ๋ชจ๋ธ์ ์์ฑํ๋ค.   
(Using a dataset consist of closed eyes and open eyes, build a model that predicts 1.0 for open eyes and 0.0 for closed eyes.)  
[๐๋ชจ๋ธ์์ฑ๊ณผ์ ๐](https://github.com/chaeyun0122/KkamppagE-book_openCV/blob/main/preprocessing_train.ipynb)
   
2. ์น์บ ์ผ๋ก๋ถํฐ ์ฌ์ฉ์์ [์ผ๊ตด์ ์ธ์](#์ผ๊ตด-์ธ์)ํ๋ค.  
(Recognize the user's face from the webcam.)  
  
3. ์ธ์ํ ์ฌ์ฉ์์ ์ผ๊ตด์์ ๋์ ํฌ๋กญํ์ฌ ๋ ๊น๋นก์ ๊ฐ์ง ๋ชจ๋ธ์ ์ ์ฉํ๋ค.  
(Apply blink detection model to cropped eyes)  
  
4. ์ค์๊ฐ์ผ๋ก ์ฌ์ฉ์์ ๋ ๊น๋นก์์ ๋ฐ๋ผ 0~1 ์ฌ์ด์ ์์ธก๊ฐ์ด ๊น๋นก์ ์ํ ๋ณ์(pred_l, pred_r)์ ์๋ฐ์ดํธ๋๋ค. <sub>[์ฐธ๊ณ  ์ฝ๋](#์ฐธ๊ณ -์ฝ๋)</sub>  
(As users blink in real time, prediction values between 0 and 1 are updated in the blink state variable.)  
  
  
## ํ์ ๋ชจ๋
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
* ๊ฐ์ ๋๊ณผ ๋ฌ ๋ ๋ฐ์ดํฐ์
* [๐URL๐](https://github.com/kairess/eye_blink_detector/blob/118b15c7a1444411cc823a540b23ad2db94c7167/dataset/dataset.csv)

### ์ผ๊ตด ์ธ์
* ํ์ต๋ ์ผ๊ตด ์ธ์ ๋ชจ๋ธ ์ฌ์ฉ
* [๐URL๐](https://github.com/davisking/dlib-models/blob/4232818ed889ba60e33d5bf5fc47d28f27a911f9/shape_predictor_68_face_landmarks.dat.bz2)

### ์ฐธ๊ณ  ์ฝ๋
* video capture, ๋ ๊น๋นก์ ์ธ์ ์ฝ๋ ์ฐธ๊ณ 
* [๐URL๐](https://github.com/kairess/eye_blink_detector/blob/118b15c7a1444411cc823a540b23ad2db94c7167/test.py)
  
> #### [๐บ  Go back to original text](#์์คํ-์ค๊ณ)  
  
  
## ๊น๋นกE-book์ ๋ค๋ฅธ ํ๋ก์ ํธ
* [ANDROID](https://github.com/chaeyun0122/KkamppagE-book_Android.git)
