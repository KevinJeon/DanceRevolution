import cv2
import argparse
import numpy as np
import os
import os.path as osp
'''
test_music

'''
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path',
                       default='/home/kevinjeon/uorl_jeon/home/dance/DanceRevolution/outputs/demo_song/Bobby McFerrin - Dont Worry Be Happy (Official Music Video)',
                       type=str)
    parser.add_argument('--output_path', default='./videos', type=str)
    args = parser.parse_args()
    return args

def visaulize(args):
    folders = os.listdir(args.image_path)
    for folder in folders:
        if not osp.exists(osp.join(args.output_path, folder)):
            os.makedirs(osp.join(args.output_path, folder))
        file_path = osp.join(args.image_path, folder) +'/img'
        files = os.listdir(file_path)
        frames = []
        for file in sorted(files):
            print(file)
            img = cv2.imread(osp.join(file_path, file))
            h, w, c = img.shape
            size = (w, h)
            frames.append(img)
        video = osp.join(osp.join(args.output_path, folder), 'video.avi')
        out = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        for frame in frames:
            out.write(frame)
        out.release()




if __name__ == '__main__':
    args = parse_args()
    visaulize(args)