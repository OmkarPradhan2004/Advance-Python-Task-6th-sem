#Playlist
#Add_Songs
#Remove_Songs
#Show_Songs
class Music:
    def __init__(self):
        self.playlist=[]

    def add_songs(self,name):
        self.playlist.append(name)
    
    def remove_Songs(self,name):
        if name in self.playlist:
            self.playlist.remove(name)
    
    def show_songs(self):
        for s in self.playlist:
            print(s)

def main():
    playlist = Music()
    while True:
        print("\n1.Add Song\n 2.Remove Song\n 3.Show Songs\n 4.Exit")
        c=int(input("Enter Choice:"))
        
        if c==1:
            n=input("Enter Song Name:")
            playlist.add_songs(n)

        elif c==2:
            n=input("Enter Song Name:")
            playlist.remove_Songs(n)

        elif c==3:
            playlist.show_songs()

        elif c==4:
            break

        else:
            print("invalid choice!")
            break

main()