ledtest:
	/usr/bin/python3 ./pwmtest.py

motortest:
	/usr/bin/python3 ./motortest.py

serve:
	flask run --host=0.0.0.0

camera:
	python ./serve_camera.py	
