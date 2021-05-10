import subprocess, os, argparse, json, time, binascii, base64, requests, sys, ffmpy
import re
from pywidevine.decrypt.wvdecrypt import WvDecrypt

parser = argparse.ArgumentParser()
parser.add_argument("-mpd", "--video-link", dest="mpd", help="CENC MPD", required=True)
parser.add_argument("-o", '--output', dest="output", help="Specify output file name with no extension", required=True)
#parser.add_argument("-lic", dest="license", help="Specify license url", required=True)
parser.add_argument("-keys", dest="keys", action="store_true", help="show keys and exit")
args = parser.parse_args()

currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)
youtubedlexe = r'python yt-dlp'
ffmpegpath = r'ffmpeg'
aria2cexe = r'aria2c'
mp4decryptexe = r'mp4decrypt'
mkvmergeexe = r'mkvmerge'
mp4dump = r'mp4dump'

FInput_video = dirPath + '/vid_enc.mp4'
FInput_audio = dirPath + '/aud_enc.m4a'
out_Audio = FInput_audio.replace('enc', 'dec')
out_Video = FInput_video.replace('enc', 'dec')
Remuxed_Video = out_Video.replace('mp4', 'H264')
Demuxed_Audio = out_Audio.replace('m4a', 'aac')

MPD = str(args.mpd)



subprocess.run([youtubedlexe, '-k', '--user-agent', 'KAIOS/2.0', '-F', MPD])
time.sleep(1)

