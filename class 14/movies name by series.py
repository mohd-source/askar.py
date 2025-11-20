# # # # movies = ["ak, bahubali ,cars 3 ,dhoom ,krish ,ninja ,pj ,pushpa ,ram "]

# # # # # n = int(input("Enter number of movies: "))

# # # # # Input movie names
# # # # # for i in range(n):  
# # # # #     name = input(f"Enter movie name {i+1}: ").strip()
# # # # #     movies.append(name)

# # # # # Sort movies A-Z
# # # # movies_sorted = sorted(movies, key=lambda x: x.lower())

# # # # print("\nSorted Movie List (A-Z):")
# # # # for movie in movies_sorted:
# # # #     print(movie)

# # # # # Count movies starting with each letter
# # # # alphabet_count = {chr(i): 0 for i in range(65, 91)}  # A-Z dictionary

# # # # for movie in movies:
# # # #     first_letter = movie[0].upper()
# # # #     if first_letter in alphabet_count:
# # # #         alphabet_count[first_letter] += 1

# # # # # Display the result
# # # # print("\nMovie Count by Starting Letter:")
# # # # for letter, count in alphabet_count.items():
# # # #     if count > 0:
# # # #         print(f"{letter}: {count}")
# # # movies = []
# # # # Input movies
# # # n = int(input("How many movies? "))

# # # for i in range(n):
# # #     movie = input(f"Movie {i+1}: ").strip()
# # #     movies.append(movie)
# # # movies = ["ak", "aaram", "bahubali", "cars 3", "dhoom", "krish", "ninja", "pj", "pushpa", "ram"]



# # # # Sort and show list
# # # print("\nSorted Movies (A-Z):")
# # # for m in sorted(movies, key=str.lower):
# # #     print(m)

# # # # Count movies by first letter
# # # print("\nMovie Count by Starting Letter:")
# # # # counts = {}

# # # # for movie in movies:
# # # #     letter = movie[0].upper()
# # # #     counts[letter] = counts.get(letter, 0) + 1
    

# # # # for letter in sorted(counts):
# # # #     print(f"{letter}: {counts[letter]}")


# # # counts = {}

# # # for movie in movies:
# # #     letter = movie[0].upper()

# # #     # Add letter if not in dictionary
# # #     if letter not in counts:
# # #         counts[letter] = []

# # #     # Add movie to that letter
# # #     counts[letter].append(movie)

# # # # Print result
# # # for letter in sorted(counts):
# # #     print(f"\n{letter}: {len(counts[letter])}")
# # #     print(counts[letter])




# # # movies = []
# # # # Input movies
# # # n = int(input("How many movies? "))

# # # for i in range(n):
# # #     movie = input(f"Movie {i+1}: ").strip()
# # #     movies.append(movie)

# # # # Sort and show list
# # # print("\nSorted Movies (A-Z):")
# # # for m in sorted(movies, key=str.lower):
# # #     print(m)

# # # # Count + store movies by starting letter
# # # print("\nMovie Count by Starting Letter:")
# # # counts = {}

# # # for movie in movies:
# # #     letter = movie[0].upper()

# # #     if letter not in counts:
# # #         counts[letter] = ][      # create an empty list for this letter

# # #     counts[letter].append(movie) # add movie to that letter list

# # # # Print letter, count, and movie names
# # # for letter in sorted(counts):
# # #     print(f"\n{letter}: {len(counts[letter])} movie(s)")
# # #     for m in counts[letter]:
# # #         print(f"  - {m}")




# # # import tkinter as tk
# # # from tkinter import messagebox

# # # # Sample movies
# # # movies = ["ak", "aaram", "bahubali", "cars 3", "dhoom", "krish", "ninja", "pj", "pushpa", "ram"]

# # # # Function to display sorted movies
# # # def show_sorted():
# # #     sorted_movies = sorted(movies, key=str.lower)
# # #     sorted_text.set("\n".join(sorted_movies))

# # # # Function to display count by first letter
# # # def show_counts():
# # #     counts = {}
# # #     for movie in movies:
# # #         letter = movie[0].upper()
# # #         if letter not in counts:
# # #             counts[letter] = []
# # #         counts[letter].append(movie)
    
# # #     result = ""
# # #     for letter in sorted(counts):
# # #         result += f"{letter}: {len(counts[letter])} movie(s)\n"
# # #         for m in counts[letter]:
# # #             result += f"  - {m}\n"
# # #     counts_text.set(result)

# # # # Function to add a new movie
# # # def add_movie():
# # #     new_movie = movie_entry.get().strip()
# # #     if new_movie:
# # #         movies.append(new_movie)
# # #         movie_entry.delete(0, tk.END)
# # #         messagebox.showinfo("Added", f"'{new_movie}' added to movies")
# # #         show_sorted()
# # #         show_counts()

