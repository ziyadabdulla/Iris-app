import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris


@st.cache_data
def load_iris_data() -> pd.DataFrame:
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data["Species"] = pd.Categorical.from_codes(
        iris.target, categories=[name.title() for name in iris.target_names]
    )
    return data


df = load_iris_data()
feature_names = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

st.title("Iris Species Visualisation")
st.write(
    "Explore how the three Iris species compare across sepal and petal "
    "measurements. The charts use the classic dataset of 150 measured flowers."
)

species = df["Species"].cat.categories.tolist()
selected_species = st.multiselect(
    "Species to include in the detailed charts",
    options=species,
    default=species,
)
filtered_df = df[df["Species"].isin(selected_species)]

metric_columns = st.columns(3)
metric_columns[0].metric("Flowers in dataset", len(df))
metric_columns[1].metric("Species", df["Species"].nunique())
metric_columns[2].metric("Flowers selected", len(filtered_df))

st.subheader("Flowers per species")
species_counts = (
    df["Species"].value_counts().reindex(species).rename_axis("Species").reset_index(name="Flowers")
)
st.bar_chart(species_counts, x="Species", y="Flowers")

st.subheader("Compare measurements")
x_axis, y_axis = st.columns(2)
with x_axis:
    x_feature = st.selectbox(
        "Horizontal axis",
        feature_names,
        index=feature_names.index("petal length (cm)"),
    )
with y_axis:
    y_feature = st.selectbox(
        "Vertical axis",
        feature_names,
        index=feature_names.index("petal width (cm)"),
    )

if filtered_df.empty:
    st.info("Select at least one species to display the detailed charts.")
else:
    st.scatter_chart(
        filtered_df,
        x=x_feature,
        y=y_feature,
        color="Species",
        height=450,
    )

st.subheader("Average measurements by species")
average_measurements = (
    df.groupby("Species", observed=False)[feature_names]
    .mean()
    .reset_index()
)
st.bar_chart(average_measurements, x="Species", y=feature_names)

st.subheader("Measurement relationships")
st.caption(
    "Values closer to 1 or -1 indicate stronger positive or negative "
    "linear relationships; values near 0 indicate weaker relationships."
)
correlation = df[feature_names].corr().rename(
    columns={
        "sepal length (cm)": "Sepal length",
        "sepal width (cm)": "Sepal width",
        "petal length (cm)": "Petal length",
        "petal width (cm)": "Petal width",
    },
)
correlation.index = [
    "Sepal length",
    "Sepal width",
    "Petal length",
    "Petal width",
]
st.dataframe(correlation.style.format("{:.2f}"), use_container_width=True)