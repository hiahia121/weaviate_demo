import weaviate
from langchain.document_loaders import DirectoryLoader, WebBaseLoader
import pandas as pd
from sentence_transformers import SentenceTransformer
import json


client = weaviate.Client(url="http://localhost:8083")

class_name = 'Stephen_Chow'

class_obj = {
        'class': class_name,
        'vectorIndexConfig': {
            'distance': 'l2-squared'
            }
        }

model = SentenceTransformer('./model')


if 1 == 0:
    client.schema.create_class(class_obj)
    # 处理数据
    df = pd.read_csv('df.csv')
    sentence_data = df["sentences"].tolist()
    sentence_embeddings = model.encode(sentence_data)
    new_data = {"sentence": sentence_data, "embeddings": sentence_embeddings.tolist()}
    new_df = pd.DataFrame(new_data)

    ## 导入数据到weaviate中

    with client.batch(batch_size=1) as batch:
        for i in range(new_df.shape[0]):
            print('importing data: {}'.format(i+1))

            properties = {'sentence_id': i+1, 'sentence': new_df.sentence[i]}

            custom_vector = new_df.embeddings[i]

            # 开始导入
            client.batch.add_data_object(
                    properties,
                    class_name=class_name,
                    vector=custom_vector
                    )
    print('import completed')

# 向量检索，开始查询
#i = model.encode(['除暴安良'])
ans = '爱的生活'
print("问题：{ans}".format(ans=ans))
query = model.encode([ans])[0].tolist()
#print(len(query))
#print(type(query))

near_vector = {'vector': query}

res = (
        client.query
        .get(class_name, ['sentence_id', 'sentence'])
        .with_near_vector(near_vector)
        .with_limit(2)
        .with_additional(['distance'])
        .do()
        )

print(res)

print(json.dumps(res, indent=2))


for i in res['data']['Get'][class_name]:
    print('='*20)
    print(i['sentence'])
