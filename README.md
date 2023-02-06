# Abstrak
	Coronavirus disease 2019 (COVID-19) merupakan penyakit infeksi
pernapasan akut yang dapat mematikan, dan dapat menyebar dengan sangat mudah.
Salah satu bentuk penanganan yang dapat dilakukan oleh setiap individu adalah
penggunaan masker. Saat manusia terbatuk, bersin dan berbicara dapat
mengeluarkan droplet berupa air liur. Penggunaan masker dapat mereduksi
perpindahan droplet yang keluar dari mulut ke orang lain.
	Penelitian ini bertujuan untuk melakukan prediksi kepada seseorang apakah
dia menggunakan masker atau tidak menggunakan masker dengan memanfaatkan
model deep learning convolution neural network. Dengan menggunakan dataset
berupa foto orang yang menggunakan masker dan tidak menggunakan masker
diolah melalu tahap preprocessing, augmentasi data, dan pemodelan. Dari hasil
model ini dapat diprediksi apakah seseorang menggunakan masker atau tidak
menggunakan masker
	Dari hasil penelitian didapat nilai akurasi dari validasi model sebesar 100%
dan nilai validation loss sebesar 0,14%. Dan akurasi dari pengujian sebesar 93,3%
jika dilakukan dengan kondisi penguji yaitu menggunakan masker dengan benar
dan tidak menggunakan masker. Dari hasil tersebut dapat disimpulkan bahwa
pemodelan untuk mendeteksi penggunaan masker sudah dapat berjalan dengan
sangat baik untuk pendeteksian penggunaan masker

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
