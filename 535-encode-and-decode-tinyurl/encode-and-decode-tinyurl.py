class Codec:
    def __init__(self):
        self.url_to_code={}
        self.code_to_url={}
        self.counter=0
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_code:
            self.counter+=1
            code=str(self.counter)
            self.url_to_code[longUrl]=code
            self.code_to_url[code]=longUrl
        code=self.url_to_code[longUrl]
        return "http: //tinyurl.com/"+code
    def decode(self, shortUrl: str) -> str:
        code=shortUrl.rsplit("/", 1)[-1]
        return self.code_to_url[code]