class Codec:
    def __init__(self):
        self.count = 0
        self.char_set = [str(i) for i in xrange(10)] + [chr(i) for i in xrange(ord('a'), ord('z')+1)] + [chr(i) for i in xrange(ord('A'), ord('Z')+1)]
        self.char_map = {self.char_set[i]: i for i in xrange(len(self.char_set))}
        self.url_map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.url_map[self.count] = longUrl
        return self.convert_num_to_char()

    def convert_num_to_char(self):
        rst = ""
        curr = self.count
        while curr > 0:
            rst = self.char_set[curr % 65] + rst
            curr /= 65
        
        size = len(rst)
        while size < 6:
            rst = "0" + rst
            size += 1
        return rst
    
    def convert_char_to_num(self, shorturl):
        rst = 0
        for i in range(0, len(shorturl)):
            if shorturl[i] not in self.char_map:
                return -1
            rst = rst * 62 + self.char_map[shorturl[i]]
        return rst

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        num = self.convert_char_to_num(shortUrl)
        if num not in self.url_map:
            return "invalid"
        return self.url_map[num]

c = Codec()
print c.char_map["0"]
short_url = c.encode("https://leetcode.com/problems/design-tinyurl")
print c.decode(short_url)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))