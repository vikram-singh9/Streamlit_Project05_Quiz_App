import streamlit as st
import random
import time


all_questions = [
    {
        "question": "Which of the following is the react framework❓",
        "options" : ["Vue.JS", "Next.JS", "Nest.JS", "None"],
        "answer" : "Next.JS"
    },
     {
        "question":"Which is the richest country in the world?",
        "options":["pakistan","russia","america","france"],
        "answer":"america"
    },
     {
        "question":"How many provinces of pakistan?",
        "options":["one","eight","three","four"],
        "answer":"four"
    }
]

st.title("Quiz App 📝")

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(all_questions)
    
question = st.session_state.current_question

st.subheader( question["question"])

option_selected = st.radio("Choose Option", question["options"], key="answer")

if st.button("Submit Answer"):
        if option_selected == question["answer"]:
            st.success("Correct")
            st.balloons()
        else:
            st.error("Wrong! The Correct options is " + question["answer"])

        time.sleep(2)

        st.session_state.current_question = random.choice(all_questions)

        st.rerun()