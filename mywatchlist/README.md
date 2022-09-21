# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[MyWatchList App](https://pbp-tugas2.herokuapp.com/mywatchlist/)

## Perbedaan antara JSON, HTML, dan XML

JSON | HTML | XML
:---: | :---: | :---:
Object JSON memiliki tipe | HTML dapat melakukan mapping data | XML data tidak memiliki tipe
JSON didukung oleh berbagai browser | Didukung oleh banyak browser yang beredar di pasaran | Melakukan parse XML antar browser terkadang sulit
JSON tidak memiliki kemampuan medsiplay data | Mudah melakukan display data melalui browser | XML dapat mendisplay datanya karena tergolong kedalam markup language
Hanya mendukung jenis encodin UTF-8 | Mendukung banyak jenis encoding | Mendukung berbagai jenis tipe encoding
Tidak mendukung adanya comments | Memperbolehkan adanya comments | Memperbolehkan adanya comments
Konten JSON lebih mudah dibaca Jika dibandingkan dengan XML | Mendukung argumen tag untuk memudahkan pembacaan data | Dokumen XML relatif sulit dibaca dan diinterpretasi

## Pentingnya Data Delivery dalam Implementasi Platform

Suatu aplikasi memerlukan adanya pertukaran data yang terjadi antara client dengan server. Terjadi interaksi antar web server dengan client sehingga data tidak memungkinkan untuk disajikan secara statis, pasti terjadi yang namanya pertukaran data sehingga data pada aplikasi berbasis web perlu disajikan secara dinamis. Dengan menyajikan data secara dinamis dapat membuat aplikasi yang sedang kita kembangkan menjadi lebih menarik dan interaktif karena menampilkan data secara realtime kepada client. Data yang akan ditampilkan kepada user akan berganti seiring waktu sesuai dengan request yang dikirim oleh client.

## Langkah-langkah Implementasi

1. Membuat sebuah `django-app` bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`
2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan `django-app` yang sudah dibuat ke dalam proyek Django.
3. Buka file `models.py` yang ada di folder `mywatchlist` dan tambahkan atribut yang diminta pada soal yaitu `watched`, `title`, `rating`, `release_date`, dan `review`.
4. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
5. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
6. Buat sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `watchlist_data.json` yang berisi data list movie dalam bentuk JSON.
7. Jalankan perintah `python manage.py loaddata watchlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.
8. Buka `views.py` yang ada pada folder `mywatchlist` dan buatlah sebuah fungsi yang berfungsi untuk menampilkan data berdasarkan tipe yang diminta client (`JSON`, `HTML`, `XML`).
9. Buat sebuah folder bernama `templates` di dalam folder aplikasi `mywatchlist` dan buat sebuah berkas bernama `watchlist.html` yang menampilkan data `JSON` yang telah kita buat ke bentuk `HTML`.
10. Buat sebuah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan routing terhadap fungsi `views` yang telah dibuat sehingga nantinya halaman `HTML` dapat ditampilkan pada browser client.
11. Daftarkan aplikasi `mywatchlist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan `path` pada variabel `urlpatterns`.

## Screenshot Postman

### HTML

![HTML](https://github.com/electyrion/tugas2-pbp/blob/main/mywatchlist/assets/images/show_html.png)

### JSON

![JSON](https://github.com/electyrion/tugas2-pbp/blob/main/mywatchlist/assets/images/show_json.png)

### XML

![XML](https://github.com/electyrion/tugas2-pbp/blob/main/mywatchlist/assets/images/show_xml.png)
