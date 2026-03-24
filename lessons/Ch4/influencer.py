class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links
        self.vanity = num_selfies + num_bio_links * 5

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"
    
    def get_vanity(self) -> int:
        return self.num_selfies + self.num_bio_links * 5