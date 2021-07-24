import sys
sys.path.append("../")
import numpy as np
import os
import gin
import secrets
import threading
import logging
import random, time
import asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends, Response, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import base64
from pydantic import BaseModel
# from fennekservice.models.samplevae.samplevae import SampleVAEModel
from mimetypes import guess_type
from fennekservice.generation import dict_models
from fennekservice.visualization import pltToString, getWaveForm, getSpectrogram
from fennekservice.generation import initializeModels, get_tsne_and_preload_model, preload_similarity, generate_sound, play_sound, play_sound_original,applyEffectsOnGeneratedFile, upload_file, decode_and_save_file, get_generation_file
from fennekservice.postprocessing import Postprocessor
from fennekservice.mongo import connect_mongoDB, get_mongoDB_presets, post_mongoDB_bookmarks,  get_mongoDB_bookmarks, get_mongoDB_bookmarkListPerUser, post_mongoDB_history, get_mongoDB_historyListPerUser, get_mongoDB_history
# from fennekservice.generation import genera3te_clap
import pymongo
from fennekservice.postprocessing import Postprocessor
from fennekservice.models.samplevae.samplevae import SampleVAEModel
#@gin.configurable
#def generate_clap(input_wave,
# _id: str = 'my_model', library_dir: str = 'mylibdir', **kwargs):
#    print("FUCK!")


class GenerateBody(BaseModel):
    data: Optional[str]
    volume_value: Optional[int]
    distortion_value: Optional[int]
    reverb_value: Optional[int]
    ae_variance: Optional[int]
    highpass_value: Optional[int]
    lowpass_value: Optional[int]
    isReversed: Optional[bool]
    selectedPoint: Optional[str]
    model: Optional[str]
    model_instrument: Optional[str]
    timestamp: Optional[str]
    username: Optional[str]


class MongoBody(BaseModel):
    id: Optional[str]
    type: Optional[str]


app = FastAPI()
security = HTTPBasic()
mongoDB_client = connect_mongoDB()


@gin.configurable
def get_valid_credentials():
    userlist = {
        "1": {
            "uname": "Ian",
            "pw": "Goodfellow"
        },
        "2": {
            "uname": "Jimmy",
            "pw": "Hendrix"
        },
        "3": {
            "uname": "Elton",
            "pw": "John"
        },
        "4": {
            "uname": "Amy",
            "pw": "Winehouse"
        }
    }
    return userlist


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    print("HERE HERE HERE HERE HERE")
    x = get_valid_credentials()

    correct_username = None
    correct_password = None

    for key in x.values():
        correct_username = secrets.compare_digest(credentials.username, key["uname"])
        correct_password = secrets.compare_digest(credentials.password, key["pw"])

        if (correct_username and correct_password):
            return credentials.username

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Anton denied your request. Does he know you?",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


@app.get('/healthcheck')
def read_root(username: str = Depends(get_current_username)):
    return 'Anton works. Greetings.'


@app.post("/getMongoDBData")
def getMongoData(body: MongoBody, username: str = Depends(get_current_username)):
    #RetrieveData
    response_content = "no audio"
    if body.type == "presets":
        x = get_mongoDB_presets(mongoDB_client, body.id)
        response = {
        "distortion_value": x["v_distortion"],
        "reverb_value": x["v_reverb"],
        "highpass_value": x["v_highpass"],
        "lowpass_value": x["v_lowpass"],
        "isReversed": x["v_isReversed"],
        "volume_value": x["v_volume"]
        }

    if body.type == "bookmark":
        #EMRHN TBD: AUch die Audio Datei zurückgeben
        print(body.id)
        x = get_mongoDB_bookmarks(username, mongoDB_client, body.id)
        response_content = x["WAV"]
        decode_and_save_file(data=response_content, username=username)
        response = {
            "result": response_content,
            "distortion_value": x["v_distortion"],
            "reverb_value": x["v_reverb"],
            "highpass_value": x["v_highpass"],
            "lowpass_value": x["v_lowpass"],
            "isReversed": x["v_isReversed"],
            "volume_value": x["v_volume"]
        }

    if body.type == "history":
        print(body.id)
        x = get_mongoDB_history(username, mongoDB_client, body.id)
        response_content = x["WAV"]
        decode_and_save_file(data=response_content, username=username)
        #base64.decode(response_content)
        #EMRHN TBD: neue Methode für history und auch audiodatei mitgeben
        #x = get_mongoDB_bookmarks(username, mongoDB_client, body.id)

        response= {"result": response_content}
    print(x)
    return response

@app.post("/getMongoDBList")
def getMongoDataList(body: MongoBody, username: str = Depends(get_current_username)):

    if body.type == "bookmarks":
        x = get_mongoDB_bookmarkListPerUser(username, mongoDB_client)

    if body.type == "history":
        x = get_mongoDB_historyListPerUser(username, mongoDB_client)
        #EMRHN TBD
    #print(x["ObjectId"])
    #print(x[0])
    #print(x[0]["_id"])
    return {
        "result": x
    }

@app.post("/generate")
async def generate(body: GenerateBody, username: str = Depends(get_current_username)):
    response_content, model_instrument = await generate_sound(body.data,model_id=body.model,model_instrument=body.model_instrument,selectedPoint=body.selectedPoint,ae_variance=body.ae_variance, username=username)

    post_mongoDB_history(uname=username, db=mongoDB_client, model=body.model, model_instrument=model_instrument, timestamp=body.timestamp, wavfile=base64.b64encode(response_content))

    return {
        "result": base64.b64encode(response_content)
        #"visualization": [
        #    {"name": "Waveform",
        #     "base64img": pltToString(getWaveForm("fennekservice/generated.wav"))},
        #    {"name": "Spectrogram",
        #     "base64img": pltToString(getSpectrogram("fennekservice/generated.wav"))}
        #]
    }

