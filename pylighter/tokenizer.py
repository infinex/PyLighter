import spacy


class SpacyTokenizer(object):
    def __init__(self, lang='en_core_web_sm'):
        self.nlp = spacy.load(lang, disable=['parser', 'tagger', 'entity','lemmatizer'])

    def word_tokenizer(self, doc, return_token_span_lookup=True):
        doc = self.nlp(doc)
        tokens = [token.text for token in doc]
        token_spans = [(token.idx, token.idx + len(token.text)) for token in doc]
        if return_token_span_lookup:
            token_spans = self.token_span_lookup(token_spans)
        return tokens, token_spans

    def token_span_lookup(self, token_spans):
        token_span_lookup_dict = {}
        for span in token_spans:
            for char_idx in range(*span):
                token_span_lookup_dict[char_idx] = span
        return token_span_lookup_dict


if __name__ == '__main__':
    tk = SpacyTokenizer()
    tokens, token_spans = tk.word_tokenizer('I love to sleep')
    print(token_spans)
