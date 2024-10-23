import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/YOLO v8n/weights/best.pt') # select your model.pt path
    model.predict(source='dataset/laji/images/val',
                project='runs/detect',
                name='aux+DAT',
                save=True,
                # visualize=True # visualize model features maps
                )