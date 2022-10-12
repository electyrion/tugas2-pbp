# Todo-List

## Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[TodoList App](https://pbp-tugas2.herokuapp.com/todolist/)

### Kegunaan `{% csrf_token %}` pada elemen `<form>` dan hal yang akan terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`

CSRF token merupakan token acak yang aman (seperti token synchronizer atau token challenge) yang digunakan untuk mencegah serangan berbasis CSRF. CSRF token haruslah unik untuk setiap sesi user dan harus berupa token acak berukuran besar untuk membuatnya menjadi ssah untuk ditebak. Dengan demikian, tidak ada situs web dan client yang memiliki CSRF token yang sama. Dalam Django, CSRF token ditentukan oleh CsrfViewMiddleware dalam file settings.py. Suatu form tersembunyi dengan kolom csrfmiddlewaretoken tersedia di semua request yang dikirim oleh client. CSRF token ditransmisikan ke client sedemikian hingga token tersebut dibutuhkan pada setiap HTTP request yang dikirim oleh client.
Jika suatu form tidak dilengkapi dengan csrf token maka akan sangat memungkinkan terdapat seorang attacker yang dapat memaksa user dari suatu web application untuk menjalankan aksi yang diinginkan oleh si penyerang melalui script yang dikirim attacker melalui form tanpa csrf token tadi. Serangan bertipe CSRF jika berhasil dapat mengancam data user dan jika user yang sedang terkena serangan merupakan administrator dari suatu web application maka kemanan seluruh web application tersebut akan terancam.

### Pembuatan `<form>` secara manual tanpa generator seperti `{{form.as_table}}`

Kita dapat membuat form pada Django tanpa generator dengan cara menggunakan file `forms.py`. Pertama buat terlebih dahulu model dari aplikasi yang ingin kita buat pada `models.py`. Setelah model berhasil dibuat langkah selanjutnya adalah mendaftar kan model yang telah dibuat tadi ke file `admin.py`. Setelah konfigurasi selesai, kita dapat membuat file untuk form bernama `forms.py`. Selanjutnya setelah form berhasil dibuat pada `forms.py`, kita dapat membuat fungsi yang bertugas untuk menghandle request dari client pada file `views.py`. Setelah fungsi untuk menghandle request berhasil dibuat, kita dapat langsung membuat file html yang berfungsi untuk menampilkan form kita pada browser pada folder `templates`. Kemudian lakukan routing untuk memetakan URL ke aplikasi yang telah kita buat. Pembuatan form selesai.

### Proses alur data pembuatan task pada `todolist` app

Django menghandle form menggunakan tehnik yang sama seperti biasanya yaitu: views menerima request kemudian melakukan aksi yang dibutuhkan untuk mengolah requet tadi termasuk didalamnya membaca data dari models kemudain men-generate return berupa laman HTML (melalui template yang kita berikan data berupa context yang telah didefinisikan pada fungsi di views.py untuk kemudian ditampilkan). Berikut ini merupakan bagan yang menunjukkan proses bagaimana Django menghandle suatu form request, dimulai dari request untuk sebuah page yang mengandung form (ditunjukkan dengan warna hijau).
![Bagan](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/assets/images/form_handling.png)
Berdasarkan bagan di atas, hal utama yang dilakukan oleh Django untuk menghandle form adalah sebagai berikut

1. Menampilkan default form sesuai request yang dikirim oleh client.
    Pada saat clien menekan tombol `Tambah Task Baru`, client akan dialihkan menuju halaman pembuatan task baru yang berisi form yang dibutuhkan untuk membuat suatu task
2. Menerima data dari submit request dan melakukan binding pada form
    Binding data pada form artinya client memasukkan data (dalam kasus ini memasukkan judul dan deskripsi task)
3. Cleaning dan Validate data
    Cleaning dilakukan untuk membersihkan input field dari invalid character yang mungkin saja digunakan oleh penyerang untuk mengirimkan konten mencurigakan menuju server dan mengubahnya menjadi script Ptython yang dapat dieksekusi.
    Proses validation mengecek apakah value yang dimasukkan oleh client merupakan value yang tepat untuk form yang bersesuaian.
4. Jika data yang dimasukkan invalid (misal client menekan tombol `create` tetapi belum mengisi form title atau description) maka pesan error akan muncul
5. Jika data yang dimasukkan merupakan data yang valid, Django akan melakukan aksi yang dibutuhkan yaitu menyimpan data yang client masukkan ke models.
6. Setelah proses penyimpanan task selesai dilaksanakan, client akan dialihkan menuju halaman utama `todolist` yang berisi daftar task yang telah dibuat oleh client.

