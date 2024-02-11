

'''


1- 	import sounddevice as sd: sounddevice kütüphanesini sd takma adıyla içe aktarır.

2- 	sure: Kayıt süresini belirten bir değişken. Bu değişkenin önceden tanımlanmış bir değeri olmalıdır.

3- 	frekans: Örnekleme frekansını belirten bir değişken. Bu, ses kaydının örnekleme frekansını Hz cinsinden belirtir.

4- 	channels=1 Kayıtta kullanılacak ses kanalı sayısını belirten bir parametre. Bu durumda, 2 kanallı (stereo) bir ses
	kaydı yapılmaktadır.

5- 	sd.rec(int(duration * freq), samplerate=freq, channels=2): Ses kaydını başlatan fonksiyon. sd.rec fonksiyonu,
	elirtilen süre ve örnekleme frekansı ile ses kaydını başlatır. int(duration * freq) ifadesi, kayıt süresini örnekleme
	frekansıyla çarpıp bir tam sayıya dönüştürerek örnek sayısını belirler. Bu kodun çalışması için öncesinde sounddevice
	kütüphanesini yüklemeniz gerekir.


'''

import sounddevice as sd
from scipy.io.wavfile import write as write_wav
import wave as wv

# Önce bazı değişkenleri tanımlayalım
frekans = 44100  # Örnekleme frekansı (Hz)
sure = 10  # Kayıt süresi (saniye)

# Ses kaydını başlat
recording = sd.rec(int(sure * frekans), samplerate=frekans, channels=1)
sd.wait()  # Kayıt tamamlanana kadar bekleyin

# Kaydedilen sesi dosyaya yazma
write_wav("recording0.wav", frekans, recording)

# Alternatif bir yöntemle sesi dosyaya yazma
with wv.open("recording1.wav", "wb") as wf:
    wf.setnchannels(1)  # 1 kanal (monaural)
    wf.setsampwidth(2)  # 2 byte'lık örnekleme genişliği
    wf.setframerate(frekans)
    wf.writeframes(recording.tobytes())