@app.post("/generate2")
async def generate(body: GenerateBody, background_tasks: BackgroundTasks, username: str = Depends(get_current_username)):
    background_tasks.add_task(write_log, message)
    response_content, model_instrument = generate_sound(body.data,model_id=body.model,model_instrument=body.model_instrument,selectedPoint=body.selectedPoint,ae_variance=body.ae_variance, username=username)
    post_mongoDB_history(uname=username, db=mongoDB_client, model=body.model, model_instrument=model_instrument, timestamp=body.timestamp, wavfile=base64.b64encode(response_content))

    return {
        "result": base64.b64encode(response_content)
        #"visualization": [
        #    {"name": "Waveform",
        #     "base64img": pltToString(getWaveForm("fennekservice/generated.wav"))},
        #    {"name": "Spectrogram",
        #     "base64img": pltToString(getSpectrogram("fennekservice/generated.wav"))}
        #]
    }


@app.post("/getVisualization")
def visualize(body: GenerateBody, username: str = Depends(get_current_username)):
    #response_content = play_clap(body.data)

    usr_outfile = "fennekservice/" + username + "-processed.wav"
    return {
        "visualization": [
            {"name": "Waveform",
             "base64img": pltToString(getWaveForm(usr_outfile))},
            {"name": "Spectrogram",
             "base64img": pltToString(getSpectrogram(usr_outfile))}
        ]
    }

@app.post("/tsne")
def tsne(body: GenerateBody, username: str = Depends(get_current_username)):
    #TSNE and Preload
    response = get_tsne_and_preload_model(model_instrument=body.model_instrument, username=username)
    response2 = []
    response2.append(response)
    return {
        "result": response2
    }

@app.post("/similarity")
def tsne(username: str = Depends(get_current_username)):
    response = preload_similarity(username=username)

    return {
        "result": response
    }

@app.post("/upload")
def upload(body: GenerateBody, username: str = Depends(get_current_username)):

    upload_file(data=body.data, username=username)

    response = "upload successfull"
    return {
        "result": response
    }

@app.post("/play")
def play(body: GenerateBody, username: str = Depends(get_current_username)):

    if body.data == "original":
        print(body.data)
        response_content = play_sound_original(selectedPoint=body.selectedPoint, username=username, model_instrument=body.model_instrument)
    else:
        response_content = play_sound(body.data, username=username)

    return {
        "result": base64.b64encode(response_content)
        #"visualization": [
        #    {"name": "Waveform",
        #     "base64img": pltToString(getWaveForm("fennekservice/processed.wav"))},
        #    {"name": "Spectrogram",
        #     "base64img": pltToString(getSpectrogram("fennekservice/processed.wav"))}
        #]
    }

@app.post("/bookmark")
def addToBookmarks(body: GenerateBody, username: str = Depends(get_current_username)):
    current_sound = get_generation_file(username=username)
    x = post_mongoDB_bookmarks(username, mongoDB_client, body.isReversed,body.lowpass_value,body.highpass_value,body.distortion_value,body.reverb_value,body.volume_value, body.model, body.model_instrument, body.timestamp, wavfile=base64.b64encode(current_sound))
    response_content = "Successfully saved it as Bookmark with id" + str(x)
    return {
        "result": response_content
    }


@app.post("/effects")
def addEffects(body: GenerateBody, username: str = Depends(get_current_username)):
    applyEffectsOnGeneratedFile(body.isReversed,body.lowpass_value,body.highpass_value,body.distortion_value,body.reverb_value,body.volume_value, username=username)
    response_content = "Successfully Applied effects on Generated.wav"
    return {
        "result": response_content
    }
@app.post("/initializeModels")
async def initializeModelsThread(body: GenerateBody, username: str = Depends(get_current_username)):
    await startThreadsForModels()

    return {
        "result": "response_content"
    }

@app.get("/{filepath:path}")
async def get_site(filepath, username: str = Depends(get_current_username)):
    if filepath == "":
        filepath = "index.html"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir_path, "fennekservice", "static", filepath)

    print(filename)

    if not os.path.isfile(filename):
        return Response(status_code=404)

    with open(filename, 'rb') as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


def main():
    #connect_mongoDB()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    gin.parse_config_file(os.path.join(dir_path, 'config.gin'))

    #loop = asyncio.get_event_loop()
    #loop.create_task(startThreadsForModels())
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", default=5000))



async def startThreadsForModels():
    #x = threading.Thread(target=initializeModels)
    print("geht es los?")
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.getLogger('matplotlib.font_manager').disabled = True
    logging.info('Initializing Models Started')
    items = 15
    workers = 8

    test = range(items)
    print(test)
    tasks = list(dict_models.keys())

    #initializeModels("Kick")
    with ThreadPoolExecutor(max_workers=workers) as e:
        #executer.map(initializeModels,)
        #e.map(test, taks)
        e.map(initializeModels, tasks)
    logging.info('Initializing Models Finished')
    #x.start()

def test(item):
    print(item)
    s = random.randrange(1,10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')

if __name__ == "__main__":
    main()
    #tsne()
