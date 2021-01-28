class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f'{self.name} - {self.length}'


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list ( songs )
        self.published = False

    def add_song(self, song: Song):
        if song.single == True:
            return f"Cannot add {song.name}. It's a single"
        if self.published == True:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append ( song )
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_names = [s.name for s in self.songs]
        if song_name not in song_names:
            return f"Song is not in the album."
        if self.published == True:
            return f"Cannot remove songs. Album is published."
        del self.songs[song_name.index(song_name)]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        res = f"Album {self.name}"+"\n"
        for song in self.songs:
            res +=f"== {song.get_info () }"+"\n"
        return res


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [album.name for album in self.albums]:
            return f"Album {album_name} is not found."
        album = [a for a in self.albums if a.name ==album_name][0]
        if  album.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        res = f"Band {self.name}" + "\n"
        for album in self.albums:
            res += f"{album.details ()}" + "\n"
        return res
