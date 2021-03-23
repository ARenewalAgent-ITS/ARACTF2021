# Dewan Kunci
---
## Deskripsi
Cipher: zeq3p1z}nr5[xL;\sq2/7wjr7\irf,hrg.jr7w;[dedr;r8p60x6e{
## Solusi
Kategori Soal: Kriptografi\
Nama: Dewan Kunci\
Cipher: zeq3p1z}nr5[xL;\sq2/7wjr7\irf,hrg.jr7w;[dedr;r8p60x6e{\
Clue 1: lihat jari jemari anda, \
Clue 2: lihat judul dan buka kamus bahasa inggris.\
Format flag: ara2021{}

Dari melihat cipher dan format flag, kemungkinan besar ini merupakan sandi subtitusi atau subtitution cipher. Letak kurung kurawal '{' yang ada di posisi terakhir cipher dan kurung kurawal '}' yang ada pada posisi ke-8 cipher sama seperti posisi kurung kurawal pada format flag menandakan hal tersebut. \

analisis 8 huruf pertama cipher:\
    zeq3p1z}\
    ara2021{\
Melihat judul soal serta cluenya, dapat disimpulkan cipher ini berhubungan dengan keyboard alias papan ketik. Pada papan ketik, terlihat asosiasi yang jelas antara simbol pada cipher dengan simbol pada format flag yang berada di posisi yang sama. Sepertinya cipher yang digunakan adalah subtitusi papan ketik. Dari analisis subtitusi hurufnya didapatkan hasil sebagai berikut:\\
    1. dari z ke a berpindah 1 posisi ke atas\
    2. dari e ke r berpindah 1 posisi ke kanan\
    3. dari q ke a berpindah 1 posisi ke bawah\
    4. dari 3 ke 2 berpindah 1 posisi ke kiri\
    5. dari p ke 0 berpindah 1 posisi ke atas\
    6. dari 1 ke 2 berpindah 1 posisi ke kanan\
    7. dari z ke 1 berpindah 1 posisi ke bawah\
    8. dari } ke { berpindah 1 posisi ke kiri\

layout papan ketik yang digunakan:
    Lowercase:                                              Uppercase:
    |1|2|3|4|5|6|7|8|9|0|-|=|                               |!|@|#|$|%|^|&|*|(|)|_|+|\
    |q|w|e|r|t|y|u|i|o|p|[|]|\|                             |Q|W|E|R|T|Y|U|I|O|P|{|}|||\
    |a|s|d|f|g|h|j|k|l|;|'|                                 |A|S|D|F|G|H|J|K|L|:|"|\
    |z|x|c|v|b|n|m|,|.|/|                                   |Z|X|C|V|B|N|M|<|>|?|\

Terdapat pola perpindahan atau shift pattern yang jelas pada hasil analisis tersebut yakni atas, kanan, bawah, kiri yang berulang atau berputar searah jarum jam (↻). Pola tersebut diteruskan untuk mendekripsi seluruh cipher dan berhasil mengungkap flag berikut ini:\
cipher:     zeq3p1z}nr5[xL;\sq2/7wjr7\irf,hrg.jr7w;[dedr;r8p60x6e{\
shift:      ↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→\
plaintext:  ara2021{https://www.mememaker.net/meme/perception-253}\

Flag: ara2021{https://www.mememaker.net/meme/perception-253}\





#### ara2021{https://www.mememaker.net/meme/perception-253}
