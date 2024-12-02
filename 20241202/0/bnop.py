"Вопрос".encode("WINDOWS-1251").decode("KOI8-R")
txt = "бМХЛЮМХЕ"
print(txt.encode("KOI8-R").decode("CP1251"))
txt = "ОХРЮМХЕ"
print(txt.encode("KOI8-R").decode("CP1251"))
