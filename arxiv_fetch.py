
import os

from llama_index import download_loader
# from llama_hub.file.unstructured import UnstructuredReader
from llama_index import SimpleDirectoryReader
from llama_index import download_loader
from pathlib import Path


#  1 get all the arxiv urls for the CS ML and AI categories
#  2 download the pdfs
#  3 extract the text from the pdfs

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()
documents = loader.load_data(urls=['https://www.arxiv-vanity.com/papers/2106.09685/'])

ReadabilityWebPageReader = download_loader("ReadabilityWebPageReader")

# or set proxy server for playwright: loader = ReadabilityWebPageReader(proxy="http://your-proxy-server:port")
# For some specific web pages, you may need to set "wait_until" to "networkidle". loader = ReadabilityWebPageReader(wait_until="networkidle")
loader = ReadabilityWebPageReader()
# documents = loader.load_data(url='https://arxiv.org/pdf/2106.09685.pdf')


UnstructuredReader = download_loader('UnstructuredReader')
# documents = UnstructuredReader.load_data(file=Path('./data/a.pdf'))

dir_reader = SimpleDirectoryReader('./data', file_extractor={
  ".pdf": UnstructuredReader(),
  ".html": UnstructuredReader(),
  ".eml": UnstructuredReader(),
})
documents = dir_reader.load_data()
print(documents[0].text)    


