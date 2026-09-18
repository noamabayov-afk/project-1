import streamlit as st

st.set_page_config(page_title="חיזוי נקודות NBA", page_icon="🏀")

# כותרת והסבר קצר
st.title("🏀 מודל חיזוי נקודות לשחקן NBA")
st.write("הזינו את אחוז השימוש (USG%) כדי לקבל את ממוצע הנקודות החזוי של השחקן.")

# פרמטרי המודל הליניארי (הדבק כאן את המספרים המדויקים שקבלת ב-Colab מ-w ו-b)
W = 45.0  # החלף בערך של w מהקוד שלך
B = -1.5  # החלף בערך של b מהקוד שלך

# קלט מהמשתמש
usg_pct = st.number_input(
    label="אחוז שימוש (USG% - בעשרוני, למשל 0.25 עבור 25%):",
    min_value=0.0,
    max_value=1.0,
    value=0.20,
    step=0.01
)

# כפתור חישוב
if st.button("חשב נקודות"):
    # חישוב הנוסחה הליניארית: y = w * x + b
    predicted_pts = W * usg_pct + B

    if predicted_pts > 0:
        st.success(f" ממוצע הנקודות החזוי: **{predicted_pts:.1f} נקודות למשחק**")
    else:
        st.warning("אחוז השימוש שהוזן נמוך מדי והתוצאה אינה הגיונית פיזיקלית.")

st.divider()
st.caption(f"משוואת המודל: $y = {W:.2f} \\cdot x + ({B:.2f})$")
