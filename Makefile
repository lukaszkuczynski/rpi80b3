install:
	pip install -r ./requirements.txt

ledtest:
	/usr/bin/python3 ./pwmtest.py

motortest:
	/usr/bin/python3 ./motortest.py

serve:
	flask run --host=0.0.0.0

camera:
	python ./serve_camera.py	

detector:
	python detect_picamera.py   --model tfmodels/detect.tflite   --labels tfmodels/coco_labels.txt --threshold 0.1
