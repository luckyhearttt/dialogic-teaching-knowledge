import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transcript & Reference", page_icon="📝", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# 1. Transcript Background & Content
# ==========================================

st.markdown("## 📝 Classroom Transcript")
st.divider()

st.markdown("""
### Transcript Background
- **Subject:** English (Grade 8, Mainland China, English as L2)
- **Activity:** Lead-in — Free talk about "healthy" and "strong"
- **Purpose:** Elicit and introduce the lesson topic
""")

st.markdown("### Transcript")

transcript_data = [
    (1, "T", 'Now, look at the screen. As you can see the topic for this class is Growing Healthy, Growing Strong. Tell me, do you think you are healthy and strong? If you think you are healthy, raise your hand. Oh, you think you are healthy. Put your hands down. You think you are healthy and strong, right? What makes you so healthy?'),
    (2, "S1", "Exercise."),
    (3, "T", "Oh, you exercise. How about you? Do you think you are healthy and strong?"),
    (4, "S2", "Yes."),
    (5, "T", "What makes you so healthy and strong?"),
    (6, "S2", "I do exercise and eat healthy food."),
    (7, "T", "Exercise and healthy food, thank you. Anyone else?"),
    (8, "S3", "I hardly eat junk food."),
    (9, "T", 'Oh, you never eat junk food. Thank you. So, most of you think you\'re healthy. But do you think you\'re strong? You think you\'re strong. What makes you so strong?'),
    (10, "S4", "I play sports."),
    (11, "T", "Do you have a lot of muscles? Because people who are strong usually have muscles, right? Do you have muscles?"),
    (12, "S4", "Maybe?"),
    (13, "T", 'Maybe, okay. So S4, you\'re saying that playing sports helps you become strong, even if you\'re not sure about the muscles part. Is that what you mean?'),
    (14, "S4", "Yes, I think sports make me strong."),
    (15, "T", 'Good. Now, S1 said exercise, S2 said exercise and healthy food, S3 said avoiding junk food, and S4 said playing sports. These are all interesting ideas. S2 mentioned both exercise AND healthy food. Do you agree with S2 that you need both? Or is one enough? What do you think, S5?'),
    (16, "S5", "I think... both"),
    (17, "T", "Okay, thank you. So it seems like many of you think being healthy needs both exercise and good food. Very good."),
]

df = pd.DataFrame(transcript_data, columns=["Turn", "Speaker", "Content"])
st.table(df.set_index("Turn"))

st.divider()

# ==========================================
# 2. APT Knowledge Base (Reference)
# ==========================================

st.markdown("## 📖 Reference: APT Talk Moves")

with st.expander("🎯 Goal 1: Help students share, expand, and clarify their thinking", expanded=False):
    st.markdown("""
**Move 1 — "Say More"**
Ask students to elaborate on a brief, vague, or unclear statement.
> *"Can you say more about that?" / "What do you mean by that?" / "Can you give an example?"*

---

**Move 2 — "Revoice"**
The teacher restates a student's reasoning and gives them a chance to confirm or correct.
> *"So let me see if I understand — you're saying … Is that right?"*
""")

with st.expander("🎯 Goal 2: Help students deepen their reasoning", expanded=False):
    st.markdown("""
**Move 3 — "Press for Reasoning"**
Ask students to explain the thinking behind their answer.
> *"Why do you think that?" / "What's your evidence?" / "How did you arrive at that answer?"*

---

**Move 4 — "Challenge"**
Offer a counter-example or alternative perspective to test and deepen reasoning.
> *"Is that always the case?" / "What if...?" / "What would someone who disagrees say?"*
""")

with st.expander("🎯 Goal 3: Help students listen carefully to one another", expanded=False):
    st.markdown("""
**Move 5 — "Restate"**
Prompt students to repeat or paraphrase what someone else said.
> *"Who can repeat what Javon just said, in your own words?"*
""")

with st.expander("🎯 Goal 4: Help students think with others", expanded=False):
    st.markdown("""
**Move 6 — "Agree / Disagree"**
Ask students to take a position on someone else's idea and explain why.
> *"Do you agree or disagree? Why?"*

---

**Move 7 — "Add On"**
Invite students to build on or extend a classmate's idea.
> *"Who can add on to what Jamal said?"*

---

**Move 8 — "Explain Other"**
Ask a student to explain another student's reasoning.
> *"Why do you think he said that?" / "Can you explain her reasoning in your own words?"*
""")

with st.expander("📐 Accountable Talk: Three Dimensions", expanded=False):
    st.markdown("""
- **To the Community:** Listen carefully, paraphrase & build on each other's ideas, challenge ideas not people.
- **To Accurate Knowledge:** Be specific and accurate, use verifiable sources.
- **To Rigorous Thinking:** Push for quality of claims & arguments, use sufficient and credible evidence.
""")









