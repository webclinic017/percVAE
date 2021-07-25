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
import logging
import threading

from fennekservice.postprocessing import Postprocessor
from fennekservice.models.samplevae.samplevae import SampleVAEModel

Samplevae_model1 = None
Samplevae_model2 = None
Samplevae_model3 = None
Samplevae_model4 = None

Samplevae_model_kick = None
Samplevae_model_snare = None
#Samplevae_model_conga = None
#Samplevae_model_cowbell = None
Samplevae_model_crash = None
#Samplevae_model_ride = None
#Samplevae_model_rimshot = None
Samplevae_model_toms = None
Samplevae_model_clap = None
Samplevae_model_hihat = None
Samplevae_model_all2 = None


def getSampleVAE(username):
    if username == "Amy":
        print(username)
        global Samplevae_model1
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


def getSampleVAEforInstrument(model_instrument):
    if model_instrument == "Kick":
        return Samplevae_model_kick
    if model_instrument == "Snare":
        return Samplevae_model_snare
    #if model_instrument == "Conga":
    #    return Samplevae_model_conga
    #if model_instrument == "Cowbell":
    #    return Samplevae_model_cowbell
    if model_instrument == "Crash":
        return Samplevae_model_crash
    #if model_instrument == "Ride":
    #    return Samplevae_model_ride
    #if model_instrument == "Rimshot":
    #    return Samplevae_model_rimshot
    if model_instrument == "Toms":
        return Samplevae_model_toms
    if model_instrument == "Clap":
        return Samplevae_model_clap
    if model_instrument == "Hihat":
        return Samplevae_model_hihat
    if model_instrument == "Similarity Search":
        return Samplevae_model_all2


