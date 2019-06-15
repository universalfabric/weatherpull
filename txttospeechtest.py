from gtts import gTTS
import playsound as ps

mytext = "In Kenosha, the current weather condition is mist, with a temperature of 68 " \
         "degrees. The relative humidity is 95 percent." \
         "The barometric pressure is 29.92 inches of mercury and" \
         "the wind is 10 miles per hour at 090." \
         "Cloud cover is 90 percent." \
         "Sunrise is at 5:15AM and sunset is at 8:31 P M"

language = "en"

myobj = gTTS(text=mytext, lang=language)
myobj.save('testspeech.mp3')

mysound = ps.playsound('testspeech.mp3')