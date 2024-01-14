import zlib

def compress_data(data):
   return zlib.compress(data)

def decompress_data(compressed_data):
   return zlib.decompress(compressed_data)

