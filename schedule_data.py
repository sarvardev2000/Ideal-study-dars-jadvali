# -*- coding: utf-8 -*-
"""
IDEAL STUDY maktabining haqiqiy dars jadvali ma'lumotlari.

MUHIM: TEACHERS (o'qituvchilar jadvali) endi QO'LDA yozilmaydi -
u CLASSES (sinflar jadvali) asosida pastdagi kod orqali AVTOMATIK hisoblanadi.
Bu xato ehtimolini kamaytiradi: bitta ma'lumot bazasi, ikki marta yozish yo'q.

Hozircha faqat 1-SINF to'liq kiritilgan. Qolgan sinflar (2-9) keyingi
bosqichlarda qo'shiladi.
"""

DAYS = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]


# ============================================================
# SINFLAR JADVALI (manba ma'lumot - shu yerga yangi sinflar qo'shiladi)
# ============================================================
# Agar biror darsda o'qituvchi ismi ko'rsatilmagan bo'lsa (masalan "Matematika"),
# bu dars sinfning SINF RAHBARI tomonidan o'tiladi - shuning uchun "ustoz"
# maydoniga sinf rahbarning ismi yozilgan.

CLASSES = {

    "1-A": {  # Sinf rahbar: Buribayeva Xolida Narzikulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Xolida"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Xolida"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Xolida"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Xolida"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Maloxat"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xolida"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Xolida"},
            {"soat": "3-dars", "fan": "Yozuv", "ustoz": "Xolida"},
            {"soat": "4-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Xolida"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Maloxat"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xolida"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Xolida"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xolida"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Maloxat"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Xolida"},
            {"soat": "5-dars", "fan": "Tarbiya", "ustoz": "Xolida"},
        ],
        "Shanba": [],
    },

    "1-B": {  # Sinf rahbar: Karimova Diyora Abdusalom qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora K."},
            {"soat": "2-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Nargiza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "5-dars", "fan": "Tasviriy sanat", "ustoz": "Diyora K."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora K."},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Diyora K."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "5-dars", "fan": "Yozuv", "ustoz": "Diyora K."},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora K."},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Diyora K."},
            {"soat": "3-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Diyora K."},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nargiza"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Diyora K."},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Diyora K."},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora K."},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Nargiza"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
        ],
        "Shanba": [],
    },

    "1-D": {  # Sinf rahbar: Ashurova Nodira Baxrom qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "3-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Nodira B."},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Nodira B."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mental", "ustoz": "Maftuna"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Nodira B."},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Nodira B."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nodira B."},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Nodira B."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nodira B."},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Nodira B."},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Nodira B."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zulfiya"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Nodira B."},
        ],
        "Shanba": [],
    },

    "1-E": {  # Sinf rahbar: Odilova Xabiba Sarvarovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xabiba"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Xabiba"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sevinch"},
            {"soat": "4-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Xabiba"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xabiba"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "3-dars", "fan": "Mental", "ustoz": "Maftuna"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Xabiba"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xabiba"},
            {"soat": "2-dars", "fan": "Yozuv", "ustoz": "Xabiba"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sevinch"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sevinch"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xabiba"},
            {"soat": "2-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sevinch"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Xabiba"},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Xabiba"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xabiba"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Xabiba"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Xabiba"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Shanba": [],
    },

    "1-V": {  # Sinf rahbar: Pardayeva Marg'uba Xoliqovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Marg'uba"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Marg'uba"},
            {"soat": "5-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Marg'uba"},
            {"soat": "2-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Marg'uba"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Marg'uba"},
            {"soat": "5-dars", "fan": "Tasviriy sanat", "ustoz": "Marg'uba"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Marg'uba"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Marg'uba"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Dilnoza"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Marg'uba"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Marg'uba"},
        ],
        "Shanba": [],
    },

    "1-F": {  # Sinf rahbar: Shadiyeva Ra'no Baxodirovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ra'no"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Ra'no"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ra'no"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Ra'no"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Ra'no"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Ra'no"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mental", "ustoz": "Maftuna"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ra'no"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ra'no"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Ra'no"},
            {"soat": "3-dars", "fan": "Yozuv", "ustoz": "Ra'no"},
            {"soat": "4-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Ra'no"},
            {"soat": "5-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ra'no"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Ra'no"},
            {"soat": "3-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Ra'no"},
            {"soat": "4-dars", "fan": "Texnologiya", "ustoz": "Ra'no"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
        ],
        "Shanba": [],
    },

    "1-G": {  # Sinf rahbar: Abdurasulova Mukaddas Tashtemirovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mukaddas"},
            {"soat": "2-dars", "fan": "Texnologiya", "ustoz": "Mukaddas"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Mukaddas"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Mukaddas"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Mukaddas"},
            {"soat": "5-dars", "fan": "Tasviriy sanat", "ustoz": "Mukaddas"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mukaddas"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Mukaddas"},
            {"soat": "3-dars", "fan": "Yozuv", "ustoz": "Mukaddas"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Mukaddas"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mukaddas"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Mukaddas"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Mukaddas"},
            {"soat": "4-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mukaddas"},
            {"soat": "2-dars", "fan": "Yozuv", "ustoz": "Mukaddas"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Mukaddas"},
        ],
        "Shanba": [],
    },

    "1-H": {  # Sinf rahbar: Vitchinkina Marina Viktorovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Marina V."},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Marina V."},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Marina V."},
            {"soat": "3-dars", "fan": "Yozuv", "ustoz": "Marina V."},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Marina V."},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Marina V."},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Marina V."},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Marina V."},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Marina V."},
            {"soat": "3-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Marina V."},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Marina V."},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Marina V."},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Marina V."},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Marina V."},
        ],
        "Shanba": [],
    },

    "1-I": {  # Sinf rahbar: Shanazarova Xurshida Valiyevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Xurshida"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Xurshida"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Xurshida"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Xurshida"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Xurshida"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Xurshida"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "3-dars", "fan": "Tasviriy sanat", "ustoz": "Xurshida"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Xurshida"},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Xurshida"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Xurshida"},
            {"soat": "2-dars", "fan": "Yozuv", "ustoz": "Xurshida"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "4-dars", "fan": "Alifbe", "ustoz": "Xurshida"},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Xurshida"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Ruxsora"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Xurshida"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Xurshida"},
        ],
        "Shanba": [],
    },

    "1-K": {  # Sinf rahbar: Ergasheva Zamira Raxmatullayevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Zamira"},
            {"soat": "2-dars", "fan": "Alifbe", "ustoz": "Zamira"},
            {"soat": "3-dars", "fan": "Yozuv", "ustoz": "Zamira"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Zamira"},
            {"soat": "2-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Zamira"},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Zamira"},
            {"soat": "5-dars", "fan": "Yozuv", "ustoz": "Zamira"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Zamira"},
            {"soat": "2-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Zamira"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Zamira"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Alifbe", "ustoz": "Zamira"},
            {"soat": "4-dars", "fan": "Yozuv", "ustoz": "Zamira"},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Zamira"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Zamira"},
            {"soat": "2-dars", "fan": "Yozuv", "ustoz": "Zamira"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
        ],
        "Shanba": [],
    },

    # ========================================================
    # 2-SINF
    # ========================================================

    "2-A": {  # Sinf rahbar: Pardayeva Shaxnoza Saibnazarovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Shaxnoza"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Shaxnoza"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Shaxnoza"},
            {"soat": "2-dars", "fan": "O'qish savodxonligi", "ustoz": "Shaxnoza"},
            {"soat": "3-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Diyora"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Shaxnoza"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Diyora"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Shaxnoza"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Shaxnoza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "5-dars", "fan": "Tarbiya", "ustoz": "Shaxnoza"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Diyora"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Diyora"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Shaxnoza"},
            {"soat": "4-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Shaxnoza"},
        ],
        "Shanba": [],
    },

    "2-B": {  # Sinf rahbar: Akmuratova Iroda Bahodir qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nargiza"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Texnologiya", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Tarbiya", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Tasviriy sanat", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Iroda"},
        ],
        "Shanba": [],
    },

    "2-D": {  # Sinf rahbar: Rajabova Nasiba Saydullayevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Tasviriy sanat", "ustoz": "Nasiba"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "5-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Nasiba"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Nasiba"},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Nasiba"},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Texnologiya", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Nasiba"},
        ],
        "Shanba": [],
    },

    "2-V": {  # Sinf rahbar: Avazova Gulchexra Alimjanovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Marina"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Gulchexra"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Gulchexra"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Gulchexra"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Gulchexra"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Gulchexra"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Marina"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Gulchexra"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Gulchexra"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Gulchexra"},
            {"soat": "5-dars", "fan": "Tasviriy sanat", "ustoz": "Gulchexra"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Gulchexra"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Marina"},
        ],
        "Shanba": [],
    },

    "2-E": {  # Sinf rahbar: Prosyannikova Veronika Sergeyevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Veronika S."},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Veronika S."},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Veronika S."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Veronika S."},
            {"soat": "4-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Veronika S."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika S."},
            {"soat": "2-dars", "fan": "Rasm", "ustoz": "Veronika S."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "5-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Veronika S."},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika S."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Veronika S."},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Veronika S."},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Veronika S."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "O'zbek tili", "ustoz": "Shaxnoza"},
            {"soat": "2-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Veronika S."},
            {"soat": "4-dars", "fan": "Texnologiya", "ustoz": "Veronika S."},
        ],
        "Shanba": [],
    },

    "2-F": {  # Sinf rahbar: Polyakova Veronika Igorevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika I."},
            {"soat": "2-dars", "fan": "O'qish savodxonligi", "ustoz": "Veronika I."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Veronika I."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika I."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Veronika I."},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "5-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika I."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Veronika I."},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Veronika I."},
            {"soat": "5-dars", "fan": "Rasm", "ustoz": "Veronika I."},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Veronika I."},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Veronika I."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Veronika I."},
            {"soat": "3-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Veronika I."},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Veronika I."},
        ],
        "Shanba": [],
    },

    "2-G": {  # Sinf rahbar: Shukurova Oksana Ilinichna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Oksana"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Oksana"},
            {"soat": "3-dars", "fan": "Musiqa", "ustoz": "Oksana"},
            {"soat": "4-dars", "fan": "Texnologiya", "ustoz": "Oksana"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Oksana"},
            {"soat": "2-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Oksana"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "5-dars", "fan": "O'qish savodxonligi", "ustoz": "Oksana"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Oksana"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Oksana"},
            {"soat": "5-dars", "fan": "Rasm", "ustoz": "Oksana"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Oksana"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Oksana"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Tarbiya", "ustoz": "Oksana"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Oksana"},
            {"soat": "4-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Oksana"},
        ],
        "Shanba": [],
    },

    "2-H": {  # Sinf rahbar: Eshonkulova Maloxat Bavakulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maloxat B."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Maloxat B."},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Maloxat B."},
            {"soat": "4-dars", "fan": "Musiqa", "ustoz": "Maloxat B."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Maloxat B."},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maloxat B."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Maloxat B."},
            {"soat": "3-dars", "fan": "Tarbiya", "ustoz": "Maloxat B."},
            {"soat": "4-dars", "fan": "Rasm", "ustoz": "Maloxat B."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maloxat B."},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Maloxat B."},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Maloxat B."},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Maloxat B."},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maloxat B."},
            {"soat": "2-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Maloxat B."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Bexruza"},
            {"soat": "5-dars", "fan": "Shaxmat", "ustoz": "Samandar"},
        ],
        "Shanba": [],
    },

    "2-I": {  # Sinf rahbar: Karimqulova Sevara Raxatullayevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Sevara"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Musharraf"},
            {"soat": "4-dars", "fan": "Musiqa", "ustoz": "Sevara"},
            {"soat": "5-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Sevara"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevara"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Sevara"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevara"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Sevara"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Sevara"},
            {"soat": "5-dars", "fan": "Rasm", "ustoz": "Sevara"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevara"},
            {"soat": "2-dars", "fan": "Tarbiya", "ustoz": "Sevara"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevara"},
            {"soat": "2-dars", "fan": "Texnologiya", "ustoz": "Sevara"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Sevara"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
        ],
        "Shanba": [],
    },

    # ========================================================
    # 3-SINF
    # ========================================================

    "3-A": {  # Sinf rahbar: Umurzakova Musharraf To'raqulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Musharraf"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Musharraf"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Musharraf"},
            {"soat": "5-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Musharraf"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Musharraf"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Musharraf"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Musharraf"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Musharraf"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Musharraf"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Musharraf"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Musharraf"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Musharraf"},
            {"soat": "3-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Musharraf"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
        ],
        "Shanba": [],
    },

    "3-B": {  # Sinf rahbar: Sultanova Farida Safaraliyevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Farida"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Farida"},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Farida"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Farida"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Farida"},
            {"soat": "2-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Farida"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Farida"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Farida"},
            {"soat": "3-dars", "fan": "O'qish savodxonligi", "ustoz": "Farida"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Farida"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Farida"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Farida"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Farida"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Farida"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Farida"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
        ],
        "Shanba": [],
    },

    "3-V": {  # Sinf rahbar: Yakubova Mashhura Kurbonboyevna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "5-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Mashhura"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Mashhura"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mashhura"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Mashhura"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mashhura"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Mashhura"},
            {"soat": "3-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Mashhura"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mashhura"},
            {"soat": "2-dars", "fan": "O'qish savodxonligi", "ustoz": "Mashhura"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulruh"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
        ],
        "Shanba": [],
    },

    "3-D": {  # Sinf rahbar: Qodirova Aziza Xujayarovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "O'zbek tili", "ustoz": "Marg'uba"},
            {"soat": "2-dars", "fan": "O'zbek tili", "ustoz": "Marg'uba"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Aziza"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Aziza"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Aziza"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Aziza"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "5-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Aziza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Aziza"},
            {"soat": "5-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Aziza"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Aziza"},
            {"soat": "3-dars", "fan": "Texnologiya", "ustoz": "Aziza"},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Aziza"},
            {"soat": "5-dars", "fan": "Rasm", "ustoz": "Aziza"},
        ],
        "Shanba": [],
    },

    "3-E": {  # Sinf rahbar: Yusupova Dilnoza Xolmuhammatova
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Dilnoza X."},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Dilnoza X."},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Dilnoza X."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Dilnoza X."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "4-dars", "fan": "Tabiiy fan (Science)", "ustoz": "Dilnoza X."},
            {"soat": "5-dars", "fan": "O'qish savodxonligi", "ustoz": "Dilnoza X."},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Dilnoza X."},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Dilnoza X."},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Dilnoza X."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Dilnoza X."},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Dilnoza X."},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Dilnoza X."},
        ],
        "Shanba": [],
    },

    "3-F": {  # Sinf rahbar: Yusufjonova Sevinch Erkin qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "2-dars", "fan": "O'qish savodxonligi", "ustoz": "Sevinch Y."},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Sevinch Y."},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "5-dars", "fan": "Tasviriy san'at", "ustoz": "Sevinch Y."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevinch Y."},
            {"soat": "2-dars", "fan": "O'qish savodxonligi", "ustoz": "Sevinch Y."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sardor"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Sardor"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Sevinch Y."},
            {"soat": "4-dars", "fan": "Informatika va axborot texnologiyalari", "ustoz": "Sevinch Y."},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Sevinch Y."},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "3-dars", "fan": "Texnologiya", "ustoz": "Sevinch Y."},
            {"soat": "4-dars", "fan": "O'qish savodxonligi", "ustoz": "Sevinch Y."},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Sevinch Y."},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sevinch Y."},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Shanba": [],
    },

    "3-G": {  # Sinf rahbar: Marupova Diyora Axmatovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora M."},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Diyora M."},
            {"soat": "5-dars", "fan": "O'qish savodxonligi", "ustoz": "Diyora M."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora M."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Diyora M."},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora M."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Diyora M."},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "5-dars", "fan": "Musiqa", "ustoz": "Diyora M."},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Diyora M."},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Diyora M."},
            {"soat": "3-dars", "fan": "Texnologiya", "ustoz": "Diyora M."},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Gulshoda"},
            {"soat": "2-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Diyora M."},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "O'qish savodxonligi", "ustoz": "Diyora M."},
        ],
        "Shanba": [],
    },

    # ========================================================
    # 4-SINF (qisman - 4-A, 4-B, 4-V, 4-G)
    # ========================================================

    "4-A": {  # Sinf rahbar: Pardayeva Marg'uba Xoliqovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Marg'uba"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Marg'uba"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Marg'uba"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Hilola"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Marg'uba"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Marg'uba"},
        ],
        "Shanba": [],
    },

    "4-B": {  # Sinf rahbar: Avazova Gulchexra Alimjanovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Gulchexra"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Gulchexra"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Gulchexra"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Gulchexra"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Gulchexra"},
        ],
        "Shanba": [],
    },

    "4-V": {  # Sinf rahbar: Giyeyeva Zumrat Maxmudali qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Zumrat"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Zumrat"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Zumrat"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zarnigor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Zumrat"},
        ],
        "Shanba": [],
    },

    "4-G": {  # Sinf rahbar: Abdurasulova Mukaddas Tashtemirovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Mukaddas"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Zumrat"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Mukaddas"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Doniyor"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Eldor"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Mukaddas"},
        ],
        "Shanba": [],
    },

    "4-D": {  # Sinf rahbar: Nurmatova Nargiza Abdug'affor qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Tabiiy fan", "ustoz": "Nargiza"},
            {"soat": "5-dars", "fan": "O'qish (rus)", "ustoz": "Nargiza"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Nargiza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "5-dars", "fan": "Rasm", "ustoz": "Nargiza"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Nargiza"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Nargiza"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "5-dars", "fan": "Texnologiya", "ustoz": "Nargiza"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Nargiza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Nargiza"},
        ],
        "Juma": [],  # TEKSHIRING: PDF matnida bu kun aniq ajratib bo'lmadi
        "Shanba": [],
    },

    "4-E": {  # Sinf rahbar: Shadiyeva Ra'no Baxodirovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Ra'no"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Ra'no"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Sardor"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Dilrabo"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Xurshid"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Ra'no"},
        ],
        "Juma": [],  # TEKSHIRING: PDF matnida bu kun aniq ajratib bo'lmadi
        "Shanba": [],
    },

    "4-F": {  # Sinf rahbar: Buribayeva Xolida Narzikulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Xolida F."},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Xolida F."},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "E'zoza"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xolida F."},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Begzod"},
            {"soat": "2-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Javohir"},
            {"soat": "3-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "4-dars", "fan": "Mantiqiy fikrlash", "ustoz": "Zafar"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Xolida F."},
        ],
        "Juma": [],  # TEKSHIRING: PDF matnida bu kun aniq ajratib bo'lmadi
        "Shanba": [],
    },

    # ========================================================
    # 5-SINF
    # ========================================================

    "5-A": {  # Sinf rahbar (Matematika): Maxmud
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "5-dars", "fan": "Informatika", "ustoz": "Sarvar"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Maxmud"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "3-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Iroda"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Informatika", "ustoz": "Sarvar"},
        ],
    },

    "5-B": {  # Sinf rahbar: Raxmonova Go'zal Bobir qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
        ],
    },

    "5-V": {  # Sinf rahbar: Sharafbayeva Pokiza Alikulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "3-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "3-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "4-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
        ],
    },

    "5-G": {  # Sinf rahbar: Sharafbayeva Pokiza Alikulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "3-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "2-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
            {"soat": "3-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Kamila"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
    },

    "5-D": {  # Sinf rahbar: Sharafbayeva Pokiza Alikulovna
        "Dushanba": [
            {"soat": "1-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Maloxat"},
            {"soat": "4-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Kamila"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Kamila"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "3-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Kamila"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "4-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Lola"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Kamila"},
        ],
    },

    # ========================================================
    # 6-SINF
    # ========================================================

    "6-A": {  # Sinf rahbar: Jalilov Bobur Toir o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "3-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "3-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "4-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
        ],
    },

    "6-B": {  # Sinf rahbar: Xusanov Doniyor Xakim o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "5-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "5-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
        ],
    },

    "6-G": {  # Sinf rahbar: Xusanov Doniyor Xakim o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "3-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "5-dars", "fan": "Informatika", "ustoz": "Sarvar"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "5-dars", "fan": "Biologiya", "ustoz": "Islom"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "2-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
        ],
    },

    "6-D": {  # Sinf rahbar: Abdullayev Abdulaziz Sobirjon o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "3-dars", "fan": "Informatika", "ustoz": "Sarvar"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "4-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Iroda"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "5-dars", "fan": "Informatika", "ustoz": "Sarvar"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "I.Feruza"},
        ],
    },

    # ========================================================
    # 7-SINF
    # ========================================================

    "7-A": {  # Sinf rahbar: Raxmonova Go'zal Bobir qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "3-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Mohichehra"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Fazliddin"},
        ],
    },

    "7-B": {  # Sinf rahbar: Abdullayev Abdulaziz Sobirjon o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "2-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Nargiza"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Islom"},
        ],
    },

    "7-V": {  # Sinf rahbar: Xusanov Doniyor Xakim o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "2-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "4-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "4-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Sarvar"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Malika"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Sarvar"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Sarvar"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
        ],
    },

    "7-G": {  # Sinf rahbar: Raxmonova Go'zal Bobir qizi
        "Dushanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "3-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "2-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "4-dars", "fan": "Fizika", "ustoz": "Noila"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "4-dars", "fan": "Fizika", "ustoz": "Noila"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Nodira"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
        ],
    },

    # ========================================================
    # 8-SINF
    # ========================================================

    "8-A": {  # Sinf rahbar: Jalilov Bobur Toir o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Ro'zigul"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "4-dars", "fan": "Tabiiy fan", "ustoz": "Saidahmad"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Maxmud"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Ro'zigul"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "2-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Fizika", "ustoz": "Noila"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Ro'zigul"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Maxmud"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Sherzod"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Ro'zigul"},
            {"soat": "3-dars", "fan": "Fizika", "ustoz": "Noila"},
            {"soat": "4-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhammadjon"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Maxmud"},
        ],
    },

    "8-B": {  # Sinf rahbar: Abdullayev Abdulaziz Sobirjon o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "5-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Ilgiz"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "2-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
    },

    "8-V": {  # Sinf rahbar: Abdullayev Abdulaziz Sobirjon o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "3-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "5-dars", "fan": "Biologiya", "ustoz": "Islom"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "3-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Umid"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Sadoqat"},
        ],
    },

    "8-D": {  # Sinf rahbar: Jalilov Bobur Toir o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
            {"soat": "4-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Iroda"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Ilhom"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "2-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Iroda"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Ilhom"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Mansur"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Musulmon"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Ilhom"},
        ],
    },

    # ========================================================
    # 9-SINF
    # ========================================================

    "9-A": {  # Sinf rahbar: Jalilov Bobur Toir o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xasan"},
            {"soat": "4-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
            {"soat": "5-dars", "fan": "Huquq", "ustoz": "Mirjalol"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
            {"soat": "4-dars", "fan": "Huquq", "ustoz": "Mirjalol"},
            {"soat": "5-dars", "fan": "Huquq", "ustoz": "Mirjalol"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Sodiq"},
            {"soat": "3-dars", "fan": "Huquq", "ustoz": "Mirjalol"},
            {"soat": "4-dars", "fan": "Huquq", "ustoz": "Mirjalol"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Muhriddin"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
        ],
    },

    "9-B": {  # Sinf rahbar: Abdullayev Abdulaziz Sobirjon o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "3-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Umid"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "4-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Umid"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Islom"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "3-dars", "fan": "Rus tili", "ustoz": "Anjelika"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Umid"},
            {"soat": "5-dars", "fan": "O'zbek tili", "ustoz": "Ro'zigul"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Tarix", "ustoz": "Shoxrux"},
        ],
    },

    "9-V": {  # Sinf rahbar: Jalilov Bobur Toir o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "3-dars", "fan": "Jismoniy tarbiya", "ustoz": "Xakim"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Asadbek"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Asadbek"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "5-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "5-dars", "fan": "Fizika", "ustoz": "Noila"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "3-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
            {"soat": "5-dars", "fan": "Ona tili", "ustoz": "Soxiba"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Gulmira"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "5-dars", "fan": "Fizika", "ustoz": "Noila"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "2-dars", "fan": "Ingliz tili", "ustoz": "Zebo"},
        ],
    },

    "9-D": {  # Sinf rahbar: Xusanov Doniyor Xakim o'g'li
        "Dushanba": [
            {"soat": "1-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "2-dars", "fan": "Biologiya", "ustoz": "Xayrullo"},
            {"soat": "3-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
            {"soat": "4-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "5-dars", "fan": "Jismoniy tarbiya", "ustoz": "Bekmurod"},
        ],
        "Seshanba": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Ismoil"},
            {"soat": "2-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "3-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "5-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
        "Chorshanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Xayrullo"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
        ],
        "Payshanba": [
            {"soat": "1-dars", "fan": "Suniy intelekt", "ustoz": "Samandar"},
            {"soat": "2-dars", "fan": "Kimyo", "ustoz": "Ismoil"},
            {"soat": "3-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "4-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
            {"soat": "5-dars", "fan": "Tarix", "ustoz": "Mirjalol"},
        ],
        "Juma": [
            {"soat": "1-dars", "fan": "Kimyo", "ustoz": "Ismoil"},
            {"soat": "2-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
            {"soat": "3-dars", "fan": "Ona tili", "ustoz": "Iroda"},
            {"soat": "4-dars", "fan": "Ingliz tili", "ustoz": "Shohida"},
            {"soat": "5-dars", "fan": "Matematika", "ustoz": "Abdurahmon"},
        ],
        "Shanba": [
            {"soat": "1-dars", "fan": "Biologiya", "ustoz": "Xayrullo"},
            {"soat": "2-dars", "fan": "Rus tili", "ustoz": "Nasiba"},
        ],
    },

}


# ============================================================
# O'QITUVCHILAR JADVALI - CLASSES asosida AVTOMATIK hisoblanadi
# ============================================================
# Bu yerga QO'LDA hech narsa yozilmaydi - kod o'zi CLASSES'dan yig'ib chiqadi.
# Shu tufayli sinf jadvali va o'qituvchi jadvali doim bir-biriga mos keladi.

def _build_teachers_from_classes(classes_dict):
    teachers = {}
    for class_name, days in classes_dict.items():
        for day, lessons in days.items():
            for lesson in lessons:
                ustoz = lesson["ustoz"]
                if ustoz not in teachers:
                    teachers[ustoz] = {d: [] for d in DAYS}
                teachers[ustoz][day].append({
                    "soat": lesson["soat"],
                    "sinf": class_name,
                    "fan": lesson["fan"],
                })
    return teachers


TEACHERS = _build_teachers_from_classes(CLASSES)
