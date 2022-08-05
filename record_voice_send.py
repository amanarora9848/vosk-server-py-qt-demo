#!/usr/bin/env python3

import sounddevice as sd
import wavio as wv


def record_sound():
    freq = 16000
    duration = 5

    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)

    sd.wait()

    wv.write("recording.wav", recording, freq, sampwidth=2)

    return 1
