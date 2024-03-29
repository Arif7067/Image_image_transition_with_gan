# -*- coding: utf-8 -*-
"""Custom_satellite_raod_image_translation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fLJYXaGStDpLW67OKeB9_Ymv0iG-42HJ
"""

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model

"""Downsampling of images

"""

def downsample(filters, size, strides = 2,apply_batchnorm = True):
  init = tf.random_normal_initializer(0. , 0.02)

  result = tf.keras.Sequential()
  result.add(tf.keras.layers.Conv2D(filters, size, strides, padding ='same',kernel_initializer = init, use_bias=False))

  if apply_batchnorm:
    result.add(tf.keras.layers.BatchNormalization())

  result.add(tf.keras.layers.LeakyReLU(alpha=0.2))

  return result

def Discriminator(image_shape):
  #weight initializer
  init = tf.random_normal_initializer(0. ,0.02)

  #source input image
  in_source_image = tf.keras.Input(shape=image_shape)
  #target  input image
  in_target_image = tf.keras.Input(shape=image_shape)

  #conacte images, channel wise
  x_merged = tf.keras.layers.concatenate([in_source_image, in_target_image])

  # C64: 4x4 kernel Stride 2x2
  dis = downsample(64,4,apply_batchnorm=False)(x_merged)

  #C128: 4 kernel, strides 2
  dis = downsample(128,4)(dis)

  #C256, 4kernel, 2 strides
  dis = downsample(256,4)(dis)

  #C512, 4 kernel, strides 2
  dis = downsample(512,4)(dis)

  #C512, 4 kernel, strides 1
  dis = downsample(512,4,strides=1)(dis)

  #patch output
  dis = tf.keras.layers.Conv2D(1,(4,4),padding = 'same', kernel_initializer = init)(dis)
  patch_output = tf.keras.layers.Activation('sigmoid')(dis)

  # define model
  model = Model([in_source_image, in_target_image], patch_output)

  # compile model
  # opt = Adam(lr=0.0002, beta_1=0.5)
  model.compile(loss="binary_crossentropy", optimizer=tf.keras.optimizers.Adam(lr=0.0002, beta_1=0.5), loss_weights=[0.5])

  return model

disc_model = Discriminator((256,256,3))
plot_model(disc_model, to_file ="disc_model.png", show_shapes=True)

#encoder for generator
def encoder_block(layers_in,n_filters, size, apply_batchnorm=True):
  # weight initialization
  init = tf.random_normal_initializer(0. , 0.02)
  # add downsampling layer
  g = tf.keras.layers.Conv2D(n_filters, size,strides=2,padding="same",kernel_initializer=init,use_bias=False)(layers_in)

  if apply_batchnorm:
    g = tf.keras.layers.BatchNormalization()(g,training=True)
  g = tf.keras.layers.LeakyReLU(alpha=0.2)(g)
  return g

# decoder for generator
def decoder_block(layers_in,skip_in, n_filters, size ,apply_droupout=True, apply_batchnorm=True):
  #weight initialization
  init = tf.random_normal_initializer(0. , 0.02)
  # add upsampling layer
  g = tf.keras.layers.Conv2DTranspose(n_filters, size,strides=2,padding="same",kernel_initializer=init,use_bias=False)(layers_in)
  # add batch normalization
  g = tf.keras.layers.BatchNormalization()(g , training=True)
  # conditionally add droupout
  if apply_droupout:
    g = tf.keras.layers.Dropout(0.5)(g ,training=True)
  # merge the skip connection
  g = tf.keras.layers.Concatenate()([g, skip_in])
  # relu activation
  g = tf.keras.layers.Activation('relu')(g)
  return g

# defining generator
def generator(image_shape=(256,256,3)):
  # weigth initializer
  init = tf.random_normal_initializer(0. , 0.02)
  # image input
  in_source_image = tf.keras.Input(shape=image_shape)

  # encoder block : C64-C128-C256-C512-C512-C512-C512-C512
  encoder1 = encoder_block(in_source_image, 64, 4, apply_batchnorm=False);
  encoder2 = encoder_block(encoder1, 128,4)
  encoder3 = encoder_block(encoder2,256,4)
  encoder4 = encoder_block(encoder3, 512,4)
  encoder5 = encoder_block(encoder4, 512,4)
  encoder6 = encoder_block(encoder5, 512,4)
  encoder7 = encoder_block(encoder6, 512,4)

  # bottleneck with no batch normalization and relu function in it
  encoder8 = tf.keras.layers.Conv2D(512, (4,4), strides =(2,2), padding = "same", kernel_initializer=init)(encoder7)
  encoder8 = tf.keras.layers.Activation("relu")(encoder8)

  # decoder block: CD512-CD512-CD512-C512-C256-C128-C64
  decoder1 = decoder_block(encoder8, encoder7, 512,4)
  decoder2 = decoder_block(decoder1, encoder6, 512,4)
  decoder3 = decoder_block(decoder2, encoder5, 512,4)
  decoder4 = decoder_block(decoder3, encoder4, 512,4, apply_droupout=False)
  decoder5 = decoder_block(decoder4, encoder3, 256,4, apply_droupout=False)
  decoder6 = decoder_block(decoder5, encoder2, 128,4, apply_droupout=False)
  decoder7 = decoder_block(decoder6, encoder1, 64, 4, apply_droupout=False)

  #output generation
  output = tf.keras.layers.Conv2DTranspose(image_shape[2], (4,4), strides=(2,2), padding = 'same', kernel_initializer=init)(decoder7)
  out_image = tf.keras.layers.Activation('tanh')(output)

  #defib=ne model
  model = Model(in_source_image, out_image)
  return model

disc_on_model = generator()
plot_model(disc_on_model, to_file ="disc_model_generator.png", show_shapes=True)

