import streamlit as st
import random
import time


all_questions = [
    {
        "question": "Which of the following is the React framework❓",
        "options": ["Vue.JS", "Next.JS", "Nest.JS", "None"],
        "answer": "Next.JS"
    },
    {
        "question": "What command is used to create a new Next.js app?",
        "options": ["npx create-react-app", "npm create-next-app", "next new", "next init"],
        "answer": "npm create-next-app"
    },
    {
        "question": "Which file is used for Next.js routing?",
        "options": ["routes.js", "pages/index.js", "server.js", "router.js"],
        "answer": "pages/index.js"
    },
    {
        "question": "What is the default port for Next.js when running locally?",
        "options": ["3000", "8080", "5000", "4000"],
        "answer": "3000"
    },
    {
        "question": "Which file is required in every Next.js project?",
        "options": ["package.json", "index.html", "server.js", "config.js"],
        "answer": "package.json"
    },
    {
        "question": "What is the primary advantage of using Next.js over React?",
        "options": ["Faster performance", "Server-side rendering (SSR)", "Automatic code splitting", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "How do you enable static site generation (SSG) in Next.js?",
        "options": ["Using getServerSideProps", "Using getStaticProps", "Using getInitialProps", "Using fetch"],
        "answer": "Using getStaticProps"
    },
    {
        "question": "Which function is used for server-side rendering (SSR) in Next.js?",
        "options": ["getStaticProps", "getServerSideProps", "getInitialProps", "fetch"],
        "answer": "getServerSideProps"
    },
    {
        "question": "Which file is used for global styles in Next.js?",
        "options": ["global.css", "index.css", "styles.css", "main.css"],
        "answer": "global.css"
    },
    {
        "question": "How can you add dynamic routes in Next.js?",
        "options": ["Using [] in the filename", "Using {} in the filename", "Using dynamicRoutes.js", "Using route.js"],
        "answer": "Using [] in the filename"
    },
    {
        "question": "What is API Routes in Next.js used for?",
        "options": ["Creating backend endpoints", "Defining page routes", "Styling components", "Handling state"],
        "answer": "Creating backend endpoints"
    },
    {
        "question": "What is the built-in CSS-in-JS library in Next.js?",
        "options": ["Styled-components", "Emotion", "Tailwind CSS", "styled-jsx"],
        "answer": "styled-jsx"
    },
    {
        "question": "What function is used to fetch data at build time?",
        "options": ["getServerSideProps", "getInitialProps", "getStaticProps", "fetch"],
        "answer": "getStaticProps"
    },
    {
        "question": "Which of these is NOT a feature of Next.js?",
        "options": ["Client-side rendering", "Server-side rendering", "Automatic static optimization", "Python backend"],
        "answer": "Python backend"
    },
    {
        "question": "Which folder is used to store API routes in Next.js?",
        "options": ["pages/api", "api", "routes", "server"],
        "answer": "pages/api"
    },
    {
        "question": "What method is used to navigate between pages in Next.js?",
        "options": ["Link component", "Navigate function", "Router.push", "window.location.href"],
        "answer": "Link component"
    },
    {
        "question": "Which command is used to build a Next.js project for production?",
        "options": ["next build", "next run", "next compile", "next deploy"],
        "answer": "next build"
    },
    {
        "question": "How do you enable incremental static regeneration (ISR) in Next.js?",
        "options": ["Using revalidate in getStaticProps", "Using getServerSideProps", "Using ISR mode", "Using prefetch"],
        "answer": "Using revalidate in getStaticProps"
    },
    {
        "question": "What does Next.js use internally for rendering?",
        "options": ["Webpack", "Babel", "ReactDOMServer", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "How can you create a dynamic API route in Next.js?",
        "options": ["Using [id].js inside pages/api", "Using dynamic.js", "Using APIrouter.js", "Using dynamicAPI.js"],
        "answer": "Using [id].js inside pages/api"
    },
    {
        "question": "Which deployment platform is optimized for Next.js?",
        "options": ["Netlify", "Heroku", "Vercel", "AWS"],
        "answer": "Vercel"
    },
    {
        "question": "Which lifecycle method is replaced by getServerSideProps in Next.js?",
        "options": ["componentDidMount", "getInitialProps", "useEffect", "componentWillMount"],
        "answer": "getInitialProps"
    }
]

# (Continue adding 50+ Next.js related questions in the same format...)

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