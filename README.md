# PBP Tugas 2 Django

[Katalog App](https://pbp-tugas2.herokuapp.com/katalog/)

## Bagan Request Cient Flow Django
![Bagan](https://github.com/electyrion/tugas2-pbp/blob/main/assets/images/bagan.png)
Penjelasan:
1. Ketika user mengakses suatu web-application, user mengirimkan HTTP Request ke server
2. urls.py menangkap request yang dikirim oleh user kemudian menghubungkannya ke view yang bersesuaian dengan request URL. urls.py juga mampu mencocokkan pola string maupun digit tertentu yang muncul pada URL dan mengantarkannya menuju view function sebagai data.
3. views.py berperan sebagai fungsi yang melakukan request handler yang menerima HTTP request kemudian me-return HTTP respose. view dapat mengakses data yang dibutuhkan untuk memenuhi request melalui models dan menyerahkan format dari response ke templates yang telah tersedia
4. Models merupakan python object yang mendefinisikan struktur data dari suatu applikasi dan menyediakan mekanisme untuk mengatur (add, modify, delet) dan memaasukkan query kedalam database
5. Template merupakan file teks yang mendefinisikan struktur maupun tampilan dari suatu file seperti halaman HTML dengan placeholder yang dapat digunakan untuk merepresentasikan konten yang sebenarnya. View dapat membuat halaman HTML secara dinamis menggunakan HTML template dan mengisinya dengan data dari model. Template juga dapat digunakan untuk mendefinisikan struktur dari file berjenis apapun tidak hanya HTML saja.

## Mengapa perlu virtual environtment?

Ketika sedang mengembangkan suatu aplikasi Python, pendekatan yang biasa digunakan adalah dengan menginstall Python, menginstall seluruh library yand diperlukan melalui terminal, menulis semua code dalam satu file .py kemudian menjalankan program python tersebut melalui terminal. Hal tersebut merupakan pendekatan paling umum yang biasanya digunakan oleh pemula. Pendekatan seperti tadi akan berjalan sempurna pada project yang berskala kecil. Namun, saat akan mengembangkan software yang kompleks, kita akan berurusan dengan banyak sekali file, packages, dan dependensi. Akibatnya, kita harus mengisolasi python environtment hanya untuk project tertentu saja. Penggunaan virtual environtment dapat menghidarkan kita dari error yang muncul akibat perbedaan versi dan jenis dependensi yang dibutuhkan untuk project yang berbeda. Virtual environtment berguna untuk mengisolasi python yang kita gunakan untuk membangun suatu project dengan python yang terinstall secara global pada system. Hal tersebut memberikan kita kontrol penuh atas project yang sedang berjalan dan membuatnnya mudah untuk dirpoduksi.

## Apakah bisa membuat aplilkasi web berbasis Django tanpa virtual environtment?

Penggunaan virtual environtment pada saat mengembangkan aplikasi web berbasis Django tidak wajib dilakukan. Namun, seperti yang sudah dijelaskan di atas, proses pengembangan aplikasi web berbasi Django yang tidak menggunakan virtual environtment akan menyusahkan para pengembang dikemudian hari seiring dengan semakin membesarnya ukuran suatu proyek. Jika kita sedang membangun beberapa aplilkasi berbasis Django secara bersamaan namun hanya menggunakan python yang terinstal secara global pada system maka akan sangat memungkinkan timbul adanya error yang tidak diinginkan. Error tersebut bisa saja muncul karena disebabkan oleh perbedaan versi dan jenis dependensi yang dibutuhkan pada setiap proyek yang sedang dikerjakan. Kesimpulannya, penggunaan virtual environtment sangat dianjurkan pada saat mengembangkan aplikasi berbasi Django agar dapat memudahkan proses pengembangannya.

## Implementasi aplikasi katalog

1. Pada views.py yang berada pada folder aplikasi katalog perlu dibuat suatu fungsi bernama show_katalog yang menerima parameter `request` dan me-return `render(request, “katalog.hml”)`.
2. Buat file baru bernama `urls.py` pada folder aplikasi `katalog` untuk melakukan routing terhadap fungsi `views` yang baru saja dibuat sehingga nantinya halaman HTML katalog dapat ditampilkan pada browser client. Tambahkan juga aplikasi `katalog` ke dalam `urls.py` yang terdapat pada folder `project_django` dengan menambahkan kode `path(‘katalog/‘, include(‘katalog.urls.’))` pada variabel `urlpatterns`
3. Load data json menggunakan syntax *python manage.py loaddata initial_catalog_data.json*. Pada fungsi views yang telah dibuat, import models yang sudah ada ke dalam file `views.py`, kemudian dalam fungsi `show_katalog` yang sudah dibuat sebelumnya tambahkan potongan kode berikut:
```shell
data_item_katalog = CatalogItem.objects.all()
   context = {
      'list_item’: data_item_katalog,
      'nama': 'Vicky'
   }
```
kemudian tambahkan `context` sebagai parameter ketiga pada pengembalian fungsi render yang sudah dibuat sebelumnya. Data yang ada pada variabel `context` tersebut akan ikut di-render oleh Django sehingga nantinya data dapat muncul di halaman HTML. Untuk menampilkan daftar katalog ke dalam tabel, perlu dilakukan iterasi terhadap variabel `list_item` yang telah dirender ke dalam file HTML.
4. Untuk melakukan deploy, pertama tambahkan file Procfile yang berguna untuk mengatur deployment. Selanjutnya pilih menu buat aplilkasi baru pada Heroku, hubungkan ke repository di github, setting api_key, dan selamat aplikasi katalog telah berhasil dideploy

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.