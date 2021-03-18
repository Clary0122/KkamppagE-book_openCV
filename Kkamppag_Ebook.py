import cv2, dlib
import time
import numpy as np
from imutils import face_utils
from keras.models import load_model
from flask import Flask, render_template

IMG_SIZE = (34, 26)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

model = load_model('model/20_43_20.h5')
model.summary()

def crop_eye(img, eye_points):
  x1, y1 = np.amin(eye_points, axis=0)
  x2, y2 = np.amax(eye_points, axis=0)
  cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

  w = (x2 - x1) * 1.2
  h = w * IMG_SIZE[1] / IMG_SIZE[0]

  margin_x, margin_y = w / 2, h / 2

  min_x, min_y = int(cx - margin_x), int(cy - margin_y)
  max_x, max_y = int(cx + margin_x), int(cy + margin_y)

  eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)

  eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]

  return eye_img, eye_rect

# main
#cap = cv2.VideoCapture('videos/3.mp4')
cap = cv2.VideoCapture(0)

#변수 초기화
total = 0
double_total = 0
long_total = 0
p1 = 0
d1 = 0
l1 = 0
page = 1
current_page = ''
d_start_time = 0  #double_blink 시작 시간
d_end_time = 0    #double_blink 측정 시간
l_start_time = 0  #long_blink 시작 시간
l_end_time = 0    #long_blink 측정 시간
double_blink = ''
long_blink = ''


while cap.isOpened():
  ret, img_ori = cap.read()

  if not ret:
    break

  img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=0.7, fy=0.7)

  img = img_ori.copy()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  faces = detector(gray)

  for face in faces:
    shapes = predictor(gray, face)
    shapes = face_utils.shape_to_np(shapes)

    eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
    eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])

    eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
    eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
    eye_img_r = cv2.flip(eye_img_r, flipCode=1)

    eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
    eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

    pred_l = model.predict(eye_input_l)
    pred_r = model.predict(eye_input_r)

    # visualize
    state_l = '+ %.1f' if pred_l > 0.1 else '- %.1f'
    state_r = '+ %.1f' if pred_r > 0.1 else '- %.1f'

    state_l = state_l % pred_l
    state_r = state_r % pred_r

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

    cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(255,255,255), thickness=2)
    cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,255,255), thickness=2)

    cv2.putText(img, state_l, tuple(eye_rect_l[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(img, state_r, tuple(eye_rect_r[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    cv2.putText(img, "BLINK: {}".format(str(total)), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,204), 2)
    cv2.putText(img, double_blink, (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

    if (double_blink == ''):
      d1 = 1
    if (double_blink == 'Double Blink') and (d1 == 1):
      double_total = double_total + 1
      page = page + 1
      d1 = 0
      break

    if (long_blink == ''):
      l1 = 1
    if (long_blink == 'Long Blink') and (l1 == 1):
      long_total = long_total + 1
      page = page - 1
      l1 = 0
      break
    
    cv2.putText(img, "D BLINK: {}".format(str(double_total)), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,204), 2)
    cv2.putText(img, long_blink, (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    
    cv2.putText(img, "L BLINK: {}".format(str(long_total)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,204), 2)
    image = cv2.imread("book/{}page.jpg".format(str(page)), cv2.IMREAD_ANYCOLOR)
    cv2.putText(image, "Page: {}".format(str(page)), (400, 900), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (106,90,205), 2)


  cv2.imshow('result', img)
  cv2.imshow('book', image)
  if cv2.waitKey(1) == ord('q'):
    break