Content = input('\nIF YOU WANT ONLY AUD PRESS 1 ELSE PRESS ANY KEY TO CONTINUE :')
if '1' in Content:
    aud_format = input('\nEnter Audio Format Which You Want ? :')
    if not os.path.exists(FInput_audio) and not os.path.exists(out_Audio):
        subprocess.run([youtubedlexe, '-k', '--user-agent', 'Hotstar;in.startv.hotstar/8.7.5 (Linux;Android 6.0.1) ExoPlayerLib/2.9.5', '-f', aud_format, '--fixup', 'never', MPD, '-o', 'aud_enc.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    else:
        pass
else:    
    aud_format = input('\nEnter Audio Format Which You Want ? :')
    vid_format = input('\nEnter Video Format :')
    try:
    
        if not os.path.exists(FInput_audio) and not os.path.exists(out_Audio):
           subprocess.run([youtubedlexe, '-k', '--user-agent', 'Hotstar;in.startv.hotstar/8.7.5 (Linux;Android 6.0.1) ExoPlayerLib/2.9.5', '-f', aud_format, '--fixup', 'never', MPD, '-o', 'aud_enc.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
        else:
            pass
    except Exception:
        pass

    if not os.path.exists(FInput_video) and not os.path.exists(out_Video):
        subprocess.run([youtubedlexe, '-k', '--user-agent', 'Hotstar;in.startv.hotstar/8.7.5 (Linux;Android 6.0.1) ExoPlayerLib/2.9.5', '-f', vid_format, '--fixup', 'never', MPD, '-o', 'vid_enc.mp4', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    else:
        pass

print('\nEnter Decryption Section...')

KID = ''
pssh = None
def find_str(s, char):
        index = 0
        if char in s:
            c = char[0]
            for ch in s:
                if ch == c and s[index:index + len(char)] == char:
                    return index
                index += 1

        return -1

mp4dump = subprocess.Popen([mp4dump, FInput_audio], stdout=subprocess.PIPE)
mp4dump = str(mp4dump.stdout.read())
A = find_str(mp4dump, 'default_KID')
KID = mp4dump[A:A + 63].replace('default_KID = ', '').replace('[', '').replace(']', '').replace(' ', '')
KID = KID.upper()
KID_video = KID[0:8] + '-' + KID[8:12] + '-' + KID[12:16] + '-' + KID[16:20] + '-' + KID[20:32]
#print('KID:{}'.format(KID_video))
if KID == '':
	KID = 'nothing'

def Get_PSSH(mp4_file):
    currentFile = __file__
    realPath = os.path.realpath(currentFile)
    dirPath = os.path.dirname(realPath)
    dirName = os.path.basename(dirPath)
    mp4dump = dirPath + "mp4dump"
    WV_SYSTEM_ID = '[ed ef 8b a9 79 d6 4a ce a3 c8 27 dc d5 1d 21 ed]'
    pssh = None
    data = subprocess.check_output([mp4dump, '--format', 'json', '--verbosity', '1', mp4_file])
    data = json.loads(data)
    for atom in data:
        if atom['name'] == 'moov':
            for child in atom['children']:
                if child['name'] == 'pssh' and child['system_id'] == WV_SYSTEM_ID:
                    pssh = child['data'][1:-1].replace(' ', '')
                    pssh = binascii.unhexlify(pssh)
                    #if pssh.startswith('\x08\x01'):
                    #   pssh = pssh[0:]
                    pssh = pssh[0:]
                    pssh = base64.b64encode(pssh).decode('utf-8')
                    return pssh
                    
pssh_mpd = Get_PSSH(FInput_audio)
pssh = pssh_mpd

license_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36' 
}

##that just need to be changed with the sunn one and put cookies in folder I will creat ## 
licurl = input("Enter Licence Data : ")
licurl = str(licurl)

def do_decrypt(pssh, licurl):
    wvdecrypt = WvDecrypt(pssh)
    chal = wvdecrypt.get_challenge()
    resp = requests.post(url=licurl, data=chal, headers=license_headers)
    license_decoded = resp.content
    license_b64 = base64.b64encode(license_decoded)
    wvdecrypt.update_license(license_b64)
    keys = wvdecrypt.start_process()

    return keys

def keysOnly(keys):
    for key in keys:
        if key.type == 'CONTENT':
            key = ('{}:{}'.format(key.kid.hex(), key.key.hex()))

    return key

print('\nGetting Keys...')
KEYS = do_decrypt(licurl=licurl, pssh=pssh)

if args.keys:
	print(keysOnly(KEYS))
	sys.exit(0)

def proper(keys):
    commandline = [mp4decryptexe]
    for key in keys:
        if key.type == 'CONTENT':
            commandline.append('--key')
            commandline.append('{}:{}'.format(key.kid.hex(), key.key.hex()))

    return commandline

def decrypt(keys_, inputt, output):
    Commmand = proper(keys_)
    Commmand.append(inputt)
    Commmand.append(output)

    wvdecrypt_process = subprocess.Popen(Commmand)
    stdoutdata, stderrdata = wvdecrypt_process.communicate()
    wvdecrypt_process.wait()

    return

def keysOnly(keys):
    for key in keys:
        if key.type == 'CONTENT':
            key = ('{}:{}'.format(key.kid.hex(), key.key.hex()))

    return key

try:
    if not os.path.exists(out_Video):
        print("\nDecrypting Video...")
        print ("Using KEY: " + keysOnly(KEYS))
        command = decrypt(KEYS, FInput_video, out_Video)
        print('Done!')
except Exception:
    pass

if not os.path.exists(out_Audio):
    print("\nDecrypting Audio...")
    print ("Using KEY: " + keysOnly(KEYS))
    command = decrypt(KEYS, FInput_audio, out_Audio)
    print('Done!')



if os.path.exists(out_Audio) and not os.path.exists(Demuxed_Audio):
    print("\nDemuxing audio...")
    ff = ffmpy.FFmpeg(executable=ffmpegpath, inputs={out_Audio: None}, outputs={Demuxed_Audio: '-c copy -metadata:s:a:0 language=tel -metadata:s:a:0 title="TheDNK" '}, global_options="-y -hide_banner -loglevel warning")
    ff.run()
    time.sleep (50.0/1000.0)
    print('Done!')

try:
    print('\nMuxing Video and Audio...')
    output=str(args.output)
    mkvmerge_command = [mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', out_Video, '--language', '0:eng', '--default-track', '0:yes', '--compression' ,'0:none', Demuxed_Audio,'--language', '0:tel','--track-order', '0:0,1:0,2:0,3:0,4:0']
    subprocess.run(mkvmerge_command)
except Exception:
    pass
    
if '1' in Content:
    print('Cleaning Directory...')
    os.remove(FInput_audio)
    os.remove(out_Audio)
    print('Done!!')
else:    
    print('Cleaning Directory...')
    if os.path.exists(output+'.mkv'):
        os.remove(out_Audio)
        os.remove(out_Video)
        os.remove(Demuxed_Audio)     
        os.remove(FInput_audio)
        os.remove(FInput_video)
        print('Done!')
    else:
        pass
