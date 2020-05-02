import numpy as np
    
class counter_func:
    def _init_(self):
        pass

    def doc_freq(self,word,DF):
        c = 0
        try:
            c = DF[word]
        except:
            pass
        return c

    def Counter(self,tokens):
        count = {}
        for w in tokens:
            try:
                count[w] = count[w]+1
            except:
                count[w] = 1
        return count

class tfidfComputation:
    def _init_(self):
        pass

    def df_of_all_words(self,processed_text,processed_title):
        DF = {}
        for i in range(len(processed_text)):
            tokens = processed_text[i]
            for w in tokens:
                try:
                    DF[w].add(i)
                except:
                    DF[w] = {i}

            tokens = processed_title[i]
            for w in tokens:
                try:
                    DF[w].add(i)
                except:
                    DF[w] = {i}
        for i in DF:
            DF[i] = len(DF[i])
        return DF

    def tfidf_body(self,processed_text,processed_title,DF):
        doc = 0

        tf_idf = {}

        pp = counter_func()
        N = len(processed_text)
        for i in range(N):
            
            tokens = processed_text[i]
            
            counter = pp.Counter(tokens + processed_title[i])
            words_count = len(tokens + processed_title[i])
            
            for token in np.unique(tokens):
                
                tf = counter[token]/words_count
                df = pp.doc_freq(token,DF)
                idf = np.log((N+1)/(df+1))
                
                tf_idf[doc, token] = tf*idf

            doc += 1

        return tf_idf

    def tfidf_of_title(self,processed_text,processed_title,DF):
        doc = 0

        tf_idf_title = {}

        pp = counter_func()
        N = len(processed_text)
        for i in range(N):
            
            tokens = processed_title[i]
            counter = pp.Counter(tokens + processed_text[i])
            words_count = len(tokens + processed_text[i])

            for token in np.unique(tokens):
                
                tf = counter[token]/words_count
                df = pp.doc_freq(token,DF)
                idf = np.log((N+1)/(df+1)) #numerator is added 1 to avoid negative values
                
                tf_idf_title[doc, token] = tf*idf

            doc += 1

        return tf_idf_title

    def merge_tfidf(self,alpha,tf_idf,tf_idf_title):
        for i in tf_idf:
            tf_idf[i] *= alpha

        for i in tf_idf_title:
            tf_idf[i] = tf_idf_title[i]

        return tf_idf

    #tf_idf matching score ranking
    def matching_score(self,query_tokens,tf_idf):
        query_weights = {}

        for key in tf_idf:
            
            if key[1] in query_tokens:
                try:
                    query_weights[key[0]] += tf_idf[key]
                except:
                    query_weights[key[0]] = tf_idf[key]
        
        query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)
        
        print(query_weights)

        doc_num = []
        
        for i in query_weights:
            doc_num.append(i[0])
        
        return doc_num

def compute_tfidf(query,processed_text,processed_title,alpha):
    obj = tfidfComputation()
    DF = obj.df_of_all_words(processed_text,processed_title)
    tf_idf = obj.tfidf_body(processed_text,processed_title,DF)
    tf_idf_title = obj.tfidf_of_title(processed_text,processed_title,DF)
    tot_tfidf = obj.merge_tfidf(alpha,tf_idf,tf_idf_title)
    final_doc_num = obj.matching_score(query,tot_tfidf);

    return final_doc_num 

if __name__ == '__main__':
    querystr = "";
        

