import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--anno_json', type=str, default='data.json', help='training model path')#--anno_json  /Users/86181/Desktop/yolov8/data.json  
    parser.add_argument('--pred_json', type=str, default='', help='data yaml path')#--pred_json  /Users/86181/Desktop/yolov8/runs/val/exp3/predictions.json
    
    return parser.parse_known_args()[0]

if __name__ == '__main__':
    opt = parse_opt()
    anno_json = opt.anno_json
    pred_json = opt.pred_json
    
    anno = COCO(anno_json)  # init annotations api
    pred = anno.loadRes(pred_json)  # init predictions api
    eval = COCOeval(anno, pred, 'bbox')
    eval.evaluate()
    eval.accumulate()
    eval.summarize()


    #python get_COCO_metrice.py --pred_json runs/val/exp3/predictions.json --anno_json data.json 