from tiktoken import Tokenizer as TiktokenTokenizer
from tiktoken.models import TokenList
import xml.etree.ElementTree as ET


def chunk_text(text, start_token='<entry>', end_token='</entry>'):
    chunks = []
    current_chunk = ''

    # Add a space before the start_token and end_token to ensure they are treated as separate tokens
    text = text.replace(start_token, ' ' + start_token)
    text = text.replace(end_token, end_token + ' ')

    tokenizer = TiktokenTokenizer()
    tokens = tokenizer.tokenize(text)

    for token_str, _ in tokens:
        if token_str == start_token:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = start_token
        elif token_str == end_token:
            current_chunk += ' ' + token_str
            chunks.append(current_chunk)
            current_chunk = ''
        else:
            current_chunk += ' ' + token_str

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


# Load and parse the XML file
tree = ET.parse('produkty.xml')
root = tree.getroot()

# Convert the XML data to a text string
text = ET.tostring(root, encoding='utf8').decode('utf8')

# Chunk the text
chunks = chunk_text(text)

for chunk in chunks:
    print(chunk)
    print('------')
