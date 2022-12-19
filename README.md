
<a href="https://github.com/Neek0tine/SpeechEmotionRecognition/blob/main/output.gif"><img src="https://github.com/Neek0tine/SpeechEmotionRecognition/blob/main/output.gif" alt="TweeToxicity" width="800"/></a><br><br>

<a href="https://github.com/Neek0tine/SpeechEmotionRecognition/issues"><img src="https://img.shields.io/github/issues/Neek0tine/SpeechEmotionRecognition"></a>
<a href="https://github.com/Neek0tine/Tweetoxicity/blob/main/LICENSE" ><img src="https://img.shields.io/github/license/Neek0tine/SpeechEmotionRecognition"></a>
<a href="https://github.com/Neek0tine/SpeechEmotionRecognition/commits/main"><img src="https://img.shields.io/github/commit-activity/m/Neek0tine/SpeechEmotionRecognition"></a>



# Speech Emotion Recognition

<h2> Intro</h2>
<b>Speech Emotion Recognition</b> adalah sebuah sistem dimana perasaan atau emosi seseorang dapat diklasifikasikan dari gaya berbicaranya. Berdasarkan teori speech emotion analysis oleh Patrik dan Klaus (2008), emosi seseorang dapat dirasakan secara nonverbal dari perubahan ritme respirasi, tensi otot yang menggetarkan suara dan mengganti karakteristik akustik, dan lain-lain. Diferensiasi dari emosi tersebut terbukti susah untuk ditentukan, karena sifat natural suara yang kompleks. Contohnya, susah dibedakan emosi spontan dan emosi yang lama terbuat, atau emosi dingin ataupun emosi yang panas.<br><br>
Menggunakan teknologi Machine Learning, diharapkan dapat ditentukan fitur-fitur unik suara yang sangat kompleks dan heterogen oleh feature analysis dan diprediksi dengan akurat menggunakan teknologi deep learning. 

## Metode

Ditentukan beberapa tahapan yang akan dilakukan dalam melakukan data mining dan modelling pada proyek ini, tahapan-tahapan tersebut adalah:
<ol>
    <li>Studi Literatur</li>
    <p> Studi literatur dilakukan untuk menentukan pendekatan terbaik untuk mendapatkan sistema yang efektif dan efisien berdasarkan penelitian dan pendekatan yang telah dilakukan sebelumnya oleh peneliti lain</p>
    <li>Pencaharian Data</li>
    <p>Data yang digunakan pada proyek ini adalah data hasil "scrapping" yang bersumber dari situs YouTube yang lalu di label secara manual berdasarkan emosi yang terdengar pada video tersebut. Video lalu disegmentasi per 3 detik yang lalu diekspor menjadi file suara .wav atau .mp3</p>
    <li>Eksplorasi dan Visualisasi Data</li>
    <p>Eksplorasi, Visualisasi Data Analysis (EVD/EDA) dilakukan untuk menentukan pendekatan yang lebih spesifik terhadap data yang dimiliki didapat di tahap sebelumnya. Analysis ini diharapkan akan memberikan ide akan parameter yang akan digunakan pada tahap ekstraksi fitur</p>
    <li> Ekstraksi Fitur</li>
    <p>Ekstraksi fitur adalah tahap terpenting dalam proyek ini, dikarenakan hasil akhir model akan ditentukan oleh seberapa baik data yang masuk ke dalam sistem. Ada banyak parameter yang dapat diubah untuk mendapatkan fitur terbaik di antara kelas. Parameter tersebut ditentukan berdasarkan hasil dari tahap sebelumnya</p>
    <li>Pembuatan Model / Aristektur <i>Deep Learning</i></li>
    <p>Pada tahap ini, data hasil ekstraksi fitur yang telah dilakukan pada tahap sebelumnya, dimasukkan ke dalam model machine learning ataupun model deep learning. Juga terdapat banyak parameter atau knofigurasi yang dapat dibuat pada saat pemodelan deep learning, tapi untuk proyek ini digunakan arsitektur yang digunakan pada salah satu studi yang telah dilakukan (RNN Bi-directional LSTM)</p>
    <li>Evaluasi dan Prediksi</li>
    <p>Tahap ini adalah tahap terakhir dari proyek, dimana model yang telah dibuat dievaluasi untuk akurasinya dan dilakukan prediksi langsung terhadap suara yang baru.</p>
</ol>


<a href="https://github.com/Neek0tine/SpeechEmotionRecognition/blob/main/methods.png"><img src="https://github.com/Neek0tine/SpeechEmotionRecognition/blob/main/output.gif" alt="TweeToxicity" width="715"/></a><br><br>

## Dataset
Dataset yang digunakan dalam analisis penelitian ini dapat diakses pada link berikut: https://tinyurl.com/DatasetAudio-KelompokC. Data tersebut merupakan hasil scrapping video di YouTube yang merepresentasikan 4 ekspresi manusia, yakni marah, sedih, senang, dan netral. Label angry terdiri dari 1.302 data, label happy terdiri dari 427 data, label neutral terdiri dari 624 data, dan label sad terdiri dari 897 data.


