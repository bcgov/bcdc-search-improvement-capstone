import pysolr
from Models import get_model


model = get_model('multi-qa-MiniLM-L6-cos-v1') # bc_data_v1


def generate_sentence_embedding(sentence):
    """Returns a sentence embedding"""
    return model.encode(sentence)


def convert_embedding_to_vector(embedding):
    """Converts a sentence embedding to a vector"""
    lst = [str(emb) for emb in embedding]
    return ','.join(lst)



def generate_vector_from_sentence(sentence):
    """Returns a vector representation of a sentence"""
    embedding = generate_sentence_embedding(sentence)
    vector = convert_embedding_to_vector(embedding) 
    return vector


def query_solr(query, num_results):
    """Takes a query and returns the search results from Solr
    Args:
        query (str): The search query.
        num_results (int): The number of results to return.
    Returns:
        list: A list of dictionaries representing the search results.
    """
    query_vector = generate_vector_from_sentence(query)
    query_search = "{!vp f=vector vector=\"%s\" cosine=false}" % (query_vector)
    f1_search = "DATASET_TITLE,DESCRIPTION,PURPOSE,LINEAGE_STATEMENT,CONTACT_LIST,OBJECT_NAME,KEYWORDS,search_column"
    search_results = pysolr.Solr('http://host.docker.internal:8983/solr/bc_data_v1').search(query_search, **{'f1': f1_search}, rows=num_results) 
    return search_results