### Langkah implementasi tugas

1. Membuat app baru dengan perintah `python manage.py startapp todolist`
2. Buka [settings.py](https://github.com/electyrion/tugas2-pbp/blob/main/project_django/settings.py) di folder `project_django` dan tambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APP` untuk mendaftarkan `todolist` ke dalam proyek Django.
3. Buka file [models.py](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/models.py) yang ada di folder `todolist` dan tambahkan models seperti yang diminta pada soal.
4. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
5. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
6. Mengimplementasikan form [registrasi](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/templates/register.html), [login](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/templates/login.html), dan `logout` seperti pada lab tempo hari yang lalu
7. Membuat halaman utama [todolist](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/templates/todolist.html) yang memuat `username` pengguna, tombol `Tambah Task Baru`, tombol `logout`, serta tabel berisi tanggal `pembuatan task`, `judul task`, dan `deskripsi task`.
8. Membuat halaman form untuk [pembuatan task](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/templates/create_task.html) yang hanya menerima input `title` dan `description`
9. Membuat [routing](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/urls.py) sehingga fungsi dapat mengakses URL berikut:
    `http://localhost:8000/todolist` berisi halaman utama yang memuat tabel task.
    `http://localhost:8000/todolist/login` berisi form login.
    `http://localhost:8000/todolist/register` berisi form registrasi akun.
    `http://localhost:8000/todolist/create-task` berisi form pembuatan task.
    `http://localhost:8000/todolist/logout` berisi mekanisme logout.
10. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh orang lain melalui Internet.

## Tugas 5: Web Design Using HTML, CSS, and CSS Framework

### Perbedaan dari Inline, Internal, dan External CSS

1. Inline CSS
Inline CSS digunakan untuk tag HTML tertentu. Atribut `<style>` digunakan untuk memberikan style ke tag HTML tertentu. Cara ini kurang direkomendasikan, karena setiap tag HTML malah harus diberikan style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline CSS. Namun, di beberapa situasi justru inline CSS menjadi berguna. Contohnya, pada saat Anda tidak memiliki akses ke file CSS atau harus mengubah style untuk 1 elemen saja
Keunggulan Inline CSS:
    - Berguna jika Anda ingin menguji dan melihat perubahan
    - Berguna untuk perbaikan cepat
    - Permintaan HTTP yang lebih kecil
Kekurangan:
    - Inline CSS harus diterapkan pada setiap elemen

2. Internal CSS
Kode CSS internal diletakkan di dalam bagian `<head>` pada halaman. Class dan ID bisa digunakan untuk merujuk pada kode CSS, namun hanya akan aktif pada halaman tersebut. Style CSS yang dipasang dengan metode ini akan di-download setiap kali halaman dipanggil, hal ini akan meningkatkan kecepatan akses. Namun, ada beberapa case dimana penggunaan internal stylesheet justru berguna. Salah satu contohnya adalah untuk mengirimkan template halaman ke seseorang – karena semuanya bisa terlihat dalam 1 halaman, maka akan lebih mudah untuk melihat previewnya. CSS internal diletakkan di dalam tag `<style></style>`.
Keunggulan:
    - Perubahan hanya terjadi pada 1 halaman
    - Class dan ID bisa digunakan oleh internal stylesheet
    - Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.
Kekurangan Internal CSS:
    - Meningkatkan waktu akses website
    - Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

3. Salah satu cara yang paling nyaman untuk menambahkan CSS ke website Anda adalah dengan menghubungkannya ke file .CSS eksternal. Dengan cara tersebut, perubahan apapun yang Anda buat pada file CSS akan tampil pada website Anda secara keseluruhan. File CSS eksternal biasanya diletakkan setelah bagian `<head>` pada halaman.
Keunggulan:
    - Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi.
    - Kecepatan loading menjadi lebih cepat.
    - File CSS yang sama bisa digunakan di banyak halaman.
Kekurangan:
    - Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

### HTML Tag

HTML Tag | Kegunaan
---|---
`<!DOCTYPE>` | Tag untuk menentukan tipe dokumen
`<html>` | Tag untuk membuat sebuah dokumen HTML
`<title>` | Tag untuk membuat judul dari sebuah halaman
`<body>` | Tag untuk membuat tubuh dari sebuah halaman
`<p>` | Tag untuk membuat paragraf
`<br>` | Memasukan satu baris putus
`<!--...-->` | Tag untuk membuat komentar
`<address>` | Tag untuk membuat kontak alamat
`<b>` | Tag untuk membuat huruf bercetak tebal
`<cite>` | Tag untuk membuat judul karya
`<code>` | Tag untuk membuat potongan kode komputer di antara text
`<font>` | Tag untuk membuat font, warna, dan ukuran untuk teks (tidak disupport lagi di HTML5)
`<small>` |  Tag untuk membuat teks kecil
`<u>` | Tag untuk membuat teks yang memiliki Gaya yang berbeda dari teks biasa lainnya
`<var>` | Tag untuk membuat sebuah variabel
`<form>` | Tag untuk membuat sebuah form HTML untuk input pengguna
`<input>` | Tag untuk membuat sebuah kontrol input
`<button>` | Tag untuk membuat sebuah tombol yang dapat diklik
`<select>` | Tag untuk membuat sebuah daftar drop-down
`<option>` | Tag untuk membuat pilihan dalam daftar drop-down
`<label>` | Tag untuk membuat sebuah label untuk sebuah elemen `<input>`
`<output>` | Tag untuk membuat hasil penghitungan (tag baru HTML5)
`<img>` | Tag untuk membuat gambar
`<map>` | Tag untuk membuat gambar-peta
`<area>` | Tag untuk membuat area dalam gambar-peta
`<audio>` | Tag untuk membuat isi suara (tag baru HTML5)
`<source>` | Tag untuk membuat sumber beberapa media untuk elemen media (`<video>` dan `<audio>`) (tag baru HTML5)
`<video>` | Tag untuk membuat sebuah video atau film (tag baru HTML5)
`<a>` | Tag untuk membuat hyperlink
`<link>` | Tag untuk membuat hubungan antara dokumen dan sumber daya eksternal (paling sering digunakan untuk link ke style sheet)
`<nav>` | Tag untuk membuat navigasi link (tag baru HTML5)
`<ul>` | Tag untuk membuat daftar dengan selain nomor
`<table>` | Tag untuk membuat tabel
`<tbody>` | Mengelompokanisi tubuh dalam sebuah tabel
`<tfoot>` | Mengelompokan isi footer dalam sebuah tabel
`<style>` | Tag untuk membuat informasi style untuk dokumen
`<div>` | Tag untuk membuat sebuah bagian dalam dokumenTag untuk membuat sebuah bagian dalam dokumen
`<header>` | Tag untuk membuat sebuah header untuk dokumen atau bagian (tag baru HTML5)
`<footer>` | Tag untuk membuat footer untuk dokumen atau bagian (tag baru HTML5)
`<head>` | Tag untuk membuat informasi tentang dokumen
`<meta>` | Tag untuk membuat metadata tentang dokumen HTML
`<base>` | Menentukan URL dasar / target untuk semua URL relatif dalam dokumen
`<script>` | Tag untuk membuat script di sisi klien
`<noscript>` | Tag untuk membuat sebuah konten alternatif bagi pengguna yang tidak mendukung script di sisi klien
`<object>` | Tag untuk membuat sebuah objek yang ditanam
`<param>` | Tag untuk membuat sebuah parameter untuk objek

### Jenis Selector CSS

1. CSS Element Selector: Memilih elemen HTML berdasarkan namanya.
2. CSS Id Selector: Memilih atribut id dari suatu elemen HTML untuk merujuk ke elemen yang spesifik. Setiap elemen memiliki id yang unik.
3. CSS Class Selector: Memilih elemen HTML berdasarkan class-nya. Cara penggunaannya adalah dengan menggunakan tanda titik kemudian diikuti oleh nama class.
4. CSS Class Universal Selector: Universal selector digunakan sebagai wildcard karakter yang memilih semua elemen yang ada pada suatu halaman.
5. CSS Group Selector: Grouping selector digunakan untuk memilih semua elemen yang memiliki gaya styling yang sama.

### Cara Implementasi

Tugas 5 ini saya kerjakan menggunakan framework bootstrap sebagai stylesheet. Dengan cara demikian, kita tidak perlu lagi repot-repot menuliskan kode css kedalam file css karena hal tersebut sudah dihandle oleh Bootstrap. Tidak hanya itu, Bootstrap juga menjadikan aplikasi web kita otomatis menjadi responsive dengan metode mobile first fluid system yang menyediakan skala hingga 12 kolom menyesuaikan dengan device yang sedang client gunakan.

## Tugas 6: Javascript dan AJAX

### Perbedaan antara Asynchronous Programming dengan Synchronous Programming

Dalam dunia pemrograman komputer, synchronous programmiing dan asynchronous programming merupakan hal yang sangat penting. Dilihat dari namanya, kita pasti sudah dapat membayangkan apa sebenarnya perbedaan di antara keduanya. Synchoronous berarti event dijalankan secara berurutan yang artinya suatu event harus diselesaikan terlebih dahulu sebelum dapat berpindah menuju event selanjutnya. Asynchronous bersifat sebaliknya yaitu event dapat dijalankan tidak bergantung pada urutan dan bahkan dapat dijalankan secara bersamaan.
Berikut merupakan tabel perbedaan di antara keduanya:

Asynchronous | Synchronous
---|---
Asynchronous bersifat multi-thread yang berarti suatu event dapat dijalankan secara parallel | Syncrhonous bersifat single-thread sehingga hanya dapat menjalankan satu perintah dalam kurun waktu tertentu
Asynchronous bersifat non-blocking yang artinya dapat mengirimkan beberapa request sekaligus kepada server | Synchronous bersifat blocking yang artinya hanya dapat mengirim satu request dalam kurun waktu tertentu dan harus menunggu request tersebut untuk mendapat response sebelum dapat mengirimkan request selanjutnya
Asynchronous meningkatna jumlah throughput karena beberapa operasi dapa dijalankan dalam kurun waktu bersamaan | Synchronous lebih lamban dan lebih sekuensial

### Event-Driven Programming

Event-driven programming merupakan suatu pendekatan dalam dunia pemrograman dimana suatu code dibuat untuk merespon suatu kejadian atau event. Event dapat dipicu oleh pengguna misalnya pada saat pengguna menekan tombol atau mengetik suatu teks pada form. Suatu set instruksi yang dibuat untuk melakukan operasi yang sering digunakan pada program atau yang biasa disebut dengan subroutine yang merespon terhadap event disebut dengan event handler. Event handler akan memastikan bahwa penanganan yang sesuai akan terjadi sebagai respons terhadap event yang memicunya. Pada tugas kali ini contoh dari event-driven programming adalah penggunaan handler untuk setiap event yang terjadi pada web seperti ketika user menekan tombol `Add Task` maka akan memanggil fungsi untuk menampilkan modal yang berisi form pengisian task baru bagi pengguna.

### Penerapan Asynchronous Programming pada AJAX

AJAX dapat membuat suatu aplikasi web untuk dapat mengirim dan mengambil data dari server secara asynchronous dari balik layar. Dengan adanya AJAX, browser dan aplikasi web lainnya tidak perlu melakukan refresh seluruh halaman dan tentunya mengganggu display dari web tersebut setiap kali pengguna melakukan manipulasi data ataupun meminta request baru pada aplikasi web. Dengan melakukan pemisahan proses penampilan data dan proses pertukaran data, AJAX bekerja sedemikian sehingga membuat halaman web dapat melakukan perubahan isi database tanpa perlu memuat ulang seluruh halaman. Script ajax yang berada di dalam tag script akan mengirimkan request kepada server dan melanjutkan eksekusinya tanpa perlu menunggu response dari request tadi.

### Proses Implementasi Tugas 6

1. Pertama saya membuat fungsi baru pada `views.py` yang berfungsi untuk mengembalikan seluruh data task yang ada berupa json yang sesuai dengan user pembuat task tersebut
2. Agar fungsi tersebut dapat diakses, buat path baru pada `urls.py` yang berada pada folder aplikasi `todolist`, path yang dimaksud yaitu `/todolist/json` yang akan mengarahkan ke fungsi yang baru saja dibuat pda poin pertama
3. Karena kita akan menggunakan ajax untuk mengimplementasikan asynchronous programming, sertakan library ajax pada `base.html` yang nantinya akan di-inherit oleh file html todolist
4. Melakukan pengambilan data todolist menggunakan [jquery AJAX](https://github.com/electyrion/tugas2-pbp/blob/main/todolist/templates/todolist.html)
5. Untuk menambahkan object task baru secara asynchronous menggunakan ajax, pertama buat fungsi baru pada `views.py`
6. Membuat path `/todolist/add` agar fungsi yang baru dibuat tadi dapat diakses
7. Membuat modal baru yang berisi form penambahan task serta menghubungkannya dengan tombol `Add Task` yang berada pada navbar
8. Membuat event handler ketika pengguna menekan tombol `create` dengan cara menghubungkannya dengan method post ajax menuju path `/todolist/add` sekaligus menutup modal pembuatan form baru
9. Menambahkan task yang telah dibuat tadi pada `content` sehingga dapat ditampilkan secara asynchronous
10. Melengkapi README.md
