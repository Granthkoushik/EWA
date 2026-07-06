from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code='a')

text = "Hello GK. I'm EWA. Nice to meet you."

generator = pipeline(
    text,
    voice="af_heart",
)

for i, (gs, ps, audio) in enumerate(generator):
    sf.write(f"output_{i}.wav", audio, 24000)

print("Done!")