def initializeModels(model_instrument):
    logging.info(f'Thread: {model_instrument} id = {threading.get_ident()}')
    logging.info(f'Thread: {model_instrument} name = {threading.currentThread().name}')
    global Samplevae_model_kick
    global Samplevae_model_snare
    global Samplevae_model_crash
    global Samplevae_model_toms
    global Samplevae_model_clap
    global Samplevae_model_hihat
    global Samplevae_model_all2
    if model_instrument == "Kick" and Samplevae_model_kick is None:
        Samplevae_model_kick = SampleVAEModel(model_id=dict_models["Kick"], instrument="Kick",
                                              library_dir=dict_library_dir["Kick"])
    if model_instrument == "Snare" and Samplevae_model_snare is None:
        Samplevae_model_snare = SampleVAEModel(model_id=dict_models["Snare"], instrument="Snare",
                                               library_dir=dict_library_dir["Snare"])
    #if model_instrument == "Conga":
        #Samplevae_model_conga = SampleVAEModel(model_id=dict_models["Conga"], instrument="Conga",
        #                                       library_dir=dict_library_dir["Conga"])
    #if model_instrument == "Cowbell":
        #Samplevae_model_cowbell = SampleVAEModel(model_id=dict_models["Cowbell"], instrument="Cowbell",
        #                                         library_dir=dict_library_dir["Cowbell"])
    if model_instrument == "Crash" and Samplevae_model_crash is None:
        Samplevae_model_crash = SampleVAEModel(model_id=dict_models["Crash"], instrument="Crash",
                                               library_dir=dict_library_dir["Crash"])
    #if model_instrument == "Ride":
        #Samplevae_model_ride = SampleVAEModel(model_id=dict_models["Ride"], instrument="Ride",
        #                                      library_dir=dict_library_dir["Ride"])
    #if model_instrument == "Rimshot":
        #Samplevae_model_rimshot = SampleVAEModel(model_id=dict_models["Rimshot"], instrument="Rimshot",
        #                                         library_dir=dict_library_dir["Rimshot"])
    if model_instrument == "Toms" and Samplevae_model_toms is None:
        Samplevae_model_toms = SampleVAEModel(model_id=dict_models["Toms"], instrument="Toms",
                                              library_dir=dict_library_dir["Toms"])
    if model_instrument == "Clap" and Samplevae_model_clap is None:
        Samplevae_model_clap = SampleVAEModel(model_id=dict_models["Clap"], instrument="Clap",
                                              library_dir=dict_library_dir["Clap"])
    if model_instrument == "Hihat" and Samplevae_model_hihat is None:
        Samplevae_model_hihat = SampleVAEModel(model_id=dict_models["Hihat"], instrument="Hihat",
                                               library_dir=dict_library_dir["Hihat"])
    if model_instrument == "Similarity Search" and Samplevae_model_all2 is None:
        Samplevae_model_all2 = SampleVAEModel(model_id=dict_models["Similarity Search"], instrument="Similarity Search",
                                              library_dir=dict_library_dir["Similarity Search"])
    logging.info(f'Thread {model_instrument}: finished')


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
def generate_sound(model_id: str = 'my_model', model_instrument: str = 'my_instrument',
                   ae_variance: float = 0.0, selectedPoint: str = '', username: str = "Ian", **kwargs):
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

    # print("Selected Point")
    # print(selectedPoint)
    # print("AE_Variance")
    # print(ae_variance)
    # if input_wave:
    #    #TODO: Do something with the input audio
    #    print("Wir haben ein input File")
    #    with open(os.path.join("cachedir", "tmpfile.wav"), "wb") as f:
    #        f.write(base64.b64decode(input_wave))

    # if model_id == "GAN":
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
        Samplevae_model = getSampleVAEforInstrument(model_instrument)
        #if Samplevae_model == None:
            #Samplevae_model = SampleVAEModel()
            #assignSampleVAE(username=username, SampleVAE=Samplevae_model)
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
            # result_wave = Samplevae_model(model_id="model_snare2", library_dir=library_dir,selectedSound = selectedPoint, ae_variance=ae_variance)
            #Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
            #                                 instrument=model_instrument,
            #                                 library_dir=dict_library_dir[model_instrument])
            #result_wave = Samplevae_model.forward(selectedSound=selectedPoint, ae_variance=ae_variance)
            #assignSampleVAE(username=username, SampleVAE=Samplevae_model)

        with open(file, "wb") as fout:
            fout.write(result_wave)

    if model_id == "Similarity Search":
        print("Similarity Search!")
        model_instrument = "Similarity Search"
        Samplevae_model = getSampleVAEforInstrument(model_instrument)
        #if Samplevae_model == None:
        #    Samplevae_model = SampleVAEModel()
            #assignSampleVAE(username=username, SampleVAE=Samplevae_model)

        #if Samplevae_model.get_instrument() == model_instrument:
        #    print("Model wieder nutzen")
        #else:
        #    Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
        #                                     instrument=model_instrument,
        #                                     library_dir=dict_library_dir[model_instrument])
            #assignSampleVAE(username=username, SampleVAE=Samplevae_model)
        similarSounds = Samplevae_model.find_similar(target_file=usr_upload_file)
        # write_similar_files_to_txt(username=username, text=similarSounds)
        result_wave = Samplevae_model.forward(selectedSound=similarSounds[0])

        path = similarSounds[0]
        dirofdir = os.path.dirname(os.path.dirname(path))
        dirname1 = os.path.basename(dirofdir)
        print(dirname1)

        for key, value in dict_models.items():
            if value == dirname1:
                print(key)
                model_instrument = key

        # with open(similarSounds[0], "rb") as f:
        #    result_wave = f.read()
        with open(file, "wb") as fout:
            fout.write(result_wave)

    fx = (
        AudioEffectsChain()
    )
    fx(file, outfile)

    gc.collect()
    return result_wave, model_instrument


def play_sound(username: str = "Ian", **kwargs):
    # print("Zeit das Processed File zurückzuschicken")
    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)

    # if input_wave:
    #    #TODO: Do something with the input audio
    #    print("Wir haben ein input File")
    #    with open(os.path.join("cachedir", "tmpfile.wav"), "wb") as f:
    #        f.write(base64.b64decode(input_wave))
    # result_wave = model(model_id=model_id, library_dir=library_dir)
    # result_wave = None
    with open(outfile, "rb") as f:
        result_wave = f.read()
    # print("lokale tests können starten ;)")
    # postprocessor = Postprocessor(result_wave)
    # outfile = postprocessor.applyEffects()
    return result_wave


def play_sound_original(selectedPoint: str = 'point', username: str = "Ian", model_instrument: str = "Kick", **kwargs):
    print("---Neuer Code :SampleVAE Model hat gerade folgendes Instrument")
    Samplevae_model = getSampleVAEforInstrument(model_instrument)
    #if Samplevae_model == None:
        #Samplevae_model = SampleVAEModel()
        #assignSampleVAE(username=username, SampleVAE=Samplevae_model)
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