# # # # GUI Setup
# # # root = tk.Tk()
# # # root.title("Movie List GUI")

# # # # Entry to add new movie
# # # tk.Label(root, text="Add a Movie:").pack()
# # # movie_entry = tk.Entry(root, width=30)
# # # movie_entry.pack()
# # # tk.Button(root, text="Add Movie", command=add_movie).pack(pady=5)

# # # # Sorted movies display
# # # tk.Label(root, text="Sorted Movies:").pack()
# # # sorted_text = tk.StringVar()
# # # tk.Label(root, textvariable=sorted_text, justify="left").pack()

# # # # Movie count display
# # # tk.Label(root, text="Movies Count by First Letter:").pack()
# # # counts_text = tk.StringVar()
# # # tk.Label(root, textvariable=counts_text, justify="left").pack()

# # # # Initialize display
# # # show_sorted()
# # # show_counts()

# # # root.mainloop()
# # # # # make a GUI window




# # import tkinter as tk
# # from tkinter import messagebox

# # # Initial movie list
# # movies = ["ak", "aaram", "bahubali", "cars 3", "dhoom", "krish", "ninja", "pj", "pushpa", "ram"]

# # # Functions
# # def update_sorted():
# #     sorted_listbox.delete(0, tk.END)
# #     for movie in sorted(movies, key=str.lower):
# #         sorted_listbox.insert(tk.END, movie)

# # def update_counts():
# #     counts_listbox.delete(0, tk.END)
# #     counts = {}
# #     for movie in movies:
# #         letter = movie[0].upper()
# #         counts.setdefault(letter, []).append(movie)
# #     for letter in sorted(counts):
# #         counts_listbox.insert(tk.END, f"{letter}: {len(counts[letter])} movie(s)")
# #         for m in counts[letter]:
# #             counts_listbox.insert(tk.END, f"   - {m}")

# # def add_movie():
# #     new_movie = movie_entry.get().strip()
# #     if new_movie:
# #         movies.append(new_movie)
# #         movie_entry.delete(0, tk.END)
# #         update_sorted()
# #         update_counts()
# #         messagebox.showinfo("Success", f"'{new_movie}' added!")

# # def remove_movie():
# #     rem_movie = movie_entry.get().strip()
# #     if rem_movie in movies:
# #         movies.remove(rem_movie)
# #         movie_entry.delete(0, tk.END)
# #         update_sorted()
# #         update_counts()
# #         messagebox.showinfo("Removed", f"'{rem_movie}' removed!")
# #     else:
# #         messagebox.showwarning("Not Found", f"'{rem_movie}' not in movie list!")

# # # GUI Setup
# # root = tk.Tk()
# # root.title("Movie Manager")
# # root.geometry("600x500")
# # root.resizable(False, False)

# # # Entry and buttons
# # top_frame = tk.Frame(root)
# # top_frame.pack(pady=10)

# # tk.Label(top_frame, text="Movie Name:").grid(row=0, column=0, padx=5)
# # movie_entry = tk.Entry(top_frame, width=30)
# # movie_entry.grid(row=0, column=1, padx=5)
# # tk.Button(top_frame, text="Add Movie", command=add_movie, bg="lightgreen").grid(row=0, column=2, padx=5)
# # tk.Button(top_frame, text="Remove Movie", command=remove_movie, bg="lightcoral").grid(row=0, column=3, padx=5)

# # # Sorted Movies Listbox
# # sorted_frame = tk.Frame(root)
# # sorted_frame.pack(pady=10, side=tk.LEFT, padx=10)

# # tk.Label(sorted_frame, text="Sorted Movies (A-Z):").pack()
# # sorted_listbox = tk.Listbox(sorted_frame, width=30, height=20)
# # sorted_listbox.pack()

# # # Counts Listbox
# # counts_frame = tk.Frame(root)
# # counts_frame.pack(pady=10, side=tk.RIGHT, padx=10)

# # tk.Label(counts_frame, text="Movies Count by First Letter:").pack()
# # counts_listbox = tk.Listbox(counts_frame, width=40, height=20)
# # counts_listbox.pack()

# # # Initialize
# # update_sorted()
# # update_counts()

# # root.mainloop()
# # # # make a GUI window




# import tkinter as tk
# from tkinter import messagebox

# movies = []  # Store all movies

# # Functions
# def add_movie():
#     movie_name = movie_entry.get().strip()
#     if movie_name:
#         movies.append(movie_name)
#         movie_entry.delete(0, tk.END)
#         update_display()
#         messagebox.showinfo("Added", f"'{movie_name}' added!")

# def update_display():
#     # Update sorted movie list
#     sorted_listbox.delete(0, tk.END)
#     for m in sorted(movies, key=str.lower):
#         sorted_listbox.insert(tk.END, m)
    
