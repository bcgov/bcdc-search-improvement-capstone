import streamlit as st
from Funcs import  query_solr
import Variables as var


def main():
    """Main function of the search engine."""
    st.title("Dataset Search Engine")
    query = st.text_input("Enter your search query here:")
    num_results = st.slider("Number of results", min_value=var.min_value, max_value=var.max_value, value=var.value)
    if st.button("Search"):
        search_results = query_solr(query, num_results)
        display_results(search_results)



def display_results(search_results):
    """
    Display the search results on the user interface.

    Args:
        search_results (list): A list of dictionaries representing the search results.
            Each dictionary should contain the following keys:
                - 'DATASET_TITLE': The title of the dataset.
                - 'KEYWORDS': Keywords associated with the dataset.
                - 'DESCRIPTION': Description of the dataset.
                - 'CONTACT_LIST': Contact information related to the dataset.
                - 'OBJECT_NAME': The name of the object.
                - 'LINEAGE_STATEMENT': Lineage statement of the dataset.
                - 'PURPOSE': The purpose of the dataset.
    
    Returns:
        None
    """
    st.subheader("Search Results:")
    for i, result in enumerate(search_results):
        st.write(f"Result {i+1}")
        st.markdown(f"#### {result['DATASET_TITLE'][0]}")
        st.markdown(f"**Keywords:** {result['KEYWORDS'][0]}")
        st.markdown(f"**Description**: {result['DESCRIPTION'][0]}")
        st.markdown(f"**Contact**: {result['CONTACT_LIST'][0]}")
        st.markdown(f"**Object Name**: {result['OBJECT_NAME'][0]}")
        st.markdown(f"**Lineage Statement**: {result['LINEAGE_STATEMENT'][0]}")
        st.markdown(f"**Purpose**: {result['PURPOSE'][0]}")
        st.write("-------------------------------------------")

if __name__ == "__main__":

    main()

 






