import os, random
import base64
import wave
import gin
from pydub import AudioSegment
from pydub.playback import play
from pysndfx import AudioEffectsChain
import librosa
import math
import gc

from fennekservice.postprocessing import Postprocessor
from fennekservice.models.samplevae.samplevae import SampleVAEModel

Samplevae_model1 = SampleVAEModel()
Samplevae_model2 = SampleVAEModel()
Samplevae_model3 = SampleVAEModel()
Samplevae_model4 = SampleVAEModel()

def getSampleVAE(username):
    if username == "Amy":
        print(username)
        global Samplevae_model1
        return Samplevae_model1
    elif username == "Elton":
        global Samplevae_model2
        return Samplevae_model2
    elif username == "Jimmy":
        global Samplevae_model3
        return Samplevae_model3
    elif username == "Ian":
        global Samplevae_model4
        return Samplevae_model4
    else:
        return SampleVAEModel()

def assignSampleVAE(username, SampleVAE):
    print("assignment of SampleVAE Instance to User started")
    if username == "Amy":
        global Samplevae_model1
        Samplevae_model1 = SampleVAE
    elif username == "Elton":
        global Samplevae_model2
        Samplevae_model2 = SampleVAE
    elif username == "Jimmy":
        global Samplevae_model3
        Samplevae_model3 = SampleVAE
    elif username == "Ian":
        global Samplevae_model4
        Samplevae_model4 = SampleVAE


dict_models = {"Kick": 'model_kick',
          "Snare": 'model_snare',
          "Conga": 'model_conga',
          "Cowbell": 'model_cowbell',
          "Crash": 'model_crash',
          "Ride": 'model_ride',
          "Rimshot": 'model_rimshot',
          "Toms": 'model_toms',
          "Clap": 'model_clap',
          "Hihat": 'model_hihat',
          "Similarity Search": 'model_all2'
          }
dict_library_dir = {
    "Kick": 'fennekservice/models/samplevae/model_kick',
    "Snare": 'fennekservice/models/samplevae/model_snare',
    "Conga": 'fennekservice/models/samplevae/model_conga',
    "Cowbell": 'fennekservice/models/samplevae/model_cowbell',
    "Crash": 'fennekservice/models/samplevae/model_crash',
    "Ride": 'fennekservice/models/samplevae/model_ride',
    "Rimshot": 'fennekservice/models/samplevae/model_rimshot',
    "Toms": 'fennekservice/models/samplevae/model_toms',
    "Clap": 'fennekservice/models/samplevae/model_clap',
    "Hihat": 'fennekservice/models/samplevae/model_hihat',
    "Similarity Search": 'fennekservice/models/samplevae'}

