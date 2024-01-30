import json
import asyncio
import speech_recognition as sr
import websockets

class SpeechRecognitionConsumer:
    async def connect(self, websocket):
        await websocket.accept()

        recognizer = sr.Recognizer()

        async def process_audio():
            while True:
                try:
                    audio_data = await websocket.recv()
                    with sr.AudioFile(audio_data) as source:
                        audio = recognizer.record(source)

                    text = recognizer.recognize_google(audio)
                    await websocket.send(json.dumps({'text': text}))

                except sr.UnknownValueError:
                    await websocket.send(json.dumps({'error': 'Speech Recognition could not understand audio'}))

                except sr.RequestError as e:
                    await websocket.send(json.dumps({'error': f'Could not request results from Google Speech Recognition service; {e}'}))

        asyncio.ensure_future(process_audio())

def as_asgi():
    return SpeechRecognitionConsumer()
