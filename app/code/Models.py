from sentence_transformers import SentenceTransformer


def get_model(model_name):
    """Returns a SentenceTransformer model"""
    print('Loading model...')
    return SentenceTransformer(model_name)
