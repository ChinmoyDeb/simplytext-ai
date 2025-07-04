MAX_TEXT_LENGTH = 7000

def split_into_chunks(text, chunk_size=3500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
