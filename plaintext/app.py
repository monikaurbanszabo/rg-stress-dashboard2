import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="RG Stressz Dashboard",
    page_icon="🤸‍♀️",
    layout="wide"
)

st.title("🤸‍♀️ Sportanalitikai Dashboard")
st.subheader("Stresszhez való viszonyulás vizsgálata ritmikus gimnasztikázók körében")

st.markdown("""
Ez a dashboard a ritmikus gimnasztikázók stresszhez való viszonyulását mutatja be.
A vizsgálat fókusza a stressz mindset, valamint a stressz kihívásként vagy fenyegetésként való értelmezése.
""")

st.sidebar.header("Adatok feltöltése")
uploaded_file = st.sidebar.file_uploader("Tölts fel egy CSV fájlt", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Az adatok sikeresen betöltve!")

else:
    st.info("Mintaadatok jelennek meg. Saját CSV feltöltésével lecserélhetők.")

    df = pd.DataFrame({
        "Sportolo": ["RG1", "RG2", "RG3", "RG4", "RG5", "RG6"],
        "Eletkor": [18, 20, 22, 19, 24, 21],
        "Stress_mindset": [3.2, 2.8, 3.6, 2.5, 3.9, 3.1],
        "Challenge": [5.8, 5.2, 6.1, 4.9, 6.4, 5.5],
        "Threat": [3.1, 4.2, 2.8, 4.8, 2.5, 3.6],
        "Tethelyzet": ["Rövid", "Rövid", "Rövid", "Rövid", "Rövid", "Rövid"]
    })

st.header("📊 Adatok áttekintése")
st.dataframe(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Résztvevők száma", len(df))

with col2:
    st.metric("Átlagéletkor", round(df["Eletkor"].mean(), 2))

with col3:
    st.metric("Stress mindset átlag", round(df["Stress_mindset"].mean(), 2))

with col4:
    st.metric("Threat átlag", round(df["Threat"].mean(), 2))

st.header("📈 Stresszmutatók összehasonlítása")

avg_values = pd.DataFrame({
    "Mutató": ["Stress mindset", "Challenge", "Threat"],
    "Átlag": [
        df["Stress_mindset"].mean(),
        df["Challenge"].mean(),
        df["Threat"].mean()
    ]
})

fig1 = px.bar(
    avg_values,
    x="Mutató",
    y="Átlag",
    title="Stresszhez kapcsolódó mutatók átlagai",
    text_auto=True
)

st.plotly_chart(fig1, use_container_width=True)

st.header("🧠 Kihívás vagy fenyegetés?")

fig2 = px.scatter(
    df,
    x="Challenge",
    y="Threat",
    size="Stress_mindset",
    hover_name="Sportolo",
    title="Challenge és Threat pontszámok kapcsolata"
)

st.plotly_chart(fig2, use_container_width=True)

st.header("👥 Sportolói profilok")

selected = st.selectbox("Válassz ki egy sportolót:", df["Sportolo"])

sportolo = df[df["Sportolo"] == selected].iloc[0]

col5, col6, col7 = st.columns(3)

with col5:
    st.metric("Stress mindset", sportolo["Stress_mindset"])

with col6:
    st.metric("Challenge", sportolo["Challenge"])

with col7:
    st.metric("Threat", sportolo["Threat"])

st.markdown("### Értelmezés")

if sportolo["Threat"] > sportolo["Challenge"]:
    st.warning("A kiválasztott sportoló inkább fenyegetésként élheti meg a stresszhelyzeteket.")
else:
    st.success("A kiválasztott sportoló inkább kihívásként értelmezheti a stresszhelyzeteket.")

st.header("📌 Következtetések")

st.markdown("""
- A ritmikus gimnasztikában a versenyhelyzet rövid ideig tart, ezért a stressz intenzíven jelentkezhet.
- A magasabb Challenge érték arra utalhat, hogy a sportoló képes kihívásként értelmezni a stresszt.
- A magasabb Threat érték azt jelezheti, hogy a sportoló fenyegetőnek vagy megterhelőnek éli meg a helyzetet.
- A Stress mindset mutató segíthet megérteni, hogy a sportoló inkább segítő vagy káros tényezőként gondol-e a stresszre.
""")

st.sidebar.markdown("---")
st.sidebar.write("Készítette: Urbán-Szabó Mónika")
st.sidebar.write("Sportág: Ritmikus gimnasztika")
