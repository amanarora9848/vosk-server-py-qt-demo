#!/usr/bin/env python3

import websockets
import wave
import json


async def run_test_wav(uri):
    async with websockets.connect(uri) as websocket:

        # wf = wave.open(sys.argv[1], "rb")
        wf = wave.open("recording.wav", "rb")
        await websocket.send('{ "config" : { "sample_rate" : %d } }' % (wf.getframerate()))
        buffer_size = int(wf.getframerate() * 2.2)  # 2.2 seconds of audio

        response_ = []

        while True:
            data = wf.readframes(buffer_size)

            if len(data) == 0:
                break

            await websocket.send(data)
            response_.append(json.loads(str(await websocket.recv())))

        await websocket.send('{"eof" : 1}')
        response_.append(json.loads(str(await websocket.recv())))

        # Gather all the recognized output text
        recognized_text = ""
        for output_dict in response_:
            if "result" in output_dict:
                recognized_text = recognized_text + output_dict['text'] + " "

        return recognized_text
