from pydub import AudioSegment
import re
import string


class Converter:

	"""
	This is a simple converter made using pydub module
	and ffmpeg.
	The wav_mp3_convert module is the engine for the
	app module or the front end of the software.
	Note that it only converts mp3 and wav files.
	"""

	def __init__(self, directory, filename):
		self.directory = directory
		self.filename = filename


	def fixDir(self):
		output = ''
		for char in self.directory:
			if char == "\\":
				output += "/"
			else:
				output += char
		if output[-1] != "/":
			output += "/"
		return output


	def _name(self):
		def symbols():
			output = ''
			punctuations = string.punctuation
			for punc in punctuations:
				if punc == ".":
					pass
				else:
					output += f'\\{punc}'
			return output

		def filePattern():
			punctuations = symbols()
			if ".mp3" in self.filename:
				return re.compile(r'[\w\d\s{0}]+[.mp3]'.format(punctuations))
			elif ".wav" in self.filename:
				return re.compile(r'[\w\d\s{0}]+[.wav]'.format(punctuations))

		def extChange():
			output = ''
			pattern = filePattern()
			group = pattern.findall(self.filename)
			for x in group:
				if x == "mp3":
					output += 'wav'
				elif x == "wav":
					output += 'mp3'
				else:
					output += x
			return output
		return extChange()


	def wav_to_mp3(self):
		file = AudioSegment.from_wav(self.fixDir() + self.filename)
		with open(self._name(), "wb") as src:
			src = file.export(self._name(), format="mp3")


	def mp3_to_wav(self):
		file = AudioSegment.from_mp3(self.fixDir() + self.filename)
		with open(self._name(), "wb") as src:
			src = file.export(self._name(), format="wav")
