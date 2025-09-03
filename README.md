# Shopee data ETL Pipeline with Airflow

Proyek ini mendemonstrasikan kemampuan dalam membangun pipa data ETL (Extract, Transform, Load) yang modern dan terotomatisasi menggunakan kombinasi 
teknologi cloud standar industri: Apache Airflow, PySpark, dan layanan Microsoft Azure. Tujuan utama proyek ini adalah mengubah data penjualan e-commerce
mentah yang tidak terstruktur menjadi dataset yang bersih, diperkaya, dan siap untuk dianalisis.

## Tinjauan Proyek
Pipa data ini dirancang untuk mensimulasikan skenario di dunia nyata di mana data dari sumber eksternal perlu diproses dalam skala besar. Alur kerja utamanya adalah sebagai berikut:
Ekstraksi Data: File .csv yang mengandung data penjualan e-commerce mentah diunggah dan disimpan di Azure Blob Storage, yang berfungsi sebagai landing zone.
Transformasi Data: Apache Spark (melalui PySpark di Azure Databricks) digunakan untuk membersihkan dan memproses data. Ini termasuk:

- `Mengubah tipe data.`

- `Memecah data kategori produk yang hierarkis menjadi kolom-kolom terpisah.`

- `Menghitung metrik bisnis penting seperti persentase diskon dan estimasi pendapatan.`

- `Pemuatan Data: Data yang sudah ditransformasi dimuat ke Azure Data Lake Storage Gen2 dalam format Parquet, yang dioptimalkan untuk performa analitik.`

- `Orkestrasi: Seluruh alur kerja diotomatisasi menggunakan Apache Airflow, memastikan eksekusi yang konsisten, terjadwal, dan tahan terhadap kegagalan.`

## Arsitektur

<img width="859" height="455" alt="image" src="https://github.com/user-attachments/assets/1eb14db8-1c0d-406c-a215-f227da79f095" />

**Komponen Teknis**
- **Orkestrasi:** Apache Airflow

- **Pemrosesan Data:** PySpark di Azure Databricks

- **Penyimpanan Data (RAW):** Azure Blob Storage

- **Penyimpanan Data (Clean):** Azure Data Lake Storage Gen2

## Cara Menjalankan Proyek
**Prasyarat**
Akun Azure dengan akses ke Azure Databricks, Azure Blob Storage, dan Azure Data Lake Storage Gen2.

Instalasi Docker dan Docker Compose.

Konfigurasi koneksi Azure di Airflow UI (via Admin > Connections).

## Langkah-langkah

- Unggah file sample_shop_2.csv ke kontainer di Azure Blob Storage Anda.

- Buat notebook PySpark di Azure Databricks yang berisi kode transformasi data, pastikan untuk menyesuaikan jalur file dan kredensial.

- Tempatkan kode DAG Airflow (etl_databricks_pipeline.py) di folder dags Anda.

- Jalankan docker-compose up -d dari terminal di direktori proyek Anda.

- Akses Airflow UI, aktifkan DAG, dan picu eksekusi secara manual.

- Proyek ini berhasil jika file .parquet yang bersih dan terstruktur muncul di Azure Data Lake Storage Gen2, siap untuk digunakan oleh tim analitik.
