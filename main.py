import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

col1,col2,col3=st.columns(3)
if "player1_position" not in st.session_state:
    st.session_state.player1_position = 0

if "player2_position" not in st.session_state:
    st.session_state.player2_position = 0

if 'turn' not in st.session_state:
    st.session_state.turn = 1

a=0
b=0

with col1:
    # st.write("It's Player 1 Move")
    st.write("""
# Player 1""")
    button1=st.button("Player 1 Move")
    if button1:
        image=["C:\\Users\\ANKIT KUMAR\\Downloads\\face_1.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_2.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_3.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_4.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_5.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_6.png"]
        lst=[]
        for i in range(random.randint(1,4)):
            random.shuffle(image)
            lst=lst+image
        placeholder = st.empty()
        if True:
            for image_path in lst:
                img = Image.open(image_path)
                placeholder.image(img)
                time.sleep(0.1)
        st.session_state.player1_position += int(lst[-1][-5])
        a=lst[-1][-5]
        


with col2:
    # st.write("It's player 2 Move")
    st.write("""
# Player 2""")
    button2=st.button('Player 2 Move')
    if button2:
        image=["C:\\Users\\ANKIT KUMAR\\Downloads\\face_1.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_2.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_3.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_4.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_5.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_6.png"]
        lst1=[]
        for i in range(random.randint(1,4)):
            random.shuffle(image)
            lst1=lst1+image
        placeholder = st.empty()
        if True:
            for image_path in lst1:
                img = Image.open(image_path)
                placeholder.image(img)
                time.sleep(0.1)
        st.session_state.player2_position += int(lst1[-1][-5])
        b=lst1[-1][-5]

    
st.write(""" 
# First Player Move -> """,a)
st.write("""
# First Player Position -> """, st.session_state.player1_position)
st.write("""
# Second Player Move -> """,b)
st.write("""
# Second Player Position""", st.session_state.player2_position)

snake = [(16, 6), (49, 11), (62, 19), (93, 90), (95, 61), (98, 78),(50,66)]
ladder = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (71, 92), (80, 99)]
snakes={i[0]:i[1] for i in snake}
ladders={j[0]:j[1] for j in ladder}



def draw_board(player1_position, player2_position):
    fig, ax = plt.subplots(figsize=(14,14))
    for row in range(10):
        for col in range(10):
            cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
            if cell_num == player1_position and cell_num == player2_position:
                color = 'purple'  
            elif cell_num == player1_position:
                color = 'blue'
            elif cell_num == player2_position:
                color = 'orange'
            else:
                color = 'white'
            ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                    bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=1'), fontsize=15)
            ax.plot([col, col + 1], [9 - row, 9 - row], color='black')
            ax.plot([col, col + 1], [10 - row, 10 - row], color='black')
            ax.plot([col, col], [9 - row, 10 - row], color='black')
            ax.plot([col + 1, col + 1], [9 - row, 10 - row], color='black')

    for start, end in snakes.items():
        start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
        end_x, end_y = (end - 1)% 10, 9 - (end - 1) // 10
        ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=20, alpha=0.4)
    for start, end in ladders.items():
        start_x, start_y = (start-1)% 10, 9 - (start - 1) // 10
        end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
        ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'g', linewidth=20, alpha=0.4)
    
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return fig

def move_player(position, roll):
    new_position = position + roll
    if new_position in snakes.keys():
        new_position = snakes[new_position]
    elif new_position in ladders.keys():
        new_position = ladders[new_position]
    return min(new_position, 100)

if button1:
    # roll = random.randint(1, 6)
    # st.write(f"🎲 Rolled a {roll}!")

    
    if st.session_state.turn == 1:
        st.session_state.player1_position = move_player(st.session_state.player1_position, int(a))
        # st.write(f"Player 1 moves to position {st.session_state.player1_position}")
        
        if st.session_state.player1_position == 100:
            st.balloons()
            st.write("🎉 Congratulations! Player 1 wins!")
        else:
            st.session_state.turn = 2 
if button2:
        st.session_state.player2_position = move_player(st.session_state.player2_position, int(a))
        # st.write(f"Player 2 moves to position {st.session_state.player2_position}")
        
        if st.session_state.player2_position == 100:
            st.balloons()
            st.write("🎉 Congratulations! Player 2 wins!")
        else:
            st.session_state.turn = 1  


with col3:
    if st.session_state.turn == 1:
        st.write("""
    ## Player 1 Move""")
    else:
        st.write("""
    ## Player 2 Move""")
st.pyplot(draw_board(st.session_state.player1_position, st.session_state.player2_position))

