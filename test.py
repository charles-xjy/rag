from langchain.docstore.document import Document

parent_relevance = {}


a = Document(
    page_content="向量索引构建慢通常和数据量、参数设置、硬件资源三个核心因素相关，针对性优化就能显著提速。",
    metadata={
        "parent_id": "doc_001",  # 所属父文档的ID
    },
)
b = Document(
    page_content="向量索引构建慢通常和数据量、参数设置、硬件资源三个核心因素相关，针对性优化就能显著提速。",
    metadata={
        "parent_id": "doc_002",  # 所属父文档的ID
    },
)
c = Document(
    page_content="向量索引构建慢通常和数据量、参数设置、硬件资源三个核心因素相关，针对性优化就能显著提速。",
    metadata={
        "parent_id": "doc_001",  # 所属父文档的ID
    },
)
child_chunks = [a, b, c, a, a, c]

for chunk in child_chunks:
    parent_id = chunk.metadata.get("parent_id")
    print(parent_id)
    if parent_id:
        # 增加相关性计数
        parent_relevance[parent_id] = parent_relevance.get(parent_id, 0) + 1
        print(
            parent_relevance.get(parent_id, 0)
        )
print(parent_relevance)  # 输出父文档相关性计数
