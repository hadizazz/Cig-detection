# Abstrak

	Rokok mengandung zat berbahaya yang dapat menyebabkan ketagihan dan berbagai 
penyakit bahkan hingga menyebabkan kematian. Dampak buruk tersebut tidak hanya 
dirasakan oleh perokok tetapi juga bisa dirasakan oleh masyarakat lainnya saat 
melakukan aktivitas pola hidup sehat terutama di kawasan tanpa asap rokok. Dengan 
demikian penelitian ini untuk membangun model penerapan deep learning pada klasifikasi 
citra untuk mendeteksi orang merokok dan tidak merokok, berbasis website agar dapat
digunakan untuk melakukan monitoring pada kawasan tanpa asap rokok.

	Dalam penelitian ini, metode yang digunakan adalah Convolutional Neural
Network dengan arsitektur MobileNetV2. Dataset yang digunakan berupa gambar orang
merokok dan tidak merokok. Sebelum data di proses akan dilakukan preprocessing data 
yaitu berupa augmentasi data, pemodelan dan implementasi.

	Penelitian ini mengusulkan sebuah aplikasi website menggunakan bahasa
pemrograman Python dengan framework flask. Aplikasi yang dibangun memiliki fitur yang
menampilkan tentang penelitian, penjelasan model, dataset, dan testing dengan 
menggunakan real time webcam atau input file. Hasil dari pengujian menunjukkan nilai 
akurasi 92.45%,presisi sebesar 95.83%, dan recall sebesar 88.46%. 
## Framework
- Keras/Tensorflow
- OpenCV
- Flask
- MobilenetV2

## Cara running aplikasi
1. Lakukan instalasi packages dengan menggunakan 2 cara ini:
- menggunakan pip
```pip install -r requirements.txt```
- menggunakan conda
```conda env create -f environment.yml```

setelah packages terinstal, masukan command di bawah pada root folder:

```
python wsgi.py
```

## Data
Dataset dapat didownload pada website resmi kaggle  <a href="https://www.kaggle.com/omkargurav/face-mask-dataset">disini</a>.

##Referensi
https://github.com/GalileoParise/CV-Mask-detection