def applyEffectsOnGeneratedFile(isReversed, lowpass_value, highpass_value, distortion_value, reverb_value, volume_value,
                                username: str = "Ian"):
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

    # 1. add Reverse
    # print(isReversed)
    if isReversed:
        fx.reverse()

    # 2. add Lowpass
    # we dump with 0
    if lowpass_value > 0:
        value = (lowpass_value / 100) * (sampleRate / 2)
        # print("New Value for Lowpass isch:")
        # print(value)
        # People Hear 20.000
        fx.lowpass(frequency=value)
    else:
        fx.lowpass(frequency=50)

    # 3. add Highpass
    if highpass_value > 0:
        # print(highpass_value)
        value = (highpass_value / 150) * (sampleRate / 2)
        # print("New Value for Highpass isch:")
        # print(value)
        fx.highpass(frequency=value)
    else:
        fx.highpass(frequency=1)

    # 4. Overdrive 0-50
    # print(distortion_value)
    value = math.floor(distortion_value / 2)
    # print("New Value for Distortion:")
    # print(value)
    fx.overdrive(distortion_value)
    value2 = value / 50 * -15
    fx.gain(value2)

    # 6. Reverb
    print(reverb_value)
    if reverb_value > 0:
        value = math.floor(reverb_value / 2)
        print("My Reverb Value")
        print(value)
        fx.reverb(reverberance=value, room_scale=value, hf_damping=value)
        fx.delay()
    else:
        print("No Reverb")

    # 7. Volume
    # print(volume_value)
    value = -30 + (volume_value / 100 * 30)
    fx.gain(value)

    # fx.reverb()
    # fx.delay()

    fx(file, outfile)

    # song = AudioSegment.from_wav("processed.wav")
    # play(song)

    return outfile


def preload_similarity(username):
    Samplevae_model = getSampleVAEforInstrument("Similarity Search")
    #if Samplevae_model == None:
    #    Samplevae_model = SampleVAEModel()
    model_instrument = "Similarity Search"
    if Samplevae_model.get_instrument() == model_instrument:
        print("Model wieder nutzen")
    # else:
    # Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
    #                                 instrument=model_instrument,
    #                                 library_dir=dict_library_dir[model_instrument])
    # assignSampleVAE(username=username, SampleVAE=Samplevae_model)
    return "success"


def get_tsne_and_preload_model(model_instrument, username):
    Samplevae_model = getSampleVAEforInstrument(model_instrument)
    if Samplevae_model == None:
        print("-----------------------SHIT--------------------")
        print(model_instrument)
        #Samplevae_model = SampleVAEModel()
        #assignSampleVAE(username=username, SampleVAE=Samplevae_model)
    outfile = "fennekservice/Ian-generated.wav"
    # print(Samplevae_model.find_similar(target_file=outfile))
    if Samplevae_model.get_instrument() == model_instrument:
        print("Model wieder nutzen")
        # result_wave = Samplevae_model.forward()
    else:
        print("Model NICHT wieder nutzen")
        print(Samplevae_model.get_instrument())
        print(model_instrument)
        # result_wave = Samplevae_model(model_id="model_snare2", library_dir=library_dir,selectedSound = selectedPoint, ae_variance=ae_variance)
        #Samplevae_model = SampleVAEModel(model_id=dict_models[model_instrument],
        #                                 instrument=model_instrument,
        #                                 library_dir=dict_library_dir[model_instrument])
        #assignSampleVAE(username=username, SampleVAE=Samplevae_model)

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

    # data = open(data, "r").read()
    # result_wave = base64.b64decode(data)

    result_wave = base64.b64decode(data)
    with open(file, "wb") as fout:
        fout.write(result_wave)

    # print(data)
    # print(username)

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

    # print(data)
    # print(username)

    return "success"


def get_generation_file(username: str = "Ian", **kwargs):
    usr_file = "fennekservice/" + username + "-generated.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)

    result_wave = None
    with open(file, "rb") as f:
        result_wave = f.read()

    return result_wave


def write_similar_files_to_txt(username: str = "Ian", text=None, **kwargs):
    outfile = open("data.txt", "w")
    usr_file = "fennekservice/" + username + "-data.txt"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)

    with open(file, "w") as f:
        result_wave = f.write(text)
