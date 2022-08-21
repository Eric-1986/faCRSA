from RootSeg.RootSeg import RootSeg
import tensorflow as tf
import tensorflow.keras
    
if __name__ == "__main__":
    model = RootSeg()
    model.summary()
    for i, layer in enumerate(model.layers):
        print(i, layer.name)