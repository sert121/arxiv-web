
from llama_index import SummaryIndex, SimpleWebPageReader
from IPython.display import Markdown, display
import os


documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://www.arxiv-vanity.com/papers/2106.09685/"]
)

print(documents.text)

