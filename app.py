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