@gin.configurable
def generate_sound(input_wave, model_id: str = 'my_model',  model_instrument: str = 'my_instrument', ae_variance: float = 0.0, selectedPoint: str = '', library_dir: str = 'mylibdir', username: str = "Ian", **kwargs):

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_upload_file_path = "fennekservice/" + username + "-upload.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)
    usr_upload_file = os.path.join(cwd, usr_upload_file_path)
    result_wave = None

    print("welches Modell wurde Gewählt?")
    print(model_id)
    print(model_instrument)

    #print("Selected Point")
    #print(selectedPoint)
    #print("AE_Variance")
    #print(ae_variance)
    #if input_wave:
    #    #TODO: Do something with the input audio
    #    print("Wir haben ein input File")
    #    with open(os.path.join("cachedir", "tmpfile.wav"), "wb") as f:
    #        f.write(base64.b64decode(input_wave))

    #if model_id == "GAN":
    #    dir_model_id = "fennekservice/models/" + model_id
    #    model_id_directory = os.path.join(cwd,dir_model_id)
    #    model_instrument_directory = os.path.join(model_id_directory,model_instrument)
    #    result_wave = random.choice(os.listdir(model_instrument_directory))
    #    file_dir = os.path.join(model_instrument_directory, result_wave)
    #
    #    with open(file_dir, "rb") as f:
    #        result_wave = f.read()
    #
    #    with open(file, "wb") as fout:
    #        fout.write(result_wave)


    if model_id == "Variational Autoencoder":
        Samplevae_model = getSampleVAE(username=username)
        print("Test GET Methods")
        if Samplevae_model.get_instrument() == model_instrument:
            print("Model wieder nutzen")
            if selectedPoint == None:
                selectedPoint = ""
            result_wave = Samplevae_model.forward(selectedSound=selectedPoint, ae_variance=ae_variance)
        else:
            print("Model NICHT wieder nutzen")
            print(Samplevae_model.get_instrument())
            print(model_instrument)
            #result_wave = Samplevae_model(model_id="model_snare2", library_dir=library_dir,selectedSound = selectedPoint, ae_variance=ae_variance)
            Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
                                             instrument=model_instrument,
                                             library_dir=dict_library_dir[model_instrument])
            result_wave = Samplevae_model.forward(selectedSound=selectedPoint, ae_variance=ae_variance)
            assignSampleVAE(username=username, SampleVAE=Samplevae_model)

        with open(file, "wb") as fout:
            fout.write(result_wave)


    if model_id == "Similarity Search":
        print("Similarity Search!")
        Samplevae_model = getSampleVAE(username=username)
        model_instrument="Similarity Search"
        if Samplevae_model.get_instrument() == model_instrument:
            print("Model wieder nutzen")
        else:
            Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
                                                 instrument=model_instrument,
                                                 library_dir=dict_library_dir[model_instrument])
            assignSampleVAE(username=username, SampleVAE=Samplevae_model)
        similarSounds = Samplevae_model.find_similar(target_file=usr_upload_file)
        #write_similar_files_to_txt(username=username, text=similarSounds)
        result_wave = Samplevae_model.forward(selectedSound=similarSounds[0])

        path = similarSounds[0]
        dirofdir = os.path.dirname(os.path.dirname(path))
        dirname1 = os.path.basename(dirofdir)
        print(dirname1)


        for key, value in dict_models.items():
            if value == dirname1:
                print(key)
                model_instrument = key

        #with open(similarSounds[0], "rb") as f:
        #    result_wave = f.read()
        with open(file, "wb") as fout:
            fout.write(result_wave)

    fx = (
        AudioEffectsChain()
    )
    fx(file, outfile)

    gc.collect()
    return result_wave, model_instrument

def play_sound(input_wave, model_id: str = 'my_model', library_dir: str = 'mylibdir',username: str = "Ian", **kwargs):
    #print("Zeit das Processed File zurückzuschicken")
    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)

    #if input_wave:
    #    #TODO: Do something with the input audio
    #    print("Wir haben ein input File")
    #    with open(os.path.join("cachedir", "tmpfile.wav"), "wb") as f:
    #        f.write(base64.b64decode(input_wave))
    #result_wave = model(model_id=model_id, library_dir=library_dir)
    #result_wave = None
    with open(outfile, "rb") as f:
        result_wave = f.read()
    #print("lokale tests können starten ;)")
    #postprocessor = Postprocessor(result_wave)
    #outfile = postprocessor.applyEffects()
    return result_wave

def play_sound_original(selectedPoint: str = 'point',username: str = "Ian", **kwargs):
    print("---Neuer Code :SampleVAE Model hat gerade folgendes Instrument")
    Samplevae_model = getSampleVAE(username=username)
    print(Samplevae_model.get_instrument())
    dir = dict_library_dir[Samplevae_model.get_instrument()] + "/Data/"
    print(dir)
    if selectedPoint[-4:] == '_0.0':
        selectedPoint = selectedPoint[:-4] + ".wav"


    file_dir = os.path.join(dir, selectedPoint)
    cwd = os.getcwd()
    file = os.path.join(cwd, file_dir)

    result_wave = None
    with open(file, "rb") as f:
        result_wave = f.read()

    return result_wave

