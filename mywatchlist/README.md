# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[MyWatchList App](https://pbp-tugas2.herokuapp.com/mywatchlist/)

## Perbedaan antara JSON, HTML, dan XML

JSON | HTML | XML
:---: | :---: | :---:
Object JSON memiliki tipe | | XML data tidak memiliki tipe
Tipe data JSON: string, number, array, Boolean | | Seluruh data XML harus berupa string
Data mudah dibaca dan diakses sebagai JSON object | | Data XML harus di-parse terlebih dahulu
JSON didukung oleh berbagai browser | | Melakukan parse XML antar browser terkadang sulit
JSON tidak memiliki kemampuan medsiplay data | | XML dapat mendisplay datanya karena tergolong kedalam markup language
JSON hanya mendukung data type text dan number | | XML mendukung berbagai data type seperti number, images text, charts, graphs, dll
Proses pengambilan value dari data tergolong mudah | | Proses pengambilan value dari data tergolong sulit
Proses deserializing/serializing Javascript dapat berjalan otomatis | | Developer harus menulis kode dalam Javascript terlebih dahulu untuk melakukan deserializing/serializing dari XML
Hanya mendukung jenis encodin UTF-8 | Mendukung banyak jenis encoding | Mendukung berbagai jenis tipe encoding
Tidak mendukung adanya comments | Memperbolehkan adanya comments | Memperbolehkan adanya comments
Konten JSON lebih mudah dibaca Jika dibandingkan dengan XML | Mendukung argumen tag untuk memudahkan pembacaan data | Dokumen XML relatif sulit dibaca dan diinterpretasi
Tidak mendukung namespaces | | Mendukung namespaces
Tingkat keamanan lebih rendah jika dibandingkan dengan XML |  | Lebih aman jika dibandingkan dengan JSON
