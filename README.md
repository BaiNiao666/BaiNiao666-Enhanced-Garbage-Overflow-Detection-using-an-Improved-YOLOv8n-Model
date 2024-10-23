# BaiNiao666-Enhanced-Garbage-Overflow-Detection-using-an-Improved-YOLOv8n-Model
# Setup prerequisites:
The experiments were conducted on a 64-bit Windows 11 OS, using Python 3.8, CUDA 11.8, an NVIDIA GeForce RTX 4090 GPU, a Xeon Platinum 8352V CPU, 24GB VRAM, and 90GB RAM. The training batch size was 8, with 200 epochs. SGD optimizer was used, and mosaic was disabled in the last 10 epochs.

# Data preparation:
The dataset, sourced from https://aistudio.baidu.com/datasetdetail/228648, contains 3349 images, divided into training (2344), testing (670), and validation (335) sets in a 7:2:1 ratio. It includes three categories: overflowing trash cans, non-overflowing trash cans, and garbage.
# Training & testing:
# 1.在data.yaml文件下配置地址：
    path: /Users/86181/Desktop/yolov8-main/
    train: ./dataset/laji/images/train
    val: ./dataset/laji/images/val
    test: ./dataset/laji/images/test
# 2.在trin.py文件下设置model：
    model = YOLO('ultralytics/cfg/models/v8/yolov8.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=8,
                close_mosaic=10,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                # resume='runs/train/v8n-innermdpiou/weights/last.last.pt', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='v8n-mdpiou',
                )
