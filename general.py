import streamlit as st


st.title("Iris: An Introduction")
st.write(
    """
    Irises are flowering plants in the genus *Iris*, named after the Greek
    goddess of the rainbow. They are known for their distinctive, often
    brightly colored flowers and are grown in gardens around the world.
    Irises occur naturally across temperate regions, commonly in meadows,
    woodland edges, and wet habitats.
    """
)

st.info(
    "The Iris flower prediction app focuses on three species from the classic "
    "Iris dataset: *Iris setosa*, *Iris versicolor*, and *Iris virginica*."
)

st.header("The three species")

setosa, versicolor, virginica = st.columns(3)

with setosa:
    st.subheader("Iris setosa")
    st.write(
        """
        A compact species that is often found in cooler, northern regions.
        In the classic dataset, setosa usually has the shortest petals, making
        it the easiest of the three species to distinguish by petal size.
        """
    )

with versicolor:
    st.subheader("Iris versicolor")
    st.write(
        """
        Commonly called the blue flag iris, this species grows in moist
        habitats such as marshes and pond margins. Its flower and measurements
        tend to fall between those of setosa and virginica.
        """
    )

with virginica:
    st.subheader("Iris virginica")
    st.write(
        """
        Also known as the Virginia iris, it is generally the largest of the
        three dataset species. It is associated with wetlands and typically
        has the longest petals in the dataset.
        """
    )

st.header("How the species are compared")
st.write(
    """
    The classic Iris dataset contains 150 flower observations, with 50
    observations for each of the three species. Each flower is described using
    four measurements, all recorded in centimeters:
    """
)

st.markdown(
    """
    - **Sepal length** and **sepal width** — dimensions of the outer,
      leaf-like parts that protect the developing flower.
    - **Petal length** and **petal width** — dimensions of the inner,
      usually colorful parts of the flower.
    """
)

st.caption(
    "Measurements are useful for distinguishing these dataset examples, "
    "but natural variation means a single measurement is not a complete "
    "botanical identification."
)