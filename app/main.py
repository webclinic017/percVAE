import sys
sys.path.append("../")

import os
import gin
import secrets
from typing import Optional
import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends, Response
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import base64
from pydantic import BaseModel
# from fennekservice.models.samplevae.samplevae import SampleVAEModel
from mimetypes import guess_type
from fennekservice.visualization import pltToString, getWaveForm, getSpectrogram
from fennekservice.generation import generate_sound, play_sound, applyEffectsOnGeneratedFile
from fennekservice.postprocessing import Postprocessor
from fennekservice.mongo import connect_mongoDB, get_mongoDB_presets, post_mongoDB_bookmarks,  get_mongoDB_bookmarks, get_mongoDB_bookmarkListPerUser
# from fennekservice.generation import genera3te_clap
import pymongo

#@gin.configurable
#def generate_clap(input_wave, model_id: str = 'my_model', library_dir: str = 'mylibdir', **kwargs):
#    print("FUCK!")


class GenerateBody(BaseModel):
    data: Optional[str]
    volume_value: Optional[int]
    distortion_value: Optional[int]
    reverb_value: Optional[int]
    highpass_value: Optional[int]
    lowpass_value: Optional[int]
    isReversed: Optional[bool]
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
    print("ok jetzt müssen wir die Backenddaten rausholen!")
    response_content = "ja geil"
    if body.type == "presets":
        x = get_mongoDB_presets(mongoDB_client, body.id)

    if body.type == "bookmark":
        print(body.id)
        x = get_mongoDB_bookmarks(username, mongoDB_client, body.id)

    print(x)
    return {
        "distortion_value": x["v_distortion"],
        "reverb_value": x["v_reverb"],
        "highpass_value": x["v_highpass"],
        "lowpass_value": x["v_lowpass"],
        "isReversed": x["v_isReversed"],
        "volume_value": x["v_volume"]
    }
@app.post("/getMongoDBList")
def getMongoDataList(body: MongoBody, username: str = Depends(get_current_username)):
    x = get_mongoDB_bookmarkListPerUser(username, mongoDB_client)
    #print(x["ObjectId"])
    #print(x[0])
    #print(x[0]["_id"])
    return {
        "result": x
    }


@app.post("/generate")
def generate(body: GenerateBody, username: str = Depends(get_current_username)):
    response_content = generate_sound(body.data,model_id=body.model,model_instrument=body.model_instrument, username=username)

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

@app.post("/play")
def play(body: GenerateBody, username: str = Depends(get_current_username)):
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
    x = post_mongoDB_bookmarks(username, mongoDB_client, body.isReversed,body.lowpass_value,body.highpass_value,body.distortion_value,body.reverb_value,body.volume_value, body.model, body.model_instrument, body.timestamp)
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


#def main():
    #connect_mongoDB()
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    gin.parse_config_file(os.path.join(dir_path, 'config.gin'))
#    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", default=5000))


#if __name__ == "__main__":
#    main()
