from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ResumeJobMatcher:

    def match(self, resume_text, job_description):

        documents = [resume_text, job_description]

        vectorizer = CountVectorizer().fit_transform(documents)

        vectors = vectorizer.toarray()

        similarity = cosine_similarity(
            [vectors[0]],
            [vectors[1]]
        )[0][0]

        return round(similarity * 100, 2)