#     # Update count by first letter
#     counts_listbox.delete(0, tk.END)
#     counts = {}
#     for movie in movies:
#         letter = movie[0].upper()
#         if letter not in counts:
#             counts[letter] = []
#         counts[letter].append(movie)
    
#     for letter in sorted(counts):
#         counts_listbox.insert(tk.END, f"{letter}: {len(counts[letter])} movie(s)")
#         for m in counts[letter]:
#             counts_listbox.insert(tk.END, f"   - {m}")

# # GUI Setup
# root = tk.Tk()
# root.title("Movie Manager GUI")
# root.geometry("600x400")

# # Top frame: add movie
# top_frame = tk.Frame(root)
# top_frame.pack(pady=10)

# tk.Label(top_frame, text="Movie Name:").grid(row=0, column=0, padx=5)
# movie_entry = tk.Entry(top_frame, width=30)
# movie_entry.grid(row=0, column=1, padx=5)
# tk.Button(top_frame, text="Add Movie", command=add_movie, bg="lightgreen").grid(row=0, column=2, padx=5)

# # Left frame: Sorted Movies
# left_frame = tk.Frame(root)
# left_frame.pack(side=tk.LEFT, padx=20, pady=10)

# tk.Label(left_frame, text="Sorted Movies (A-Z):").pack()
# sorted_listbox = tk.Listbox(left_frame, width=30, height=20)
# sorted_listbox.pack()

# # Right frame: Counts by First Letter
# right_frame = tk.Frame(root)
# right_frame.pack(side=tk.RIGHT, padx=20, pady=10)

# tk.Label(right_frame, text="Movie Count by First Letter:").pack()
# counts_listbox = tk.Listbox(right_frame, width=40, height=20)
# counts_listbox.pack()

# root.mainloop()


import tkinter as tk
from tkinter import messagebox, ttk

movies = []  # Store all movies

# Functions
def add_movie():
    movie_name = movie_entry.get().strip()
    if movie_name:
        movies.append(movie_name)
        movie_entry.delete(0, tk.END)
        update_display()
        # messagebox.showinfo("Added", f"'{movie_name}' added!")

def update_display():
    # Update sorted movie list
    sorted_listbox.delete(0, tk.END)
    for m in sorted(movies, key=str.lower):
        sorted_listbox.insert(tk.END, m)
    
    # Update count by first letter
    counts_listbox.delete(0, tk.END)
    counts = {}
    for movie in movies:
        letter = movie[0].upper()
        counts.setdefault(letter, []).append(movie)
    
    for letter in sorted(counts):
        counts_listbox.insert(tk.END, f"{letter}: {len(counts[letter])} movie(s)")
        for m in counts[letter]:
            counts_listbox.insert(tk.END, f"   - {m}")

# GUI Setup
root = tk.Tk()
root.title("🎬 Movies GUI")
root.geometry("700x500")
root.config(bg="#1e1e1e")  # dark background

# Fonts
title_font = ("Helvetica", 14, "bold")
list_font = ("Helvetica", 12)
button_font = ("Helvetica", 11, "bold")

# Top Frame: Add Movie
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=10)

tk.Label(top_frame, text="Movie Name:", fg="white", bg="#1e1e1e", font=title_font).grid(row=0, column=0, padx=5)
movie_entry = tk.Entry(top_frame, width=30, font=list_font)
movie_entry.grid(row=0, column=1, padx=5)
tk.Button(top_frame, text="Add Movie", command=add_movie, bg="#4caf50", fg="white",
          font=button_font, activebackground="#45a049").grid(row=0, column=2, padx=5)

# Left Frame: Sorted Movies
left_frame = tk.Frame(root, bg="#1e1e1e")
left_frame.pack(side=tk.LEFT, padx=20, pady=10)

tk.Label(left_frame, text="Sorted Movies (A-Z):", fg="white", bg="#1e1e1e", font=title_font).pack()
sorted_listbox = tk.Listbox(left_frame, width=30, height=20, font=list_font, bg="#2e2e2e", fg="white",
                            selectbackground="#4caf50", selectforeground="white")
sorted_listbox.pack()

# Right Frame: Counts by First Letter
right_frame = tk.Frame(root, bg="#1e1e1e")
right_frame.pack(side=tk.RIGHT, padx=20, pady=10)

tk.Label(right_frame, text="Movie Count by First Letter:", fg="white", bg="#1e1e1e", font=title_font).pack()
counts_listbox = tk.Listbox(right_frame, width=40, height=20, font=list_font, bg="#2e2e2e", fg="white",
                            selectbackground="#4caf50", selectforeground="white")
counts_listbox.pack()

# Initialize display
update_display()

root.mainloop()
