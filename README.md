# step1: weaviate安装
```
docker-compose up -d
```

# 下载中文模型转成向量
```
GanymedeNil/text2vec-large-chinese
```

# main.py包含数据构造，导入向量数据到weaviate，进行向量数据查询

# 代码结构
├── [ 488]  df.csv
├── [ 755]  docker-compose.yml
├── [ 145]  downloadmodel.py
├── [1.8K]  main.py
├── [ 237]  model
│   ├── [ 821]  config.json
│   ├── [  69]  eval_results.txt
│   ├── [ 154]  model.safetensors -> ../../../../root/.cache/huggingface/hub/models--GanymedeNil--text2vec-large-chinese/blobs/eaf5cb71c0eeab7db3c5171da504e5867b3f67a78e07bdba9b52d334ae35adb3
│   ├── [ 154]  pytorch_model.bin -> ../../../../root/.cache/huggingface/hub/models--GanymedeNil--text2vec-large-chinese/blobs/5883cb940ac5509b75e9fe23a9aea62694045849dc8c8c2da2894861a045d7f5
│   ├── [ 443]  README.md
│   ├── [ 125]  special_tokens_map.json
│   ├── [ 514]  tokenizer_config.json
│   ├── [429K]  tokenizer.json
│   └── [107K]  vocab.txt
├── [ 218]  README.md
└── [ 221]  requirements.txt
