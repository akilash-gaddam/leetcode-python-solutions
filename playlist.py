class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None
    def add_song_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def add_song_end(self,data):
        new_node=Node(data)
        temp=self.head
        if temp is None:
            self.head=new_node
            return
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def add_song_position(self,data,position):
        new_node=Node(data)
        if position==1:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        if self.head is None:
            self.head=new_node
            return
        else:
            for _ in range(position-2):
                if temp.next is None:
                    temp.next=new_node
                    return
                temp=temp.next
            temp1=temp.next
            temp.next=new_node
            new_node.next=temp1
    def remove_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            return
    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            return
    def remove_position(self,position):
        if position<=0:
            print("invalid position")
            return

        if self.head is None:
            return 
        if self.head.next is None:
            self.head=None
            return 
        else:
            temp=self.head
            for _ in range(position-2):
                if temp.next is None or temp.next.next is None:
                    print("invalid position")
                    return
                temp=temp.next
            temp.next=temp.next.next
            return
    def search(self,data):
        if self.head is None:
            print("list empty")
        else:
            c=1
            temp=self.head
            while temp:
                if temp.data == data:
                    print("position is :",c)
                    return
                else:
                    temp=temp.next
                    c+=1
            print("song not in list")
    def display(self):
        temp=self.head
        while temp:
            print(f"{temp.data}->",end="")
            temp=temp.next
        print("")
    def count(self):
        temp=self.head
        c=0
        while temp:
            temp=temp.next
            c+=1
        print("count is : ",c)
    def reverse(self):
            prev = None
            curr = self.head

            while curr is not None:
                nxt = curr.next  
                curr.next = prev 
                prev = curr 
                curr = nxt  

            self.head = prev  
        
        
playlist=linkedlist()


def print_menu():
    menu = """
    ==================================================
                 MUSIC PLAYLIST MANAGER
    ==================================================
     1. Add a song to the beginning
     2. Add a song to the end
     3. Insert a song at a specified position
     4. Remove the first song
     5. Remove the last song
     6. Remove a song at a specified position
     7. Search for a song and display its position
     8. Display the total number of songs
     9. Display the complete playlist
    10. Reverse the playlist order
    11. Exit
    ==================================================
    """
    print(menu)
while True:
    print_menu()
    choice = input("Enter your choice (1-11): ").strip()

    match choice:
        case '1':
            song=input("enter song : ")
            playlist.add_song_beg(song)

        case '2':
            song=input("enter song:")
            playlist.add_song_end(song)
        case '3':
            p=int(input("enter position:"))
            song=input("enter song:")
            playlist.add_song_position(song,p)
        case '4':

            print("removing first song")
            playlist.remove_first()
        case '5':
            print("removing last song")
            playlist.remove_last()
        case '6':
            p=int(input("enter position:"))
            playlist.remove_position(p)
        case '7':
            song=input("enter song to search:")
            playlist.search(song)
        case '8':
            playlist.count()
        case '9':
            playlist.display()
        case '10':
            playlist.reverse()
            playlist.display()
        case '11':
            print("Exiting application. Goodbye!")
            break
        case _:
            print("Invalid input! Please select a number from 1 to 11.")

