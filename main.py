import cv2 as cv

foto = cv.imread("gambar/upacara1.jpeg")
foto_gray = cv.cvtColor(foto, cv.COLOR_BGR2GRAY)

cc_wajah = cv.CascadeClassifier("env/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
if cc_wajah.empty():
    raise IOError("file XML tidak di temukan")

hasil = cc_wajah.detectMultiScale(foto_gray, scaleFactor=1.1)
print(hasil)

jumlah_wajah = len(hasil)
print("Terdeteksi", jumlah_wajah, "orang didalam gambar")

x = (hasil[0][0])
y = (hasil[0][1])
w = (hasil[0][2])
h = (hasil[0][3])

for (x,y,w,h) in hasil:
    cv.rectangle(foto, (x,y), (x+w,y+h), color=(0,225,0), thickness=5)

cv.imshow("Foto Presiden RI 2", foto)
cv.imwrite("hasil-deteksi.jpg", foto)
cv.waitKey(0)
cv.destroyAllWindows()