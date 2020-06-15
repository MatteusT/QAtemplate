from .apps import QaGuiConfig


def get_contexts(question, n_paragraphs):
    '''
    :param question:
    :param n_paragraphs:
    :return question_paragraphs:

    Use the list of paragraphs extracted in QaGuiConfig.paragraphs and
    the vectorizer function in QaGuiConfig.vectorizer
    '''

    return ["dummy paragraph", "another dummy paragraph"]


def get_answer(question, paragraph):
    '''
    :param question:
    :param paragraph:
    :return answer:

    Use the transformer models initiated in QaGuiConfig to extract the answer
    '''

    return "dummy answer"
