## Testing python & pandas
## Without Dockerfile

Step Runnnig Postgres:
1. masuk terminal
2. Masuk postgres dengan menggunakan perintah "su postgres”
3. Lakukan perintah psql
3. Lakukan create database dengan perintah “create database female_test;”
4. Lakukan create database, table dan column menggunakan aplikasi pgadmin
5. Import data:
    a. masuk kembali ke terminal sebelumnya dan lakukan perintah "\copy customer from '{dict}/database.csv' WITH DELIMITER ',' CSV HEADER;"

Step Runnnig Program:
1. install python Python 3.6.6
2. install python3-pip
3. install vurtualenv (pip install virtualenv)
4. buat virtualenv(virtualenv test-env)
5. jalankan virtualenv (. test-env/bin/activate)
6. masuk direktori simple_test
7. install requirement (pip -r install requirement.txt)
8. jalankan program python user_feed.py untuk facebook feed
9. buka browser masuk ke alamat http://0.0.0.0:5000/ (port 5000 mungkin bisa berubah)
10. jalankan program python data_table.py untuk test data table
