import wave
import io
import sys
sys.path.append('..')
from util import *


def main():


	if len(sys.argv) != 2:
		raise ValueError('Missing argument: Audio File')
	 
	imf = sys.argv[1]
	 
	print(f'Reading {imf} ...')

	message = 	readTXT("secret_file_in.txt")
	#message  = 	readIMG('pic.png')

	message = message + "!)NF@^&I^U%$&T&#@&"

	message_bits = tobits(message) 
	MESSAGE_LENGTH = len(message_bits)


	obj = wave.open(imf,'rb')
	

	nchannels, sampwidth, framerate, nframes, comptype, compname = obj.getparams()
	
	frames = bytearray(obj.readframes(nframes))

	#if (MESSAGE_LENGTH > len(frames)): 
		#raise ValueError('Message does not fit! \n')

	out = wave.open(imf[:-4]+'-2.wav','wb')
	out.setparams(obj.getparams())
	out.setnframes(nframes)

	for i in range(MESSAGE_LENGTH):
		frames[i] = addint(int(frames[i]),message_bits[i])

	out.writeframes(frames)

	obj.close()
	out.close()
	print("Done!")


if __name__ == '__main__':
    main()
