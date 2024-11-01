import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=8,
                close_mosaic=10,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                # resume='runs/train/aux-attention/weights/last.pt', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='v8n-inner0.9',
                )