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

	obj = wave.open(imf,'rb')
	nframes = obj.getnframes()
	frames = bytearray(obj.readframes(nframes))


	bitlist = []

	for i in range(len(frames)):
		bitlist.append(getLSB(int(frames[i])))

		if(len(bitlist) > 144 ):

			if (frombits(bitlist[-144:]) == "!)NF@^&I^U%$&T&#@&" ): break


	print ("Done!")

	data = frombits(bitlist[:-144])
	toTXT(data)


if __name__ == '__main__':
    main()