def applyEffectsOnGeneratedFile(isReversed, lowpass_value, highpass_value, distortion_value,reverb_value,volume_value,username: str = "Ian"):
    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)

    result_wave = None
    with open(file, "rb") as f:
        result_wave = f.read()
    fx = (
        AudioEffectsChain()
    )

    print("Librosa Sagt die Samplerate ist")
    sampleRate = librosa.get_samplerate(file)
    print(librosa.get_samplerate(file))

    #1. add Reverse
    #print(isReversed)
    if isReversed:
        fx.reverse()

    #2. add Lowpass
    #we dump with 0
    if lowpass_value > 0:
        value = (lowpass_value/100) * (sampleRate / 2)
        #print("New Value for Lowpass isch:")
        #print(value)
        #People Hear 20.000
        fx.lowpass(frequency=value)
    else:
        fx.lowpass(frequency=50)

    #3. add Highpass
    if highpass_value> 0:
        #print(highpass_value)
        value = (highpass_value / 150) * (sampleRate / 2)
        #print("New Value for Highpass isch:")
        #print(value)
        fx.highpass(frequency=value)
    else:
        fx.highpass(frequency=1)

    #4. Overdrive 0-50
    #print(distortion_value)
    value = math.floor(distortion_value / 2)
    #print("New Value for Distortion:")
    #print(value)
    fx.overdrive(distortion_value)
    value2 = value/50 * -15
    fx.gain(value2)

    #6. Reverb
    print(reverb_value)
    if reverb_value > 0:
        value = math.floor(reverb_value/2)
        print("My Reverb Value")
        print(value)
        fx.reverb(reverberance=value, room_scale=value, hf_damping=value)
        fx.delay()
    else:
        print ("No Reverb")

    #7. Volume
    #print(volume_value)
    value = -30 + (volume_value/100*30)
    fx.gain(value)

    #fx.reverb()
    #fx.delay()

    fx(file, outfile)

    #song = AudioSegment.from_wav("processed.wav")
    #play(song)

    return outfile

def preload_similarity(username):
    Samplevae_model = getSampleVAE(username=username)
    model_instrument = "Similarity Search"
    if Samplevae_model.get_instrument() == model_instrument:
        print("Model wieder nutzen")
    else:
        Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
                                         instrument=model_instrument,
                                         library_dir=dict_library_dir[model_instrument])
        assignSampleVAE(username=username, SampleVAE=Samplevae_model)
    return "success"

def get_tsne_and_preload_model(model_instrument, username):
    Samplevae_model = getSampleVAE(username=username)
    outfile = "fennekservice/Ian-generated.wav"
    #print(Samplevae_model.find_similar(target_file=outfile))
    if Samplevae_model.get_instrument() == model_instrument:
        print("Model wieder nutzen")
        #result_wave = Samplevae_model.forward()
    else:
        print("Model NICHT wieder nutzen")
        print(Samplevae_model.get_instrument())
        print(model_instrument)
        # result_wave = Samplevae_model(model_id="model_snare2", library_dir=library_dir,selectedSound = selectedPoint, ae_variance=ae_variance)
        Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
                                         instrument=model_instrument,
                                         library_dir=dict_library_dir[model_instrument])
        assignSampleVAE(username=username, SampleVAE=Samplevae_model)

    response = {"name": model_instrument}
    data = Samplevae_model.get_TSNE()
    for x in data:
        x['x'] = float(x['x'])
        x['y'] = float(x['y'])

    response["data"] = data

    return response

def upload_file(data: str = "", username: str = "Ian", **kwargs):
    usr_file = "fennekservice/" + username + "-upload.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)

    #data = open(data, "r").read()
    #result_wave = base64.b64decode(data)

    result_wave = base64.b64decode(data)
    with open(file, "wb") as fout:
        fout.write(result_wave)

    #print(data)
    #print(username)

    return "success"

def decode_and_save_file(data: str = "", username: str = "Ian", **kwargs):
    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"

    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)

    result_wave = base64.b64decode(data)
    with open(file, "wb") as fout:
        fout.write(result_wave)

    with open(outfile, "wb") as fout:
        fout.write(result_wave)

    #print(data)
    #print(username)

    return "success"

def get_generation_file(username: str = "Ian", **kwargs):
    usr_file = "fennekservice/" + username + "-generated.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)

    result_wave = None
    with open(file, "rb") as f:
        result_wave = f.read()

    return result_wave

def write_similar_files_to_txt(username: str = "Ian", text = None , **kwargs):
    outfile = open("data.txt", "w")
    usr_file = "fennekservice/" + username + "-data.txt"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)

    with open(file, "w") as f:
        result_wave = f.write(text)