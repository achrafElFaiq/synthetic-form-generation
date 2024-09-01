from datetime import datetime

import synth_form_dataset
import math
import sys
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import Polygon
import numpy as np
import torch
import utils.img_f as cv2
import json
import os


widths=[]


def generate(data, write, draw=False, writeNoJson=False, do_masks=True, tokenizer=None):
    '''Generates the images, and optionally saves them or displays them.
    '''
    global i
    batchSize = data['img'].size(0)
    print(f"batchSize = {batchSize}")
    # Pour toutes les images
    for b in range(batchSize):
    		# Mise au format
        img = (1-data['img'][b,0:1].permute(1,2,0))/2.0
        img = torch.cat((img,img,img),dim=2)
        if do_masks:
          show = data['img'][b,1]>0
          mask = data['img'][b,1]<0
          img[:,:,0] *= ~mask
          img[:,:,1] *= ~show
        if data['mask_label'] is not None:
            img[:,:,2] *= 1-data['mask_label'][b,0]
        # Affichage du contenu futur du json
        print(data['imgName'][b])
        print('{} - {}'.format(data['img'].min(),data['img'].max()))
        print('questions and answers')
        for q,a in zip(data['questions'][b],data['answers'][b]):
           print(q+' : '+a)
        tok_len=-1
        if write and (q=='json>' or writeNoJson):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generate a timestamp
            filename = f"result/synth_form_example_{timestamp}.png"  # Construct the filename
            filenameTemp = filename
            j = 0
            while os.path.exists(filenameTemp):
                j += 1
                filenameTemp = filename.split('.')[0] + '_' + str(j) + ".png"
            cv2.imwrite(filenameTemp, (img.numpy() * 255)[:, :, 0].astype(np.uint8))
            i += 1
            # Ecriture du json
            if q=='json>':
                a=a[:-1]
                data=json.loads(a)
                with open(filenameTemp.split('.')[0] + ".json",'w') as f:
                  json.dump(data, f, indent=4)
        if draw :
            cv2.imshow('x',(img*255).numpy().astype(np.uint8))
            cv2.show()
    print('batch complete')
    return tok_len


if __name__ == "__main__":
		# Gestion des paramètres : Dossier de données, sauvegarde des images ou non, sauvegarde des images ne pouvant pas être converties en .json ou non, et nombre d'itérations
    if len(sys.argv)>1:
        repeat = int(sys.argv[1])
    else:
        repeat=100
    if len(sys.argv)>2:
        write = (sys.argv[2].lower() == "true")
    else:
        write = True
    if len(sys.argv)>3:
        writeNoJson = (sys.argv[3].lower() == "true")
    else:
        writeNoJson = False
    if len(sys.argv)>4:
        dirPath = sys.argv[4]
    else:
        dirPath = './data/'
    if len(sys.argv)>5:
        do_masks = (sys.argv[5].lower() == "true")
    else:
        do_masks = True

    data = synth_form_dataset.SynthFormDataset(dirPath=dirPath, split='train', config={
  	"data_set_name": "SynthFormDataset",
        "font_dir": "./data/fonts",
        "batch_size": repeat,
        "rescale_range": [1.0,1.0],
        "crop_params": {
                "crop_size":[1152,768],
                "pad":0,
                "rot_degree_std_dev": 1
            },
        "do_masks": do_masks,
        "questions": 1,
        "image_size": [1150,760],
        "cased": True,
        "color": True,
        "use_json": 'streamlined',
        "shuffle": True,
        "max_qa_len_out": 500,
        "max_qa_len_in": 500,
})

    dataLoader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=True, num_workers=0, collate_fn=synth_form_dataset.collate)
    dataLoaderIter = iter(dataLoader)

    tokenizer=None
    max_tok_len=0
    
    if write:
        try:
            os.mkdir('result')
        except FileExistsError:
            pass
    
    i = 0
    
    try:
        while i < repeat:
            tl = generate(next(dataLoaderIter), write, False, writeNoJson, do_masks, tokenizer)
            max_tok_len = max(max_tok_len,tl)
    except StopIteration:
        pass
    print('done')
    print('max')
    print(max_tok_len)
