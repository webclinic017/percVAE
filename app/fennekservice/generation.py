import os, random
import base64
import wave
import gin
from pydub import AudioSegment
from pydub.playback import play
from pysndfx import AudioEffectsChain
import librosa
import math

from fennekservice.postprocessing import Postprocessor
from fennekservice.models.samplevae.samplevae import SampleVAEModel

Samplevae_model = SampleVAEModel()

@gin.configurable
def generate_sound(input_wave, model_id: str = 'my_model',  model_instrument: str = 'my_instrument', library_dir: str = 'mylibdir', username: str = "Ian", **kwargs):

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    usr_file = "fennekservice/" + username + "-generated.wav"
    usr_outfile = "fennekservice/" + username + "-processed.wav"
    cwd = os.getcwd()
    file = os.path.join(cwd, usr_file)
    outfile = os.path.join(cwd, usr_outfile)
    result_wave = None

    print("welches Modell wurde Gewählt?")
    print(model_id)
    print(model_instrument)

    #if input_wave:
    #    #TODO: Do something with the input audio
    #    print("Wir haben ein input File")
    #    with open(os.path.join("cachedir", "tmpfile.wav"), "wb") as f:
    #        f.write(base64.b64decode(input_wave))

    if model_id == "GAN":
        dir_model_id = "fennekservice/models/" + model_id
        model_id_directory = os.path.join(cwd,dir_model_id)
        model_instrument_directory = os.path.join(model_id_directory,model_instrument)
        result_wave = random.choice(os.listdir(model_instrument_directory))
        file_dir = os.path.join(model_instrument_directory, result_wave)

        with open(file_dir, "rb") as f:
            result_wave = f.read()

        with open(file, "wb") as fout:
            fout.write(result_wave)


    if model_id == "Variational Autoencoder":
        print("SampleVAE!")
    #result_wave = Samplevae_model(model_id=model_id, library_dir=library_dir)
        result_wave = Samplevae_model(model_id="model_snare2", library_dir=library_dir)

        with open(file, "wb") as fout:
            fout.write(result_wave)

    fx = (
        AudioEffectsChain()
    )
    fx(file, outfile)

    return result_wave

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


def tsne_experiment(model_id):
    outfile = "fennekservice/Ian-generated.wav"
    #print(Samplevae_model.find_similar(target_file=outfile))
    response = {"name": model_id}
    data = Samplevae_model.get_TSNE()
    for x in data:
        x['x'] = float(x['x'])
        x['y'] = float(x['y'])

    response["data"] = data

    return response


