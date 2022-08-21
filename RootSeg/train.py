from tensorflow import keras
import numpy as np
from tensorflow.keras import backend as K
from tensorflow.keras.callbacks import (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau,
                             TensorBoard)
from tensorflow.keras.optimizers import Adam
from PIL import Image
from RootSeg.RootSeg import RootSeg


def generate_arrays_from_file(jpg_path, label_path, lines, batch_size):
    n = len(lines)
    i = 0
    while 1:
        X_train = []
        Y_train = []
        for _ in range(batch_size):
            if i == 0:
                np.random.shuffle(lines)
            name = lines[i].split(';')[0]
            img = Image.open(jpg_path + name)
            img = img.resize((WIDTH, HEIGHT))
            img = np.array(img)
            img = np.reshape(img, [WIDTH, HEIGHT, 3])
            img = img / 255
            X_train.append(img)

            name = (lines[i].split(';')[1]).replace("\n", "")
            img = Image.open(label_path + name)
            img = img.resize((WIDTH, HEIGHT))
            img = np.array(img)
            seg_labels = np.zeros((int(HEIGHT), int(WIDTH), NCLASSES))
            for c in range(NCLASSES):
                seg_labels[:, :, c] = (img[:, :, 0] == c).astype(int)
            seg_labels = np.reshape(seg_labels, (-1, NCLASSES))
            Y_train.append(seg_labels)

            i = (i + 1) % n
        X_train = np.array(X_train)
        Y_train = np.array(Y_train)

        yield (np.array(X_train), np.array(Y_train))

if __name__ == "__main__":
    # input image size
    HEIGHT = 512
    WIDTH = 512
    # background + root = 2
    NCLASSES = 2
    lr = 1e-4
    batch_size = 16
    epoch = 200
    train_list_path = ""
    # save model weight files and tensorboard log files
    log_dir = ""
    jpg_path = ""
    label_path = ""

    model = RootSeg(n_classes=NCLASSES,input_height=HEIGHT, input_width=WIDTH)

    with open(train_list_path,"r") as f:
        lines = f.readlines()
        
    np.random.seed(10101)
    np.random.shuffle(lines)
    np.random.seed(None)
    num_val = int(len(lines)*0.1)
    num_train = len(lines) - num_val

    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
                                    monitor='val_loss', save_weights_only=True, save_best_only=False, period=2)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)


    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=lr),
                  metrics=['accuracy'])
    Tensorboard = TensorBoard(log_dir=log_dir, histogram_freq=1, write_grads=True)
    print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
    model.fit_generator(generate_arrays_from_file(jpg_path, label_path, lines[:num_train], batch_size),
                        steps_per_epoch=max(1, num_train // batch_size),
                        validation_data=generate_arrays_from_file(jpg_path, label_path, lines[num_train:], batch_size),
                        validation_steps=max(1, num_val // batch_size),
                        epochs=epoch,
                        initial_epoch=0,
                        callbacks=[checkpoint, reduce_lr, early_stopping,Tensorboard])