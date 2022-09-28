# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[TodoList App](https://pbp-tugas2.herokuapp.com/todolist/)

## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan hal yang akan terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`

CSRF token merupakan token acak yang aman (seperti token synchronizer atau token challenge) yang digunakan untuk mencegah serangan berbasis CSRF. CSRF token haruslah unik untuk setiap sesi user dan harus berupa token acak berukuran besar untuk membuatnya menjadi ssah untuk ditebak. Dengan demikian, tidak ada situs web dan client yang memiliki CSRF token yang sama. Dalam Django, CSRF token ditentukan oleh CsrfViewMiddleware dalam file settings.py. Suatu form tersembunyi dengan kolom csrfmiddlewaretoken tersedia di semua request yang dikirim oleh client. CSRF token ditransmisikan ke client sedemikian hingga token tersebut dibutuhkan pada setiap HTTP request yang dikirim oleh client.
Jika suatu form tidak dilengkapi dengan csrf token maka akan sangat memungkinkan terdapat seorang attacker yang dapat memaksa user dari suatu web application untuk menjalankan aksi yang diinginkan oleh si penyerang melalui script yang dikirim attacker melalui form tanpa csrf token tadi. Serangan bertipe CSRF jika berhasil dapat mengancam data user dan jika user yang sedang terkena serangan merupakan administrator dari suatu web application maka kemanan seluruh web application tersebut akan terancam.

## Pembuatan `<form>` secara manual tanpa generator seperti `{{form.as_table}}`

Kita dapat membuat form pada Django tanpa generator dengan cara menggunakan file `forms.py`. Pertama buat terlebih dahulu model dari aplikasi yang ingin kita buat pada `models.py`. Setelah model berhasil dibuat langkah selanjutnya adalah mendaftar kan model yang telah dibuat tadi ke file `admin.py`. Setelah konfigurasi selesai, kita dapat membuat file untuk form bernama `forms.py`. Selanjutnya setelah form berhasil dibuat pada `forms.py`, kita dapat membuat fungsi yang bertugas untuk menghandle request dari client pada file `views.py`. Setelah fungsi untuk menghandle request berhasil dibuat, kita dapat langsung membuat file html yang berfungsi untuk menampilkan form kita pada browser pada folder `templates`. Kemudian lakukan routing untuk memetakan URL ke aplikasi yang telah kita buat. Pembuatan form selesai.

## Proses alur data pembuatan task pada `todolist` app

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

## Langkah implementasi tugas
